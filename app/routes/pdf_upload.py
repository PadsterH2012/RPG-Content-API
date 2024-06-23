from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.ollama_client import generate_content
from app.database import get_db
from sqlalchemy.orm import Session
from app.models.character import Character
from app.schemas.character import CharacterCreate
import fitz  # PyMuPDF

router = APIRouter()

@router.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDFs are allowed.")
    
    # Read the PDF file
    pdf_content = await file.read()
    doc = fitz.open(stream=pdf_content, filetype="pdf")
    
    # Extract text from the PDF
    text = ""
    for page in doc:
        text += page.get_text()
    
    # Process the extracted text to generate content
    character_name = "Giblo Trellis"  # Example character name
    prompt = f"Extract details for the character {character_name} from the following text: {text}"
    character_details = generate_content(prompt)
    
    # Save the character details to the database
    character_data = CharacterCreate(
        name=character_name,
        backstory=character_details,  # Assuming the generated content includes backstory
        behaviors="",
        sample_speech="",
        traits=""
    )
    db_character = Character(**character_data.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    
    return {"character_id": db_character.id, "character_details": character_details}
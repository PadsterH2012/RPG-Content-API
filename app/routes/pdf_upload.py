from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.ollama_client import generate_content
from app.models.character import Character
from app.schemas.character import CharacterCreate
import fitz  # PyMuPDF
import logging
import json

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
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
        prompt = f"Extract character names, traits, and behaviors from the following text: {text}"
        character_details = generate_content(prompt)
        
        # Parse the character details (this is a simplified example)
        # You need to implement the logic to parse the character details from the response
        try:
            character_data = json.loads(character_details)
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="Failed to parse character details from LLM response")
        
        # Assuming the response is a list of characters with their details
        for character in character_data:
            parsed_details = {
                "name": character.get("name", "Unknown"),
                "backstory": character.get("backstory", ""),
                "behaviors": character.get("behaviors", ""),
                "sample_speech": character.get("sample_speech", ""),
                "traits": character.get("traits", "")
            }
            
            # Save the character details to the database
            character_data = CharacterCreate(**parsed_details)
            db_character = Character(**character_data.dict())
            db.add(db_character)
            db.commit()
            db.refresh(db_character)
        
        return {
            "message": "PDF uploaded and processed successfully",
            "character_id": db_character.id,
            "parsed_details": parsed_details
        }
    except Exception as e:
        logger.error(f"Error processing PDF: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
from flask import Blueprint, jsonify, request, render_template, current_app
from werkzeug.utils import secure_filename
import os
from .db import get_db_connection
from .pdf_utils import extract_text_from_pdf

bp = Blueprint('routes', __name__)

UPLOAD_FOLDER = 'uploaded_pdfs'
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/upload', methods=['GET', 'POST'])
def upload_pdf():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            text = extract_text_from_pdf(file_path)
            # Save text to the database or further processing
            return jsonify({'extracted_text': text}), 200
        return jsonify({'error': 'Invalid file format'}), 400
    return render_template('upload.html')

@bp.route('/api-routes')
def api_routes():
    routes = [
        {'method': 'GET', 'route': '/names/random'},
        {'method': 'GET', 'route': '/traits/random'},
        {'method': 'GET', 'route': '/behaviors/random'},
        {'method': 'GET', 'route': '/plots/random'},
        {'method': 'GET', 'route': '/encounters/random'},
        {'method': 'POST', 'route': '/names'},
        {'method': 'POST', 'route': '/traits'},
        {'method': 'POST', 'route': '/behaviors'},
        {'method': 'POST', 'route': '/plots'},
        {'method': 'POST', 'route': '/encounters'},
        {'method': 'POST', 'route': '/upload'}
    ]
    return render_template('api_routes.html', routes=routes)

@bp.route('/names/random', methods=['GET'])
def get_random_name():
    conn = get_db_connection()
    name = conn.execute("SELECT name FROM names ORDER BY RANDOM() LIMIT 1").fetchone()
    conn.close()
    return jsonify({'name': name['name'] if name else None})

@bp.route('/traits/random', methods=['GET'])
def get_random_trait():
    conn = get_db_connection()
    trait = conn.execute("SELECT trait FROM traits ORDER BY RANDOM() LIMIT 1").fetchone()
    conn.close()
    return jsonify({'trait': trait['trait'] if trait else None})

@bp.route('/behaviors/random', methods=['GET'])
def get_random_behavior():
    conn = get_db_connection()
    behavior = conn.execute("SELECT behavior FROM behaviors ORDER BY RANDOM() LIMIT 1").fetchone()
    conn.close()
    return jsonify({'behavior': behavior['behavior'] if behavior else None})

@bp.route('/plots/random', methods=['GET'])
def get_random_plot():
    conn = get_db_connection()
    plot = conn.execute("SELECT content FROM plots ORDER BY RANDOM() LIMIT 1").fetchone()
    conn.close()
    return jsonify({'plot': plot['content'] if plot else None})

@bp.route('/encounters/random', methods=['GET'])
def get_random_encounter():
    conn = get_db_connection()
    encounter = conn.execute("SELECT content FROM encounters ORDER BY RANDOM() LIMIT 1").fetchone()
    conn.close()
    return jsonify({'encounter': encounter['content'] if encounter else None})

@bp.route('/names', methods=['POST'])
def add_name():
    name = request.json.get('name')
    insert_name(name)
    return jsonify({'status': 'success'}), 201

@bp.route('/traits', methods=['POST'])
def add_trait():
    trait = request.json.get('trait')
    insert_trait(trait)
    return jsonify({'status': 'success'}), 201

@bp.route('/behaviors', methods=['POST'])
def add_behavior():
    behavior = request.json.get('behavior')
    insert_behavior(behavior)
    return jsonify({'status': 'success'}), 201

@bp.route('/plots', methods=['POST'])
def add_plot():
    content = request.json.get('content')
    insert_plot(content)
    return jsonify({'status': 'success'}), 201

@bp.route('/encounters', methods=['POST'])
def add_encounter():
    content = request.json.get('content')
    insert_encounter(content)
    return jsonify({'status': 'success'}), 201

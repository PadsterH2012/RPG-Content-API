from flask import Blueprint, jsonify, request
from .db import get_db_connection

bp = Blueprint('routes', __name__)

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

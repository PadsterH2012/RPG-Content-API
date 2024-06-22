# RPG Content API

This project provides an API for generating and managing RPG content elements such as names, traits, behaviors, plots, and encounters. The elements can be retrieved randomly to create diverse and dynamic RPG scenarios.

## Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/RPG-Content-API.git
    cd RPG-Content-API
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Initialize the database:
    ```sh
    python -c "from app.db import get_db_connection; conn = get_db_connection(); with open('schema.sql') as f: conn.executescript(f.read()); conn.close()"
    ```

### Running the Application

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

- `GET /names/random`
- `GET /traits/random`
- `GET /behaviors/random`
- `GET /plots/random`
- `GET /encounters/random`
- `POST /names`
- `POST /traits`
- `POST /behaviors`
- `POST /plots`
- `POST /encounters`

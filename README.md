# Search Agents

A Python project for creating search agents.

## Project Structure

```
search-agents/
├── src/
│   └── search_agents/      # Main package
│       ├── __init__.py
│       └── hello.py        # Hello World class for testing
├── tests/                  # Test directory
│       ├── __init__.py
│       └── test_hello.py
├── docs/                   # Documentation
├── requirements.txt        # Project dependencies
├── setup.py               # Setup configuration
└── README.md              # This file
```

## Setup Instructions

### 1. Create Virtual Environment

```bash
python3 -m venv venv
```

### 2. Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Project in Development Mode

```bash
pip install -e .
```

## Testing

Run the hello world test:

```bash
# Using pytest
pytest tests/test_hello.py -v

# Or run tests directly
python tests/test_hello.py
```

Run the hello world class directly:

```bash
python src/search_agents/hello.py
```

## Development

- **Code Formatting:** `black src/ tests/`
- **Linting:** `flake8 src/ tests/`
- **Type Checking:** `mypy src/`
- **Test Coverage:** `pytest --cov=src/search_agents tests/`

## License

MIT License

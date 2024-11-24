#!/bin/bash
# Create a virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Virtual environment setup complete. Use 'source venv/bin/activate' to activate."

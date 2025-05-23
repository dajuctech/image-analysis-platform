#!/bin/bash

echo "🔄 Starting image preprocessing..."

# Activate virtual environment if needed
# source venv/bin/activate

# Run data ingestion
python src/data_ingestion.py

echo "✅ Preprocessing complete."

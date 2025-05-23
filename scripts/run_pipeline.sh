#!/bin/bash

echo "🚀 Running full pipeline..."

# Step 1: Preprocess images
echo "🔧 Preprocessing images..."
python src/data_ingestion.py

# Step 2: Train model (make sure model.py has train hook)
echo "🧠 Training model..."
python -c "
from src.model import build_cnn_model, train_model
# You should replace below with real data pipeline
print('🧪 Replace with actual training dataset')
"

# Step 3: Log complete
echo "✅ Pipeline execution complete."

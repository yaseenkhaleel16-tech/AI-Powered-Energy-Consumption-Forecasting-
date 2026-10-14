from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from src.forecasting import run_pipeline

if __name__ == "__main__":
    run_pipeline()

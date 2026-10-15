from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / r"C:\y23\placement_prediction_app\data\placement_predict_50k_Dataset1.csv"
df = pd.read_csv(CSV_PATH)
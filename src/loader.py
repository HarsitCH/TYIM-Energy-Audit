#only reads CSV
import pandas as pd
from pathlib import Path


def load_equipment_data():
    """
    Loads the equipment CSV and returns a pandas DataFrame.
    """
    #Path(__File__) -> locates files 

    project_root = Path(__file__).resolve().parent.parent

    csv_path = project_root / "data" / "equipment.csv"

    df = pd.read_csv(csv_path)

    return df
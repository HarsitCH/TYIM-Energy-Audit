#exports tables 
from pathlib import Path


def export_to_excel(df):
    """
    Exports the calculated energy audit data
    to an Excel file.
    """

    project_root = Path(__file__).resolve().parent.parent

    tables_folder = project_root / "output" / "tables"

    tables_folder.mkdir(parents=True, exist_ok=True)

    output_file = tables_folder / "equipment_analysis.xlsx"

    df.to_excel(output_file, index=False)

    print(f"\nExcel file saved to:\n{output_file}")
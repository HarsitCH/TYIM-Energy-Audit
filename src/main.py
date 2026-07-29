# Runs the whole Energy Audit Project

import pandas as pd

from loader import load_equipment_data
from calculator import calculate_energy

from visualizer import (
    create_annual_energy_chart,
    create_energy_distribution_chart,
    create_load_comparison_chart,
    create_energy_projection_chart,
)

from exporter import export_to_excel


pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


def main():

    print("=" * 60)
    print("TYIM ENERGY AUDIT ANALYSIS")
    print("=" * 60)

    print("\nLoading equipment data...")
    equipment = load_equipment_data()

    print("Performing energy calculations...")
    equipment = calculate_energy(equipment)

    print("Generating charts...")
    create_annual_energy_chart(equipment)
    create_energy_distribution_chart(equipment)
    create_load_comparison_chart(equipment)
    create_energy_projection_chart(equipment)

    print("Exporting Excel report...")
    export_to_excel(equipment)

    print("\nCalculated Energy Audit Data:\n")
    print(equipment)

    print("\nAll tasks completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()
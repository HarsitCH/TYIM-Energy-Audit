# TYIM Energy Audit Analysis

A Python-based Energy Audit Analysis project developed as part of the **The Young Indians Movement (TYIM)** Energy Audit Program.

This project analyzes electrical energy consumption of a school computer laboratory by calculating connected load, operating load, daily, monthly, and annual energy consumption. It also generates visualizations and exports the calculated results to Excel for reporting purposes.

---

## Features

- Calculates connected and operating electrical loads
- Computes daily, monthly, and annual energy consumption
- Generates professional energy audit charts
- Exports calculated data to Microsoft Excel
- Modular Python code for easy maintenance and extension

---

## Project Structure

```
TYIM-Energy-Audit/
│
├── data/
│   └── equipment.csv
│
├── output/
│   ├── figures/
│   └── tables/
│
├── src/
│   ├── main.py
│   ├── loader.py
│   ├── calculator.py
│   ├── visualizer.py
│   └── exporter.py
│
├── README.md
├── LICENSE
└── requirements.txt
```

---

## Generated Outputs

The project automatically generates:

### Charts

- Connected Load vs Operating Load
- Daily Energy Consumption by Equipment Category
- Percentage Distribution of Daily Energy Consumption
- Projected Daily, Monthly and Annual Energy Consumption

### Excel Report

- Equipment analysis
- Connected load calculations
- Operating load calculations
- Energy consumption summary

---
## Graphs 
![alt text](annual_energy.png)
![alt text](energy_distribution.png)
![alt text](energy_projection.png)
![alt text](<load_comparison - Copy.png>)
## Technologies Used

- Python 3
- pandas
- matplotlib
- openpyxl

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/TYIM-Energy-Audit.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Navigate to the project directory and run:

```bash
python src/main.py
```

The generated charts will be saved in:

```
output/figures/
```

The Excel report will be saved in:

```
output/tables/
```

---

## Educational Purpose

This project was developed solely for educational purposes as part of the TYIM Energy Audit Program.

The calculations are based on the equipment inventory, operating hours, and assumptions applicable to the audited facility.

---

## Author

**C H HARSIT**

GitHub: https://github.com/HarsitCH
#only performs calculations
import pandas as pd

from config import (
    WORKING_DAYS_MONTH,
    WORKING_DAYS_YEAR,
)
#Creating the function 
def calculate_energy(df):
    """
    Calculates load and energy values
    for every equipment.
    """

    df["Connected_Load_W"] = (
        df["Installed_Quantity"]
        * df["Rated_Power_W"]
    )

    df["Operating_Load_W"] = (
        df["Operating_Quantity"]
        * df["Rated_Power_W"]
    )

    df["Daily_Energy_kWh"] = (
        df["Operating_Load_W"]
        * df["Daily_Hours"]
    ) / 1000

    df["Monthly_Energy_kWh"] = (
        df["Daily_Energy_kWh"]
        * WORKING_DAYS_MONTH
    )

    df["Annual_Energy_kWh"] = (
        df["Daily_Energy_kWh"]
        * WORKING_DAYS_YEAR
    )

    return df
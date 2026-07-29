import matplotlib.pyplot as plt
from pathlib import Path


def get_figures_folder():
    project_root = Path(__file__).resolve().parent.parent
    figures_folder = project_root / "output" / "figures"
    figures_folder.mkdir(parents=True, exist_ok=True)
    return figures_folder


# --------------------------------------------------------
# Figure 11.1
# Daily Energy Consumption by Equipment Category
# --------------------------------------------------------

def create_annual_energy_chart(df):

    plt.figure(figsize=(10, 6))

    equipment = [
        "Desktop\nComputers",
        "Split Air\nConditioners",
        "Ceiling\nFans",
        "LED Tube\nLights",
        "Laser\nPrinters",
        "Central\nUPS",
        "Network\nEquipment"
    ]

    energy = df["Daily_Energy_kWh"]

    colors = [
        "#4E79A7",
        "#F28E2B",
        "#59A14F",
        "#E15759",
        "#76B7B2",
        "#EDC948",
        "#AF7AA1"
    ]

    bars = plt.bar(
        equipment,
        energy,
        color=colors,
        edgecolor="#333333",
        linewidth=0.8
    )

    plt.title(
        "Daily Energy Consumption by Equipment Category",
        fontsize=16,
        fontweight="bold",
        pad=15
    )

    plt.xlabel(
        "Equipment Category",
        fontsize=12,
        fontweight="bold"
    )

    plt.ylabel(
        "Daily Energy Consumption (kWh)",
        fontsize=12,
        fontweight="bold"
    )

    plt.grid(
        axis="y",
        linestyle="--",
        linewidth=0.6,
        alpha=0.35
    )

    ax = plt.gca()
    ax.set_axisbelow(True)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.35,
            f"{height:.2f}",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold"
        )

    plt.tight_layout()

    chart_path = get_figures_folder() / "annual_energy.png"

    plt.savefig(
        chart_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


# --------------------------------------------------------
# Figure 11.2
# Percentage Distribution of Daily Energy Consumption
# --------------------------------------------------------

def create_energy_distribution_chart(df):

    plt.figure(figsize=(8, 8))

    plt.pie(
        df["Daily_Energy_kWh"],
        labels=[
            "Desktop",
            "AC",
            "Fans",
            "LED",
            "Printers",
            "UPS",
            "Network"
        ],
        autopct="%1.1f%%",
        startangle=90,
        shadow=True,
        wedgeprops={
            "edgecolor": "white",
            "linewidth": 1
        },
        textprops={
            "fontsize": 10
        }
    )

    plt.title(
        "Percentage Distribution of Daily Energy Consumption",
        fontsize=15,
        fontweight="bold",
        pad=15
    )

    plt.tight_layout()

    chart_path = get_figures_folder() / "energy_distribution.png"

    plt.savefig(
        chart_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


# --------------------------------------------------------
# Figure 9.1
# Connected vs Operating Load
# --------------------------------------------------------

def create_load_comparison_chart(df):

    plt.figure(figsize=(10, 6))

    equipment = [
        "Desktop",
        "AC",
        "Fans",
        "LED",
        "Printers",
        "UPS",
        "Network"
    ]

    x = range(len(equipment))
    width = 0.38

    plt.bar(
        [i - width/2 for i in x],
        df["Connected_Load_W"],
        width,
        label="Connected Load",
        color="#4E79A7",
        edgecolor="black"
    )

    plt.bar(
        [i + width/2 for i in x],
        df["Operating_Load_W"],
        width,
        label="Operating Load",
        color="#F28E2B",
        edgecolor="black"
    )

    plt.xticks(x, equipment)

    plt.title(
        "Connected Load vs Operating Load",
        fontsize=16,
        fontweight="bold",
        pad=15
    )

    plt.xlabel(
        "Equipment Category",
        fontsize=12,
        fontweight="bold"
    )

    plt.ylabel(
        "Power (W)",
        fontsize=12,
        fontweight="bold"
    )

    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.35
    )

    ax = plt.gca()
    ax.set_axisbelow(True)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.legend()

    plt.tight_layout()

    chart_path = get_figures_folder() / "load_comparison.png"

    plt.savefig(
        chart_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


# --------------------------------------------------------
# Figure 11.3
# Projected Daily / Monthly / Annual Consumption
# --------------------------------------------------------

def create_energy_projection_chart(df):

    plt.figure(figsize=(8, 6))

    daily = df["Daily_Energy_kWh"].sum()
    monthly = df["Monthly_Energy_kWh"].sum()
    annual = df["Annual_Energy_kWh"].sum()

    periods = [
        "Daily",
        "Monthly",
        "Annual"
    ]

    energy = [
        daily,
        monthly,
        annual
    ]

    colors = [
        "#4E79A7",
        "#59A14F",
        "#F28E2B"
    ]

    bars = plt.bar(
        periods,
        energy,
        color=colors,
        edgecolor="black"
    )

    plt.title(
        "Projected Energy Consumption",
        fontsize=15,
        fontweight="bold",
        pad=15
    )

    plt.xlabel(
        "Time Period",
        fontsize=12,
        fontweight="bold"
    )

    plt.ylabel(
        "Energy Consumption (kWh)",
        fontsize=12,
        fontweight="bold"
    )

    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.35
    )

    ax = plt.gca()
    ax.set_axisbelow(True)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f"{height:.2f}",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold"
        )

    plt.tight_layout()

    chart_path = get_figures_folder() / "energy_projection.png"

    plt.savefig(
        chart_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()
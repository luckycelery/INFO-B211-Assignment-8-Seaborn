"""
INFO-B211 — Data Visualization Assignment
Author: Emma

This script loads exercise heart-rate data and produces:
1. A heatmap of pulse values
2. Categorical plots of pulse by diet and exercise type
3. Six Seaborn plots (relational, distributional, categorical) using the planets dataset

All plots are saved as PNG files for easy viewing.
"""

# ============================
# Imports
# ============================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

sns.set_theme(style="whitegrid")  # global aesthetic


# ============================
# Helper: Save Plots
# ============================

def save_plot(filename):
    """
    Saves the current matplotlib figure to a PNG file.

    Parameters:
        filename (str): Name of the output file.
    """
    # Create an output folder if it doesn't exist
    os.makedirs("plots", exist_ok=True)

    # Save the figure inside the folder
    plt.savefig(f"plots/{filename}", dpi=300, bbox_inches="tight")
    plt.close()  # Close figure so memory doesn't fill up


# ============================
# Data Loading Functions
# ============================

def load_exercise_data(filepath):
    """Loads and cleans the exercise dataset."""
    df = pd.read_csv(filepath)
    df.columns = ["id", "pulse_1min", "pulse_15min", "pulse_30min", "diet", "exercise_type"]
    return df


def load_planets_data():
    """Loads the built-in Seaborn planets dataset."""
    return sns.load_dataset("planets")


# ============================
# Plotting Functions — Exercise Data
# ============================

def plot_pulse_heatmap(df):
    """Creates and saves a heatmap of pulse correlations."""
    pulse_data = df[["pulse_1min", "pulse_15min", "pulse_30min"]]

    plt.figure(figsize=(6, 4))
    sns.heatmap(pulse_data.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap of Pulse Measurements")

    # Tick positions (0, 1, 2 because it's a 3×3 heatmap)
    positions = [0, 1, 2]

    # Clean labels
    labels = ["Pulse 1 Min", "Pulse 15 Min", "Pulse 30 Min"]
    #Apply labels and rotate for readability
    plt.xticks(positions, labels, rotation=45)
    plt.yticks(positions, labels, rotation=0)

    save_plot("exercise_heatmap.png")


def plot_categorical_exercise(df):
    """Creates and saves categorical plots for diet and exercise type."""

    # Convert pulse columns into long format for easier plotting
    long_df = df.melt(
        id_vars=["diet", "exercise_type"],
        value_vars=["pulse_1min", "pulse_15min", "pulse_30min"],
        var_name="time_point",
        value_name="pulse"
    )

    # Replace ugly names with readable ones
    long_df["time_point"] = long_df["time_point"].replace({
    "pulse_1min": "Pulse 1 Min",
    "pulse_15min": "Pulse 15 Min",
    "pulse_30min": "Pulse 30 Min"
    })

    # Plot 1 — Pulse by Diet
    plt.figure(figsize=(8, 5))
    sns.violinplot(data=long_df, x="diet", y="pulse", hue="time_point")
    plt.title("Pulse Values by Diet Type")
    plt.xlabel("Diet Type")
    plt.ylabel("Pulse")
    plt.legend(title="Time Point")
    save_plot("pulse_by_diet.png")

    # Plot 2 — Pulse by Exercise Type
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=long_df, x="exercise_type", y="pulse", hue="time_point")
    plt.title("Pulse Values by Exercise Type")
    plt.xlabel("Exercise Type")
    plt.ylabel("Pulse (BPM)")
    plt.legend(title="Time Point")
    

    save_plot("pulse_by_exercise_type.png")


# ============================
# Plotting Functions — Planets Dataset
# ============================

def planets_relational_plots(planets):
    """Creates and saves two improved relational plots."""

    # ============================
    # Mass vs Distance
    # ============================

    plt.figure(figsize=(8, 6))

    # Scatterplot with transparency + smaller points
    sns.scatterplot(
        data=planets,
        x="distance",
        y="mass",
        hue="method",
        palette="tab10",
        alpha=0.6,
        s=40
    )

    # Use log scales to handle extreme ranges
    plt.xscale("log")
    plt.yscale("log")

    plt.title("Planet Mass vs Distance (Log Scales for Clarity)")
    plt.xlabel("Distance from Star (log scale)")
    plt.ylabel("Planet Mass (log scale)")

    # Move legend outside the plot for readability
    plt.legend(title="Discovery Method", bbox_to_anchor=(1.05, 1), loc="upper left")

    save_plot("planets_relational_scatter.png")

    # ============================
    # Lineplot: Average Mass by Year
    # ============================

    plt.figure(figsize=(7, 5))
    sns.lineplot(data=planets, x="year", y="mass", estimator="mean")
    plt.title("Average Planet Mass by Discovery Year")
    plt.xlabel("Discovery Year")
    plt.ylabel("Average Mass")
    save_plot("planets_relational_line.png")

    # Lineplot
    plt.figure(figsize=(7, 5))
    sns.lineplot(data=planets, x="year", y="mass", estimator="mean")
    plt.title("Average Planet Mass by Discovery Year")
    save_plot("planets_relational_line.png")


def planets_distribution_plots(planets):
    """Creates and saves two distribution plots."""

    # Histogram
    plt.figure(figsize=(7, 5))
    sns.histplot(planets["mass"].dropna(), kde=True)
    plt.title("Distribution of Planet Mass")
    save_plot("planets_distribution_hist.png")

    # KDE plot
    plt.figure(figsize=(7, 5))
    sns.kdeplot(data=planets, x="distance", fill=True)
    plt.title("Density of Planet Distance")
    save_plot("planets_distribution_kde.png")


def planets_categorical_plots(planets):
    """Creates and saves two categorical plots."""

    # Boxplot
    plt.figure(figsize=(7, 5))
    sns.boxplot(data=planets, x="method", y="mass")
    plt.title("Planet Mass by Discovery Method")
    plt.xticks(rotation=90)
    save_plot("planets_categorical_box.png")

    # Countplot
    plt.figure(figsize=(7, 5))
    sns.countplot(data=planets, x="method")
    plt.title("Count of Planets by Discovery Method")
    plt.xticks(rotation=90)
    save_plot("planets_categorical_count.png")


# ============================
# Main Execution Function
# ============================

def main():
    """Runs all visualizations and saves them as PNG files."""

    exercise_df = load_exercise_data("Exercise_Data.csv")
    planets_df = load_planets_data()

    # Exercise plots
    plot_pulse_heatmap(exercise_df)
    plot_categorical_exercise(exercise_df)

    # Planets plots
    planets_relational_plots(planets_df)
    planets_distribution_plots(planets_df)
    planets_categorical_plots(planets_df)


# ============================
# Script Entry Point
# ============================

if __name__ == "__main__":
    main()

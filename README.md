# INFO-B211 — Seaborn Data Visualization Project

## 1. Exercise Heart-Rate Data (Elementary School Partnership)

A local gym partnered with an elementary school to help students understand how **diet and exercise affect heart rate**. The gym collected pulse measurements at three time intervals—1 minute, 15 minutes, and 30 minutes—under different diet types and exercise conditions. This data was provided in **Exercise_Data.csv**.

### **Required Visualizations**
- A **heatmap** showing correlations between pulse measurements  
- A **categorical plot** of pulse values by **diet type**  
- A **categorical plot** of pulse values by **exercise type**  
- Clear titles, axis labels, and legends  
- High‑quality visual aesthetics (extra credit eligible)

### **Summary of Visual Findings (Student-Friendly Explanation)**

- The **heatmap** shows that pulse measurements taken at 15 and 30 minutes are strongly related, meaning heart rate stays elevated for a while after exercise.  
- The **diet plot** shows that pulse values vary slightly by diet type, but the biggest changes come from **time** and **activity**, not diet alone.  
- The **exercise plot** clearly demonstrates that:
  - **Resting** has the lowest pulse values  
  - **Walking** increases heart rate  
  - **Running** produces the highest pulse values  
  - Heart rate generally decreases from 1 minute → 15 minutes → 30 minutes as the body recovers  

### **Conclusion for Elementary Students**
These visualizations help students see that:
- Exercise makes your heart beat faster  
- More intense exercise (like running) raises your heart rate more than light activity  
- Your heart rate gradually returns to normal as you rest  
- Diet may play a role, but **movement** is the biggest factor in heart‑rate changes  

This makes the data relatable and helps students understand how their bodies respond to activity.

---

## 2. Planets Dataset Visualizations

The second part of the assignment required creating **two visualizations for each of the three major Seaborn plot types**:

- **Relational plots*  
- **Distribution plots**  
- **Categorical plots**  

Each plot needed descriptive titles, axis labels, legends, and strong visual clarity.

### **Included Visualizations**
- **Relational:**  
  - Scatterplot of planet mass vs. distance (log scales)  
  - Lineplot of average planet mass by discovery year  

- **Distributional:**  
  - Histogram of planet mass  
  - KDE plot of planet distance  

- **Categorical:**  
  - Boxplot of planet mass by discovery method  
  - Countplot of planets by discovery method  

### **Notable Insights from the Planets Dataset**

- The **scatterplot** reveals that most discovered planets cluster at lower masses and shorter distances, especially those found using the radial velocity method.  
- The **lineplot** shows how the average mass of discovered planets has changed over time, likely reflecting improvements in detection technology.  
- The **mass histogram** demonstrates that **small planets are far more common** than large ones.  
- The **distance KDE** shows that most planets are found relatively close to their stars.  
- The **categorical plots** highlight that:
  - Some discovery methods (like radial velocity and transit) dominate the field  
  - Different methods tend to detect planets with different mass ranges  

### **Most Insightful Graph(s)**
The **scatterplot (mass vs. distance)** is especially informative because it simultaneously shows:
- how mass and distance relate,  
- how discovery methods differ, and  
- how log scaling reveals patterns that would otherwise be hidden.

The **countplot** is also notable because it clearly illustrates which discovery methods are most widely used, giving context to the rest of the dataset.

---

Together, these visualizations demonstrate the ability to clean, reshape, and analyze data while communicating insights clearly and effectively.

---

## Project Overview
This project was created for the INFO-B211 Data Visualization assignment. The goal of the project is to demonstrate proficiency in Python-based data visualization using **pandas**, **Seaborn**, and **Matplotlib**. The script loads two datasets—**exercise heart-rate data** and the built‑in **Seaborn planets dataset**—and produces a series of visualizations that explore correlations, distributions, and categorical relationships.

All generated plots are automatically saved as **PNG files** inside a `plots/` directory for easy viewing and submission.

---

## Purpose of the Project
The purpose of this project is to:

- Practice loading, cleaning, and manipulating real-world datasets  
- Apply Seaborn’s relational, distributional, and categorical plotting tools  
- Produce clear, readable, and aesthetically consistent visualizations  
- Demonstrate modular code design through reusable functions  
- Strengthen understanding of data storytelling through visual analysis  

The project includes:

1. A **heatmap** of pulse measurements  
2. **Categorical plots** showing pulse values by diet and exercise type  
3. Six visualizations using the **planets** dataset (relational, distributional, categorical)

---

## Project Structure & Design
Although this project does not use object‑oriented classes, it follows a **modular functional design**, where each component of the workflow is encapsulated in its own function. This mirrors class‑based organization by separating responsibilities and improving readability, maintainability, and scalability.

Below is an explanation of each function, its purpose, parameters, and limitations.

---

## Function Descriptions

### 1. `save_plot(filename)`
**Purpose:**  
Saves the current Matplotlib figure to the `plots/` directory.

**Parameters:**  
- `filename` *(str)* — name of the output PNG file

**Behavior:**  
- Creates the `plots/` directory if it does not exist  
- Saves the figure at high resolution  
- Closes the figure to prevent memory buildup  

**Limitations:**  
- Assumes a figure already exists  
- Only saves PNG files  

---

### 2. `load_exercise_data(filepath)`
**Purpose:**  
Loads and cleans the exercise heart‑rate dataset.

**Parameters:**  
- `filepath` *(str)* — path to the CSV file

**Behavior:**  
- Reads the CSV  
- Renames columns for consistency  
- Returns a cleaned DataFrame  

**Limitations:**  
- Assumes the CSV has the expected column order  
- No error handling for missing or malformed data  

---

### 3. `load_planets_data()`
**Purpose:**  
Loads the built‑in Seaborn planets dataset.

**Behavior:**  
- Returns a DataFrame containing exoplanet discovery data  

**Limitations:**  
- Dependent on Seaborn’s dataset availability  

---

## Visualization Functions

### 4. `plot_pulse_heatmap(df)`
**Purpose:**  
Creates a correlation heatmap of pulse measurements at 1, 15, and 30 minutes.

**Parameters:**  
- `df` — exercise dataset

**Behavior:**  
- Computes correlations  
- Applies readable axis labels  
- Saves the heatmap  

**Limitations:**  
- Only visualizes three pulse columns  
- Assumes numeric data  

---

### 5. `plot_categorical_exercise(df)`
**Purpose:**  
Creates two categorical plots:  
- Pulse by diet  
- Pulse by exercise type  

**Parameters:**  
- `df` — exercise dataset

**Behavior:**  
- Converts pulse columns to long format  
- Renames time‑point labels for readability  
- Creates violin and box plots  
- Saves both plots  

**Limitations:**  
- Does not handle missing diet/exercise categories  
- Assumes pulse values are numeric  

---

## Planets Dataset Visualizations

### 6. `planets_relational_plots(planets)`
**Purpose:**  
Creates relational plots showing:  
- Mass vs distance (log‑scaled scatterplot)  
- Average mass by discovery year (lineplot)

**Parameters:**  
- `planets` — planets dataset

**Behavior:**  
- Uses log scales to handle extreme ranges  
- Adds clear axis labels and legend  
- Saves both plots  

**Limitations:**  
- Duplicate lineplot call (intentional or oversight)  
- Sensitive to missing mass/distance values  

---

### 7. `planets_distribution_plots(planets)`
**Purpose:**  
Creates distribution plots:  
- Histogram of planet mass  
- KDE plot of planet distance  

**Limitations:**  
- KDE may be skewed by extreme outliers  

---

### 8. `planets_categorical_plots(planets)`
**Purpose:**  
Creates categorical plots:  
- Boxplot of mass by discovery method  
- Countplot of planets by method  

**Limitations:**  
- Some categories have very small sample sizes  
- Long method names require rotation for readability  

---

## Main Execution

### 9. `main()`
**Purpose:**  
Coordinates the entire workflow.

**Behavior:**  
- Loads both datasets  
- Calls all visualization functions  
- Saves all outputs  

---

## Limitations of the Overall Project
- No exception handling for missing files or malformed data  
- Some plots may be affected by extreme outliers  
- Duplicate lineplot in `planets_relational_plots()`  
- No class‑based structure (assignment allowed functional design)  
- Assumes all required libraries are installed  

---

## Summary
This project demonstrates a complete, modular approach to data visualization using Python. Through a series of well‑structured functions, it loads data, cleans it, visualizes it, and saves the results in a reproducible and organized manner. The design emphasizes clarity, readability, and maintainability—core principles of good software and data science practice.

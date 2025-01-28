# ETS Decomposition for Time Series Analysis  

## Overview  
This repository demonstrates **ETS decomposition (Error/Trend/Seasonality)** for time series analysis using Python. It explores the concepts of additive and multiplicative models and applies these techniques to the **International Airline Passengers dataset**. The project is designed to provide a clear understanding of time series components such as trend, seasonality, and error, using tools provided by the **Statsmodels** library.  

## Features  
- Explanation of ETS decomposition concepts.  
- Hands-on implementation with Python libraries: `pandas`, `numpy`, and `statsmodels`.  
- Comparison of additive vs. multiplicative models.  
- Visualization of decomposed time series components.  

## Dataset  
The dataset used in this project is the **International Airline Passengers dataset**, which provides monthly passenger totals (in thousands) from January 1949 to December 1960.  

## Installation  

1. Clone the repository:  
   ```  
   git clone https://github.com/iamaniketray/Time-Series-ETS-Decomposition.git  
   cd Time-Series-ETS-Decomposition  
Create a virtual environment (optional but recommended):


python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  

Install the required libraries:
pip install -r requirements.txt  
The following Python libraries are required:

pandas
numpy
matplotlib
statsmodels
To install them manually:


pip install pandas numpy matplotlib statsmodels  
Open the Jupyter notebook:


jupyter notebook 01_ETS_Decomposition.ipynb  
Run through the cells to:

Understand ETS decomposition concepts.
Load and preprocess the dataset.
Apply seasonal decomposition (additive and multiplicative models).
Visualize time series components.
Project Structure
01_ETS_Decomposition.ipynb: Main notebook containing the explanation, code, and visualizations.
/Data/: Directory to store the dataset (e.g., airline_passengers.csv).
requirements.txt: List of dependencies for the project.
Results
This project highlights the following:

Decomposed time series components (trend, seasonality, residuals).
Difference between additive and multiplicative models.
Insights into time series data for forecasting.
References
Statsmodels Seasonal Decompose Documentation
Decomposition of Time Series on Wikipedia
Forecasting: Principles and Practice

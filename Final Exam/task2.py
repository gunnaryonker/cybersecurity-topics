import pandas as pd
import numpy as np

# Load the dataset
# Make sure to have the file Dataset_Task2.csv in the same directory
df = pd.read_csv('Dataset_Task2.csv')

# Query the dataset for the total watch hours in a week
def total_watch_hours(dataframe):
    return dataframe['Watch hours'].sum()

total_hours = total_watch_hours(df)
# Print total watch hours without noise to compare later on
print(f"Total Watch Hours without Noise: {total_hours}")

# Implementing the Laplace Mechanism for Differential Privacy
def laplace_noise(data, epsilon, sensitivity):
    """
    Add Laplace noise to the data.
    The scale parameter (b) for the Laplace noise is sensitivity / epsilon.
    """
    return data + np.random.laplace(0, sensitivity / epsilon)

# Sensitivity of sum query: The sensitivity for the sum query will be the maximum value possible 
# for an individual's contribution, which is the maximum watch hours in the dataset.
sensitivity = df['Watch hours'].max()

# Given epsilon value
epsilon = 0.8
noisy_total = laplace_noise(total_hours, epsilon, sensitivity)
# Print total watch hours with noise added to compare
print(f"Total Watch Hours with Noise (Differential Privacy): {noisy_total}")


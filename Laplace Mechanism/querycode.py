import pandas as pd
import numpy as np

# Define the differential privacy mechanism
def dp_mechanism(true_ans, sensitivity, epsilon):
    b = sensitivity / epsilon
    noise = np.random.laplace(0, b)
    rand_ans = true_ans + noise
    return rand_ans

# Load the dataset
df = pd.read_csv('Dataset.csv', delimiter=',')

# Define the privacy budget
epsilon_total = 2.5
epsilon_query1 = epsilon_total / 3
epsilon_query2 = epsilon_total / 3
epsilon_query3 = epsilon_total / 3

# Implement Query 1: Return the number of individuals in the dataset with salaries between $90,000 and $120,000
# Sensitivity for Query 1 is 1 (adding or removing one person)
sensitivity_query1 = 1
query1_result = df.loc[(df['Salary'] >= 90000) & (df['Salary'] <= 120000)].shape[0]
dp_query1_result = dp_mechanism(query1_result, sensitivity_query1, epsilon_query1)
print(f'Query 1 - True answer: {query1_result}')
print(f'Query 1 - Randomized answer: {dp_query1_result}')
print()

# Implement Query 2: Return the highest salary in the dataset
# Sensitivity for Query 2 is the difference between the current highest salary and the second-highest salary
sorted_salaries = df['Salary'].sort_values(ascending=False)
sensitivity_query2 = sorted_salaries.iloc[0] - sorted_salaries.iloc[1]
query2_result = sorted_salaries.iloc[0]
dp_query2_result = dp_mechanism(query2_result, sensitivity_query2, epsilon_query2)
print(f'Query 2 - True answer: {query2_result}')
print(f'Query 2 - Randomized answer: {dp_query2_result}')
print()

# Implement Query 3: Return the median salary in the dataset
# Sensitivity for Query 3 is the maximum change in median value when you remove or add a single individual
sorted_salaries = df['Salary'].sort_values(ascending=True)
num_individuals = len(sorted_salaries)
median_index = num_individuals // 2

# Calculate sensitivity for Query 3
sensitivity_query3 = max(
    abs(sorted_salaries.iloc[median_index] - sorted_salaries.iloc[median_index - 1]),
    abs(sorted_salaries.iloc[median_index] - sorted_salaries.iloc[median_index + 1])
)

query3_result = df['Salary'].median()
dp_query3_result = dp_mechanism(query3_result, sensitivity_query3, epsilon_query3)
print(f'Query 3 - True answer: {query3_result}')
print(f'Query 3 - Randomized answer: {dp_query3_result}')
print()

# Ensure that the total budget is within the desired εTotal (2.5)
total_epsilon_used = epsilon_query1 + epsilon_query2 + epsilon_query3
print(f'Total privacy budget used: {total_epsilon_used}')

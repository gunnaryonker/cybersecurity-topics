import pandas as pd
import random

# Load the provided dataset
def load_dataset(file_name):
    return pd.read_csv(file_name)

# Randomized Response Mechanism
def randomized_response(row):
    # A) Generate a random number between 1 and 3
    rand_num = random.randint(1, 3)
    
    # B) If the random number is 1 or 2, return the original response
    if rand_num in [1, 2]:
        return row['Response']
    
    # C) If the random number is 3, flip a weighted coin
    else:
        # Flip a coin with 20% probability of landing heads and 80% tails
        if random.choices([True, False], [0.2, 0.8])[0]:
            return "Yes"
        else:
            return "No"

def main():
    # Load the original dataset from the CSV file
    data = load_dataset("Dataset_Task1.csv")
    
    # Apply the Randomized Response Mechanism to each row's response. This is done to introduce
    # randomness into the dataset
    data['Response'] = data.apply(randomized_response, axis=1)
    
    # Save the modified dataset to a new CSV file
    data.to_csv("Modified_Dataset_Task1.csv", index=False)
    

    print("Randomized Response Mechanism Complete - New Dataset saved as Modified_Dataset_Task1.csv")

# Run the main function
if __name__ == "__main__":
    main()

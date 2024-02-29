import pandas as pd
import random

def modify_specific_columns(csv_path, output_csv_path, columns, num_changes=200, value_range=(1, 100)):
    # Read the CSV file
    df = pd.read_csv(csv_path)
    
    # Ensure only the specified columns are considered
    target_columns = [col for col in columns if col in df.columns]
    
    # Calculate changes per column if num_changes is more than the number of available cells
    changes_per_column = num_changes // len(target_columns)
    
    for column in target_columns:
        # Get number of rows for the column
        num_rows = df[column].shape[0]
        
        # Randomly select row indices to change
        row_indices = random.sample(range(num_rows), min(changes_per_column, num_rows))
        
        for row_index in row_indices:
            # Generate a random new value within the specified range
            new_value = random.randint(*value_range)
            df.at[row_index, column] = new_value
    
    # Save the modified DataFrame to a new CSV file
    df.to_csv(output_csv_path, index=False)

# Example usage
csv_path = './stages_results_per_rider.test.csv'
output_csv_path = csv_path
columns_to_modify = ['duration', 'speed']
modify_specific_columns(csv_path, output_csv_path, columns_to_modify)

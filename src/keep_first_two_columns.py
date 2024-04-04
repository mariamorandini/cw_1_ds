import pandas as pd  
import os

def keep_first_two_columns(file_path):
    "Given as Input the file path, this function clean the dataset of columns after the 2nd"

    df = pd.read_csv(file_path, header=0)
    df.fillna(0)
    df = df.iloc[:, :2] 

    output_directory = './data/cleaned/'
    os.makedirs(output_directory, exist_ok=True)
    
    # Save the DataFrame to a CSV file in the cleaned directory

    output_file_path = os.path.join(output_directory, 'sbarchi-per-giorno.csv')
    df.to_csv(output_file_path, index=False)

    return output_file_path

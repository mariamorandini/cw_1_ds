import pandas as pd  
import os

def count_immigrants_by_region(file_path):
    """Given as Input the file path, intended to be the file accoglienza.csv, this 
    fucntion creates a new dataset host_spot_by_region.csv where people by region have been merged,
    keeping distingued the different hosts places """

    
    df = pd.read_csv(file_path, header=0)
    df.fillna(0)
    df = df.groupby('Regione', as_index=False).sum()
    columns_to_consider = ['Regione','Immigrati presenti negli hot spot', 'Immigrati presenti nei centri di accoglienza', 
                      'Immigrati presenti nei centri SIPROIMI', 'Immigrati presenti nei centri SAI']
    
    df = df [columns_to_consider]


    output_directory = './data/cleaned/'
    os.makedirs(output_directory, exist_ok=True)
    
    # Save the DataFrame to a CSV file in the cleaned directory

    output_file_path = os.path.join(output_directory, 'host_spot_by_region.csv')
    df.to_csv(output_file_path, index=False)

    return output_file_path
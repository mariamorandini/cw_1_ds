import pandas as pd
import os

def adding_values(csv_file_path):

    """ this function creates the merged dataset of accoglienza.csv, 
    dropping the date and adding the total number of immigrants for each region indepentdent of time
    also  adds the total number of immigrants, regardless of where they are 
    """
    df = pd.read_csv(csv_file_path, header = 0)
    df.fillna(0)

    # Specify the columns to sum over
    columns_to_sum = ['Immigrati presenti negli hot spot', 'Immigrati presenti nei centri di accoglienza', 
                      'Immigrati presenti nei centri SIPROIMI', 'Immigrati presenti nei centri SAI']

    # Calculate the sum across specified columns
    df['total_immigrants'] = df[columns_to_sum].sum(axis=1)
    df = df.groupby('Regione', as_index=False).sum()
    df = df[['Regione', 'total_immigrants']]

    output_directory = './data/cleaned/'
    os.makedirs(output_directory, exist_ok=True)
    output_file_path = os.path.join(output_directory, 'merged_accoglienza.csv')
    df.to_csv(output_file_path, index=False)

    return output_file_path
    



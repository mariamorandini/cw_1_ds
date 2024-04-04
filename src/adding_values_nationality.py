import pandas as pd
import os

def adding_values_nationality(csv_file_path):

    """ this function creates the merged dataset of nazionalità.csv, 
    dropping the date and adding the total number of immigrants for each nationality
    """
    df = pd.read_csv(csv_file_path, header = 0)
    df.fillna(0)

    df = df.groupby('Nazione', as_index=False).sum()

    df = df[["Nazione", "Valore"]]

    italian_to_english = {
        'Afghanistan': 'Afghanistan',
        'Algeria': 'Algeria',
        'Bangladesh': 'Bangladesh',
        'Burkina Faso': 'Burkina Faso',
        'Camerun': 'Cameroon',
        'Costa d\'Avorio': 'Ivory Coast',
        'Egitto': 'Egypt',
        'Eritrea': 'Eritrea',
        'Etiopia': 'Ethiopia',
        'Gambia': 'Gambia',
        'Guinea': 'Guinea',
        'Iran': 'Iran',
        'Iraq': 'Iraq',
        'Mali': 'Mali',
        'Marocco': 'Morocco',
        'Nigeria': 'Nigeria',
        'Pakistan': 'Pakistan',
        'Senegal': 'Senegal',
        'Siria': 'Syria',
        'Somalia': 'Somalia',
        'Sudan': 'Sudan',
        'Tunisia': 'Tunisia',
        'Turchia': 'Turkey',
        'Ucraina': 'Ukraine',
        'altre': 'Others'  
    }

    df['Nazione'] = df['Nazione'].map(italian_to_english)


    output_directory = './data/cleaned/'
    os.makedirs(output_directory, exist_ok=True)
    output_file_path = os.path.join(output_directory, 'merged_nazionalita.csv')
    df.to_csv(output_file_path, index=False)

    return output_file_path
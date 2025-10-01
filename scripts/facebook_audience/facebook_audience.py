# %% imports
import pandas as pd


def preprocess_facebook_audience(df_entry):
    # birthday to date, DD/MM/YYYY
    df_entry['birthday'] = pd.to_datetime(df_entry['birthday'], format='%d/%m/%Y', errors='coerce')
    # current year
    current_year = pd.Timestamp.now().year
    # calculate age
    df_entry['age'] = current_year - df_entry['birthday'].dt.year
    # drop birthday column
    df_entry = df_entry.drop(columns=['birthday'])
    # rename columns
    df_entry = df_entry.rename(columns={
        "email": "email",
        "name": "fn",
        "last_name": "ln",
        "phone": "phone",
        "country": "country",
        "city": "ct",
        "state": "st",
        "gender": "gen",
        "age": "age",
    })
    return df_entry


def generate_facebook_audience_csv(df_entry):
    df_entry = df_entry.drop_duplicates(subset=['email'])
    # Only include columns that exist in the DataFrame
    columns = ['email', 'fn', 'ln', 'phone', 'country', 'ct', 'st', 'gen', 'age']
    columns_present = [col for col in columns if col in df_entry.columns]
    df_entry = df_entry[columns_present]
    # generate download file
    return df_entry.to_csv(index=False)

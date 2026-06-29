import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Create database
def load_data(file_name, table_name):
    # Load CSV into DB
    with sqlite3.connect('data/data.db') as conn:
        df = pd.read_csv(file_name)
        df.to_sql(table_name, conn, if_exists='replace', index=False)

# Clean dataset
def clean_data(is_legendary):
    query = """
    SELECT 
        pokedex_number,
        name,
        type1,
        type2,
        hp,
        attack,
        defense,
        sp_attack,
        sp_defense,
        speed,
        base_total,
        height_m,
        weight_kg,
        generation,
        is_legendary
    FROM pokemon
    WHERE generation < 5
        AND is_legendary = ?
    """

    with sqlite3.connect('data/data.db') as conn:
        df = pd.read_sql(query, conn, params=(is_legendary,))
    
    # Capitalise types
    df['type1'] = df['type1'].str.capitalize()
    df['type2'] = df['type2'].str.capitalize()

    return df

def main():
    load_data('data/pokemon.csv', 'pokemon')

    legendary = clean_data(1)
    regular = clean_data(0)

    print(legendary)

if __name__ == "__main__":
    main()
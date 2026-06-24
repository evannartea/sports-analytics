import pandas as pd
import sqlite3
from rapidfuzz import process

# Create database
conn = sqlite3.connect('data/data.db')

# Read CSVs
pokemon = pd.read_csv('data/pokemon.csv')
pokedex = pd.read_csv('data/pokedex.csv')

# Create tables
pokemon.to_sql('pokemon', conn, if_exists='replace', index=False)
pokedex.to_sql('pokedex', conn, if_exists='replace', index=False)

# SQL merge dataset + clean
query = """
SELECT *
FROM pokemon
"""
df_clean = pd.read_sql(query, conn)

print(df_clean)

""""
# Rename to match column headers
pokedex = pokedex.rename(columns={'name': 'Name'})


# Merge datasets
merged_df = pokemon.merge(
    pokedex[['pokedex_number', 'Name']],
    on='Name',
    how='left'
)

# Clean dataset
df_clean = merged_df[
    (merged_df['Generation'] < 5) &
    (~merged_df['Name'].str.contains('Mega|Primal', na=False))
    ]

print(df_clean.to_string())

print(process.extractOne("Deoxys", pokemon['Name']))
"""


import os
import pandas as pd
import re
from datetime import datetime

# -----------------------
# Utility Functions
# -----------------------

# def camel_to_snake(name):
#     return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

# def convert_columns(df):
#     df.columns = [camel_to_snake(col) for col in df.columns]
#     return df

# -----------------------
# Step 1: Ingest Files
# -----------------------

def ingest_files(input_folder, raw_folder):
    os.makedirs(raw_folder, exist_ok=True)
    
    for file in os.listdir(input_folder):
        if file.endswith(".csv"):
            path = os.path.join(input_folder, file)
            df = pd.read_csv(path)

            # Drop url column if it exists
            if 'url' in df.columns:
                df = df.drop(columns=['url'])

            # Convert column names
            df = convert_columns(df)

            # Add timestamp
            df['ingested_at'] = datetime.now()

            # Save to raw folder
            df.to_csv(os.path.join(raw_folder, file), index=False)
            print(f"[Ingested] {file}")

# -----------------------
# Step 2: Race Results
# -----------------------

# def transform_race_results(raw_folder, transformed_folder):
#     os.makedirs(transformed_folder, exist_ok=True)

#     circuits = pd.read_csv(os.path.join(raw_folder, 'circuits.csv'))
#     races = pd.read_csv(os.path.join(raw_folder, 'races.csv'))
#     drivers = pd.read_csv(os.path.join(raw_folder, 'drivers.csv'))
#     results = pd.read_csv(os.path.join(raw_folder, 'results.csv'))
#     constructors = pd.read_csv(os.path.join(raw_folder, 'constructors.csv'))

#     df = results \
#         .merge(drivers, on='driver_id') \
#         .merge(races, on='race_id') \
#         .merge(circuits, on='circuit_id') \
#         .merge(constructors, on='constructor_id')

#     df['driver_name'] = df['forename'] + ' ' + df['surname']
#     df['team'] = df['name_y']  # constructor name

#     final = df[[
#         'race_name', 'year', 'location', 'date',
#         'driver_name', 'number', 'nationality_x',
#         'grid', 'position_order', 'fastest_lap', 'time', 'points', 'team'
#     ]].rename(columns={
#         'number': 'driver_number',
#         'nationality_x': 'driver_nationality',
#         'position_order': 'position',
#         'time': 'race_time'
#     })

#     final.to_csv(os.path.join(transformed_folder, 'race_results.csv'), index=False)
#     print("[Transformed] race_results.csv ✔")

# -----------------------
# Step 3: Driver Standings
# -----------------------

# def transform_driver_standings(raw_folder, transformed_folder):
#     results = pd.read_csv(os.path.join(raw_folder, 'results.csv'))
#     drivers = pd.read_csv(os.path.join(raw_folder, 'drivers.csv'))
#     races = pd.read_csv(os.path.join(raw_folder, 'races.csv'))

#     df = results \
#         .merge(drivers, on='driver_id') \
#         .merge(races[['race_id', 'year']], on='race_id')

#     df['driver_name'] = df['forename'] + ' ' + df['surname']

#     grouped = df.groupby(['year', 'driver_name', 'nationality'])['points'].sum().reset_index()
#     grouped = grouped.rename(columns={
#         'year': 'race_year',
#         'nationality': 'driver_nationality',
#         'points': 'total_points'
#     })

#     grouped.to_csv(os.path.join(transformed_folder, 'driver_standings.csv'), index=False)
#     print("[Transformed] driver_standings.csv ✔")

# # -----------------------
# # Run All Steps
# -----------------------

# def run_pipeline(input_folder='input', raw_folder='raw', transformed_folder='transformed'):
#     print(" Starting Data Pipeline...\n")
#     ingest_files(input_folder, raw_folder)
#     print("\n Transforming Race Results...")
#     transform_race_results(raw_folder, transformed_folder)
#     print("\n Transforming Driver Standings...")
#     transform_driver_standings(raw_folder, transformed_folder)
#     print("\n Pipeline Completed Successfully!")


# #  Entry point
# if __name__ == '__main__':
#     run_pipeline()

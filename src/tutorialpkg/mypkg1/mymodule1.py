mock_database = {
    1: {'name': 'Alice', 'email': 'alice@example.com', 'age': 30},
    42: {'name': 'Bob', 'email': 'bob@example.com', 'age': 45},
}
import pandas as pd
from pathlib import Path
from tutorialpkg.mypkg2.mymodule2_1 import calculate_area_of_circle, fetch_user_data
# Tutor Solutions
def describe_dataframe(df):
    """ Description of the contents of the data using Pandas dataframe functions.

            Read the data from the file and perform the following operations:
            - Display the first 5 rows of the dataframe
            - Display the shape of the dataframe
            - Display the column names
            - Display the data types of the columns
            - Display summary statistics
            - Display any missing values in the dataframe

           Parameters:
           data_file (Path): Filepath of the file in csv or excel format

    """

    # Display the shape of the dataframe
    print("\nShape of the dataframe:")
    print(df.shape)

    # Display the first 5 rows of the dataframe
    print("First 5 rows of the dataframe:")
    print(df.head())

    # Display the last 5 rows of the dataframe
    print("Last 5 rows of the dataframe:")
    print(df.tail())

    # Display the column names
    print("\nColumn names:")
    print(df.columns)

    # Display the data types of the columns
    print("\nData types of the columns:")
    print(df.dtypes)

    # Display summary statistics
    print("\nSummary statistics:")
    print(df.describe())

    # Display any missing values in the dataframe
    print("Rows with missing values:")
    print(df[df.isna().any(axis=1)])

    # Print columns with missing values
    print("\nColumns with missing values:")
    print(df.isnull().sum())


if __name__ == '__main__':
    # The functions are in the modules in mypkg2. You will need to import them.

    # Calculate the area of a circle with a radius of 10. Print the result.
    area = calculate_area_of_circle(10)
    print(f"The area is {area}.")

    # Use the fetch_user_data(user_id, database) function to print the data for the user with ID 42 that is in `mock_database` variable.
    print(fetch_user_data(42, mock_database))

    # Locate the data file `paralmpics_raw.csv` relative to this file using pathlib.Path. Prove it exists.
    data_file_root = Path(__file__).parent / 'data' / 'paralympics_raw.csv'
    if data_file_root.exists():
        print(f"Data file found: {data_file_root}")
    else:
        print("Data file not found.")
    # Tutor Solutions
    # Activity 2: Filepath of the csv data file
    paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")

    # Activity 2: Filepath of the Excel data file.
    paralympics_datafile_excel = Path(__file__).parent.parent.joinpath("data", "paralympics_all_raw.xlsx")

    # Activity 2: Filepath of the NPC codes csv data file
    npc_csv = Path(__file__).parent.parent.joinpath("data", "npc_codes.csv")

    # Activity 2: Read the data from the files into a Pandas dataframe. Version includes error handling for the file read
    try:
        paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")
        events_csv_df = pd.read_csv(paralympics_datafile_csv)
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

    events_excel_df = pd.read_excel(paralympics_datafile_excel)
    medal_standings_df = pd.read_excel(paralympics_datafile_excel, sheet_name="medal_standings")
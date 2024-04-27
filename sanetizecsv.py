import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import io

# Path to the original CSV file
csv_path = 'table.csv'

# Path to the new CSV file with the additional column
new_csv_path = 'new_file.csv'

def extract_first_column(csv_file):
    # Read the CSV file using pandas
    df = pd.read_csv(csv_file, sep=';')
    # Extract the values from the first column
    first_column_values = df.iloc[:, 0].tolist()
    return first_column_values

def process_csv_row(row):
    deliver_link = row['DELIVERLINK']

    # Check if the deliver link is a URL
    if deliver_link.startswith('http://') or deliver_link.startswith('https://'):
        # Send a GET request to retrieve the content of the link
        response = requests.get(deliver_link)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the link with the label "Acessar"
            access_link = soup.find_all('a')[1]

            # Check if the link is found
            if access_link:
                # Extract the URL from the link's href attribute
                csv_url = access_link['href']

                 # Resolver a URL absoluta se for uma URL relativa
                if not csv_url.startswith('http://') and not csv_url.startswith('https://'):
                    parsed_url = urlparse(deliver_link)
                    csv_url = f"{parsed_url.scheme}://{parsed_url.netloc}{csv_url}"

                # Send a GET request to the redirected CSV URL
                csv_response = requests.get(csv_url)

                # Check if the request was successful
                if csv_response.status_code == 200:
                    # Extract the first column values from the CSV content
                    csv_content = csv_response.text
                    df_csv = pd.read_csv(io.StringIO(csv_content), sep=';')
                    first_column_values = df_csv.iloc[:, 0].tolist()

                    # Add the first column values as a comma-separated string
                    additional_data = ','.join(first_column_values)
                    row['ADDITIONAL_DATA'] = additional_data

    return row

# Read the original CSV file using pandas
df_original = pd.read_csv(csv_path, sep=';')

# Process each row
processed_rows = [process_csv_row(row) for _, row in df_original.iterrows()]

# Convert the processed rows back to a pandas DataFrame
df_processed = pd.DataFrame(processed_rows)

# Add the new fieldname for the additional column
df_processed['ADDITIONAL_DATA'] = ""

# Write the processed DataFrame to the new CSV file
df_processed.to_csv(new_csv_path, index=False, sep=';')
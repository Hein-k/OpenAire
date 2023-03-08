import json
import requests

# Set the path to your JSON file
json_file_path = "downloadttls/paths.json"

# Set the path to the folder where you want to save the downloaded files
download_folder_path = "downloadttls/output/"

# Load the JSON file
with open(json_file_path, "r") as f:
    data = json.load(f)

# Extract the download links from the JSON data
download_links = [file["links"]["self"] for file in data['files']]

# Download each file
for link in download_links:
    
    # Get the filename from the link
    filename = link.split("/")[-1]
    
    # Set the path where the file will be saved
    download_path = download_folder_path + filename
    
    # Download the file
    response = requests.get(link)
    
    # Save the file to disk
    with open(download_path, "wb") as f:
        f.write(response.content)
    

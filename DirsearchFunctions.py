import json
import requests
from concurrent.futures import ThreadPoolExecutor


def check_directory(target_url, directory):
    url = f"{target_url}/{directory}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"- Directory found: {url}")


def main(dictPath):
    target_url = input("Enter the target URL: ")

    with open(dictPath, 'r') as file:
        data = json.load(file)

    common_directories = data.get("common_directories", [])

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(check_directory, target_url, directory) for directory in common_directories]

        for future in futures:
            future.result()

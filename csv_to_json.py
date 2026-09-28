# csv_to_json.py
# Converts a CSV file into a JSON format for API consumption.

import csv
import json

def convert_csv_to_json(csv_filepath, json_filepath):
    data = []
    try:
        with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
                
        with open(json_filepath, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
            
        print(f"Successfully converted {csv_filepath} to {json_filepath}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    convert_csv_to_json("input.csv", "output.json")

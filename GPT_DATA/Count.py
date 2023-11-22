import os
import json

def read_json_files(folder_path):
    json_data = []
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if filename.endswith('.json'):
            with open(file_path, 'r') as file:
                data = json.load(file)
                json_data.append(data)
    
    return json_data

folder_path = 'concept_data/AboveBelow'
result = read_json_files(folder_path)

sum = 0
for data in result:
    sum += len(data['train'])

print(sum)
import os
import json

def collect_data(dataset):
    inputs = [example['input'] for example in dataset]
    outputs = [example['output'] for example in dataset]
    return inputs, outputs

def read_data_from_json(json_file_path, task):
    try:
        # JSON 파일을 열고 읽기 모드로 엽니다.
        with open(json_file_path, "r") as json_file:
            # JSON 데이터를 읽습니다.
            data = json.load(json_file)

            train_data = data[task]

            return train_data
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
        return None
    except KeyError:
        print(f"Key 'train' not found in the JSON data.")
        return None
    
def combine_data_from_directory(directory_path, task):
    combined_data = {
        "input": [],
        "output": [],
        "task": []
    }

    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith(".json"):
                json_file_path = os.path.join(root, filename)
                data = collect_data(read_data_from_json(json_file_path, task))
                if data is not None:
                    combined_data["input"].append(data[0])
                    combined_data["output"].append(data[1])
                    combined_data["task"].append(os.path.basename(root))

    return combined_data

output_train_directory = "/home/jovyan/Desktop/Wongyu/combined_data/train_combined.json"
output_test_directory = "/home/jovyan/Desktop/Wongyu/combined_data/test_combined.json"

train_folder_path = "/home/jovyan/Desktop/Wongyu/concept_train_data"
task_folder_path = "/home/jovyan/Desktop/Wongyu/concept_test_data"

combined_train_data = combine_data_from_directory(train_folder_path, "train")
combined_test_data = combine_data_from_directory(task_folder_path, "train")

# 데이터를 하나의 JSON 파일에 저장
with open(output_train_directory, "w") as json_file:
    json.dump(combined_train_data, json_file)

with open(output_test_directory, "w") as json_file:
    json.dump(combined_test_data, json_file)
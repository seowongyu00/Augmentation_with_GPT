import json

def read_data_from_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    

json_file_path = '/home/jovyan/Desktop/Wongyu/combined_data/train_combined.json'

data = read_data_from_json(json_file_path)

# 데이터를 저장할 빈 리스트 생성
prompt_data = []

# 여러 개의 prompt와 completion 쌍을 생성하고 리스트에 추가
for i in range(len(data["input"])):
    for j in range(len(data['input'][i])):
        prompt = 'Try solving the next ARC problem: Identify any patterns or rules in the given input images and generate the output accordingly. Hint: '

        if data['task'][i] == 'Center':
          prompt += "Place the input image in the center and add something to the output."
        elif data['task'][i] == 'MoveToBoundary':
          prompt += "You just need to move the objects attached to the boundary to random positions."
        elif data['task'][i] == 'FilledNotFilled':
          prompt += "referring to the empty spaces and the filled ones."
        elif data['task'][i] == 'InsideOutside':
          prompt += "It is a problem related to inside and outside, so think about it carefully."
        elif data['task'][i] == 'AboveBelow':
          prompt += "Filling the empty space between the upper and lower divided areas."
        elif data['task'][i] == 'ExtractObjects':
          prompt += "I added other elements besides the input object to create the output."
        elif data['task'][i] == 'Order':
          prompt += "It is a sorting problem, so think carefully about the order."
        elif data['task'][i] == 'HorizontalVertical':
          prompt += "It is a problem related to vertical and horizontal aspects, so think about it carefully."
        elif data['task'][i] == 'SameDifferent':
          prompt += "You just need to add differently shaped objects."
        elif data['task'][i] == 'ExtendToBoundary':
          prompt += "Make the connected parts that are currently connected to the boundary disconnected."
        elif data['task'][i] == 'CleanUp':
          prompt += "Adding noise-like elements."
        elif data['task'][i] == 'Copy':
          prompt += "You just need to find the identical part and randomly remove one of them."
        elif data['task'][i] == 'Count':
          prompt += "You just need to create random objects anywhere to match the quantity."
        elif data['task'][i] == 'CompleteShape':
          prompt += "You need to disrupt the completed shape."
        elif data['task'][i] == 'TopBottom3D':
          prompt += "Try to distinguish the objects in the 3D space based on their vertical positioning."
        elif data['task'][i] == 'TopBottom2D':
          prompt += "You just need to consider the top and bottom."
        completion = ''

        for k in range(len(data['input'][i])):
            if j != k:
                prompt += f"Input: {data['output'][i][k]}, output: {data['input'][i][k]}"
        prompt += f"Input: {data['output'][i][k]}"
        completion += f"The output I predicted is {data['input'][i][k]}"

        prompt_data.append({"prompt": prompt, "completion": completion})
print(len(prompt_data))

# 결과 확인
for item in prompt_data:
    print(item)

file_path = 'finetune_train_data.json'  # 파일 경로 및 이름 설정
with open(file_path, "w") as json_file:
    json.dump(prompt_data, json_file)


json_file_path = '/home/jovyan/Desktop/Wongyu/combined_data/test_combined.json'

data = read_data_from_json(json_file_path)

# 데이터를 저장할 빈 리스트 생성
prompt_data = []

# 여러 개의 prompt와 completion 쌍을 생성하고 리스트에 추가
for i in range(len(data["input"])):
    for j in range(len(data['input'][i])):
        prompt = 'Try solving the next ARC problem: Identify any patterns or rules in the given input images and generate the output accordingly. Hint: '

        if data['task'][i] == 'Center':
          prompt += "Place the input image in the center and add something to the output."
        elif data['task'][i] == 'MoveToBoundary':
          prompt += "You just need to move the objects attached to the boundary to random positions."
        elif data['task'][i] == 'FilledNotFilled':
          prompt += "referring to the empty spaces and the filled ones."
        elif data['task'][i] == 'InsideOutside':
          prompt += "It is a problem related to inside and outside, so think about it carefully."
        elif data['task'][i] == 'AboveBelow':
          prompt += "Filling the empty space between the upper and lower divided areas."
        elif data['task'][i] == 'ExtractObjects':
          prompt += "I added other elements besides the input object to create the output."
        elif data['task'][i] == 'Order':
          prompt += "It is a sorting problem, so think carefully about the order."
        elif data['task'][i] == 'HorizontalVertical':
          prompt += "It is a problem related to vertical and horizontal aspects, so think about it carefully."
        elif data['task'][i] == 'SameDifferent':
          prompt += "You just need to add differently shaped objects."
        elif data['task'][i] == 'ExtendToBoundary':
          prompt += "Make the connected parts that are currently connected to the boundary disconnected."
        elif data['task'][i] == 'CleanUp':
          prompt += "Adding noise-like elements."
        elif data['task'][i] == 'Copy':
          prompt += "You just need to find the identical part and randomly remove one of them."
        elif data['task'][i] == 'Count':
          prompt += "You just need to create random objects anywhere to match the quantity."
        elif data['task'][i] == 'CompleteShape':
          prompt += "You need to disrupt the completed shape."
        elif data['task'][i] == 'TopBottom3D':
          prompt += "Try to distinguish the objects in the 3D space based on their vertical positioning."
        elif data['task'][i] == 'TopBottom2D':
          prompt += "You just need to consider the top and bottom."
        completion = ''

        for k in range(len(data['input'][i])):
            if j != k:
                prompt += f"Input: {data['output'][i][k]}, output: {data['input'][i][k]}"
        prompt += f"Input: {data['output'][i][k]}"
        completion += f"The output I predicted is {data['input'][i][k]}"

        prompt_data.append({"prompt": prompt, "completion": completion})
print(len(prompt_data))

# 결과 확인
for item in prompt_data:
    print(item)

file_path = 'finetune_test_data.json'  # 파일 경로 및 이름 설정
with open(file_path, "w") as json_file:
    json.dump(prompt_data, json_file)
import jsonlines

def read_jsonl(file_path):
    data_list = []
    with jsonlines.open(file_path) as reader:
        for obj in reader:
            data_list.append(obj)
    return data_list

def write_jsonl(data_list, save_path):
    with jsonlines.open(save_path, mode='w') as writer:
        for data in data_list:
            writer.write(data)

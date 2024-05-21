import os

def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return sum(1 for _ in file)

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(content)

def main():
    folder_path = './'  
    file_names = ['1.txt', '2.txt', '3.txt']
    
    files_info = []
    
    for file_name in file_names:
        full_path = os.path.join(folder_path, file_name)
        line_count = count_lines(full_path)
        files_info.append((file_name, line_count, read_file(full_path)))
    
    
    files_info.sort(key=lambda x: x[1])
    
    result_content = []
    
    for file_name, line_count, lines in files_info:
        result_content.append(f"{file_name}\n")
        result_content.append(f"{line_count}\n")
        result_content.extend(lines)
        result_content.append("\n")  
    
    write_to_file('result.txt', result_content)

if __name__ == "__main__":
    main()

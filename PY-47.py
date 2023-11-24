def open_n_read(file_name):
    """read and print only"""
    with open(file_name, 'r') as file:
        print(file.read())


def append_data(file_name, data):
    """append data to the file"""
    with open(file_name, 'a') as file:
        file.write(data)


def line_formation(file_name, length=5):
    """rewriting text in a file with a given line length"""
    with open(file_name, 'r') as old_file:
        words = old_file.read().replace('\n', ' ').split(' ')
    if length < 1:
        length = 1
    elif length > len(words):
        length = len(words)
    with open(file_name, 'w') as new_file:
        for i in range(0, len(words), length):
            new_file.write(' '.join(words[i:i+length]))
            new_file.write('\n')
    print('File has been reformed:', '\n' if len(words) > 0 else 'File is empty')
    open_n_read(file_name)


#open_n_read('lorum.txt')
#append_data('lorum.txt', 'Ave Satan')
#line_formation('lorum.txt', 7)


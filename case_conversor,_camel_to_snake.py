def convert_token(token):
    cursor = 0
    converted_token = ''
    while cursor < len(token):
        if cursor > 0 and token[cursor].isupper() and token[cursor - 1] != '_':
            converted_token += '_' + token[cursor].lower()
        elif cursor > 0 and token[cursor - 1].isupper() and converted_token[-1].islower():
            converted_token += token[cursor].lower()
        else:
            converted_token += token[cursor]
        cursor += 1
    return converted_token

filename = input('Digit input file: ')

input_file_content = open(filename).read()

output_file = open('.'.join(filename.split('.')[:-1]) + '_.' + filename.split('.')[-1], 'w')

cursor_1 = 0
cursor_2 = 0
valid = False

token = ''

while cursor_2 < len(input_file_content):
    if not valid and (input_file_content[cursor_2].isalpha() or input_file_content[cursor_2] == '_'):
        cursor_1 = cursor_2
        valid = True

    elif valid and not (input_file_content[cursor_2].isalnum() or input_file_content[cursor_2] == '_'):
        valid = False
        token = input_file_content[cursor_1:cursor_2]
        output_file.write(convert_token(token))
        output_file.write(input_file_content[cursor_2])

    elif not valid and not (input_file_content[cursor_2].isalpha() or input_file_content[cursor_2] == '_'):
        output_file.write(input_file_content[cursor_2])

    if input_file_content[cursor_2] == '\\':
        cursor_2 += 1
        output_file.write(input_file_content[cursor_2])

    cursor_2 += 1
"""
    Hides message into bmp image.
    Structure is about splitting message to 2 bits and switching them with last 2 bits of rgb bytes.
    (First 8 bytes of rgb data)'s last 2 bits keep information of how long message is.
    So that we can get message bits more effectively.
"""


def bury_message(img_path, message, new_name='Stega.bmp'):
    with open(img_path, mode='rb') as img:
        img_data = img.read()

    rgb_data = img_data[54:]
    binary_data_to_insert = list()
    b_count = len(message) * 4

    for char in message:
        bits = bin(ord(char))[2:].zfill(8)
        binary_data_to_insert.append(bits[:2])
        binary_data_to_insert.append(bits[2:4])
        binary_data_to_insert.append(bits[4:6])
        binary_data_to_insert.append(bits[6:8])

    new_byte_array = bytes()
    bb_count = bin(b_count)[2:].zfill(16)

    for b in range(8):
        edited_byte_str = bin(rgb_data[b])[2:].zfill(8)[:6] + bb_count[b*2: b*2+2]
        new_byte_array += int(edited_byte_str, 2).to_bytes(2, byteorder='big')

    for rgb_byte, insterting_bits in zip(rgb_data, binary_data_to_insert):
        edited_byte_str = bin(rgb_byte)[2:].zfill(8)[:6] + insterting_bits
        new_byte_array += int(edited_byte_str, 2).to_bytes(2, byteorder='big')

    final_data = img_data[:54] + new_byte_array + img_data[54+b_count + 8:]
    with open(new_name, mode='wb') as f:
        f.write(final_data)


def dig_up_message(img_path):
    decrypted_byte_array = ''
    message_len = 0
    with open(img_path, mode='rb') as f:
        new_rgb_bytes = f.read()[54:]
        for index, rgb_byte in enumerate(new_rgb_bytes):
            decrypted_byte_array += bin(rgb_byte)[2:].zfill(2)
            if index == 15:
                message_len = ''
                for i in range(0, 32, 4):
                    message_len += bin(int(decrypted_byte_array[i:i + 4], 2))[2:].zfill(2)
                message_len = int(message_len, 2)
                decrypted_byte_array = str()
            if index == message_len*4 + 15:
                break
    decrypted_bits = ''
    message = str()
    for i in range(0, message_len*4, 4):
        decrypted_bits += bin(int(decrypted_byte_array[i:i+4], 2))[2:].zfill(2)
    for i in range(0, len(decrypted_bits), 8):
        message += chr(int(decrypted_bits[i: i+8], 2))
    return message


"""
bury_message('test.bmp', 'very very secret message', 'Buried.bmp')
buried_message = dig_up_message('Buried.bmp')
print(buried_message)
"""

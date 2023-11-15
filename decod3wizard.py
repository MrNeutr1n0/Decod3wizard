# Carefully read the readme.md before running the code
# Modifying any part of the code may cause it to malfunction

import hashlib
import base64
import binascii
import codecs
import textwrap
from prettytable import PrettyTable

def print_banner():
    print("		============================================")
    print("	       |					    |")
    print("	       ||       {!}   Decod3wizard   {!}           ||")
    print("	       ||      by Abid Ahmad [@MrNeoTr1n0]         ||")
    print("	       |					    |")
    print("		============================================")
    print("")
    print("	[ Identify Hash/Encodings --> Decode continuously like magic  ] ")
    print()

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def clean_decoded_value(decoded_value):
    if isinstance(decoded_value, bytes):
        return decoded_value.decode('utf-8', 'ignore').strip()
    return decoded_value.strip()

def is_readable(s):
    return all(32 <= ord(c) <= 126 for c in s)

def identify_and_decode(input_str):
    if is_ascii(input_str):
        try:
            decoded_bytes = base64.b64decode(input_str)
            decoded_str = clean_decoded_value(decoded_bytes)
            return "Base64", decoded_str
        except binascii.Error:
            pass

    encoding_types = ['hex', 'rot_13', 'url']
    for encoding in encoding_types:
        try:
            decoded_bytes = codecs.decode(input_str, encoding)
            decoded_str = clean_decoded_value(decoded_bytes)
            return encoding.capitalize(), decoded_str
        except (binascii.Error, ValueError):
            pass

    hash_types = {
        32: "MD5",
        40: "SHA-1",
        64: "SHA-256",
        56: "SHA-224",
        96: "SHA-384",
        128: "SHA-512",
    }
    hash_length = len(input_str)
    if hash_length in hash_types:
        return hash_types[hash_length], input_str

    return "Unrecognized", input_str

def create_table():
    table = PrettyTable()
    table.field_names = ["Type", "Value"]
    table.align = "l"  # Left align the columns
    table.border = True
    table.header = True
    table.horizontal_char = "-"
    table.vertical_char = "|"
    table.junction_char = "+"
    return table

def wrap_text(text, width=70):
    """Wrap text for better display in the table."""
    return '\n'.join(textwrap.wrap(text, width))

def add_table_row(table, type_identified, value):
    table.add_row([type_identified, wrap_text(value)])
    table.add_row(['', ''])  # Add an empty row for separation

def single_mode():
    input_hash = input("Enter the hash or encoded value: ")
    table = create_table()

    type_identified, decoded_value = identify_and_decode(input_hash)
    add_table_row(table, type_identified, input_hash)
    
    if decoded_value != input_hash:
        add_table_row(table, "Decoded", decoded_value)

    print(table)

def magic_mode():
    input_hash = input("Enter the hash or encoded value: ")
    table = create_table()

    max_depth = 10  # Maximum depth of recursive decoding

    for _ in range(max_depth):
        if not is_readable(input_hash):
            break

        type_identified, decoded_value = identify_and_decode(input_hash)
        add_table_row(table, type_identified, input_hash)

        if decoded_value == input_hash:
            break

        input_hash = decoded_value

    print(table)

def main():
    print_banner()
    print("  [1] Single Mode")
    print("  [2] Magic Mode")
    mode = input("        >> ")

    if mode == "1":
        single_mode()
    elif mode == "2":
        magic_mode()
    else:
        print("Invalid mode")

if __name__ == "__main__":
    main()

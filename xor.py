""" Tenta converter um texto para numero, aplique um xor e escreva a saida para um arquivo,
no mesmo programa adicione a opção de ler um arquivo que desfaça o xor e converta a mensagem cifrada para texto """



def encrypt_text(text, key):
    ciphertext_nums = []
    for i, char in enumerate(text):
        key_char = key[i % len(key)]
        original_char_code = ord(char)
        code_char_key = ord(key_char) 
        encrypted_code = original_char_code ^ code_char_key
        ciphertext_nums.append(encrypted_code)
    return ciphertext_nums

def decipher_numbers(list_numbers, key):
    
    deciphered_text = ""
    for i, num in enumerate(list_numbers):
        key_char = key[i % len(key)]
        code_char_key = ord(key_char)
        encrypted_code = num ^ code_char_key
        deciphered_text += chr(encrypted_code)
    return deciphered_text

def salvar_arquivo(file_name, encrypted_data):
   
    try:
        with open(file_name, 'wb') as f:
            f.write(bytes(encrypted_data))
        print(f"\n Sucesso Mensagem cifrada salva em '{file_name}'")
    except IOError as e:
        print(f"\n Erro  Não foi possível salvar o arquivo: {e}")

def read_file(file_name):
    
    try:
        with open(file_name, 'rb') as f:
            data_bytes = f.read()
            list_numbers = list(data_bytes)
            print(f"\nSucesso Arquivo '{file_name}' lido.")
            return list_numbers
    except FileNotFoundError:
        print(f"\n Erro Arquivo '{file_name}' não encontrado.")
        return None
    except IOError as e:
        print(f"\n Erro Não foi possível ler o arquivo: {e}")
        return None



""" Tenta converter um texto para numero, aplique um xor e escreva a saida para um arquivo,
no mesmo programa adicione a opção de ler um arquivo que desfaça o xor e converta a mensagem cifrada para texto """



def encrypt_text(text: str, key:int) ->str:
    return ''.join(chr(ord(c) ^ key) for c in text)


def salvar_arquivo(file_name, encrypted_data):
    try:
        with open(file_name, 'w', encoding="utf-8") as f:  # <-- modo texto
            f.write(encrypted_data)
        print(f"\n Sucesso: Mensagem cifrada salva em '{file_name}'")
    except IOError as e:
        print(f"\n Erro: Não foi possível salvar o arquivo: {e}")

def read_file(file_name):
    try:
        with open(file_name, 'r', encoding="utf-8") as f:  # <-- modo texto
            data_str = f.read()
            print(f"\n Sucesso: Arquivo '{file_name}' lido.")
            return data_str
    except FileNotFoundError:
        print(f"\n Erro: Arquivo '{file_name}' não encontrado.")
        return None
    except IOError as e:
        print(f"\n Erro: Não foi possível ler o arquivo: {e}")
        return None


# Exemplo de uso

msg = "jeiel"
key = 123


encrypted = encrypt_text(msg, key)
salvar_arquivo("bb.bin", encrypted)
print("codificada: ", encrypted)

loaded = read_file("bb.bin")

print(" Decifrada:", encrypt_text(encrypted, key))



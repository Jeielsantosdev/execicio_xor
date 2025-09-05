from xor import *
import getpass

def main():
    
    while True:
        print("\n--- Criptografia com XOR ---")
        print("1. Cifrar mensagem para arquivo")
        print("2. Decifrar mensagem de arquivo")
        print("3. Sair")
        
        opcoes = input("Escolha uma opção (1, 2 ou 3): ")
        
        if opcoes == '1':
            mensage = input("Digite a mensagem a ser cifrada: ")
            key = getpass.getpass("Digite a key secreta: ")
            output_file = input("Digite o nome do arquivo para salvar a mensagem cifrada (ex: dados.bin): ")
            
            if not key:
                print("\nErro A key não pode estar em branco.")
                continue

            encrypted_data = encrypt_text(mensage, key)
            salvar_arquivo(output_file, encrypted_data)

            
        elif opcoes == '2':
            input_file = input("Digite o nome do arquivo a ser decifrado (ex: dados.bin): ")
            key = getpass.getpass("Digite a key secreta: ")

            if not key:
                print("\nErro A key não pode estar em branco.")
                continue

            encrypted_data = read_file(input_file)
            if encrypted_data:
                original_message = decipher_numbers(encrypted_data, key)
                print("-" * 30)
                print(f"Mensagem decifrada: {original_message}")
                print("-" * 30)

        elif opcoes == '3':
            print("Saindo do programa. Até mais!")
            break
            
        else:
            print("\n[AVISO] Opção inválida. Por favor, escolha 1, 2 ou 3.")


# Executa o programa
if __name__ == "__main__":
    main() 

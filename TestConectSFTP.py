import paramiko



def test_sftp_connection(host, port, username, password):
    try:
        # Cria um objeto de transporte SSH
        transport = paramiko.Transport((host, int(port)))
        transport.connect(username=username, password=password)

        # Cria um objeto SFTP a partir do transporte SSH
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Testa a conexão SFTP listando o diretório remoto
        dirlist = sftp.listdir('.')
        print("Diretório remoto:")
        print(dirlist)

        # Encerra a conexão SFTP
        sftp.close()

        # Encerra o transporte SSH
        transport.close()

        # Retorna um status de sucesso
        return True

    except paramiko.AuthenticationException:
        # Retorna o tipo de erro para autenticação inválida
        return "Autenticação inválida"

    except paramiko.SSHException:
        # Retorna o tipo de erro para erro de conexão SSH
        return "Erro de conexão SSH"

    except Exception as e:
        # Retorna o tipo de erro genérico
        return str(e)

if __name__ == '__main__':
    
    print('>>>>>>>>>>>>>>>>>>>>>>>>>Teste Conexão SFTP>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('\n')
    print('Informar dados de acesso da conexão SFTP')
    print('\n')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>Teste Conexão SFTP>>>>>>>>>>>>>>>>>>>>>>>>>\n')
    # Lê os argumentos de linha de comando
    
    print(f"\nInforme o host (sem http):")
    #ex: 'ci-lcb-sftp-ronda-prd01.eastus2.azurecontainer.io'
    host = input()
    
    print(f"\nInforme a porta de conexão:")
    #ex: '22'
    port = input() 
    print(f"\nInforme username da conexão:")
    #ex: 'amsaccess'
    username = input()
    
    print(f"\nInforme password da conexão:")
    #ex: '@rc3L07sftplcbronda'
    password = input()
    
    print(f"\nInforme hostkey da conexão:(enter para None)")
    #'IAeRwRH4efzv8zEhOW6l3E2fK9rjTQqzT0+1fbpG2vI'
    hostkeys = input()

    print('Teste...\n')
    # Testa a conexão SFTP
    result = test_sftp_connection(host, port, username, password)

    # Exibe o resultado
    if result == True:
        print(f"\nConexão SFTP bem-sucedida.\n")
    else:
        print("Falha na conexão SFTP. Tipo de erro:", result)

    # Espera pelo usuário pressionar Enter para encerrar o programa
    input("\nPressione Enter para sair.")
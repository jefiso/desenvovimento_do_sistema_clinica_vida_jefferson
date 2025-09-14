def cadastrar_paciente(pacientes):
    '''permite cadastrar novo paciente'''
    try:
        nome = input('Nome do Paciante:')
        idade = int(input('Idade:'))
        telefone = input('telefone:')
        #crie um dicionario para o paciente
        novo_paciente = {
            "nome" = nome,
            'idade' = idade,
            'telefone' = telefone
        }
        # adiciona o dicionario a lista de paciente
        pacientes.append(novo_paciente)
        print('Paciente cadastrado com sucesso!.')

    except ValueError:
        print('ERRO: A idade deve ser um numero inteiro.')
    except Exception as e:
        print(f"Ocorreu um erro ao cadastrar o paciente: {e}")

        
print("Olá! Eu sou seu primeiro chatbot em Python.")
print("Digite 'sair' para encerrar.\n")

while True:
    mensagem = input("Você: ").lower()

    if mensagem == "oi":
        print("Bot: Olá! Tudo bem?")
    elif mensagem == "como você está":
        print("Bot: Estou funcionando perfeitamente 😄")
    elif mensagem == "qual seu nome":
        print("Bot: Sou um chatbot criado em Python.")
    elif mensagem == "sair":
        print("Bot: Até logo!")
        break
    else:
        print("Bot: Ainda estou aprendendo. Não entendi isso.")

from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
#myChatBot.loadModel()
#criar o modelo
myChatBot.createModel()

print('\033[1;35m'+"Bem vindo ao Chatbot"+'\033[0;0m')


pergunta = input("como posso te ajudar?")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print('\033[34m'+resposta + "   ["+intencao[0]['intent']+"]"+'\033[0;0m')


while (intencao[0]['intent']!="despedida"):
    pergunta = input("posso lhe ajudar com algo a mais?")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print('\033[34m'+resposta + "   ["+intencao[0]['intent']+"]"+'\033[0;0m')

print("Foi um prazer atendê-lo")

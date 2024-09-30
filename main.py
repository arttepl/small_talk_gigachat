import yaml
from langchain_core.messages import HumanMessage
from langchain_community.chat_models.gigachat import GigaChat

# Загрузка конфигурационного файла
try:
    with open("config.yaml") as f:
        config = yaml.safe_load(f)
except FileNotFoundError as e:
    print(f'Не был найден конфигурационный файл, завершение работы программы')
    exit(0)

# Авторизация в GigaChat
conn = GigaChat(
    credentials=config.get('credential_token'),
    scope="GIGACHAT_API_PERS",
    model="GigaChat",
    # Отключает проверку наличия сертификатов НУЦ Минцифры
    verify_ssl_certs=False,
    streaming=False
)

messages = []

while(True):
    user_input = input("Пользователь: ")
    messages.append(HumanMessage(content=user_input))
    res = conn.invoke(messages)
    messages.append(res)
    print("GigaChat: ", res.content)
from database import Chat, get_session


session = get_session()

new_user = Chat(name="Чат 2")
session.add(new_user)
session.commit()

all_chats = session.query(Chat).where(Chat.id == 1)
for chat in all_chats:
    print(chat.id, chat.name)

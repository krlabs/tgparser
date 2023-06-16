from telethon.sync import TelegramClient
 
import csv
 
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

api_id =  APP_ID
api_hash = 'APP_HASH'
phone = '+telegramphonenumber'
 
client = TelegramClient(phone, api_id, api_hash)
client.start()
chats = []
last_date = None
size_chats = 2000
groups=[]
result = client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=size_chats,
            hash = 0
        ))
chats.extend(result.chats)
for chat in chats:
   try:
       if chat.megagroup== True:
           groups.append(chat)
   except:
       continue
print('Оберіть номер групи зі списку:')
i=0
for g in groups:
   print(str(i) + '- ' + g.title)
   i+=1
g_index = input("Введіть потрібну цифру: ")
target_group=groups[int(g_index)]
print('Парсимо користувачів...')
all_participants = []
all_participants = client.get_participants(target_group)
 
print('Зберігаємо в  файл...')
with open("members.csv","w",encoding='UTF-8') as f:
   writer = csv.writer(f,delimiter=",",lineterminator="\n")
   writer.writerow(['username','name','group'])
   for user in all_participants:
       if user.username:
           username= user.username
       else:
           username= ""
       if user.first_name:
           first_name= user.first_name
       else:
           first_name= ""
       if user.last_name:
           last_name= user.last_name
       else:
           last_name= ""
       name= (first_name + ' ' + last_name).strip()
       writer.writerow([username,name,target_group.title])     
print('Парсинг учасників групи успішно виконано.')

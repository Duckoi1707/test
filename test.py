import time
import random
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetAllStickersRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID
api_id = 17349
api_hash = '344583e45741c457fe1862106095a5eb'
#api id với hash để im ko cần thay
phone = '+'
session_file = 'robin'  # tên string
password = ''  # khong có pass 2 thì để im


rephi = [
    "Tâm sự ib nè",
    "Hi anh",
    "Tâm sự như nàooooo",
    "<3",
    "Chào anh?",
    "Hí lu",
    "Hi cho xem ciu i",
    "Hi bạn??",
    "Hi chào nha!!",
    "nhận shôw",
    "❌❌Nhận shôw uy tín, có phí nha m.n ❤️",
    "Xâu móc rên thủ dâm theo yêu cầu thì liên hệ em nha 🥰🥰🥰",
    "E nhân shôw uy tín",
    "Gọi video lên đỉnh cùng em không anh ơi",
    "Ai tâm sự cùng bé ko",
    "Cho tui chịch với",
    "Em sv năm 3 hutech",
    "Có zai vũng tàu nào lọt đây ko ???"
    "Em tìm bạn xã giao ạ, ai thích thì cứ nhắn e",
    "Em caII phí ai cần nhắn em nha",
    "Gọi video mà làm nhau nứng thì liên hệ Em ngay 🧚🏻‍♀️🧚🏻‍♀️🧚🏻‍♀️. Có phí đó nha",
    "có clip gửi tôi phát",
    "Cần tuyen phi cong",
    ]
inbox = [
    "Xem live thì tải app **QQL849.COM** vào phòng 291 của em nhé!",
    "Em đang trên **QQL849.COM** live rồi",
    "Tham gia nhóm chat cùng tụi em: https://t.me/+vlq2hqZTx4tlNTBl",
    "Hi anh",
    "Gửi cu đi",
    "Thôi nha",
    "Em ngủ xí",
    "Anh vào nhóm em chơi đi",
    "https://t.me/+vlq2hqZTx4tlNTBl",
    "Nứng cac thì vô t.me/vetmang có đầy link ngon",
    ]
group_id = [-1001721890611]  # không hoạt động gr nào thì chèn id gr đó vô
if __name__ == '__main__':
    # sử dụng sequential_updates=True để reply người tag
    client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)


    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private:
            time.sleep(1)
            await client.send_message(event.message.from_id, random.choice(inbox))  # chat riêng
        if event.is_group:  # chat trong group
            print(event,event.chat_id)
            if event.chat_id anot in group_id:
                # cập nhật khi có người tag hoặc rep
                from_ = await event.client.get_entity(event.from_id)
                if from_.bot == False: #tuỳ chọn tin nhắn
                    return
                print(from_.first_name, from_.last_name,
                      event.message.text, event.from_id)
                text = str(event.message.message)
                if text != -1:
                    await event.reply(random.choice(rephi))
                    pass
    print(time.asctime(), '-', 'Auto-replying...')
    client.start(phone, password)
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')
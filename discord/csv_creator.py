from datetime import datetime
from random import choice

names = ['FSF', 'GNU', 'BSD', 'Stallman the best', 'Vim']
image_uls = ['little devil', 'tux', 'fish', 'vim logo', 'some random guy']
texts = [
    'The Free Software Foundation is a non-profit organization founded by Richard Stallman ',
    'The Linux kernel is a free and open-source monolithic  modular multitasking  Unix-like operating system kernel',
    'FreeBSD is an operating system used to power modern servers desktops and embedded platforms ',
    'Vim is a highly configurable text editor built to make creating and changing any kind of text very efficient',
]
nicknames = ['John', 'Stallman', 'Bramm', 'Torvalds', 'Gates', 'Cook']

if __name__ == "__main__":
    with open('data.scv', 'w+') as file:
        data: list[str] = [
            '\n',
            'name,image_url,server,\n',
            *[','.join([
                choice(names), choice(image_uls), '\n'
            ]) for i in range(1, 200)],
            '\n',
            'nickname,image_url,user,\n',
            *[','.join([
                choice(nicknames), choice(image_uls), '\n'
            ]) for i in range(1, 200)],
            '\n',
            'name,server_id,chat,\n',
            *[','.join([
                choice(names), str(i), '\n'
            ]) for i in range(1, 200)],
            '\n',
            'time,text,read,chat_id,sender_id,message,\n',
            *[','.join([
                datetime.now().isoformat(), choice(texts), str(bool(i % 2)), str(int(i / 2)), str(int(i / 2)), '\n'
            ]) for i in range(2, 400)],
        ]
        file.writelines(data)

import datetime
import logging
import configparser
from html import escape
import random
import datetime

from pymongo import ASCENDING, MongoClient
import telebot
from telebot import types, util

# Configuração do logging
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

config = configparser.ConfigParser()
config.read('bot.conf')

TOKEN = config['PITUCHOBOT']['TOKEN']
MONGO_CON = config['PITUCHOBOT']['MONGO_CON']
GROUP_LOG = config['PITUCHOBOT']['PITUCHO_GROUP']
NAME_BOT = config['PITUCHOBOT']['BOT_NAME']
USERNAME_BOT = config['PITUCHOBOT']['BOT_USERNAME']
OWNER = int(config['PITUCHOBOT']['OWNER_ID'])


client = MongoClient(MONGO_CON)
db = client['pitucho_bot']


bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

# Comandos
bot.set_my_commands(
    [
        telebot.types.BotCommand('/start', 'Início do bot'),
        telebot.types.BotCommand(
            '/felicidade', 'Medidor de nível de felicidade 🙂'
        ),
        telebot.types.BotCommand('/raiva', 'Medidor de nível de raiva 🤬'),
        telebot.types.BotCommand(
            '/estado', 'Adivinha em qual estado você mora 🌏'
        ),
        telebot.types.BotCommand('/stickers', 'Envia uma figurinha'),
        telebot.types.BotCommand(
            '/presidente', 'Adivinha quem é o seu presidente 🇧🷷'
        ),
        telebot.types.BotCommand('/sorte', 'Veja a sua sorte'),
        telebot.types.BotCommand('/orientacao', 'Adivinha o seu gênero ⚧'),
        telebot.types.BotCommand(
            '/casamento', 'Adivinha a data do seu casamento 👨‍❤️‍👨'
        ),
        telebot.types.BotCommand(
            '/nascimento', 'Adivinha a data do seu nascimento'
        ),
        telebot.types.BotCommand('/morte', 'Adivinha a data da sua morte 😵'),
        telebot.types.BotCommand(
            '/filho',
            'Adivinha o nome, gênero e quando você vai ter um filho 👶',
        ),
        telebot.types.BotCommand('/signo', 'Adivinha o seu signo ♈️'),
        telebot.types.BotCommand('/religiao', 'Adivinha a sua religião 🤍'),
        telebot.types.BotCommand(
            '/ator', 'Adivinha o seu ator/atriz preferida 🥰'
        ),
        telebot.types.BotCommand('/altura', 'Adivinha a sua altura 🤏'),
        telebot.types.BotCommand('/idade', 'Adivinha a sua idade 🎯'),
        telebot.types.BotCommand(
            '/sistema', 'Adivinha o seu socioeconômico-políticos 🎫'
        ),
        telebot.types.BotCommand('/profissao', 'Adivinha a sua profissão 💼'),
        telebot.types.BotCommand(
            '/saudades', 'Escolha de 0 a 100 quanto de saudades você tem 😰'
        ),
        telebot.types.BotCommand(
            '/ciumes', 'Escolha de 0 a 100 quanto de ciúmes você tem 😠'
        ),
        telebot.types.BotCommand(
            '/apaixonado', 'Medidor de nível de paixão 😍'
        ),
        telebot.types.BotCommand('/gado', 'Medidor de nível de gado 🐮'),
        telebot.types.BotCommand('/tpm', 'Medidor de nível de TPM 😤'),
        telebot.types.BotCommand(
            '/gostosura', 'Medidor de nível de gostosura 😈'
        ),
        telebot.types.BotCommand('/chato', 'Medidor de nível de chatice 😒'),
        telebot.types.BotCommand('/burro', 'Medidor de nível de burrice 🥴'),
        telebot.types.BotCommand('/treteiro', 'Medidor de nível de tretas 🤬'),
        telebot.types.BotCommand(
            '/sexo', 'Medidor de nível de potencial sexual 🔞'
        ),
        telebot.types.BotCommand('/fake', 'Descobre se você é fake 🛃'),
        telebot.types.BotCommand(
            '/serbanido', 'Descobre se você vai ser banido 🚷'
        ),
        telebot.types.BotCommand(
            '/seradm', 'Descobre se você pode ser adm 👮‍♀️'
        ),
        telebot.types.BotCommand(
            '/filme', 'Adivinha a categoria de filme preferido 🎬'
        ),
        telebot.types.BotCommand('/clima', 'Adivinha o seu clima preferido 🌪'),
        telebot.types.BotCommand(
            '/numerodasorte', 'Gera o seu número da sorte 🎰'
        ),
        telebot.types.BotCommand('/desafio', 'Propõe um desafio para você 🏆'),
        telebot.types.BotCommand(
            '/musica', 'Adivinha o seu estilo musical preferido 🎼'
        ),
        telebot.types.BotCommand('/jogo', 'Envia um jogo aleatório 🎮'),
        telebot.types.BotCommand('/cor', 'Adivinha a sua cor preferida 🔴'),
        telebot.types.BotCommand(
            '/crush', 'Adivinha a primeira letra do seu crush 🥰'
        ),
        telebot.types.BotCommand('/time', 'Adivinha o seu time do coração 😂'),
        telebot.types.BotCommand('/fruta', 'Adivinha a sua fruta preferida 🍎'),
        telebot.types.BotCommand(
            '/curiosidade',
            'Envia aleatoriamente uma curiosidade sobre o mundo 👀',
        ),
        telebot.types.BotCommand('/sigma', 'Mede o seu nível sigma 🗿🍷'),
    ],
    telebot.types.BotCommandScope('all_private_chats'),
)

bot.set_my_commands(
    [
        telebot.types.BotCommand(
            '/felicidade', 'Medidor de nível de felicidade 🙂'
        ),
        telebot.types.BotCommand('/raiva', 'Medidor de nível de raiva 🤬'),
        telebot.types.BotCommand(
            '/estado', 'Adivinha em qual estado você mora 🌏'
        ),
        telebot.types.BotCommand('/stickers', 'Envia uma figurinha'),
        telebot.types.BotCommand(
            '/presidente', 'Adivinha quem é o seu presidente 🇧🷷'
        ),
        telebot.types.BotCommand('/sorte', 'Veja a sua sorte'),
        telebot.types.BotCommand('/orientacao', 'Adivinha o seu gênero ⚧'),
        telebot.types.BotCommand(
            '/casamento', 'Adivinha a data do seu casamento 👨‍❤️‍👨'
        ),
        telebot.types.BotCommand(
            '/nascimento', 'Adivinha a data do seu nascimento'
        ),
        telebot.types.BotCommand('/morte', 'Adivinha a data da sua morte 😵'),
        telebot.types.BotCommand(
            '/filho',
            'Adivinha o nome, gênero e quando você vai ter um filho 👶',
        ),
        telebot.types.BotCommand('/signo', 'Adivinha o seu signo ♈️'),
        telebot.types.BotCommand('/religiao', 'Adivinha a sua religião 🤍'),
        telebot.types.BotCommand(
            '/ator', 'Adivinha o seu ator/atriz preferida 🥰'
        ),
        telebot.types.BotCommand('/altura', 'Adivinha a sua altura 🤏'),
        telebot.types.BotCommand('/idade', 'Adivinha a sua idade 🎯'),
        telebot.types.BotCommand(
            '/sistema', 'Adivinha o seu socioeconômico-políticos 🎫'
        ),
        telebot.types.BotCommand('/profissao', 'Adivinha a sua profissão 💼'),
        telebot.types.BotCommand(
            '/saudades', 'Escolha de 0 a 100 quanto de saudades você tem 😰'
        ),
        telebot.types.BotCommand(
            '/ciumes', 'Escolha de 0 a 100 quanto de ciúmes você tem 😠'
        ),
        telebot.types.BotCommand(
            '/apaixonado', 'Medidor de nível de paixão 😍'
        ),
        telebot.types.BotCommand('/gado', 'Medidor de nível de gado 🐮'),
        telebot.types.BotCommand('/tpm', 'Medidor de nível de TPM 😤'),
        telebot.types.BotCommand(
            '/gostosura', 'Medidor de nível de gostosura 😈'
        ),
        telebot.types.BotCommand('/chato', 'Medidor de nível de chatice 😒'),
        telebot.types.BotCommand('/burro', 'Medidor de nível de burrice 🥴'),
        telebot.types.BotCommand('/treteiro', 'Medidor de nível de tretas 🤬'),
        telebot.types.BotCommand(
            '/sexo', 'Medidor de nível de potencial sexual 🔞'
        ),
        telebot.types.BotCommand('/fake', 'Descobre se você é fake 🛃'),
        telebot.types.BotCommand(
            '/serbanido', 'Descobre se você vai ser banido 🚷'
        ),
        telebot.types.BotCommand(
            '/seradm', 'Descobre se você pode ser adm 👮‍♀️'
        ),
        telebot.types.BotCommand(
            '/filme', 'Adivinha a categoria de filme preferido 🎬'
        ),
        telebot.types.BotCommand('/clima', 'Adivinha o seu clima preferido 🌪'),
        telebot.types.BotCommand(
            '/numerodasorte', 'Gera o seu número da sorte 🎰'
        ),
        telebot.types.BotCommand('/desafio', 'Propõe um desafio para você 🏆'),
        telebot.types.BotCommand(
            '/musica', 'Adivinha o seu estilo musical preferido 🎼'
        ),
        telebot.types.BotCommand('/jogo', 'Envia um jogo aleatório 🎮'),
        telebot.types.BotCommand('/cor', 'Adivinha a sua cor preferida 🔴'),
        telebot.types.BotCommand(
            '/crush', 'Adivinha a primeira letra do seu crush 🥰'
        ),
        telebot.types.BotCommand('/time', 'Adivinha o seu time do coração 😂'),
        telebot.types.BotCommand('/fruta', 'Adivinha a sua fruta preferida 🍎'),
        telebot.types.BotCommand(
            '/curiosidade',
            'Envia aleatoriamente uma curiosidade sobre o mundo 👀',
        ),
        telebot.types.BotCommand('/sigma', 'Mede o seu nível sigma 🗿🍷'),
    ],
    telebot.types.BotCommandScope('all_group_chats'),
)


def search_user(user_id):
    return db.users.find_one({'user_id': user_id})


def add_user_db(message):
    first_name = message.from_user.first_name
    last_name = str(message.from_user.last_name).replace('None', '')
    return db.users.insert_one(
        {
            'user_id': message.from_user.id,
            'name': f'{first_name} {last_name}',
            'sudo': 'false',
        }
    )


def update_user_info(user_id, key, arg):
    try:
        arg = arg.replace('None', '')
    except AttributeError:
        pass
    return db.users.update_one(
        {'user_id': user_id},
        {'$set': {key: arg}},
    )


def banned(user_id):
    user = search_user(user_id)
    if user and user.get('banned') == 'true':
        return True
    return False


def sudo(user_id):
    user = search_user(user_id)
    if user and user.get('sudo') == 'true':
        return True
    return False


# Função para adicionar o grupo ao banco de dados


def add_group_to_db(chat_id, chat_name):
    return db.chats.insert_one(
        {'chat_id': chat_id, 'chat_name': chat_name, 'chat_banned': 'false'}
    )


# procurar grupo


def search_group(chat_id):
    return db.chats.find_one({'chat_id': chat_id})


def remove_chat_db(chat_id):
    db.chats.delete_one({'chat_id': chat_id})


# Manipulador para quando o bot é adicionado a um novo grupo
def send_new_group_message(chat):
    if chat.username:
        chatusername = f'@{chat.username}'
    else:
        chatusername = 'Private Group'
    bot.send_message(
        GROUP_LOG,
        text=f'#{USERNAME_BOT} #New_Group\n'
        f'<b>Chat:</b> {chat.title}\n'
        f'<b>ID:</b> <code>{chat.id}</code>\n'
        f'<b>Link:</b> {chatusername}',
        parse_mode='html',
        disable_web_page_preview=True,
    )

@bot.my_chat_member_handler()
def send_group_greeting(message: types.ChatMemberUpdated):
    try:
        old_member = message.old_chat_member
        new_member = message.new_chat_member
        if message.chat.type != 'private' and new_member.status in [
            'member',
            'administrator',
        ]:
            chat_id = message.chat.id
            chat_name = message.chat.title

            if chat_id == GROUP_LOG:
                logging.info(
                    f'Ignorando armazenamento de chat com ID {chat_id}, pois corresponde ao ID do canal configurado.'
                )
                return

            existing_chat = search_group(chat_id)

            if existing_chat:
                logging.info(
                    f'O bate-papo com ID {chat_id} já existe no banco de dados.'
                )
                return

            add_group_to_db(chat_id, chat_name)
            logging.info(
                f'O bot foi adicionado no grupo {chat_name} - ({chat_id})'
            )
            send_new_group_message(message.chat)

            if message.chat.type in ['group', 'supergroup', 'channel']:
                markup = types.InlineKeyboardMarkup()
                report_bugs = types.InlineKeyboardButton(
                    'Relatar bugs', url='https://t.me/kylorensbot'
                )
                markup.row(report_bugs)
                bot.send_message(
                    chat_id,
                    'Olá, meu nome é Pitucho! Obrigado por me adicionado em seu grupo.\n\nEu sou bot com vários comandos divertidos e legais.',
                    reply_markup=markup,
                )
    except Exception as e:
        logging.info(f'Error handling group greeting: {e}')


@bot.message_handler(content_types=['left_chat_member'])
def on_left_chat_member(message):
    if message.left_chat_member.id == bot.get_me().id:
        chat_id = message.chat.id
        chat_name = message.chat.title

        remove_chat_db(chat_id)
        logging.info(f'O bot foi removido do grupo {chat_name} - ({chat_id})')


# COMANDOS SUDO


@bot.message_handler(commands=['sudo'])
def sudo_command(message):
    if message.chat.type == 'private' and message.from_user.id == OWNER:
        if len(message.text.split()) == 2:
            user_id = int(message.text.split()[1])
            user = search_user(user_id)
            if user:
                if user.get('sudo') == 'true':
                    bot.send_message(
                        message.chat.id,
                        'Este usuário já tem permissão de sudo.',
                    )
                elif user.get('banned') == 'true':
                    bot.send_message(
                        message.chat.id,
                        'Você não pode conceder permissão de sudo a um usuário banido.',
                    )
                else:
                    result = db.users.update_one(
                        {'user_id': user_id}, {'$set': {'sudo': 'true'}}
                    )
                    if result.modified_count > 0:
                        if message.from_user.username:
                            username = '@' + message.from_user.username
                        else:
                            username = 'Não tem um nome de usuário'
                        updated_user = db.users.find_one({'user_id': user_id})
                        if updated_user:
                            bot.send_message(
                                message.chat.id,
                                f"<b>Novo sudo adicionado com sucesso</b>\n\n<b>ID:</b> <code>{user_id}</code>\n<b>Nome:</b> {updated_user.get('name')}\n<b>Username:</b> {username}",
                            )
                            bot.send_message(
                                GROUP_LOG,
                                f"<b>#{NAME_BOT} #New_sudo</b>\n<b>ID:</b> <code>{user_id}</code>\n<b>Name:</b> {updated_user.get('name')}\nU<b>sername:</b> {username}",
                            )
                    else:
                        bot.send_message(
                            message.chat.id, 'User not found in the database.'
                        )
            else:
                bot.send_message(
                    message.chat.id, 'User not found in the database.'
                )
        else:
            bot.send_message(
                message.chat.id,
                'Por favor, forneça um ID de usuário após /sudo.',
            )


@bot.message_handler(commands=['unsudo'])
def unsudo_command(message):
    if message.chat.type == 'private' and message.from_user.id == OWNER:
        if len(message.text.split()) == 2:
            user_id = int(message.text.split()[1])
            user = search_user(user_id)
            if user:
                if user.get('sudo') == 'false':
                    bot.send_message(
                        message.chat.id,
                        'Este usuário já não tem permissão de sudo.',
                    )
                else:
                    result = db.users.update_one(
                        {'user_id': user_id}, {'$set': {'sudo': 'false'}}
                    )
                    if result.modified_count > 0:
                        if message.from_user.username:
                            username = '@' + message.from_user.username
                        else:
                            username = 'Não tem um nome de usuário'
                        updated_user = db.users.find_one({'user_id': user_id})
                        if updated_user:
                            bot.send_message(
                                message.chat.id,
                                f"<b>User sudo removido com sucesso</b>\n\n<b>ID:</b> <code>{user_id}</code>\n<b>Nome:</b> {updated_user.get('name')}\n<b>Username:</b> {username}",
                            )
                            bot.send_message(
                                GROUP_LOG,
                                f"<b>#{NAME_BOT} #Rem_sudo</b>\n<b>ID:</b> <code>{user_id}</code>\n<b>Nome:</b> {updated_user.get('name')}\n<b>Username:</b> {username}",
                            )
                    else:
                        bot.send_message(
                            message.chat.id,
                            'Usuário não encontrado no banco de dados.',
                        )
            else:
                bot.send_message(
                    message.chat.id,
                    'Usuário não encontrado no banco de dados.',
                )
        else:
            bot.send_message(
                message.chat.id,
                'Por favor, forneça um ID de usuário após /unsudo.',
            )


@bot.message_handler(commands=['ban'])
def ban_command(message):
    if message.chat.type == 'private':
        user_id = message.from_user.id
        user = search_user(user_id)
        if user and user.get('sudo') == 'true':
            if len(message.text.split()) == 2:
                ban_user_id = int(message.text.split()[1])
                ban_user = search_user(ban_user_id)
                if ban_user:
                    if ban_user.get('banned') == 'true':
                        bot.send_message(
                            message.chat.id,
                            'Este usuário já foi banido anteriormente.',
                        )
                    elif ban_user.get('sudo') == 'true':
                        bot.send_message(
                            message.chat.id,
                            'Você não pode banir um usuário com permissão de sudo.',
                        )
                    else:
                        result = db.users.update_one(
                            {'user_id': ban_user_id},
                            {'$set': {'banned': 'true'}},
                        )
                        if result.modified_count > 0:
                            if message.from_user.username:
                                username = '@' + message.from_user.username
                            else:
                                username = 'Não tem um nome de usuário'
                            updated_user = db.users.find_one(
                                {'user_id': ban_user_id}
                            )
                            if updated_user:
                                bot.send_message(
                                    message.chat.id,
                                    f"<b>Usuário banido</b>\n\n<b>ID:</b> <code>{ban_user_id}</code>\n<b>nome:</b> {updated_user.get('name')}\n<b>Username: {username}",
                                )
                                bot.send_message(
                                    GROUP_LOG,
                                    f"<b>#{NAME_BOT} #user_banned</b>\n<b>ID:</b> <code>{user_id}</code>\n<b>Nome:</b> {updated_user.get('name')}\n<b>Username: {username}",
                                )
                            else:
                                bot.send_message(
                                    message.chat.id,
                                    'Usuário não encontrado no banco de dados.',
                                )
                else:
                    bot.send_message(
                        message.chat.id,
                        'Usuário não encontrado no banco de dados.',
                    )
            else:
                bot.send_message(
                    message.chat.id,
                    'Por favor, forneça um ID de usuário após /ban.',
                )
        else:
            bot.send_message(
                message.chat.id,
                'Você não tem permissão para usar este comando.',
            )


@bot.message_handler(commands=['unban'])
def unban_command(message):
    if message.chat.type == 'private':
        user_id = message.from_user.id
        user = search_user(user_id)
        if user and user.get('sudo') == 'true':
            if len(message.text.split()) == 2:
                unban_user_id = int(message.text.split()[1])
                unban_user = search_user(unban_user_id)
                if unban_user:
                    if unban_user.get('banned') == 'false':
                        bot.send_message(
                            message.chat.id, 'Este usuário já não está banido.'
                        )
                    elif unban_user.get('sudo') == 'true':
                        bot.send_message(
                            message.chat.id,
                            'Você não pode desbanir um usuário com permissão de sudo.',
                        )
                    else:
                        result = db.users.update_one(
                            {'user_id': unban_user_id},
                            {'$set': {'banned': 'false'}},
                        )
                        if result.modified_count > 0:
                            if message.from_user.username:
                                username = '@' + message.from_user.username
                            else:
                                username = 'Não tem um nome de usuário'
                            updated_user = db.users.find_one(
                                {'user_id': unban_user_id}
                            )
                            if updated_user:
                                bot.send_message(
                                    message.chat.id,
                                    f"<b>Usuário uban</b>\n\n<code>{unban_user_id}</code>\n<b>Nome:</b> {updated_user.get('name')}\n<b>Username:</b> {username}",
                                )
                                bot.send_message(
                                    GROUP_LOG,
                                    f"<b>#{NAME_BOT} #User_unbanned</b>\n<b>ID:</b> <code>{user_id}</code>\n<b>Nome:</b> {updated_user.get('name')}\n<b>Username:</b> {username}",
                                )
                            else:
                                bot.send_message(
                                    message.chat.id,
                                    'Usuário não encontrado no banco de dados.',
                                )
                else:
                    bot.send_message(
                        message.chat.id,
                        'Usuário não encontrado no banco de dados.',
                    )
            else:
                bot.send_message(
                    message.chat.id,
                    'Por favor, forneça um ID de usuário após /unban.',
                )
        else:
            bot.send_message(
                message.chat.id,
                'Você não tem permissão para usar este comando.',
            )


@bot.message_handler(commands=['ban_gp'])
def ban_group(message):
    if message.chat.type != 'private':
        bot.reply_to(
            message, 'Este comando só pode ser usado em chat privado.'
        )
        return

    user_id = message.from_user.id

    if not sudo(user_id):
        bot.reply_to(message, 'Você não tem permissão para usar este comando.')
        return

    if len(message.text.split()) != 2:
        bot.reply_to(message, 'Uso correto: /ban_gp chat_id')
        return

    chat_id = int(message.text.split()[1])

    # Procure o grupo no banco de dados
    group = search_group(chat_id)

    if group:
        db.chats.update_one(
            {'chat_id': chat_id}, {'$set': {'chat_banned': 'true'}}
        )

        try:
            bot.leave_chat(chat_id)
        except Exception as e:
            bot.reply_to(message, f'Erro ao sair do grupo: {str(e)}')
            return

        bot.reply_to(
            message, f'Grupo {chat_id} foi banido e o bot saiu do grupo.'
        )
    else:
        bot.reply_to(message, 'Grupo não encontrado no banco de dados.')


# start


@bot.message_handler(commands=['start'])
def start(message):
    try:
        if message.chat.type != 'private':
            return

        first_name = message.from_user.first_name

        text_start = f'Olá, {first_name}!\n\nEu sou o <b>{NAME_BOT}</b>. Sou um bot para animar seu dia e grupo, consigo adivinhar seus sentimentos, time, presidente e ator preferido...\n\nSinta-se à vontade para me adicionar aos seus grupos.'

        markup = types.InlineKeyboardMarkup()
        add_to_group_button = types.InlineKeyboardButton(
            '✨ Adicione-me ao seu grupo',
            url=f'https://t.me/{USERNAME_BOT}?startgroup=true',
        )
        commands_button = types.InlineKeyboardButton(
            '🗃 Lista de Comandos', callback_data='commands'
        )
        info_button = types.InlineKeyboardButton(
            '❓ Informações', callback_data='info'
        )

        markup.add(add_to_group_button)
        markup.add(commands_button, info_button)

        bot.send_message(message.chat.id, text_start, reply_markup=markup)
    except Exception as e:
        logging.error('erro: ') 

@bot.callback_query_handler(
    func=lambda call: call.message.chat.type == 'private'
)
def callback_handler(callback_query):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id

    if callback_query.data == 'commands':
        commands = [
            '/felicidade - medidor de nível de felicidade 🙂',
            '/raiva - medidor de nível de raiva 🤬',
            '/estado - adivinha qual estado você mora 🌏',
            '/stickers - envia uma figurinha',
            '/presidente - adivinha qual é o seu presidente 🇧🇷',
            '/sorte - veja sua sorte',
            '/genero - adivinha qual é o seu gênero ⚧',
            '/casamento - adivinha a data do seu casamento 👨‍❤️‍👨',
            '/nascimento - adivinha a data do seu nascimento',
            '/morte - adivinha a data da sua morte 😵',
            '/filho - adivinha o nome, gênero e quando você vai ter um filho 👶',
            '/signo - adivinha seu signo ♈️',
            '/religiao - adivinha sua religião 🤍',
            '/ator - adivinha seu ator/atriz preferida 🥰',
            '/altura - adivinha sua altura 🤏',
            '/idade - adivinha sua idade 🎯',
            '/sistema - adivinha seu socioeconômico-políticos 🎫',
            '/profissao - adivinha sua profissão 💼',
            '/saudades - escolha de 0 a 100 quanto de saudades você tem 😰',
            '/ciumes - escolha de 0 a 100 quanto de ciúmes você tem 😠',
            '/apaixonado - medidor de nível de paixão 😍',
            '/gado - medidor de nível de gado 🐮',
            '/tpm - medidor de nível de TPM 😤',
            '/gostosura - medidor de nível de gostosura 😈',
            '/chato - medidor de nível de chatice 😒',
            '/burro - medidor de nível de burrice 🥴',
            '/treteiro - medidor de nível de tretas 🤬',
            '/sexo - medidor de nível de potencial sexual 🔞',
            '/fake - descobre se você é fake 🛃',
            '/serbanido - descobre se você vai ser banido 🚷',
            '/seradm - descobre se você pode ser adm 👮‍♀️',
            '/filme - adivinha a categoria de filme preferido 🎬',
            '/clima - adivinha seu clima preferido 🌪',
            '/numerodasorte - gera seu número da sorte 🎰',
            '/desafio - propõe um desafio para você 🏆',
            '/musica - adivinha seu estilo musical preferido 🎼',
            '/jogo - envia um game aleatório 🎮',
            '/cor - adivinha sua cor preferida🔴',
            '/crush - adivinha a primeira letra do seu crush🥰',
            '/time - adivinha seu time do coração😂',
            '/fruta - adivinha sua fruta preferida🍎',
            '/curiosidade - envia aleatoriamente curiosidade sobre o mundo👀',
            '/sigma - mede seu nível sigma🗿🍷',
        ]

        commands_text = '\n'.join(commands)

        markup = types.InlineKeyboardMarkup()
        back_button = types.InlineKeyboardButton(
            '⬅️ Voltar', callback_data='back_to_start'
        )
        markup.add(back_button)

        bot.edit_message_text(
            f'<b>Lista de Comandos:</b>\n\n{commands_text}',
            chat_id=chat_id,
            message_id=message_id,
            parse_mode='HTML',
            disable_web_page_preview=True,
            reply_markup=markup,
        )

    elif callback_query.data == 'info':
        markup = types.InlineKeyboardMarkup()
        projects_button = types.InlineKeyboardButton(
            '🗂 Projetos', url='https://t.me/infolbrabo'
        )
        support_button = types.InlineKeyboardButton(
            '👨‍💻 Suporte', url='https://t.me/kylorensbot'
        )
        back_button = types.InlineKeyboardButton(
            '⬅️ Voltar', callback_data='back_to_start'
        )

        markup.add(projects_button, support_button)
        markup.row(back_button)

        bot.edit_message_text(
            'Sou um bot com muitas funções interessantes e divertidas.\n\nAqui estão todas as informações para te ajudar a usar o bot. <b>Basta clicar em uma delas.</b>',
            chat_id=chat_id,
            message_id=message_id,
            parse_mode='HTML',
            disable_web_page_preview=True,
            reply_markup=markup,
        )

    elif callback_query.data == 'back_to_start':
        first_name = callback_query.from_user.first_name

        text_start = f'Olá, {first_name}!\n\nEu sou o <b>{NAME_BOT}</b>. Sou um bot para animar seu dia e grupo, consigo adivinhar seus sentimentos, time, presidente e ator preferido...\n\nSinta-se à vontade para me adicionar aos seus grupos.'

        markup = types.InlineKeyboardMarkup(row_width=2)
        add_to_group_button = types.InlineKeyboardButton(
            '✨ Adicione-me ao seu grupo',
            url=f'https://t.me/{USERNAME_BOT}?startgroup=true',
        )
        commands_button = types.InlineKeyboardButton(
            '🗃 Lista de Comandos', callback_data='commands'
        )
        info_button = types.InlineKeyboardButton(
            '❓ Informações', callback_data='info'
        )

        markup.add(add_to_group_button)
        markup.row(commands_button, info_button)

        bot.edit_message_text(
            text_start,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=markup,
        )


# felicidade
def get_funny_phrase(felicidade):
    phrases = {
        (0, 20): [
            'Hoje não tá fácil, hein? 😕',
            'Anime-se! O dia ainda pode melhorar. 😊',
            'Se precisar desabafar, estou aqui! 🤗',
        ],
        (21, 40): [
            'Vamos dar a volta por cima! 💪',
            'A alegria está a caminho! 🎈',
            'Respire fundo e sorria! 😄',
        ],
        (41, 60): [
            'Um dia razoável, não é? 😃',
            'Continua assim, que tá indo bem! 👏',
            'A felicidade está batendo à sua porta! 🚪',
        ],
        (61, 80): [
            'Estamos falando de um feliz aqui! 🥳',
            'Quase lá! A felicidade é logo ali! 🌟',
            'Esse sorriso tá difícil de tirar do rosto, hein? 😁',
        ],
        (81, 100): [
            'Eita, bicho feliz esse! 🤩',
            'É festa! Você está nas nuvens! ☁️',
            'Transbordando alegria e felicidade! 🌈',
        ],
    }
    for (min_val, max_val), options in phrases.items():
        if min_val <= felicidade <= max_val:
            return random.choice(options)


@bot.message_handler(commands=['felicidade'])
def felicidade(message):
    felicidade = random.randint(0, 100)

    frase = get_funny_phrase(felicidade)
    emojis = [
        '😊',
        '😄',
        '🤩',
        '🎉',
        '🌟',
        '💖',
    ] 
    emoji = random.choice(emojis)

    grafico = (
        '🟩' * (felicidade // 10) + '🟩' + '⬜️' * ((100 - felicidade) // 10)
    )

    resposta = (
        '<b>Nível de Felicidade</b>\n\n'
        f'<i>Sua felicidade hoje está em {felicidade}%</i> {emoji}\n\n'
        f'{frase}\n\n'
        f'{grafico} <b>{felicidade}%</b>'
    )

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
        logging.info(
            f'Usuário {message.from_user.username} solicitou nível de felicidade: {felicidade}%'
        )
    except Exception as e:
        bot.send_message(message.chat.id, resposta, parse_mode='HTML')
        logging.info(
            f'Usuário {message.from_user.username} solicitou nível de felicidade, mas a mensagem original foi apagada: {felicidade}%'
        )



# raiva


def get_funny_phrase(nivel_raiva):
    phrases = {
        (0, 20): [
            'Estou tranquilo como um lago. 😌',
            'Tudo sob controle. 😎',
            'Raiva? O que é isso? 😇',
        ],
        (21, 40): [
            'Algumas coisas estão me irritando. 😠',
            'Preciso de um momento para respirar. 😤',
            'Vou me acalmar, prometo. 😬',
        ],
        (41, 60): [
            'Estou começando a perder a paciência. 😡',
            'Vamos manter a calma, certo? 😠',
            'Respirar fundo... 😤',
        ],
        (61, 80): [
            'Estou ficando muito irritado! 😤',
            'Preciso de um tempo sozinho. 😡',
            'Grrrr! 😠',
        ],
        (81, 100): [
            'AHHHHHHHHH! 🤬',
            'Fogo nos olhos! 🤯',
            'Alguém me segura!!! 🤯',
        ],
    }
    for (min_val, max_val), options in phrases.items():
        if min_val <= nivel_raiva <= max_val:
            return random.choice(options)


@bot.message_handler(commands=['raiva'])
def raiva(message):
    nivel_raiva = random.randint(0, 100)

    frase = get_funny_phrase(nivel_raiva)
    emojis = [
        '🤬',
        '😠',
        '😤',
        '😡',
        '🤯',
        '😬',
        '😇',
        '😌',
        '😎',
    ] 
    emoji = random.choice(emojis)

    grafico = (
        '🟩' * (nivel_raiva // 10) + '🟨' + '🟨' * ((100 - nivel_raiva) // 10)
    )

    resposta = (
        '<b>Nível de Raiva</b>\n\n'
        f'Seu nível de raiva está em {nivel_raiva}% {emoji}\n\n'
        f'{frase}\n\n'
        f'{grafico} <b>{nivel_raiva}%</b>'
    )

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(message.chat.id, resposta, parse_mode='HTML')


# estado

estados_br = {
    'AC': 'Acre 🌳 - Terra do Açaí',
    'AL': 'Alagoas 🏖️ - Terra das Belas Praias',
    'AP': 'Amapá 🌊 - Terra do Marco Zero',
    'AM': 'Amazonas 🌿 - Terra das Águas e Florestas',
    'BA': 'Bahia 🌞 - Terra da Alegria',
    'CE': 'Ceará 🌅 - Terra do Sol',
    'DF': 'Distrito Federal 🏛️ - Terra do Poder',
    'ES': 'Espírito Santo 🏝️ - Terra das Praias e Montanhas',
    'GO': 'Goiás 🐂 - Terra do Peão de Rodeio',
    'MA': 'Maranhão 🍍 - Terra do Reggae',
    'MT': 'Mato Grosso 🌄 - Terra dos Chapadões',
    'MS': 'Mato Grosso do Sul 🐎 - Terra do Pantanal',
    'MG': 'Minas Gerais ⛏️ - Terra dos Mineiros',
    'PA': 'Pará 🚢 - Terra do Açaí e do Carimbó',
    'PB': 'Paraíba 🍌 - Terra do Brega',
    'PR': 'Paraná 🏞️ - Terra das Cataratas',
    'PE': 'Pernambuco 🎭 - Terra do Frevo',
    'PI': 'Piauí 🏜️ - Terra do Caju',
    'RJ': 'Rio de Janeiro 🏖️ - Terra do Samba',
    'RN': 'Rio Grande do Norte 🌅 - Terra do Sol',
    'RS': 'Rio Grande do Sul 🍷 - Terra do Churrasco',
    'RO': 'Rondônia 🌲 - Terra da Floresta Amazônica',
    'RR': 'Roraima 🌌 - Terra das Estrelas',
    'SC': 'Santa Catarina ⛷️ - Terra do Frio',
    'SP': 'São Paulo 🏙️ - Terra da Garoa',
    'SE': 'Sergipe 🏝️ - Terra do Mangue',
    'TO': 'Tocantins 🌵 - Terra das Cachoeiras',
}


@bot.message_handler(commands=['estado'])
def estado(message):
    estado_adivinhado = random.choice(list(estados_br.keys()))
    resposta = (
        f'Adivinho que você mora em {estados_br[estado_adivinhado]}! 😄🌏🏠'
    )
    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(message.chat.id, resposta, parse_mode='HTML')


# STICKERS

stickers = [
    'CAACAgEAAxkBAAI372P9EexHmVfMTcT_MCJ5t926Q9yqAAIDAgACNWo5RyQSIVGbaQABni4E',
    'CAACAgEAAxkBAAI382P9EiC0kLNfI_Hm9fa7hzQluXEyAAKoAANRd4FGRA1UrSGDIhMuBA',
    'CAACAgEAAxkBAAI39WP9EjBMkIh_hoJnSlgU0vUeR4FHAALiAgACv61ZRwnoA02nk7m4LgQ',
    'CAACAgEAAxkBAAI392P9Ej6BSN0JnZuuv1qcP3dRbevAAALNAgACdUPARt-YJYI7KAwMLgQ',
    'CAACAgEAAxkBAAI3-WP9EpY9GxILI1Ag-cGCdufvLnfUAAKoAwAC43YpR2Ez7kkNmVDdLgQ',
    'CAACAgEAAxkBAAI3-2P9Eqwpz8JdcsX3QHyHCtxmBFeUAAKEAgAC5rPYRN9l-ILQZmgILgQ',
    'CAACAgEAAxkBAAI3_2P9EwagjWrmZXa0aqbbCDXZBNVqAAKmAgACJWFIRahFRq1swkXvLgQ',
    'CAACAgEAAxkBAAI4AWP9ExwP6ufGkvflfpZe5mQtruyVAAIJBQACgg-YRW7u-iSKZ0nwLgQ',
    'CAACAgEAAxkBAAI4A2P9EymeK0iNi5A6Vs3RTefltDR5AAKaAgACxuxYRogsOeOjfwABHC4E',
    'CAACAgEAAxkBAAI4BWP9Ezl6mQP7ePOkr-RZepNTm21DAAJ5AgACIe2IRCTcfyltcgHnLgQ',
    'CAACAgEAAxkBAAI4B2P9E0cdVWMHm3gTX9lmwg8E1eW_AAKsAgACkpYJRvriPDMz9Io9LgQ',
    'CAACAgEAAxkBAAI4CWP9E1QYNLMECpfHz0Naa8a1EsYmAALBBAACou6gRZrADhBMgKymLgQ',
    'CAACAgEAAxkBAAI4C2P9E2nT5TDh33wCgU-SwC5OJzy-AALGAgACPxlJRevtrl4R9gexLgQ',
    'CAACAgEAAxkBAAI4DWP9E4tSOG82QGLnn2QKpRmIJPDnAAKEAgACNQRhRm-d4gpAX_0YLgQ',
    'CAACAgEAAxkBAAI4D2P9E6vwif-4ZyXZR1H2RaqOQTVMAAL8AQAC86JgRjmei8lYtEVXLgQ',
    'CAACAgEAAxkBAAI4EWP9E73Ec5RMziA7Yn52z2yuKsuUAAIOAgACAXRgRkm3He87ZfamLgQ',
    'CAACAgEAAxkBAAI4E2P9E-Jd1gic6ILIh_Qv4nrGnEBcAAIHAgACPF94RideIGdEdIwLLgQ',
    'CAACAgEAAxkBAAI4FWP9E_13ZWcSmzEF6fXYfVueSzI1AAIcBAACHep5RRlG1_uiTiP-LgQ',
]


@bot.message_handler(commands=['stickers'])
def send_sticker(message):
    random_sticker = random.choice(stickers)
    bot.send_sticker(message.chat.id, random_sticker)


# CANDIDATOS A PRESIDENCIA

candidatos = [
    {
        'nome': 'Jair Bolsonaro',
        'partido': 'PL',
        'imagem': 'https://opopularmm.com.br/wp-content/uploads/2018/10/BOLSONARO-750x750.jpg',
    },
    {
        'nome': 'Lula',
        'partido': 'PT',
        'imagem': 'https://asmetro.org.br/portalsn/wp-content/uploads/2022/12/lula-site.png',
    },
    {
        'nome': 'Ciro Gomes',
        'partido': 'PDT',
        'imagem': 'https://todospelaeducacao.org.br/wordpress/wp-content/uploads/2018/08/candidato-ciro-gomes.jpg',
    },
    {
        'nome': 'João Doria',
        'partido': 'PSDB',
        'imagem': 'https://pbs.twimg.com/profile_images/1519326494488776705/v_hRn0jz_400x400.jpg',
    },
    {
        'nome': 'Marina Silva',
        'partido': 'REDE',
        'imagem': 'https://pbs.twimg.com/profile_images/1577255224741400576/_1Vi_i-g_400x400.jpg',
    },
    {
        'nome': 'Sérgio Moro',
        'partido': 'UB',
        'imagem': 'https://pbs.twimg.com/profile_images/1559524571174297602/NIso6rDG_400x400.jpg',
    },
    {
        'nome': 'Eduardo Leite',
        'partido': 'PSDB',
        'imagem': 'https://media.licdn.com/dms/image/C4E03AQEvOFeTZp40ag/profile-displayphoto-shrink_800_800/0/1650287742747?e=2147483647&v=beta&t=G1uUOJEC7t2upBZ0FrBJ5wFxRZZOQZs3iufNzALBnLk',
    },
    {
        'nome': 'Geraldo Alckmin',
        'partido': 'PSB',
        'imagem': 'https://pbs.twimg.com/profile_images/1587509953425997824/C5aKzsY0_400x400.jpg',
    },
    {
        'nome': 'Padre Kelmon',
        'partido': 'DEM',
        'imagem': 'https://i.em.com.br/K8JiPm7KaASNcmCOfllkz71RSNM=/820x0/smart/imgsapp.em.com.br/app/noticia_127983242361/2022/09/29/1400246/padre-kelmon-candidato-do-ptb_1_53369.jpg',
    },
    {
        'nome': 'Cabo Daciolo',
        'partido': 'PATRI',
        'imagem': 'https://pbs.twimg.com/profile_images/1591111452043223048/904rAJQl_400x400.jpg',
    },
    {
        'nome': 'Guilherme Boulos',
        'partido': 'PSOL',
        'imagem': 'https://conteudo.imguol.com.br/c/parceiros/6a/2020/11/27/guilherme-boulos-foto-guilherme-santos-sul-21-1606514489514_v2_450x450.jpg.webp',
    },
    {
        'nome': 'Luciano Huck',
        'partido': "Sem 'partido'",
        'imagem': 'https://pbs.twimg.com/profile_images/1500173998080016387/wuOSWMir_400x400.jpg',
    },
    {
        'nome': 'Fernando Haddad',
        'partido': 'PT',
        'imagem': 'https://pbs.twimg.com/profile_images/1580018698961690624/BKkWfeFV_400x400.jpg',
    },
    {
        'nome': 'Álvaro Dias',
        'partido': 'PODE',
        'imagem': 'https://www.senado.leg.br/senadores/img/fotos-oficiais/senador945.jpg',
    },
    {
        'nome': "Manuela D'Ávila",
        'partido': 'PCdoB',
        'imagem': 'https://www.diariodocentrodomundo.com.br/wp-content/uploads/2018/07/manuela-1-640x455.jpg',
    },
]


@bot.message_handler(commands=['presidente'])
def presidente(message):
    candidato_aleatorio = random.choice(candidatos)
    nome = candidato_aleatorio['nome']
    partido = candidato_aleatorio['partido']
    imagem = candidato_aleatorio['imagem']

    resposta = f'🇧🇷 Seu presidente é: {nome}\n' f'Partido: {partido}\n'

    try:
        bot.send_photo(
            message.chat.id,
            imagem,
            caption=resposta,
            reply_to_message_id=message.message_id,
        )
    except Exception as e:
        bot.send_photo(message.chat.id, imagem, caption=resposta)


# SORTE

stickers = {
    'certo': [
        {
            'file_id': 'CAACAgEAAxkBAAI5h2QtieP7zFJBVcfnrf1_9KMDlp59AAJLAwAChp9xRVK5tjL-i3fTLwQ',
        },
    ],
    'errado': [
        {
            'file_id': 'CAACAgEAAxkBAAI5iWQtieXBc5WZT8qLGE2P0uwGH4hkAALTAwACz1FpRSowYSAHqFppLwQ',
        },
    ],
}


@bot.message_handler(commands=['sorte'])
def sorte(message):
    probabilidade_certo = (
        random.random()
    )  
    if probabilidade_certo <= 0.15:
        sticker = random.choice(stickers['certo'])
    else:
        sticker = random.choice(stickers['errado'])
    try:
        bot.send_sticker(
            message.chat.id,
            sticker['file_id'],
            reply_to_message_id=message.message_id,
        )
    except Exception as e:
        bot.send_sticker(message.chat.id, sticker['file_id'])


# orientação sexual

orientacoes_sexuais = [
    {'nome': 'Heterossexual', 'emoji': '👫'},
    {'nome': 'Homossexual', 'emoji': '👬👭'},
    {'nome': 'Bissexual', 'emoji': '👬👭👫'},
    {'nome': 'Pansexual', 'emoji': '👬👭👫💖'},
    {'nome': 'Assexual', 'emoji': '🚫🍆💏'},
    {'nome': 'Demissexual', 'emoji': '💑👬👭'},
    {'nome': 'Graysexual', 'emoji': '👥🔘'},
    {'nome': 'Polissexual', 'emoji': '👥👥👬👭'},
    {'nome': 'Queer', 'emoji': '🏳️‍🌈'},
    {'nome': 'Aromântico', 'emoji': '❤️🚫'},
    {'nome': 'Bigênero', 'emoji': '⚥'},
    {'nome': 'Não-binário', 'emoji': '🚻'},
    {'nome': 'Gênero-fluido', 'emoji': '🌊'},
    {'nome': 'Transgênero', 'emoji': '🏳️‍⚧️'},
    {'nome': 'Cisgênero', 'emoji': '♂️♀️'},
    {'nome': 'Intersexo', 'emoji': '⚧'},
    {'nome': 'Dois-espíritos', 'emoji': '🏳️‍⚧️'},
    {'nome': 'Transexual', 'emoji': '🚻🔀'},
]


@bot.message_handler(commands=['orientacao'])
def orientacao(message):
    orientacao_aleatoria = random.choice(orientacoes_sexuais)
    nome = orientacao_aleatoria['nome']
    emoji = orientacao_aleatoria['emoji']

    resposta = f'Sua orientação sexual é: {nome} {emoji} ⚧'

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


# CASAMENTO

meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro',
]

horas = [
    '8:00',
    '12:30',
    '15:45',
    '18:15',
    '20:00',
    '22:30',
    '10:00',
    '14:30',
    '17:00',
    '19:30',
    '21:00',
    '23:30',
]

# Lista de letras para o nome do cônjuge
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


@bot.message_handler(commands=['casamento'])
def casamento(message):
    mes_aleatorio = random.choice(meses)
    hora_aleatoria = random.choice(horas)
    letra_aleatoria = random.choice(letras)
    emoji_coracao = '❤️'
    emoji_relogio = '⏰'
    emoji_anel = '💍'

    resposta = (
        f'🎉 Parabéns! Sua data de casamento é: {mes_aleatorio} {hora_aleatoria}.\n'
        f"Seu cônjuge tem o nome que começa com a letra '{letra_aleatoria}'. {emoji_coracao} {emoji_relogio} {emoji_anel}"
    )

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


# nascimento

meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro',
]

dias = list(range(1, 32))

horas = [
    '8:00',
    '12:30',
    '15:45',
    '18:15',
    '20:00',
    '22:30',
    '10:00',
    '14:30',
    '17:00',
    '19:30',
    '21:00',
    '23:30',
]


@bot.message_handler(commands=['nascimento'])
def nascimento(message):
    mes_aleatorio = random.choice(meses)
    dia_aleatorio = random.choice(dias)
    hora_aleatoria = random.choice(horas)
    emoji_data = '📅'
    emoji_relogio = '⏰'

    resposta = (
        f'🎉 Parabéns! Sua data de nascimento é: {mes_aleatorio} {dia_aleatorio}, às {hora_aleatoria}.\n'
        f'{emoji_data} {emoji_relogio}'
    )

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


# MORTE

meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro',
]

dias = list(range(1, 32))

horas = [
    '8:00',
    '12:30',
    '15:45',
    '18:15',
    '20:00',
    '22:30',
    '10:00',
    '14:30',
    '17:00',
    '19:30',
    '21:00',
    '23:30',
]


@bot.message_handler(commands=['morte'])
def morte(message):
    mes_aleatorio = random.choice(meses)
    dia_aleatorio = random.choice(dias)
    hora_aleatoria = random.choice(horas)
    emoji_data = '💀'
    emoji_relogio = '⏰'

    resposta = (
        f'⚰️ Oh, que mistério! A data da sua morte é: {mes_aleatorio} {dia_aleatorio}, às {hora_aleatoria}.\n'
        f'{emoji_data} {emoji_relogio}'
    )

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


# FILHO

nomes_bebes = [
    'Ana',
    'João',
    'Maria',
    'Pedro',
    'Laura',
    'Lucas',
    'Julia',
    'Gabriel',
    'Clara',
    'Enzo',
]

generos = ['menino', 'menina']

anos = list(range(2023, 2040))


@bot.message_handler(commands=['filho'])
def filho(message):
    nome_bebe_aleatorio = random.choice(nomes_bebes)
    genero_aleatorio = random.choice(generos)
    ano_previsto = random.choice(anos)
    emoji_bebe = '👶'
    emoji_calendario = '📅'

    resposta = (
        f'🍼 Parabéns! O nome do seu futuro filho será {nome_bebe_aleatorio}, um {genero_aleatorio}.\n'
        f'Ele/ela chegará ao mundo em {ano_previsto}. {emoji_bebe} {emoji_calendario}'
    )

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


# SIGNO

signos = [
    {
        'nome': 'Áries',
        'emoji': '♈️',
        'descricao': 'Pessoas arianas são conhecidas por sua coragem, determinação e energia. Elas são líderes naturais e gostam de desafios.',
        'dataInicio': '21 de março',
        'dataFim': '19 de abril',
    },
    {
        'nome': 'Touro',
        'emoji': '♉️',
        'descricao': 'Pessoas taurinas são conhecidas por sua perseverança, confiabilidade e sensualidade. Elas são leais e gostam de conforto e estabilidade.',
        'dataInicio': '20 de abril',
        'dataFim': '20 de maio',
    },
    {
        'nome': 'Gêmeos',
        'emoji': '♊️',
        'descricao': 'Pessoas geminianas são conhecidas por sua versatilidade, curiosidade e inteligência. Elas são sociáveis e gostam de novidades e mudanças.',
        'dataInicio': '21 de maio',
        'dataFim': '20 de junho',
    },
    {
        'nome': 'Câncer',
        'emoji': '♋️',
        'descricao': 'Pessoas cancerianas são conhecidas por sua sensibilidade, empatia e intuição. Elas são protetoras e gostam de estar em ambientes acolhedores.',
        'dataInicio': '21 de junho',
        'dataFim': '22 de julho',
    },
    {
        'nome': 'Leão',
        'emoji': '♌️',
        'descricao': 'Pessoas leoninas são conhecidas por sua autoconfiança, criatividade e generosidade. Elas gostam de estar no centro das atenções e de serem reconhecidas.',
        'dataInicio': '23 de julho',
        'dataFim': '22 de agosto',
    },
    {
        'nome': 'Virgem',
        'emoji': '♍️',
        'descricao': 'Pessoas virginianas são conhecidas por sua praticidade, perfeccionismo e inteligência. Elas são organizadas e gostam de resolver problemas.',
        'dataInicio': '23 de agosto',
        'dataFim': '22 de setembro',
    },
    {
        'nome': 'Libra',
        'emoji': '♎️',
        'descricao': 'Pessoas librianas são conhecidas por sua diplomacia, equilíbrio e sociabilidade. Elas valorizam a harmonia e gostam de estar em grupos.',
        'dataInicio': '23 de setembro',
        'dataFim': '22 de outubro',
    },
    {
        'nome': 'Escorpião',
        'emoji': '♏️',
        'descricao': 'Pessoas escorpianas são conhecidas por sua intensidade, mistério e paixão. Elas são profundas e gostam de ter controle sobre as situações.',
        'dataInicio': '23 de outubro',
        'dataFim': '21 de novembro',
    },
    {
        'nome': 'Sagitário',
        'emoji': '♐️',
        'descricao': 'Pessoas sagitarianas são conhecidas por sua liberdade, otimismo e espírito aventureiro. Elas gostam de explorar e descobrir coisas novas.',
        'dataInicio': '22 de novembro',
        'dataFim': '21 de dezembro',
    },
    {
        'nome': 'Capricórnio',
        'emoji': '♑️',
        'descricao': 'Pessoas capricornianas são conhecidas por sua ambição, disciplina e determinação. Elas são responsáveis e gostam de alcançar metas.',
        'dataInicio': '22 de dezembro',
        'dataFim': '19 de janeiro',
    },
    {
        'nome': 'Aquário',
        'emoji': '♒️',
        'descricao': 'Pessoas aquarianas são conhecidas por sua originalidade, independência e idealismo. Elas são inovadoras e gostam de quebrar padrões estabelecidos.',
        'dataInicio': '20 de janeiro',
        'dataFim': '18 de fevereiro',
    },
    {
        'nome': 'Peixes',
        'emoji': '♓️',
        'descricao': 'Pessoas piscianas são conhecidas por sua sensibilidade, intuição e imaginação. Elas são empáticas e gostam de ajudar os outros.',
        'dataInicio': '19 de fevereiro',
        'dataFim': '20 de março',
    },
]


@bot.message_handler(commands=['signo'])
def signo(message):
    data_nascimento = random.choice(signos)
    nome_signo = data_nascimento['nome']
    emoji_signo = data_nascimento['emoji']
    descricao_signo = data_nascimento['descricao']

    resposta = (
        f'<b>🌟 Seu signo é {nome_signo} {emoji_signo}.</b>\n\n'
        f'{descricao_signo}'
    )

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


# RELIGIAO

religioes = [
    {
        'nome': 'Cristianismo',
        'emoji': '✝️',
        'descricao': 'Religião que crê em Jesus Cristo como o filho de Deus e salvador da humanidade.',
        'fundador': 'Jesus Cristo',
    },
    {
        'nome': 'Islamismo',
        'emoji': '☪️',
        'descricao': 'Religião que segue os ensinamentos do profeta Maomé e crê em Alá como o único Deus.',
        'fundador': 'Maomé',
    },
    {
        'nome': 'Judaísmo',
        'emoji': '✡️',
        'descricao': 'Religião que se baseia no Antigo Testamento e acredita na vinda do Messias.',
        'fundador': 'Abraão',
    },
    {
        'nome': 'Budismo',
        'emoji': '☸️',
        'descricao': 'Religião que busca a iluminação através da meditação e do estudo dos ensinamentos de Buda.',
        'fundador': 'Buda',
    },
    {
        'nome': 'Hinduísmo',
        'emoji': '🕉️',
        'descricao': 'Religião que crê na reencarnação e no karma, e venera vários deuses e deusas.',
        'fundador': "Não há um 'fundador' definido",
    },
    {
        'nome': 'Siquismo',
        'emoji': '☬',
        'descricao': 'Religião que segue os ensinamentos do Guru Nanak e prega a igualdade e a fraternidade.',
        'fundador': 'Guru Nanak',
    },
    {
        'nome': 'Candomblé',
        'emoji': '🔮',
        'descricao': 'Religião afro-brasileira que cultua os orixás e entidades ancestrais africanas.',
        'fundador': "Não há um 'fundador' definido",
    },
    {
        'nome': 'Wicca',
        'emoji': '🌙',
        'descricao': 'Religião neopagã que se baseia na magia e na natureza, e celebra os ciclos da Lua.',
        'fundador': 'Gerald Gardner',
    },
    {
        'nome': 'Zoroastrismo',
        'emoji': '🕊️',
        'descricao': 'Religião antiga do Irã que acredita em um Deus supremo, Ahura Mazda, e na luta entre o bem e o mal.',
        'fundador': 'Zaratustra',
    },
    {
        'nome': 'Xintoísmo',
        'emoji': '🎎',
        'descricao': 'Religião japonesa que venera os kami, espíritos divinos da natureza e dos antepassados.',
        'fundador': "Não há um 'fundador' definido",
    },
    {
        'nome': 'Santo Daime',
        'emoji': '🍃',
        'descricao': 'Religião brasileira que utiliza um chá alucinógeno, o ayahuasca, em seus rituais.',
        'fundador': 'Raimundo Irineu Serra',
    },
    {
        'nome': 'Satanismo',
        'emoji': '👹',
        'descricao': 'Movimento que cultua Satanás como um símbolo da liberdade individual e da rebelião contra a moral religiosa.',
        'fundador': 'Anton LaVey',
    },
    {
        'nome': 'Jainismo',
        'emoji': '🕉️',
        'descricao': 'Religião indiana que prega a não-violência, o respeito a todas as formas de vida e a busca pela libertação do ciclo de reencarnação.',
        'fundador': 'Mahavira',
    },
    {
        'nome': 'Taoismo',
        'emoji': '☯️',
        'descricao': 'Filosofia religiosa chinesa que busca o equilíbrio entre opostos e a harmonia com a natureza.',
        'fundador': 'Lao Tsé',
    },
]


@bot.message_handler(commands=['religiao'])
def religiao(message):
    religiao_aleatoria = random.choice(religioes)
    nome_religiao = religiao_aleatoria['nome']
    emoji_religiao = religiao_aleatoria['emoji']
    descricao_religiao = religiao_aleatoria['descricao']
    fundador_religiao = religiao_aleatoria['fundador']

    resposta = (
        f'<b>🙏 Sua religião é {nome_religiao} {emoji_religiao}.</b>\n\n'
        f'{descricao_religiao}\n\n'
        f'Fundador: {fundador_religiao}'
    )

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


# ATOR

atores = [
    {
        'nome': 'Meryl Streep',
        'idade': 72,
        'filmes': [
            'O Diabo Veste Prada',
            'Kramer vs. Kramer',
            'A Dama de Ferro',
        ],
        'oscar': True,
        'emoji': '⭐️',
    },
    {
        'nome': 'Tom Hanks',
        'idade': 65,
        'filmes': ['Forrest Gump', 'Náufrago', 'O Resgate do Soldado Ryan'],
        'oscar': True,
        'emoji': '⭐️',
    },
    {
        'nome': 'Leonardo DiCaprio',
        'idade': 47,
        'filmes': ['O Lobo de Wall Street', 'Titanic', 'O Regresso'],
        'oscar': True,
        'emoji': '⭐️',
    },
    {
        'nome': 'Emma Stone',
        'idade': 33,
        'filmes': ['La La Land', 'Birdman', 'As Serviçais'],
        'oscar': True,
        'emoji': '⭐️',
    },
    {
        'nome': 'Denzel Washington',
        'idade': 67,
        'filmes': ['Dia de Treinamento', 'Malcolm X', 'Um Limite Entre Nós'],
        'oscar': True,
        'emoji': '⭐️',
    },
    {
        'nome': 'Cate Blanchett',
        'idade': 52,
        'filmes': ['Blue Jasmine', 'O Aviador', 'Elizabeth'],
        'oscar': True,
        'emoji': '⭐️',
    },
    {
        'nome': 'Robert De Niro',
        'idade': 78,
        'filmes': [
            'Taxi Driver',
            'O Poderoso Chefão Parte II',
            'Touro Indomável',
        ],
        'oscar': True,
        'emoji': '⭐️',
    },
    {
        'nome': 'Joaquin Phoenix',
        'idade': 47,
        'filmes': ['Coringa', 'Gladiador', 'Ela'],
        'oscar': True,
        'emoji': '⭐️',
    },
    {
        'nome': 'Anthony Hopkins',
        'idade': 84,
        'filmes': [
            'O Silêncio dos Inocentes',
            'Hannibal',
            'Oito Mulheres e um Segredo',
        ],
        'oscar': True,
        'emoji': '⭐️',
    },
    {
        'nome': 'Morgan Freeman',
        'idade': 84,
        'filmes': [
            'Um Sonho de Liberdade',
            'Conduzindo Miss Daisy',
            'Truque de Mestre',
        ],
        'oscar': True,
        'emoji': '⭐️',
    },
]


@bot.message_handler(commands=['ator'])
def ator(message):
    ator_aleatorio = random.choice(atores)
    nome_ator = ator_aleatorio['nome']
    idade_ator = ator_aleatorio['idade']
    filmes_ator = ', '.join(ator_aleatorio['filmes'])
    tem_oscar = 'Sim' if ator_aleatorio['oscar'] else 'Não'
    emoji_ator = ator_aleatorio['emoji']

    resposta = (
        f'🎬 Seu ator/atriz preferido é {nome_ator} {emoji_ator}.\n'
        f'Idade: {idade_ator} anos\n'
        f'Filmes famosos: {filmes_ator}\n'
        f'Ganhou um Oscar: {tem_oscar}'
    )

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


# ALTURA


@bot.message_handler(commands=['altura'])
def altura(message):
    altura_minima = 140
    altura_maxima = 200

    altura_aleatoria = (
        random.randint(altura_minima, altura_maxima) / 100.0
    ) 
    altura_formatada = f'{altura_aleatoria:.2f}'.replace(
        '.', ','
    ) 

    if altura_aleatoria < 1.60:
        emoji = '🤏' 
    elif altura_aleatoria < 1.70:
        emoji = '🚶‍♂️'  
    else:
        emoji = '🏋️‍♂️' 
    resposta = f'Sua altura é: {altura_formatada} m {emoji}'

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


# IDADE


@bot.message_handler(commands=['idade'])
def idade(message):
    idade_minima = 18
    idade_maxima = 100

    idade_aleatoria = random.randint(idade_minima, idade_maxima)

    if idade_aleatoria < 30:
        emoji = '👶'  
    elif idade_aleatoria < 60:
        emoji = '👨'  
    else:
        emoji = '🧓'  

    resposta = f'Sua idade é: {idade_aleatoria} anos {emoji}'

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


# SISTEMA

sistemas = [
    {
        'nome': 'Capitalismo',
        'codenome': 'Capitalista',
        'descricao': 'Sistema econômico em que os meios de produção são de propriedade privada e as atividades econômicas são guiadas pelo mercado.',
        'emoji': '💰',
    },
    {
        'nome': 'Socialismo',
        'codenome': 'Socialista',
        'descricao': 'Sistema econômico em que os meios de produção são de propriedade coletiva e as atividades econômicas são planejadas e controladas pelo Estado.',
        'emoji': '👥',
    },
    {
        'nome': 'Comunismo',
        'codenome': 'Comunista',
        'descricao': 'Sistema político e econômico que busca a eliminação das classes sociais e a propriedade coletiva dos meios de produção.',
        'emoji': '🚩',
    },
    {
        'nome': 'Anarquismo',
        'codenome': 'Anarquista',
        'descricao': 'Filosofia política que defende a eliminação do Estado e a organização da sociedade em comunidades autônomas e auto-geridas.',
        'emoji': 'Ⓐ',
    },
    {
        'nome': 'Fascismo',
        'codenome': 'Facista',
        'descricao': 'Ideologia política autoritária que enfatiza o nacionalismo, o militarismo e o totalitarismo.',
        'emoji': '🕊️',
    },
    {
        'nome': 'Monarquia',
        'codenome': 'Monarquista',
        'descricao': 'Sistema político em que o poder é exercido por um monarca, geralmente de forma hereditária.',
        'emoji': '👑',
    },
    {
        'nome': 'República',
        'codenome': 'Republicano',
        'descricao': 'Sistema político em que o poder é exercido pelo povo ou seus representantes eleitos.',
        'emoji': '🗳️',
    },
    {
        'nome': 'Democracia',
        'codenome': 'Democrata',
        'descricao': 'Sistema político em que o poder é exercido pelo povo ou seus representantes eleitos, através de processos democráticos.',
        'emoji': '🗳️',
    },
    {
        'nome': 'Teocracia',
        'codenome': 'Teocrata',
        'descricao': 'Sistema político em que o poder é exercido por líderes religiosos ou por uma religião oficial.',
        'emoji': '🕍',
    },
    {
        'nome': 'Meritocracia',
        'codenome': 'Meritocrata',
        'descricao': 'Sistema político em que o poder é exercido por indivíduos com base em seus méritos e habilidades.',
        'emoji': '🎓',
    },
    {
        'nome': 'Plutocracia',
        'codenome': 'Plutocrata',
        'descricao': 'Sistema político em que o poder é exercido pelos mais ricos ou pelos proprietários de grandes empresas.',
        'emoji': '💰',
    },
    {
        'nome': 'Oligarquia',
        'codenome': 'Oligárquico',
        'descricao': 'Sistema político em que o poder é exercido por um pequeno grupo de pessoas.',
        'emoji': '👥',
    },
    {
        'nome': 'Totalitarismo',
        'codenome': 'Totalitário',
        'descricao': 'Sistema político em que o Estado tem controle total sobre a sociedade e a economia.',
        'emoji': '🛡️',
    },
    {
        'nome': 'Autocracia',
        'codenome': 'Autocrata',
        'descricao': 'Sistema político em que o poder é exercido por uma pessoa ou por um pequeno grupo de pessoas, sem qualquer participação popular ou limitações constitucionais.',
        'emoji': '👤',
    },
]


@bot.message_handler(commands=['sistema'])
def sistema(message):
    sistema_aleatorio = random.choice(sistemas)
    nome = sistema_aleatorio['nome']
    codenome = sistema_aleatorio['codenome']
    descricao = sistema_aleatorio['descricao']
    emoji = sistema_aleatorio['emoji']

    resposta = f'Seu sistema socioeconômico-político é: {nome} ({codenome}) {emoji}\n\nDescrição: {descricao}'

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


# profissao

# Lista de profissões
profissoes = [
    {
        'nome': 'Médico',
        'emoji': '⚕️',
    },
    {
        'nome': 'Advogado',
        'emoji': '⚖️',
    },
    {
        'nome': 'Professor',
        'emoji': '📚',
    },
    {
        'nome': 'Engenheiro',
        'emoji': '🔧',
    },
    {
        'nome': 'Designer',
        'emoji': '🎨',
    },
    {
        'nome': 'Chef de Cozinha',
        'emoji': '👨‍🍳',
    },
    # ... Outras profissões aqui
]


@bot.message_handler(commands=['profissao'])
def profissao(message):
    profissao_aleatoria = random.choice(profissoes)
    nome = profissao_aleatoria['nome']
    emoji = profissao_aleatoria['emoji']

    resposta = f'Sua profissão é: {nome} {emoji}'

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


# SAUDADES


@bot.message_handler(commands=['saudades'])
def saudades(message):
    valor_saudades = random.randint(0, 100)
    resposta = obter_frase_saudades(valor_saudades)

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


def obter_frase_saudades(valor_saudades):
    frases_saudades = [
        'Você está muito bem! 😊',
        'Um pouco de saudades, mas nada demais. 😌',
        'Saudades moderadas. 😥',
        'Você está com muitas saudades! 😢',
        'A saudade está insuportável! 😭',
        'Nem lembro o que é saudade! 🙃',
        'Saudades? Eu não conheço essa palavra. 😄',
        'Se você fosse um lugar, eu já estaria lá! 😍',
        'Só um pouquinho de saudades. 😬',
        'Nem saudades, nem falta. 😉',
        'A saudade aperta, mas a esperança de se reencontrar é maior! ❤️',
        'Já pode voltar, a saudade bateu forte. 😞',
    ]

    emoji_saudades = [
        '😊',
        '😌',
        '😥',
        '😢',
        '😭',
        '🙃',
        '😄',
        '😍',
        '😬',
        '😉',
        '❤️',
        '😞',
    ]

    indice = min(valor_saudades // 10, len(frases_saudades) - 1)

    return frases_saudades[indice] + ' ' + emoji_saudades[indice]


# CIUMES


@bot.message_handler(commands=['ciumes'])
def ciumes(message):
    valor_ciumes = random.randint(0, 100)
    resposta = obter_frase_ciumes(valor_ciumes)

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


def obter_frase_ciumes(valor_ciumes):
    frases_ciumes = [
        'Você é uma pessoa muito tranquila, sem ciúmes! 😇',
        'Zero ciúmes por aqui! 😊',
        'Não existe espaço para ciúmes em seu coração! ❤️',
        'Apenas um pouquinho de ciúmes... 😉',
        'Seu ciúmes é leve como uma brisa suave! 😌',
        'Um ciúmes moderado! 😠',
        'O ciúmes está começando a aparecer... 😬',
        'Você está com ciúmes! 😡',
        'O ciúmes está dominando... 😤',
        'Apenas mais um pouco para explodir! 😡😡😡',
        'CIÚMES NÍVEL MÁXIMO! 😤😡🔥',
        'Você é o mestre do ciúmes! Ciumento profissional! 😠😠😠',
    ]

    emoji_ciumes = ['😇', '😊', '❤️', '😉', '😌', '😠', '😬', '😡', '😤', '😡😡😡', '😠😠😠']

    indice = min(valor_ciumes // 10, len(frases_ciumes) - 1)

    return frases_ciumes[indice] + ' ' + emoji_ciumes[indice]


# APAIXONADO


@bot.message_handler(commands=['apaixonado'])
def apaixonado(message):
    valor_paixao = random.randint(0, 100)
    resposta = obter_frase_paixao(valor_paixao)

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


def obter_frase_paixao(valor_paixao):
    frases_paixao = [
        'Você não está apaixonado no momento. 😐',
        'Seu coração está frio, sem paixão. ❄️',
        'Apenas um leve toque de paixão. 😊',
        'Você está começando a sentir a paixão. 😍',
        'Seu coração está aquecido pela paixão. ❤️',
        'A paixão está no ar! 💓',
        'Você está profundamente apaixonado! 💘',
        'A paixão está tomando conta de você. 💖',
        'Seu coração está em chamas de paixão! 🔥',
        'Paixão total! Não há como escapar! 😍😍😍',
        'Você está completamente e irremediavelmente apaixonado! 😍😍😍',
    ]

    emoji_paixao = [
        '😐',
        '❄️',
        '😊',
        '😍',
        '❤️',
        '💓',
        '💘',
        '💖',
        '🔥',
        '😍😍😍',
        '😍😍😍',
    ]

    indice = min(valor_paixao // 10, len(frases_paixao) - 1)

    return frases_paixao[indice] + ' ' + emoji_paixao[indice]


# GADO


@bot.message_handler(commands=['gado'])
def gado(message):
    valor_gado = random.randint(0, 100)
    resposta = obter_frase_gado(valor_gado)

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


def obter_frase_gado(valor_gado):
    frases_gado = [
        "Você não está 'gado' no momento. 😐",
        "Você está bem tranquilo, nada de 'gado'. 😌",
        "Só um pouquinho de 'gado'. 🐄",
        "Você está começando a 'gadar'. 😅",
        "Há algum 'gado' por aí. 🐮",
        "Você está definitivamente 'gado'! 🐃",
        "Muito 'gado'! Não tem volta. 🐂",
        "Totalmente 'gado'! 🐄🔥",
        "Seu nível de 'gado' é fora de série! 🐄💖",
        "Você é 'gado' até o último fio de cabelo! 🐄🔥😍",
        "O nível de 'gado' é absurdo! Você está 'gado' demais! 🐄🔥😍🤯",
    ]

    emoji_gado = ['😐', '😌', '🐄', '😅', '🐮', '🐃', '🐂', '🐄🔥', '🐄💖', '🐄🔥😍', '🐄🔥😍🤯']

    indice = min(valor_gado // 10, len(frases_gado) - 1)

    return frases_gado[indice] + ' ' + emoji_gado[indice]


# TPM


@bot.message_handler(commands=['tpm'])
def tpm(message):
    valor_tpm = random.randint(0, 100)
    resposta = obter_frase_tpm(valor_tpm)

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


def obter_frase_tpm(valor_tpm):
    frases_tpm = [
        'Você está muito tranquilo, sem sinais de TPM. 😌',
        'Nenhuma TPM à vista, você está ótima! 😄',
        'A TPM está bem fraca, não se preocupe. 😅',
        'Você está começando a sentir um pouquinho de TPM. 😠',
        'Alguns sintomas de TPM estão aí. 😡',
        'A TPM está se aproximando. 😡😤',
        'Você está passando por uma TPM moderada. 😤',
        'A TPM está te dominando. 😠😤',
        'Sua TPM está forte! 😤😡',
        'Totalmente dominada pela TPM. 😤😡😡',
        'TPM extrema! Cuidado com as explosões! 😡😤😡',
    ]

    emoji_tpm = ['😌', '😄', '😅', '😠', '😡', '😡😤', '😤', '😠😤', '😤', '😤😡', '😡😤😡']

    indice = min(valor_tpm // 10, len(frases_tpm) - 1)

    return frases_tpm[indice] + ' ' + emoji_tpm[indice]


# gostosura


@bot.message_handler(commands=['gostosura'])
def gostosura(message):
    valor_gostosura = random.randint(0, 100)
    resposta = obter_frase_gostosura(valor_gostosura)

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


def obter_frase_gostosura(valor_gostosura):
    frases_gostosura = [
        'Você não está muito gostoso(a) hoje. 😇',
        'Você é adorável, mas não muito gostoso(a). 😊',
        'Com uma pitada de gostosura. 😋',
        'Você está bem gostoso(a) hoje. 😈',
        'Muito gostoso(a)! 😍',
        'Você é uma delícia! 😘',
        'Gostosura pura! 😋😘',
        'Indescritivelmente gostoso(a)! 😏😘',
        'Você é a gostosura em pessoa! 😈😍',
        'Ninguém é mais gostoso(a) do que você! 😈😍😘',
    ]

    emoji_gostosura = ['😇', '😊', '😋', '😈', '😍', '😘', '😋😘', '😏😘', '😈😍', '😈😍😘']

    indice = min(valor_gostosura // 10, len(frases_gostosura) - 1)

    return frases_gostosura[indice] + ' ' + emoji_gostosura[indice]


# chato


@bot.message_handler(commands=['chato'])
def chato(message):
    valor_chatice = random.randint(0, 100)
    resposta = obter_frase_chatice(valor_chatice)

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


def obter_frase_chatice(valor_chatice):
    frases_chatice = [
        'Você não está chato hoje. 😇',
        'Você é bastante agradável. 😊',
        'Nada de chato por aqui. 😋',
        'Com um toque de chatice. 😒',
        'Você está um pouco chato. 😒',
        'Está difícil de lidar hoje. 😓',
        'Realmente chato. 😑',
        'Chatice extrema. 😠',
        'Insuportavelmente chato. 😫',
        'Ninguém aguenta mais a chatice! 😖',
    ]

    emoji_chatice = ['😇', '😊', '😋', '😒', '😒', '😓', '😑', '😠', '😫', '😖']

    indice = min(valor_chatice // 10, len(frases_chatice) - 1)

    return frases_chatice[indice] + ' ' + emoji_chatice[indice]


# burrice


@bot.message_handler(commands=['burro'])
def burro(message):
    valor_burrice = random.randint(0, 100)
    resposta = obter_frase_burrice(valor_burrice)

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


def obter_frase_burrice(valor_burrice):
    frases_burrice = [
        'Você é super inteligente! 🤓',
        'Não há vestígios de burrice aqui! 😄',
        'Inteligência brilha em você! 😁',
        'Um pouquinho confuso, mas tudo bem! 😅',
        'Pequenos lapsos de burrice. 🙃',
        'Parece que você está se esforçando... 😐',
        'Alguns momentos de burrice. 🧐',
        'Hmmm... a burrice está se manifestando. 🤨',
        'Burrice em crescimento. 😫',
        'Uau, a burrice está no nível máximo! 🥴',
    ]

    emoji_burrice = ['🤓', '😄', '😁', '😅', '🙃', '😐', '🧐', '🤨', '😫', '🥴']

    indice = min(valor_burrice // 10, len(frases_burrice) - 1)

    return frases_burrice[indice] + ' ' + emoji_burrice[indice]


# treteiro


@bot.message_handler(commands=['treteiro'])
def treteiro(message):
    valor_tretas = random.randint(0, 100)
    resposta = obter_frase_tretas(valor_tretas)

    chat_id = message.chat.id

    try:
        bot.reply_to(message, resposta, parse_mode='HTML')
    except Exception as e:
        bot.send_message(chat_id, resposta, parse_mode='HTML')


def obter_frase_tretas(valor_tretas):
    frases_tretas = [
        'Paz e amor sempre! 🕊️',
        'Nada de tretas por aqui! 😇',
        'Zero tretas detectadas! 😌',
        'Pequenas tretas, mas nada demais! 😬',
        'Parece que as tretas estão surgindo... 😠',
        'Alguns problemas, mas podemos superá-los! 😡',
        'Está ficando sério, cuidado com as tretas! 🤨',
        'Definitivamente muitas tretas acontecendo... 🤬',
        'Aqui é zona de guerra! 🧨',
        'Tretas destruindo o lugar! 💥',
    ]

    emoji_tretas = ['🕊️', '😇', '😌', '😬', '😠', '😡', '🤨', '🤬', '🧨', '💥']

    indice = min(valor_tretas // 10, len(frases_tretas) - 1)

    return frases_tretas[indice] + ' ' + emoji_tretas[indice]


# FAKE

# Função para calcular a probabilidade de ser fake (exemplo aleatório)
def calcular_probabilidade_fake(nome, foto_perfil):
    probabilidade_nome = random.randint(0, 100)
    probabilidade_foto_perfil = random.randint(0, 100)

    media_probabilidades = (probabilidade_nome + probabilidade_foto_perfil) / 2

    return media_probabilidades


# Comando /fake
@bot.message_handler(commands=['fake'])
def comando_fake(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    nome_usuario = message.from_user.first_name

    # Simulamos a obtenção da foto de perfil com um exemplo
    # Na prática, você pode usar bibliotecas ou APIs para fazer isso
    # Neste exemplo, assumimos que todos os usuários têm uma foto de perfil
    foto_perfil_usuario = (
        f'https://tg.org/user_{user_id}/profile_photo'  # Exemplo fictício
    )

    # Calcula a probabilidade de ser fake
    probabilidade_fake = calcular_probabilidade_fake(
        nome_usuario, foto_perfil_usuario
    )

    if probabilidade_fake > 80:
        resposta = f'🚫 Você pode ser uma conta fake! Probabilidade: {probabilidade_fake}%'
    else:
        resposta = f'✅ Você parece ser uma conta legítima. Probabilidade: {probabilidade_fake}%'

    # Responde com reply_to se houver uma mensagem
    try:
        bot.reply_to(message, resposta)
    except Exception as e:
        bot.send_message(chat_id, resposta)


# serbanido

# Função para calcular a probabilidade de banimento
def calcular_probabilidade_banimento(usuario):
    probabilidade_comportamento = random.randint(0, 100)
    probabilidade_denúncias = random.randint(0, 100)
    probabilidade_atividade_suspeita = random.randint(0, 100)

    media_probabilidades = (
        probabilidade_comportamento
        + probabilidade_denúncias
        + probabilidade_atividade_suspeita
    ) / 3

    return media_probabilidades


# Comando /serbanido
@bot.message_handler(commands=['serbanido'])
def comando_ser_banido(message):
    chat_id = message.chat.id
    nome_usuario = message.from_user.first_name

    # Calcula a probabilidade de ser banido
    probabilidade_banimento = calcular_probabilidade_banimento(
        message.from_user
    )

    if probabilidade_banimento > 80:
        resposta = f'🚷 Você tem uma alta probabilidade de ser banido! Probabilidade: {probabilidade_banimento}%'
    else:
        resposta = f'✅ Parece que você está seguro por enquanto. Probabilidade de banimento: {probabilidade_banimento}%'

    # Responde com reply_to se houver uma mensagem
    try:
        bot.reply_to(message, resposta)
    except Exception as e:
        bot.send_message(chat_id, resposta)


# ser adm

# Função para calcular a probabilidade de se tornar administrador
def calcular_probabilidade_ser_adm(usuario):
    probabilidade_contribuicao = random.randint(0, 100)
    probabilidade_responsabilidade = random.randint(0, 100)
    probabilidade_conhecimento = random.randint(0, 100)

    media_probabilidades = (
        probabilidade_contribuicao
        + probabilidade_responsabilidade
        + probabilidade_conhecimento
    ) / 3

    return media_probabilidades


# Comando /seradm
@bot.message_handler(commands=['seradm'])
def comando_ser_adm(message):
    chat_id = message.chat.id
    nome_usuario = message.from_user.first_name

    # Calcula a probabilidade de se tornar administrador
    probabilidade_ser_adm = calcular_probabilidade_ser_adm(message.from_user)

    if probabilidade_ser_adm > 80:
        resposta = f'👮‍♀️ Você tem uma alta probabilidade de se tornar administrador! Probabilidade: {probabilidade_ser_adm}%'
    else:
        resposta = f'✅ Parece que você ainda precisa trabalhar mais para se tornar administrador. Probabilidade de ser adm: {probabilidade_ser_adm}%'

    # Responde com reply_to se houver uma mensagem
    try:
        bot.reply_to(message, resposta)
    except Exception as e:
        bot.send_message(chat_id, resposta)


# filme

categorias = [
    {
        'emoji': '🎬',
        'descricao': 'Ação',
        'sobre': 'Filmes de ação geralmente envolvem cenas de luta, perseguições e tiroteios. São conhecidos por terem muita adrenalina e emoção.',
    },
    {
        'emoji': '🎭',
        'descricao': 'Drama',
        'sobre': 'Filmes de drama são conhecidos por envolverem conflitos emocionais e problemas pessoais dos personagens. Podem ser baseados em histórias verdadeiras ou fictícias.',
    },
    {
        'emoji': '🤖',
        'descricao': 'Ficção Científica',
        'sobre': 'Filmes de ficção científica apresentam conceitos e ideias futuristas, científicas ou tecnológicas. Podem envolver viagens no tempo, realidades alternativas e alienígenas.',
    },
    {
        'emoji': '👻',
        'descricao': 'Terror',
        'sobre': 'Filmes de terror são conhecidos por assustar e causar medo no público. Podem envolver fantasmas, monstros e serial killers.',
    },
    {
        'emoji': '🤠',
        'descricao': 'Western',
        'sobre': 'Filmes de western se passam no Velho Oeste americano e envolvem tiroteios, duelos e cavalgadas. São conhecidos por seus personagens emblemáticos, como xerifes, cowboys e foras-da-lei.',
    },
    {
        'emoji': '🎥',
        'descricao': 'Documentário',
        'sobre': "Filmes documentários apresentam fatos e informações 'sobre' um determinado assunto ou evento. Podem ser 'sobre' a natureza, história ou política, por exemplo.",
    },
    {
        'emoji': '🍿',
        'descricao': 'Comédia',
        'sobre': 'Filmes de comédia são conhecidos por fazerem o público rir. Podem envolver piadas, situações engraçadas e personagens cômicos.',
    },
    {
        'emoji': '👊',
        'descricao': 'Artes Marciais',
        'sobre': 'Filmes de artes marciais apresentam lutas e técnicas de combate de diferentes disciplinas, como karatê, judô e kung fu.',
    },
    {
        'emoji': '🧝‍♂️',
        'descricao': 'Fantasia',
        'sobre': "Filmes de fantasia envolvem elementos mágicos e 'sobre'naturais, como dragões, elfos e magia. Podem ser baseados em livros e lendas.",
    },
    {
        'emoji': '🌊',
        'descricao': 'Aventura',
        'sobre': 'Filmes de aventura envolvem jornadas, explorações e descobertas. Podem envolver elementos de ação e ficção científica.',
    },
]

# Comando /filme
@bot.message_handler(commands=['filme'])
def adivinhar_categoria_filme(message):
    chat_id = message.chat.id

    # Escolha aleatória de uma categoria de filme
    categoria_aleatoria = random.choice(categorias)

    resposta = f'🎬 Sua categoria de filme preferida é: {categoria_aleatoria["descricao"]}\n\n'
    resposta += f'{categoria_aleatoria["sobre"]}\n'

    try:
        bot.reply_to(message, resposta)
    except Exception as e:
        bot.send_message(chat_id, resposta)


# CLIMA

# Lista de climas
climas = [
    {
        'emoji': '🌞',
        'descricao': 'Ensolarado',
    },
    {
        'emoji': '☁️',
        'descricao': 'Nublado',
    },
    {
        'emoji': '🌧️',
        'descricao': 'Chuvoso',
    },
    {
        'emoji': '❄️',
        'descricao': 'Neve',
    },
    {
        'emoji': '⛈️',
        'descricao': 'Tempestuoso',
    },
    {
        'emoji': '🌪',
        'descricao': 'Tornado',
    },
]

# Comando /clima
@bot.message_handler(commands=['clima'])
def adivinhar_clima_preferido(message):
    chat_id = message.chat.id

    # Escolha aleatória de um clima
    clima_aleatorio = random.choice(climas)

    resposta = f'Seu clima preferido é: {clima_aleatorio["descricao"]} {clima_aleatorio["emoji"]}\n'

    try:
        bot.reply_to(message, resposta)
    except Exception as e:
        bot.send_message(chat_id, resposta)


# NUMERO DA SORTE

# Comando /numerodasorte
@bot.message_handler(commands=['numerodasorte'])
def gerar_numero_da_sorte(message):
    chat_id = message.chat.id

    # Gere um número aleatório de 6 dígitos
    numero_da_sorte = random.randint(100000, 999999)

    resposta = f'Seu número da sorte é: {numero_da_sorte}'

    try:
        bot.reply_to(message, resposta)
    except Exception as e:
        bot.send_message(chat_id, resposta)


# DESAFIO

# Lista de desafios
desafios = [
    {
        'emoji': '🏋️‍♂️',
        'explicacao': 'Fazer 20 flexões',
    },
    {
        'emoji': '🏃‍♀️',
        'explicacao': 'Correr 5 km em menos de 30 minutos',
    },
    {
        'emoji': '🧘‍♂️',
        'explicacao': 'Meditar por 10 minutos',
    },
    {
        'emoji': '📚',
        'explicacao': 'Ler um livro inteiro em um dia',
    },
    {
        'emoji': '🎨',
        'explicacao': 'Desenhar um retrato realista',
    },
    {
        'emoji': '🎯',
        'explicacao': 'Acertar 10 tiros em um alvo a 10 metros de distância',
    },
    {
        'emoji': '🧗‍♂️',
        'explicacao': 'Escalar uma parede de escalada com 10 metros de altura',
    },
    {
        'emoji': '🏊‍♀️',
        'explicacao': 'Nadar 1 km sem parar',
    },
    {
        'emoji': '🎹',
        'explicacao': 'Aprender a tocar uma música nova no piano',
    },
    {
        'emoji': '🚴‍♂️',
        'explicacao': 'Andar de bicicleta por 50 km em um dia',
    },
    {
        'emoji': '🧘‍♀️',
        'explicacao': 'Fazer uma aula de yoga avançada',
    },
    {
        'emoji': '🎬',
        'explicacao': 'Escrever, dirigir e editar um curta-metragem de 5 minutos',
    },
    {
        'emoji': '🏭',
        'explicacao': 'Construir uma peça de mobília do zero',
    },
    {
        'emoji': '📝',
        'explicacao': 'Escrever um poema ou conto curto',
    },
    {
        'emoji': '🎨',
        'explicacao': 'Pintar um retrato a óleo',
    },
]

# Comando /desafio
@bot.message_handler(commands=['desafio'])
def enviar_desafio(message):
    chat_id = message.chat.id

    # Escolha aleatoriamente um desafio da lista
    desafio_aleatorio = random.choice(desafios)

    # Formate a mensagem usando HTML
    resposta = f"{desafio_aleatorio['emoji']} <b>Desafio do Dia</b> {desafio_aleatorio['emoji']}<pre>\n{desafio_aleatorio['explicacao']}</pre>"

    try:
        bot.reply_to(message, resposta)
    except Exception as e:
        bot.send_message(chat_id, resposta)


# JOGO


# Comando /jogo
@bot.message_handler(commands=['jogo'])
def enviar_jogo(message):
    chat_id = message.chat.id

    # Escolha aleatoriamente um jogo
    randomIndex = random.randint(0, 5)

    # Envie o jogo correspondente com um emoji e duração de animação de 5 segundos
    if randomIndex == 0:
        bot.send_dice(chat_id, emoji='🎲', animation_duration=5)
    elif randomIndex == 1:
        bot.send_dice(chat_id, emoji='🎯', animation_duration=5)
    elif randomIndex == 2:
        bot.send_dice(chat_id, emoji='🎳', animation_duration=5)
    elif randomIndex == 3:
        bot.send_dice(chat_id, emoji='⚽️', animation_duration=5)
    elif randomIndex == 4:
        bot.send_dice(chat_id, emoji='🎰', animation_duration=5)
    elif randomIndex == 5:
        bot.send_dice(chat_id, emoji='🏀', animation_duration=5)


# Comando /musica
@bot.message_handler(commands=['musica'])
def adivinhar_estilo_musical(message):
    chat_id = message.chat.id

    # Estilos musicais e suas descrições
    estilos_musicais = [
        {'emoji': '🎸', 'descricao': 'Rock'},
        {'emoji': '🎤', 'descricao': 'Pop'},
        {'emoji': '🎹', 'descricao': 'Eletrônica'},
        {'emoji': '🎷', 'descricao': 'Jazz'},
        {'emoji': '🎻', 'descricao': 'Clássica'},
        {'emoji': '🥁', 'descricao': 'Hip-Hop'},
        {'emoji': '🎶', 'descricao': 'Indie'},
        {'emoji': '🪕', 'descricao': 'Folk'},
        {'emoji': '🎵', 'descricao': 'Reggae'},
        {'emoji': '🎧', 'descricao': 'R&B'},
    ]

    # Escolha aleatoriamente um estilo musical
    estilo_musical = random.choice(estilos_musicais)

    # Envie o estilo musical adivinhado
    resposta = f"🎼 Seu estilo musical preferido é: {estilo_musical['emoji']} {estilo_musical['descricao']} 🎼"
    try:
        bot.reply_to(message, resposta)
    except Exception as e:
        bot.send_message(chat_id, resposta)


# COR

# Comando /cor
@bot.message_handler(commands=['cor'])
def adivinhar_cor_preferida(message):
    chat_id = message.chat.id

    # Cores e suas descrições
    cores = [
        {'emoji': '🔴', 'descricao': 'Vermelha'},
        {'emoji': '🟢', 'descricao': 'Verde'},
        {'emoji': '🔵', 'descricao': 'Azul'},
        {'emoji': '🟡', 'descricao': 'Amarela'},
        {'emoji': '🟣', 'descricao': 'Roxa'},
        {'emoji': '🟠', 'descricao': 'Laranja'},
        {'emoji': '🟤', 'descricao': 'Marrom'},
        {'emoji': '⚫', 'descricao': 'Preta'},
        {'emoji': '⚪', 'descricao': 'Branca'},
        {'emoji': '🟦', 'descricao': 'Turquesa'},
    ]

    cor_preferida = random.choice(cores)

    resposta = f"Sua cor preferida é: {cor_preferida['emoji']} {cor_preferida['descricao']} 🔴"
    try:
        bot.reply_to(message, resposta)
    except Exception as e:
        bot.send_message(chat_id, resposta)


# Comando /crush
@bot.message_handler(commands=['crush'])
def adivinhar_primeira_letra_crush(message):
    chat_id = message.chat.id

    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    primeira_letra = random.choice(letras)

    resposta = f'🥰 A primeira letra do nome do seu crush é: {primeira_letra} 🥰'
    try:
        bot.reply_to(message, resposta)
    except Exception as e:
        bot.send_message(chat_id, resposta)


# TIME

times = [
    {
        'nome': 'Flamengo',
        'imagemUrl': 'https://freevectorlogo.net/wp-content/uploads/2012/11/clube-de-regatas-do-flamengo-logo-vector-400x400.png',
        'estadio': 'Maracanã',
        'anoCriacao': '1895',
        'mascote': 'Urubu',
        'curiosidade': 'O Flamengo é o clube de futebol mais popular do Brasil, com a maior torcida do país.',
        'brasileiroes': 8,
    },
    {
        'nome': 'Corinthians',
        'imagemUrl': 'https://knoow.net/wp-content/uploads/2016/11/Logo-Corinthians.png',
        'estadio': 'Neo Química Arena',
        'anoCriacao': '1910',
        'mascote': 'Mosqueteiro',
        'curiosidade': 'O Corinthians é o clube de futebol com a maior torcida do estado de São Paulo.',
        'brasileiroes': 7,
    },
    {
        'nome': 'São Paulo',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1426319619200110596/m6gH60GL_400x400.jpg',
        'estadio': 'Morumbi',
        'anoCriacao': '1930',
        'mascote': 'São Paulo Man',
        'curiosidade': 'O São Paulo é o clube de futebol brasileiro com mais títulos internacionais, com 12 conquistas.',
        'brasileiroes': 6,
    },
    {
        'nome': 'Palmeiras',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1611063929916035095/se9po_Sh_400x400.jpg',
        'estadio': 'Allianz Parque',
        'anoCriacao': '1914',
        'mascote': 'Periquito',
        'curiosidade': 'O Palmeiras é o clube de futebol brasileiro com mais títulos nacionais, com 14 conquistas.',
        'brasileiroes': 11,
    },
    {
        'nome': 'Santos',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1615807063950598144/tSi5F77L_400x400.jpg',
        'estadio': 'Vila Belmiro',
        'anoCriacao': '1912',
        'mascote': 'Baleia',
        'curiosidade': 'O Santos é o clube de futebol brasileiro com mais títulos da Copa Libertadores da América, com 3 conquistas.',
        'brasileiroes': 8,
    },
    {
        'nome': 'Internacional',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1609276600582799362/iEniyUQp_400x400.png',
        'estadio': 'Beira-Rio',
        'anoCriacao': '1909',
        'mascote': 'Sací',
        'curiosidade': 'O Internacional é o clube de futebol brasileiro com mais títulos internacionais no século XX, com 7 conquistas.',
        'brasileiroes': 3,
    },
    {
        'nome': 'Grêmio',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1587444689568993280/jqTDMBmJ_400x400.jpg',
        'estadio': 'Arena do Grêmio',
        'anoCriacao': '1903',
        'mascote': 'Mosqueteiro',
        'curiosidade': 'O Grêmio é o clube de futebol brasileiro com mais títulos da Copa do Brasil, com 6 conquistas.',
        'brasileiroes': 2,
    },
    {
        'nome': 'Atlético-MG',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1467629667268112390/Ge6CuQfD_400x400.jpg',
        'estadio': 'Mineirão',
        'anoCriacao': '1908',
        'mascote': 'Galo',
        'curiosidade': 'O Atlético-MG é o clube de futebol brasileiro com mais títulos da Copa Conmebol, com 2 conquistas.',
        'brasileiroes': 2,
    },
    {
        'nome': 'Cruzeiro',
        'imagemUrl': 'https://pbs.twimg.com/media/ENQk13uW4AAU4nK?format=jpg&name=small',
        'estadio': 'Mineirão',
        'anoCriacao': '1921',
        'mascote': 'Raposa',
        'curiosidade': 'O Cruzeiro é o clube de futebol brasileiro com mais títulos da Copa do Brasil, ao lado do Grêmio, com 6 conquistas.',
        'brasileiroes': 4,
    },
    {
        'nome': 'Fluminense',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1609912077786746885/2F0rzkrh_400x400.jpg',
        'estadio': 'Maracanã',
        'anoCriacao': '1902',
        'mascote': 'Guerreiro',
        'curiosidade': 'O Fluminense é o clube de futebol brasileiro que mais conquistou o Campeonato Carioca, com 31 títulos.',
        'brasileiroes': 4,
    },
    {
        'nome': 'Botafogo',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1617191347852656641/Eb_gIMxP_400x400.jpg',
        'estadio': 'Engenhão',
        'anoCriacao': '1904',
        'mascote': 'Alvinegro',
        'curiosidade': 'O Botafogo é o clube de futebol brasileiro que mais vezes foi vice-campeão do Campeonato Brasileiro, com 5 vice-campeonatos.',
        'brasileiroes': 2,
    },
    {
        'nome': 'Vasco',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1620489733687083010/PRxiI2Jk_400x400.jpg',
        'estadio': 'São Januário',
        'anoCriacao': '1898',
        'mascote': 'Gigante',
        'curiosidade': 'O Vasco é o clube de futebol brasileiro que mais vezes foi campeão da Copa do Brasil, com 4 conquistas.',
        'brasileiroes': 4,
    },
    {
        'nome': 'Ceará',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1587278883732217857/lro974U6_400x400.jpg',
        'estadio': 'Arena Castelão',
        'anoCriacao': '1914',
        'mascote': 'Vozão',
        'curiosidade': 'O apelido "Vozão" surgiu em 1969, quando o Ceará disputou a Taça Brasil e foi elogiado pela voz forte de sua torcida.',
        'brasileiroes': 0,
    },
    {
        'nome': 'Chapecoense',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/934097344655773696/3K95PVdH_400x400.jpg',
        'estadio': 'Arena Condá',
        'anoCriacao': '1973',
        'mascote': 'Índio Condá',
        'curiosidade': 'A Chapecoense é o único clube de Santa Catarina a conquistar um título internacional, a Copa Sul-Americana de 2016.',
        'brasileiroes': 0,
    },
    {
        'nome': 'Coritiba',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1610677205981437953/L-ak1cT2_400x400.jpg',
        'estadio': 'Couto Pereira',
        'anoCriacao': '1909',
        'mascote': 'Vovô Coxa',
        'curiosidade': 'O Coritiba foi o primeiro time brasileiro a realizar uma excursão ao exterior, em 1928, jogando na Europa.',
        'brasileiroes': 1,
    },
    {
        'nome': 'CSA',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1613677488726589442/de0A7nA__400x400.jpg',
        'estadio': '',
        'anoCriacao': '',
        'mascote': '',
        'curiosidade': '',
        'brasileiroes': 0,
    },
    {
        'nome': 'Atlético-PR',
        'imagemUrl': 'https://static-wp-tor15-prd.torcedores.com/wp-content/uploads/2018/03/atletico-pr-300x300.jpg',
        'estadio': 'Arena da Baixada',
        'anoCriacao': '1924',
        'mascote': 'Furacão',
        'curiosidade': 'Foi o primeiro clube do sul do país a conquistar um título internacional, a Sul-Americana de 2018.',
        'brasileiroes': 1,
    },
    {
        'nome': 'Bahia',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1611322042212651010/ZtlPQ8BG_400x400.jpg',
        'estadio': 'Arena Fonte Nova',
        'anoCriacao': '1931',
        'mascote': 'Super-homem',
        'curiosidade': 'Foi o primeiro clube do Norte-Nordeste a conquistar um título internacional, a Copa do Nordeste de 2002.',
        'brasileiroes': 2,
    },
    {
        'nome': 'Goiás ',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1611755823687950336/sgvpPTvR_400x400.jpg',
        'estadio': 'Serra Dourada',
        'anoCriacao': '1943',
        'mascote': 'Verdão',
        'curiosidade': 'É o único clube goiano a ter participado da Copa Libertadores da América e a ter chegado a uma final de Copa Sul-Americana e de Copa do Brasil. ',
        'brasileiroes': 0,
    },
    {
        'nome': 'Red Bull Bragantino',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1609503108261978112/cFXWKxiE_400x400.jpg',
        'estadio': 'Estádio Nabi Abi Chedid',
        'anoCriacao': '1928',
        'mascote': 'Touro',
        'curiosidade': "O clube foi fundado como Bragantino, mas em 2019 foi comprado pelo grupo Red Bull e mudou seu 'nome'.",
        'brasileiroes': 0,
    },
    {
        'nome': 'Fortaleza',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1603764504126492674/iZs-LGQQ_400x400.jpg',
        'estadio': 'Arena Castelão',
        'anoCriacao': '1918',
        'mascote': 'Leão',
        'curiosidade': 'O Fortaleza foi o primeiro clube do Nordeste a disputar uma final de Campeonato Brasileiro, em 1960.',
        'brasileiroes': 0,
    },
    {
        'nome': 'Sport',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1620504487713546318/_iC_8nMh_400x400.jpg',
        'estadio': 'Ilha do Retiro',
        'anoCriacao': '1905',
        'mascote': 'Leão',
        'curiosidade': 'O Sport é o único clube do Nordeste a disputar a Libertadores da América.',
        'brasileiroes': 1,
    },
    {
        'nome': 'Santa Cruz',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1625890990383943682/eKSnyAos_400x400.jpg',
        'estadio': 'Arruda',
        'anoCriacao': '1914',
        'mascote': 'Cobra Coral',
        'curiosidade': 'O Santa Cruz é o time pernambucano que mais vezes participou do Campeonato Brasileiro.',
        'brasileiroes': 0,
    },
    {
        'nome': 'Vila Nova',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1610447696812285955/Nfi4_Az9_400x400.jpg',
        'estadio': 'Onésio Brasileiro Alvarenga',
        'anoCriacao': '1943',
        'mascote': 'Tigrão',
        'curiosidade': 'O Vila Nova é o único clube goiano a disputar a Série A do Campeonato Brasileiro.',
        'brasileiroes': 0,
    },
    {
        'nome': 'Salgueiro',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1131931961/2010_sac_topo2_400x400.jpg',
        'estadio': 'Cornélio de Barros',
        'anoCriacao': '1999',
        'mascote': 'Carcará',
        'curiosidade': 'O Salgueiro é o único clube do sertão pernambucano que disputou a Série C do Campeonato Brasileiro.',
        'brasileiroes': 0,
    },
    {
        'nome': 'Atlético-GO',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1229374310659379200/RpeEwctQ_400x400.jpg',
        'estadio': 'Antônio Accioly',
        'anoCriacao': '1937',
        'mascote': 'Dragão',
        'curiosidade': 'O Atlético-GO é o único clube goiano que já participou da Série A do Campeonato Brasileiro.',
        'brasileiroes': 0,
    },
    {
        'nome': 'Vitória',
        'imagemUrl': 'https://pbs.twimg.com/profile_images/1587778873592320000/UABdZsRp_400x400.jpg',
        'estadio': 'Manoel Barradas',
        'anoCriacao': '1899',
        'mascote': 'Leão',
        'curiosidade': 'O Vitória é o clube baiano com mais participações na Série A do Campeonato Brasileiro.',
        'brasileiroes': 0,
    },
]

# Comando /time
@bot.message_handler(commands=['time'])
def adivinhar_time_coracao(message):
    chat_id = message.chat.id

    time = random.choice(times)

    mensagem = f"{time['imagemUrl']}\n\n"
    mensagem += f"Nome: {time['nome']}\n"
    mensagem += f"Estádio: {time['estadio']}\n"
    mensagem += f"Ano de Criação: {time['anoCriacao']}\n"
    mensagem += f"Mascote: {time['mascote']}\n"
    mensagem += f"Curiosidade: {time['curiosidade']}\n"
    mensagem += f"Campeonatos Brasileiros: {time['brasileiroes']}"

    try:
        bot.send_photo(
            chat_id,
            time['imagemUrl'],
            caption=mensagem,
            reply_to_message_id=message.message_id,
        )

    except Exception as e:
        bot.send_photo(chat_id, time['imagemUrl'], caption=mensagem)


# Lista de frutas
frutas = [
    '🍏 Maçã',
    '🍌 Banana',
    '🍇 Uva',
    '🍈 Melão',
    '🍉 Melancia',
    '🍊 Laranja',
    '🍓 Morango',
    '🍑 Pêssego',
    '🍍 Abacaxi',
    '🥭 Manga',
    '🍒 Cereja',
    '🥝 Kiwi',
    '🍎 Pera',
    '🍏 Kiwi',
    '🍅 Tomate (sim, é uma fruta!)',
]

# Comando /fruta
@bot.message_handler(commands=['fruta'])
def adivinhar_fruta_preferida(message):
    chat_id = message.chat.id

    try:
        fruta = random.choice(frutas)

        mensagem = f'Sua fruta preferida é: {fruta}'

        bot.reply_to(message, mensagem)

    except Exception as e:
        bot.reply_to(
            message,
            f'Ocorreu um erro ao adivinhar a sua fruta preferida: {str(e)}',
        )


# curiosidade

curiosidades = [
    'A lua cheia aparece no céu por cerca de 29 dias',
    'Os cavalos não conseguem vomitar',
    'O primeiro computador foi inventado na década de 1940',
    'O som se propaga mais rápido na água do que no ar',
    'A maior montanha-russa do mundo tem mais de 140 metros de altura',
    'O olho humano é capaz de distinguir mais de 10 milhões de cores',
    'A cidade de Veneza, na Itália, é formada por 118 ilhas',
    'A Mona Lisa é o quadro mais famoso do mundo',
    'O coração bate em média 100.000 vezes por dia',
    'O elefante é o maior animal terrestre',
    'Um raio pode chegar a uma temperatura de 30.000 graus Celsius.',
    'A lua é o único satélite natural da Terra.',
    'A água é o único elemento que é encontrado naturalmente na natureza em três estados diferentes: líquido, sólido e gasoso.',
    'O cérebro humano pesa cerca de 1,3 kg.',
    'O nariz humano é capaz de distinguir mais de 1 trilhão de cheiros diferentes.',
    'A cidade mais populosa do mundo é Tóquio, com uma população de mais de 37 milhões de pessoas.',
    'O diamante é a substância mais dura conhecida pelo homem.',
    'O coração humano bate cerca de 100.000 vezes por dia.',
    'A baleia-azul é o maior animal do planeta, podendo chegar a medir mais de 30 metros de comprimento.',
    'O Sol é uma estrela e está localizado a cerca de 149,6 milhões de quilômetros da Terra.',
    'O mel é o único alimento que não estraga.',
    'O olho humano é capaz de distinguir mais de 10 milhões de cores diferentes.',
    'O crocodilo é capaz de sobreviver por mais de um ano sem comer.',
    'O território da Rússia é o maior do mundo, com mais de 17 milhões de quilômetros quadrados.',
    'A barata é capaz de sobreviver por mais de uma semana sem a cabeça.',
    'O pinguim é a única ave que é capaz de nadar, mas não voar.',
    'O canguru é capaz de pular até 3 vezes a sua própria altura.',
    'O Planeta Terra tem cerca de 4,5 bilhões de anos.',
    'O peixe-palhaço é capaz de mudar de sexo ao longo da vida, podendo nascer macho e depois se tornar fêmea.',
    'O Google é o site mais visitado do mundo.',
    'A banana é a fruta mais consumida no mundo.',
    'O recorde mundial de velocidade em terra é de 1.609 km/h, alcançado pelo carro Bloodhound SSC.',
    'O corvo é um dos poucos animais que é capaz de fabricar e utilizar ferramentas.',
    'A Gran Pirâmide de Gizé, no Egito, é a única das Sete Maravilhas do Mundo Antigo que ainda existe.',
    'Aves têm um órgão chamado pipoqueira que as ajuda a digerir alimentos duros como sementes.',
    'Os buracos negros são regiões do espaço onde a gravidade é tão forte que nem a luz consegue escapar.',
    'O tatu-bola é capaz de se enrolar completamente em uma bola para se proteger dos predadores.',
    'O Google foi criado em 1996 como um projeto de pesquisa de doutorado na Universidade de Stanford.',
    'A cidade de Istambul, na Turquia, é a única cidade que está situada em dois continentes: Europa e Ásia.',
    'O elefante é o único animal que é capaz de se reconhecer em um espelho.',
    'O tigre é o maior felino do mundo.',
    'A velocidade da luz é de aproximadamente 299.792.458 metros por segundo.',
    'A Antártida é o continente mais frio do planeta, com temperaturas que podem chegar a -89,2 graus Celsius.',
    'O besouro rinoceronte é capaz de suportar mais de 850 vezes o seu próprio peso.',
    'O maior animal terrestre do planeta é o elefante-africano.',
    'O voo comercial mais longo do mundo é feito entre Singapura e Nova York, com uma duração de mais de 18 horas.',
    'O urso polar é o único urso que é capaz de viver exclusivamente em regiões de gelo.',
    'O Monte Everest é a montanha mais alta do mundo, com uma altitude de 8.848 metros.',
    'O caranguejo-aranha-japonês é o maior artrópode do mundo, podendo medir até 3,8 metros de comprimento.',
    'O planeta Vênus é o mais quente do Sistema Solar, com uma temperatura média de 462 graus Celsius.',
    'O bico do pelicano pode comportar até 13 litros de água.',
    'O deserto do Saara é o maior deserto quente do mundo.',
    'O rinoceronte-branco é o segundo maior animal terrestre do mundo, perdendo apenas para o elefante.',
    'O coração da baleia-azul é tão grande que um ser humano adulto poderia nadar através das suas artérias.',
    'O lobo é o animal selvagem mais amplamente distribuído do mundo.',
    'O quetzal é a ave nacional da Guatemala.',
    'O animal que tem o maior tempo de vida é a tartaruga-gigante-das-galápagos, que pode viver mais de 150 anos.',
    'O hipopótamo é capaz de ficar submerso na água por até 5 minutos.',
    'A Grande Barreira de Corais é o maior sistema de recifes de coral do mundo.',
    'O crocodilo de água salgada é o maior réptil do mundo, podendo chegar a medir mais de 7 metros de comprimento.',
    'O sistema nervoso humano é capaz de transmitir sinais a uma velocidade de até 400 km/h.',
    'O nome completo do personagem Mickey Mouse é Michael Theodore Mouse.',
    'A música é capaz de ativar diversas áreas do cérebro humano.',
    'O Pólo Norte é o ponto mais ao norte da Terra.',
    'O agente secreto mais famoso do mundo é James Bond.',
    'O joelho humano é a articulação mais complexa do corpo humano.',
    'O estudo do comportamento humano é chamado de psicologia.',
    'A girafa é o animal mais alto do mundo, podendo chegar a medir mais de 5 metros de altura.',
    'O orvalho é formado pela condensação do vapor de água que se encontra no ar.',
    'A língua mais falada no mundo é o Mandarim, seguido pelo Espanhol, Inglês, Hindi e Árabe.',
    'As estrelas do mar não têm cérebros, mas têm olhos na ponta de cada braço.',
    'A luz leva aproximadamente 8 minutos para viajar do Sol até a Terra.',
    'O coração humano bate cerca de 100.000 vezes por dia.',
    'O maior mamífero do mundo é a baleia-azul, podendo chegar a medir 30 metros de comprimento.',
    'A cidade mais populosa do mundo é Tóquio, no Japão, com mais de 37 milhões de habitantes.',
    'As bactérias encontradas no intestino humano podem pesar até 2 kg.',
    'O país mais populoso do mundo é a China, com mais de 1,4 bilhões de habitantes.',
    'O relâmpago pode aquecer o ar a uma temperatura cinco vezes mais quente que a superfície do Sol.',
    'A água cobre aproximadamente 71% da superfície da Terra.',
    'O maior vulcão do sistema solar é o Monte Olimpo, em Marte, que tem três vezes a altura do Monte Everest.',
    'Os pandas gigantes são nativos apenas da China.',
    'A Antártida é o lugar mais frio da Terra, com temperaturas que podem chegar a -90°C.',
    'Apenas 5% do oceano já foi explorado pelos seres humanos.',
    'O riso reduz o estresse, fortalece o sistema imunológico e melhora a saúde mental.',
    'A maior ilha do mundo é a Groenlândia, que é cerca de 14 vezes maior que a Inglaterra.',
    'As unhas das mãos crescem mais rapidamente do que as dos pés.',
    'O ponto mais profundo do oceano é a Fossa das Marianas, que tem cerca de 11 km de profundidade.',
    'O deserto do Saara é o maior deserto quente do mundo, cobrindo uma área de 9,2 milhões de km².',
    'A abelha rainha pode viver até 5 anos, enquanto as abelhas operárias vivem apenas algumas semanas.',
    'O cérebro humano tem capacidade para armazenar até 2,5 petabytes de informação.',
    'O rio Amazonas é o rio mais longo do mundo, com cerca de 6.400 km de extensão.',
    'As formigas podem levantar até 50 vezes o seu próprio peso.',
    'O maior animal terrestre é o elefante africano, podendo pesar até 12 toneladas.',
    'O maior desfiladeiro do mundo é o Grand Canyon, nos Estados Unidos, com cerca de 446 km de comprimento.',
    'O sangue humano é composto por cerca de 55% de plasma e 45% de células.',
    'O arco-íris pode ser visto apenas quando o sol está brilhando e chovendo ao mesmo tempo.',
    'Os olhos de um avestruz são maiores do que o seu cérebro.',
    'A velocidade da luz é de cerca de 299.792.',
]

# Comando /curiosidade
@bot.message_handler(commands=['curiosidade'])
def enviar_curiosidade(message):
    chat_id = message.chat.id

    try:
        curiosidade = random.choice(curiosidades)

        bot.send_message(chat_id, curiosidade)

    except Exception as e:
        bot.send_message(
            chat_id, f'Ocorreu um erro ao buscar uma curiosidade: {str(e)}'
        )


# sigma


@bot.message_handler(commands=['sigma'])
def sigma(message):
    nivelSigma = random.randint(1, 100)

    gifSigma = None
    if nivelSigma < 30:
        gifSigma = (
            'https://media.tenor.com/Wg9fW_XEft0AAAAC/pout-christian-bale.gif'
        )
    elif nivelSigma < 40:
        gifSigma = 'https://media.tenor.com/Xa3KRCTJUuUAAAAd/homelander-theboysfinale.gif'
    elif nivelSigma < 50:
        gifSigma = (
            'https://media.tenor.com/lPcexeCDyZ8AAAAd/gentleman-giga-chad.gif'
        )
    elif nivelSigma < 60:
        gifSigma = (
            'https://media.tenor.com/1WyZr_xNiVwAAAAC/sigma-sigma-male.gif'
        )
    elif nivelSigma < 70:
        gifSigma = 'https://media.tenor.com/V69OjtC-eFAAAAAd/sigma-male-sigma-from-ohio.gif'
    elif nivelSigma < 90:
        gifSigma = 'https://media.tenor.com/Rv4pV5ppmVsAAAAC/homelander-laser-eyes.gif'
    else:
        gifSigma = (
            'https://media.tenor.com/QNpimm5BA-QAAAAd/good-day-smile.gif'
        )

    mensagem = f'Seu nível Sigma é {nivelSigma} 🗿🍷'
    mensagem_com_gif = f'{mensagem}'

    try:

        bot.send_animation(
            message.chat.id,
            gifSigma,
            caption=mensagem,
            reply_to_message_id=message.message_id,
        )
    except Exception as e:
        bot.send_animation(message.chat.id, gifSigma, mensagem_com_gif)


print('Bot iniciando ...')
bot.infinity_polling(allowed_updates=util.update_types, skip_pending=True)
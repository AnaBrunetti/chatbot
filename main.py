import telebot
from pycotacao import get_exchange_rates, CurrencyCodes

CHAVE_API = "5758637736:AAHYd0RGyaaIU2UkEG9dOBOYnmdhqAlgmeU"

bot = telebot.TeleBot(CHAVE_API)
help_text = """
Cotações em reais hoje:

    Por moedas
    /dolar
    /dolar_autraliano
    /euro
    /rand
    /yuan

    Tabela de cotações
    /tabela
"""

def show_coin_quotation(coin):
    cotacao = get_exchange_rates(coin)
    buy_rate = cotacao.buying_rate
    sell_rate = cotacao.selling_rate
    return f"""
    Compra: {buy_rate}. Venda: {sell_rate}.
    """

# Moeda mais usada na América
@bot.message_handler(commands=["dolar"])
def dolar(mensagem):
    bot.send_message(mensagem.chat.id, show_coin_quotation(CurrencyCodes.USD))

# Moeda mais usada na Oceania
@bot.message_handler(commands=["dolar_autraliano"])
def dolar_autraliano(mensagem):
    bot.send_message(mensagem.chat.id, show_coin_quotation(CurrencyCodes.CAD))

# Moeda mais usada na Europa
@bot.message_handler(commands=["euro"])
def euro(mensagem):
    bot.send_message(mensagem.chat.id, show_coin_quotation(CurrencyCodes.EUR))

# Moeda mais usada na Africa
@bot.message_handler(commands=["rand"])
def rand(mensagem):
    bot.send_message(mensagem.chat.id, show_coin_quotation(CurrencyCodes.ZAR))

# Moeda mais usada na Asia
@bot.message_handler(commands=["yuan"])
def yuan(mensagem):
    bot.send_message(mensagem.chat.id, show_coin_quotation(CurrencyCodes.CNY))

# Função para retornar todas as cotações
@bot.message_handler(commands=["tabela"])
def tabela(mensagem):
    table = f"""Tabela de cotações:
    _________________________________    
      Moedas    | Compra    | Venda      
    |________________________________|
      Dolar         | {get_exchange_rates(CurrencyCodes.USD).buying_rate}      | {get_exchange_rates(CurrencyCodes.USD).selling_rate}     
    |________________________________|
      Dolar Au   | {get_exchange_rates(CurrencyCodes.CAD).buying_rate}      | {get_exchange_rates(CurrencyCodes.CAD).selling_rate}     
    |________________________________|
      Euro          | {get_exchange_rates(CurrencyCodes.EUR).buying_rate}      | {get_exchange_rates(CurrencyCodes.EUR).selling_rate}      
    |________________________________|
      Rand         | {get_exchange_rates(CurrencyCodes.ZAR).buying_rate}      | {get_exchange_rates(CurrencyCodes.ZAR).selling_rate}      
    |________________________________|
      Yuan         | {get_exchange_rates(CurrencyCodes.CNY).buying_rate}      | {get_exchange_rates(CurrencyCodes.CNY).selling_rate}      
    |________________________________|
    """
    bot.send_message(mensagem.chat.id, table)

# Função de ajuda
@bot.message_handler(commands=["help"])
def help(mensagem):
    bot.send_message(mensagem.chat.id, help_text)

# Retorno de mensagem para qualquer caso
def verify(_):
    return True
@bot.message_handler(func=verify)
def answer(mensagem):
    bot.reply_to(mensagem, help_text)

bot.polling()
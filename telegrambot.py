import os
import telebot

def sendMessage(data):
  API_KEY = os.environ['API_KEY']
  tg_bot = telebot.TeleBot(API_KEY, parse_mode="MARKDOWN")
  channel = os.environ['CHANNEL']
  try:
    tg_bot.send_message(
      channel,
      data,
      parse_mode="MARKDOWN",
    )
    return True
  
  except KeyError:
    tg_bot.send_message(
      channel,
      data,
      parse_mode="MARKDOWN",
    )
    
  except Exception as e:
    print("[X] Telegram Error\n>", e)
    
  return False

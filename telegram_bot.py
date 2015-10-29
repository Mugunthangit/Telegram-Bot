import logging
import telegram
import feedparser

LAST_UPDATE_ID = None

d = feedparser.parse('URL_to_feed')
#Replace the rss link in "URL_to_Feed"... For Example http://johnbokma.com/index.rss
latest_update = d.entries[0].title + " " + d.entries[0].link
#To get the latest updates in rss feed...   

def main():
    global LAST_UPDATE_ID
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Telegram Bot Authorization Token
    bot = telegram.Bot('place your token')
    # This will be our global variable to keep the latest update_id when requesting
    # for updates. It starts with the latest update_id if available.
    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError:
        LAST_UPDATE_ID = None

    while True:
        echo(bot)

def echo(bot):
    global LAST_UPDATE_ID
    # Request updates after the last updated_id
    for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=10):
        # chat_id is required to reply any message
		chat_id = update.message.chat_id
		message = update.message.text.encode('utf-8')
		if (message == '/place_your_keyword(user_wish)'): #Give any keyword to use this bot
			# Reply the message
            bot.sendMessage(chat_id=chat_id,text=latest_update)
            # Updates global offset to get the new updates
            LAST_UPDATE_ID = update.update_id + 1
    
if __name__ == '__main__':
    main()
    
    

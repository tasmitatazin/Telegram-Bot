from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN: Final = #add token here
BOT_USERNAME: Final = '@banana_egg_milk_bot'

#create a start command 
#make it asyncronous 
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hey! Welcome!  I am Tas bot')

#make help command 
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hey! How can I, Tas bot help you today?')

#now a custom command
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('You have used the custom command')


#Handle responses so that the bot can respond
#takes type string and returns string
def handle_response(text: str) -> str:
    #craete a simple if else bot 
    #add processed text so its no longer case sensitive
    processed: str = text.lower()
    if 'Hi' in processed: 
        return 'hey!'
    if 'how are you?' in processed: 
        return 'great! what about you?'
    if 'I love you' in processed:
        return 'I love you too!'
    if ' whats better? Telegram or Whatsapp?' in processed: 
        return 'def Telegram' 

    return 'I did not really undestand, could you elaborate?'

#need to create functions to handle the messages 

async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type #how we will know if its a group chat or provate chat 
    text:str = update.message.text #incoming message

    #create print statement for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"') #get the user id who is sending the message 

     #bot will not respond unless its called in group 
    if message_type =='group':
            if BOT_USERNAME in text:
                new_text:str = text.replace(BOT_USERNAME,'').strip()
                response:str= handle_response(new_text)
            else: 
                 return
    else: # for private chats
        response: str = handle_response(text)


    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update:Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__=='__main__':
    print('starting bot....')
    app = Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))

    #messages 
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #errors
    app.add_error_handler(error)

    print('polling....')
    app.run_polling(poll_interval=2)







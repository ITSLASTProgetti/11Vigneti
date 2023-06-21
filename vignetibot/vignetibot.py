from urllib.request import urlopen
from telegram import Update
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext

# IMPORTANTE: inserire il token fornito dal BotFather nella seguente stringa
with open("token.txt", "r") as f:
    TOKEN = f.read()
    #print("Il tuo token è ", TOKEN)
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Comandi disponibili:
        /paese: scegli il paese
        """)
async def paese(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("bussolengo", url='http://umap.openstreetmap.fr/it/map/bussolengo_931563?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true'),
                 InlineKeyboardButton("castelnuovo", url='https://umap.openstreetmap.fr/it/map/castelnuovo_931588?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true'),
                 InlineKeyboardButton("lazise", url='http://umap.openstreetmap.fr/it/map/lazise_931580?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')],
                [InlineKeyboardButton("mozzecane", url='https://umap.openstreetmap.fr/it/map/mozzecane_931586?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true'),
                 InlineKeyboardButton("pastrengo", callback_data='pastrengo'),
                 InlineKeyboardButton("pescantina", callback_data='pescantina')],
                [InlineKeyboardButton("sommacampagna", callback_data='sommacampagna'),
                 InlineKeyboardButton("sona", callback_data='sona'),
                 InlineKeyboardButton("valeggio", callback_data='valleggio')],
                [InlineKeyboardButton("vigasio", callback_data='vigasio'),
                 InlineKeyboardButton("villafranca", callback_data='villafranca')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Seleziona un paese:', reply_markup=reply_markup)



def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('paese', paese))
    app.run_polling()

if __name__=='__main__':
   main()

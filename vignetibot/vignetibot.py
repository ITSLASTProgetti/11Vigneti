from urllib.request import urlopen
import os
import csv
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
    /area: per vedere l'area occupata dai vigneti nei singoli paesi
        """)
async def paese(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("bussolengo", url='http://umap.openstreetmap.fr/it/map/bussolengo_931563?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true'),
                 InlineKeyboardButton("castelnuovo", url='https://umap.openstreetmap.fr/it/map/castelnuovo_931588?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true'),
                 InlineKeyboardButton("lazise", url='http://umap.openstreetmap.fr/it/map/lazise_931580?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')],
                [InlineKeyboardButton("mozzecane", url='https://umap.openstreetmap.fr/it/map/mozzecane_931586?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true'),
                 InlineKeyboardButton("pastrengo", url='https://umap.openstreetmap.fr/it/map/pastrengo_931613?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true'),
                 InlineKeyboardButton("pescantina", url='https://umap.openstreetmap.fr/it/map/pescantina_931615?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')],
                [InlineKeyboardButton("sommacampagna", url='https://umap.openstreetmap.fr/it/map/sommacampagna_931617?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true'),
                 InlineKeyboardButton("sona", url='https://umap.openstreetmap.fr/it/map/sona_931618?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true'),
                 InlineKeyboardButton("valeggio", url='https://umap.openstreetmap.fr/it/map/valeggio_931620?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')],
                [InlineKeyboardButton("vigasio", url='https://umap.openstreetmap.fr/it/map/vigasio_931632?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true'),
                 InlineKeyboardButton("villafranca", url='https://umap.openstreetmap.fr/it/map/villafranca_931629?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Seleziona un paese:', reply_markup=reply_markup)


# Directory contenente i file CSV
directory = '../data'

# Elenco dei file CSV nella cartella
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

# Lista delle aree totali dei file CSV
aree_totali = []

# Funzione per calcolare l'area totale di un file CSV
def calcola_area_totale(file):
    with open(os.path.join(directory, file), 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        prima_riga = True  # Variabile per tenere traccia della prima riga
        area_totale = 0  # Variabile per tenere traccia dell'area totale del file
        for row in csv_reader:
            if prima_riga:
                prima_riga = False
                continue  # Salta la prima riga del file CSV
            area = float(row[3])  # Indicizza il valore della colonna 'area'
            area_totale += area
        aree_totali.append(area_totale)

# Calcola l'area totale di ogni file CSV
for file in csv_files:
    calcola_area_totale(file)

# Funzione per mostrare le aree totali dei file CSV
async def area(update: Update, context: CallbackContext):
    text = "Area occupata dai vigneti nei singoli paesi:\n\n"
    for i, area in enumerate(aree_totali):
        text += f"{csv_files[i]}: {area}\n"
    await update.message.reply_text(text)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('paese', paese))
    app.add_handler(CommandHandler('area', area))
    app.run_polling()

if __name__=='__main__':
   main()
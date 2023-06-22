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
    /ordine: per vedere l'area occupata dai vigneti nei singoli paesi (in ordine decrescente)
    /prop: per vedere la proporzione tra l'area totale dei paesi di verona e l'area dei vigneti dei paesi di verona
    /propaese: per vedere la proporzione tra l'area dei singoli paesi di verona e l'area dei dei vigneti di ogni singolo paese
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
aree_totali_metri_quadrati = []


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
            area_pollici_quadrati = float(row[3])  # Indicizza il valore della colonna 'area' in pollici quadrati
            area_metri_quadrati = area_pollici_quadrati * 0.00064516  # Converti l'area in metri quadrati
            area_totale += area_metri_quadrati
        aree_totali_metri_quadrati.append(area_totale)


# Calcola l'area totale di ogni file CSV
for file in csv_files:
    calcola_area_totale(file)




# Ordina le aree totali dal maggiore al minore
aree_totali_metri_quadrati_ordinate = sorted(aree_totali_metri_quadrati, reverse=True)


# Funzione per mostrare le aree totali dei file CSV
async def area(update: Update, context: CallbackContext):
    text = "Area occupata dai vigneti nei singoli paesi:\n\n"
    for i, area in enumerate(aree_totali_metri_quadrati):
        text += f"{csv_files[i]}: {area} m²\n"
    await update.message.reply_text(text)

  

# Funzione per mostrare le aree totali dei file CSV in ordine decrescente in metri quadrati
async def ordine(update: Update, context: CallbackContext):
    text = "Area occupata dai vigneti nei singoli paesi (in ordine decrescente):\n\n"
    for area in aree_totali_metri_quadrati_ordinate:
        index = aree_totali_metri_quadrati.index(area)
        file = csv_files[index]
        text += f"{file}: {area} m²\n"
    await update.message.reply_text(text)

async def prop(update: Update, context: CallbackContext,):

    input_data = {
            'Bussolengo': 24280000,
            'Castelnuovo del Garda': 13450000,
            'Lazise': 65000000,
            'Mozzecane': 24700000,
            'Pastrengo': 8960000,
            'Pescantina': 19700000,
            'Sommacampagna': 40910000,
            'Sona': 41140000,
            'Valeggio sul Mincio': 63900000,
            'Vigasio': 30800000,
            'Villafranca di Verona': 57430000
        }

    # Calcola l'area totale dei vigneti restituita dalla funzione "area()"
    area_vigneti = sum(aree_totali_metri_quadrati)

    # Calcola l'area totale dei vigneti in base ai dati di input
    area_vigneti_input = sum(input_data.values())

    # Calcola la proporzione tra l'area dei vigneti restituita dalla funzione "area()" e l'area dei vigneti in base ai dati di input
    proporzione = area_vigneti_input / area_vigneti

    # Crea il testo di risposta
    text = f"Area totale dei vigneti: {area_vigneti} m²\n"
    text += f"Area totale dei paesi: {area_vigneti_input} m²\n"
    text += f"Proporzione dell'area totale dei paesi rispetto all'area totale dei vigneti: {proporzione:.2%}"


    # Invia il messaggio di risposta
    await update.message.reply_text(text)

async def propaese(update: Update, context: CallbackContext):
    aree_per_paese = {}
    for i, area in enumerate(aree_totali_metri_quadrati):
        aree_per_paese[csv_files[i]] = area
        text = f"{csv_files[i]}: {area} m²\n"
    # Salva il dizionario nel contesto
    context.user_data['aree_per_paese'] = aree_per_paese
    
    # Calcola la somma delle aree totali
    area_totale = sum(aree_per_paese.values())

    # Calcola la proporzione per ogni paese
    text_prop = "\nProporzione delle aree per paese:\n\n"
    for paese, area in aree_per_paese.items():
        proporzione = area / area_totale
        text_prop += f"{paese}: {proporzione:.2%}\n"
    
    await update.message.reply_text(text_prop)



def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('paese', paese))
    app.add_handler(CommandHandler('area', area))
    app.add_handler(CommandHandler('ordine', ordine))
    app.add_handler(CommandHandler('prop', prop))
    app.add_handler(CommandHandler('propaese', propaese))

    app.run_polling()

if __name__=='__main__':
   main()
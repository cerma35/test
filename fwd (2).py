from pyrogram import Client, filters
import requests
import json
import re

API_ID = 20906264 #api id da prendere su my.telegram.org
API_HASH = "2c4e62366097ff3f08081fc11e779bc1" #api hash da prendere su my.telegram.org

canale_dove_prendere_mex = 'TopOfferteExclusive' #inserire il tag del canale/gruppo da cui prendere i messaggi
canale_dove_inviare = "@amazonrecensioniit" #inserire il tag del canale/gruppo a cui mandare i messaggi

app = Client('fwd_bott', api_id=API_ID, api_hash=API_HASH) #fwd_bott e' il nome del file dove si salvera' la sessione


print("bot avviato!") #scrive che il bot e' stato avviato

@app.on_message(filters.chat(canale_dove_prendere_mex))
def update_command(client,message):
	try: #gestione in caso errore (puo' verificarsi un errore quando il messaggio non corrisponde a quello voluto)
		message_dict = json.loads(str(message)) #trasforma il messaggio in json per prendere i dati

		
		asin = message_dict["reply_markup"]["inline_keyboard"][0][0]["url"].split("dp/")[1].split("/?")[0] #ottieni asin dal messaggio
		bottone_link = f"[LINK](https://www.amazon.it/dp/{asin}/?tag=eryones-21&psc=1)" #crea il bottone con scritto LINK
		nuovomessaggio = message.nuovo_testo = re.sub(r'https://amzn\.to/[a-zA-Z0-9]+', bottone_link, str(message.text.markdown)+"\n\n**@amazonrecensioniit**") #cambia ref nel nuovo messaggio
		
		app.send_message(canale_dove_inviare, nuovomessaggio) #invia il messaggio sul canale/gruppo
	except:
		pass
app.run()
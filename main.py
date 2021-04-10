
import os
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
import requests
import mysql.connector
from telegram.utils import helpers
import logging
import time
import random
from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyKeyboardRemove,ParseMode
from telegram.ext import Updater,CommandHandler,CallbackQueryHandler,ConversationHandler,MessageHandler,CallbackContext,Filters
coin=requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d")
coingecko=coin.json()
admin='1093222544'
TOKEN='1762560403:AAGWkC57kJgn-LXbTVeo7E43wLS0M2St818'
conn = mysql.connector.connect(host="sql10.freemysqlhosting.net",user="sql10402965",password="pato.7788", database="sql10402965")
cursor = conn.cursor()

def rbtc(bt,cid):
    cursor.execute("""
UPDATE wmc
SET btc=%s
WHERE cid=%s    
    """,(bt,cid,))
def reth(bt,cid):
    cursor.execute("""
UPDATE wmc
SET eth=%s
WHERE cid=%s    
    """,(bt,cid,)
    )
def rltc(bt,cid):
    cursor.execute("""
UPDATE wmc
SET ltc=%s
WHERE cid=%s    
    """,(bt,cid,)
    )
def rtikets(bt,cid):
    cursor.execute("""
UPDATE wmc
SET tikets=%s
WHERE cid=%s    
    """,(bt,cid,)
    )


def row(cid):
    
    cursor.execute("""
SELECT * FROM wmc WHERE cid=%s 
    """,(cid ,))
    row=cursor.fetchall()
    row=row[0]
    return row
def litecoin():
    for i in coingecko:
        if i['symbol']=='ltc':
            price=i['current_price']
    return price
def start(update:Update,context:CallbackContext):
    
    cid=update.message.chat.id  
    name=update.message.chat.username
    dt=update.message.date
    mid=update.message.message_id
    data=(cid, name , dt , mid)
    try:
        cursor.execute("""
        INSERT INTO wmc (cid,nom,date,mid) VALUE (%s , %s ,%s , %s )""",data)
    except:
        cid=update.message.chat.id
        mid=update.message.message_id

        cursor.execute("""
        UPDATE wmc
        SET mid=%s
        WHERE cid=%s""",(mid,cid,))
        update.message.reply_text('select the language',reply_markup=ReplyKeyboardMarkup([['🇫🇷Francais','🏴󠁧󠁢󠁥󠁮󠁧󠁿english']],resize_keyboard='true'))
        context.bot.sendMessage(text='hu',chat_id=admin)
    else:
    	cursor.execute("""
        UPDATE wmc
        SET mid=%s
        WHERE cid=%s""",(mid,cid,))

    	gt=update.message.text[13:25]
    	update.message.reply_text('select the language',reply_markup=ReplyKeyboardMarkup([['🇫🇷Francais','🏴󠁧󠁢󠁥󠁮󠁧󠁿english']],resize_keyboard='true'))
    	try:
    	 context.bot.sendMessage(text='➕ vous avez un nouveau refferal 🎉\n\n'
 'bonus : +1🎟',chat_id=gt)
    	 bt=row(cid)[6]+1
    	 rtikets(bt,gt)
    	except:
    		time.sleep(0.00000000000001)
    	
    		

def francais(update:Update,context:CallbackContext):
            	update.message.reply_text(
f"BIENVENUE sur [Win Max currency ](t.me/wmcurrency_bot) 💸💰💵\n"
f"nous distribuons les cryptomonaies tels que :\n"
f"   👉[le bitcoin](https//:www.coingecko.com) :\n"
f"       💧prix actuel:${coingecko[0]['current_price']}\n"
f"   👉[l'ethereum](https//:www.coingecko.com) :\n"
f"       💧prix actuel:${coingecko[1]['current_price']}\n"
f"   👉[le litecoin](https//:www.coingecko.com) :\n"
f"       💧prix actuel:${litecoin()}\n"
f"en effet pour recevoir de la cryptomonaie\n"
f"il faut respecter les etapes suivantes:\n"
f"1️⃣ envoyez votre lien a un ami\n"
f"     ♦️ vous obtenez un tiket pour chaque ami\n"
f"     ♦️ vous obtenez aussi 20% de leurs gains\n"
f"2️⃣ cliquer sur le bouton 'Distributeur'\n"
f"     ♦️ plusieurs options vous seront proposées\n"
f"     ♦️ choisissez celle qui vous convient\n"
f"ainsi vous recevez des cryptomonaies dont le retrait\n"
f"se fait en cliquant sur le bouton '👛Retrait'\n"
f"contactez le support en cas de soucis:💬support\n"
f"sur le fonctionnement du bot",reply_markup=ReplyKeyboardMarkup([['🏦Distributeur','👤Compte'],['🗣Refferal','🛒Ameliorer','👛Retrait'],['🧮megeboom bonus','💬support 24/7']],resize_keyboard='true'),parse_mode=ParseMode.MARKDOWN)


def english(update:Update,context:CallbackContext):
             
             if row(update.message.chat.id)[4]==update.message.message_id-2:
             	update.message.reply_text(row(update.message.chat.id)[5])
def distributeur(update:Update,context:CallbackContext):
                    plan=row(update.message.chat.id)[5]
                    if plan=='gratuit':
                        em1='✅'
                        em2='❌'
                        em3='❌'
                        em4='❌'
                        em5='❌'
                    elif plan=='v1':
                        em1='❌'
                        em2='✅'
                        em3='❌'
                        em4='❌'
                        em5='❌'
                    elif plan=='v2':
                        em1='❌'
                        em2='❌'
                        em3='✅'
                        em4='❌'
                        em5='❌'
                    elif plan=='pro':
                        em1='❌'
                        em2='❌'
                        em3='❌'
                        em4='✅'
                        em5='❌'
                    elif plan=='promax':
                        em1='❌'
                        em2='❌'
                        em3='❌'
                        em4='❌'
                        em5='✅'
                    update.message.reply_text(
"🎪DISTRIBUTEUR:LITECOIN\n"
"tantez votre chance en cliquant "
"sur le bouton d'en bas dans tout "
"les cas on ne perd jamais 😁. "
"vos gains sont pris au hazard dans "
"l'interval min ~ max en fontion "
"de votre niveau (gratuit,v1,...) "
"pour augmenter votre niveau,allez "
"sur le bouton 🛒ameliorer\n"
"      *min*       *max*        (📋*plan*)\n"
f"🔥 0.003 ~0.005 ltc ({em1}gratuit)\n"
f"🔥 0.010 ~0.050 ltc ({em2}v1)\n"
f"🔥 0.070 ~0.200 ltc ({em3}v2)\n"
f"🔥 0.250 ~0.360 ltc ({em4}pro)\n"
f"🔥 0.500 ~0.870 ltc ({em5}pro2)\n" 


     	
,parse_mode=ParseMode.MARKDOWN
,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("10🎟",callback_data="1")]])
 )
                    update.message.reply_text(
"🎪DISTRIBUTEUR:ETHEREUM\n"
"tantez votre chance en cliquant "
"sur le bouton d'en bas dans tout "
"les cas on ne perd jamais 😁. "
"vos gains sont pris au hazard dans "
"l'interval min ~ max en fontion "
"de votre niveau (gratuit,v1,...) "
"pour augmenter votre niveau,allez "
"sur le bouton 🛒ameliorer\n"
"      *min*       *max*         (📋*plan*)\n"
f"🔥 0.001 ~0.002 eth ({em1}gratuit)\n"
f"🔥 0.004 ~0.006 eth ({em2}v1)\n"
f"🔥 0.007 ~0.009 eth ({em3}v2)\n"
f"🔥 0.010 ~0.060 eth ({em4}pro)\n"
f"🔥 0.070 ~0.500 eth ({em5}pro2)\n"
 
,parse_mode=ParseMode.MARKDOWN
,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("45🎟",callback_data="2")]])
 )
                    update.message.reply_text(
"🎪DISTRIBUTEUR:BITCOIN\n"
"tantez votre chance en cliquant "
"sur le bouton d'en bas dans tout "
"les cas on ne perd jamais 😁. "
"vos gains sont pris au hazard dans "
"l'interval min ~ max en fontion "
"de votre niveau (gratuit,v1,...) "
"pour augmenter votre niveau,allez "
"sur le bouton 🛒ameliorer\n"
"      *min*       *max*         (📋*plan*)\n"
f"🔥 0.001 ~0.002 btc ({em1}gratuit)\n"
f"🔥 0.003 ~0.004 btc ({em2}v1)\n"
f"🔥 0.005 ~0.006 btc ({em3}v2)\n"
f"🔥 0.006 ~0.011 btc ({em4}pro)\n"
f"🔥 0.012 ~0.085 btc ({em5}pro2)\n"
,parse_mode=ParseMode.MARKDOWN
,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("80🎟",callback_data="3")]])

 )
                    update.message.reply_text(
"tu veux acceder au menu?👇"
,reply_markup=ReplyKeyboardMarkup([['🔙RETOUR']],resize_keyboard='true')   
)
def retour(update:Update,context:CallbackContext):
    update.message.reply_text(f"BIENVENUE sur [Win Max currency ](t.me/wmcurrency_bot) 💸💰💵\n"
f"nous distribuons les cryptomonaies tels que :\n"
f"   👉[le bitcoin](https//:www.coingecko.com) :\n"
f"       💧prix actuel:${coingecko[0]['current_price']}\n"
f"   👉[l'ethereum](https//:www.coingecko.com) :\n"
f"       💧prix actuel:${coingecko[1]['current_price']}\n"
f"   👉[le litecoin](https//:www.coingecko.com) :\n"
f"       💧prix actuel:${litecoin()}\n"
f"en effet pour recevoir de la cryptomonaie\n"
f"il faut respecter les etapes suivantes:\n"
f"1️⃣ envoyez votre lien a un ami\n"
f"     ♦️ vous obtenez un tiket pour chaque ami\n"
f"     ♦️ vous obtenez aussi 20% de leurs gains\n"
f"2️⃣ cliquer sur le bouton 'Distributeur'\n"
f"     ♦️ plusieurs options vous seront proposées\n"
f"     ♦️ choisissez celle qui vous convient\n"
f"ainsi vous recevez des cryptomonaies dont le retrait\n"
f"se fait en cliquant sur le bouton '👛Retrait'\n"
f"contactez le support en cas de soucis:💬support\n"
f"sur le fonctionnement du bot",reply_markup=ReplyKeyboardMarkup([['🏦Distributeur','👤Compte'],['🗣Refferal','🛒Ameliorer','👛Retrait'],['🧮megeboom bonus','💬support 24/7']],resize_keyboard='true'),parse_mode=ParseMode.MARKDOWN
)
    
def eth(update:Update,context:CallbackContext):
    cid=update.callback_query.message.chat.id
    plan=row(cid)[5]
    if plan=='gratuit':
        			if row(cid)[6]-45>=0:
        				TS= row(cid)[6]-45
        				rtikets(TS,cid)
        			
        				arg=round(random.uniform(0.001,0.002),6)
        				BT=row(cid)[8]+float(arg)
        				reth(BT,cid)
        				update.callback_query.answer(f"+{arg} eth ✅✅✅✅"
"    -45🎟  🔻")
        			else:
        				update.callback_query.answer("🚫🚫🚫nombre de tikets insuffisant pour recevoir le bonus , envoyez votre 🔗lien a des 👥amis pour en recevoir gratuitement ❗️ " ,show_alert='true')
        
            
        
       
    if plan=='V1':
        if row(cid)[6]-45>0:
        	TS=row(cid)[6]-45
        	rtikets(TS,cid)
        	arg=round(random.uniform(0.004,0.006),6)
        	BT=row(cid)[8]+arg
        	reth(BT,cid)
        	update.callback_query.answer(f"+{arg} eth ✅✅✅✅"
"    -45🎟  🔻")
			
        else:
        	update.callback_query.answer("🚫🚫🚫nombre de tikets insuffisant pour recevoir le bonus , envoyez votre 🔗lien a des 👥amis pour en recevoir gratuitement ❗️ " ,show_alert='true')
        
        



    if plan=='V2':
        arg=round(random.uniform(0.007,0.009),6)
        if row(cid)[6]-45>0:
        	TS= row(cid)[6]-45
        	rtikets(TS,cid)
        	BT=row(cid)[8]+arg
        	reth(BT,cid)
        	update.callback_query.answer(f"+{arg} eth ✅✅✅✅"
"    -45🎟  🔻")
			
        else:
        	update.callback_query.answer("🚫🚫🚫nombre de tikets insuffisant pour recevoir le bonus , envoyez votre 🔗lien a des 👥amis pour en recevoir gratuitement ❗️ " ,show_alert='true')
        
            
    if plan=='PRO':
        arg=round(random.uniform(0.01,0.06),6)
        if row(cid)[6]-45>0:
        	TS= row(cid)[6]-45
        	rtikets(TS,cid)
        	BT=row(cid)[8]+arg
        	reth(BT,cid)
        	update.callback_query.answer(f"+{arg} eth ✅✅✅✅"
"    -45🎟  🔻")
			
        else:
        	update.callback_query.answer("🚫🚫🚫nombre de tikets insuffisant pour recevoir le bonus , envoyez votre 🔗lien a des 👥amis pour en recevoir gratuitement ❗️ " ,show_alert='true')
    if plan=='PROMAX':
         arg=round(random.uniform(0.07,0.5),6)
         if row(cid)[6]-45>0:
         	TS= row(cid)[6]-45
         	rtikets(TS,cid)
         	BT=row(cid)[8]+arg
         	reth(BT,cid)
         	update.callback_query.answer(f"+{arg} eth ✅✅✅✅"
"    -45🎟  🔻")
         else :
         	update.callback_query.answer("🚫🚫🚫nombre de tikets insuffisant pour recevoir le bonus , envoyez votre 🔗lien a des 👥amis pour en recevoir gratuitement ❗️ " ,show_alert='true')

def ltc(update:Update,context:CallbackContext):
    cid=update.callback_query.message.chat.id
    plan=row(cid)[5]
    if plan=='gratuit':
        arg=round(random.uniform(0.003,0.005),6)
        if row(cid)[6]-10>0:
        	TS=row(cid)[6]-10
        	rtikets(TS,cid)
        	update.callback_query.answer(f"+{arg} ltc ✅✅✅✅"
"    -10🎟  🔻")
        	BT=row(cid)[9]+arg
        	rltc(BT,cid)
        else:
        	update.callback_query.answer("🚫🚫🚫nombre de tikets insuffisant pour recevoir le bonus , envoyez votre 🔗lien a des 👥amis pour en recevoir gratuitement ❗️ " ,show_alert='true')                       
    if plan=='V1':
      arg=round(random.uniform(0.01,0.05),6)
      if row(cid)[6]-10>0:
        	TS=row(cid)[6]-10
        	rtikets(TS,cid)
        	update.callback_query.answer(f"+{arg} ltc ✅✅✅✅"
"    -10🎟  🔻")
        	BT=row(cid)[9]+arg
        	rltc(BT,cid)
      else:
        	update.callback_query.answer("🚫🚫🚫nombre de tikets insuffisant pour recevoir le bonus , envoyez votre 🔗lien a des 👥amis pour en recevoir gratuitement ❗️ " ,show_alert='true') 
      
    if plan=='V2':
      arg=round(random.uniform(0.07,0.2),6)
      if row(cid)[6]-10>0:
        	TS=row(cid)[6]-10
        	rtikets(TS,cid)
        	update.callback_query.answer(f"+{arg} ltc ✅✅✅✅"
"    -10🎟  🔻")
        	BT=row(cid)[9]+arg
        	rltc(BT,cid)
      else:
        	update.callback_query.answer("🚫🚫🚫nombre de tikets insuffisant pour recevoir le bonus , envoyez votre 🔗lien a des 👥amis pour en recevoir gratuitement ❗️ " ,show_alert='true') 
    if plan=='PRO':
      arg=round(random.uniform(0.25,0.36),6)
      if row(cid)[6]-10>0:
        	TS=row(cid)[6]-10
        	rtikets(TS,cid)
        	update.callback_query.answer(f"+{arg} ltc ✅✅✅✅"
"    -10🎟  🔻")
        	BT=row(cid)[9]+arg
        	rltc(BT,cid)
      else:
        	update.callback_query.answer("🚫🚫🚫nombre de tikets insuffisant pour recevoir le bonus , envoyez votre 🔗lien a des 👥amis pour en recevoir gratuitement ❗️ " ,show_alert='true') 
    if plan=='PROMAX':
      arg=round(random.uniform(0.5,0.7),6)
      if row(cid)[6]-10>0:
        	TS=row(cid)[6]-10
        	rtikets(TS,cid)
        	update.callback_query.answer(f"+{arg} ltc ✅✅✅✅"
"    -10🎟  🔻")
        	BT=row(cid)[9]+arg
        	rltc(BT,cid)
      else:
        	update.callback_query.answer("🚫🚫🚫nombre de tikets insuffisant pour recevoir le bonus , envoyez votre 🔗lien a des 👥amis pour en recevoir gratuitement ❗️ " ,show_alert='true') 

def btc(update:Update,context:CallbackContext):
    cid= update.callback_query.message.chat.id
    plan=row(cid)[5]
    if plan=='gratuit':
        arg=round(random.uniform(0.003,0.005),6)
        if row(cid)[6]-80>0:
        	TS= row(cid)[6]-80
        	rtikets(TS,cid)
        	update.callback_query.answer(f"+ {arg} btc ✅✅✅✅"
"    -80🎟  🔻")
        	BT=row(cid)[7]+arg
        	rbtc(BT,cid)
        
        else :
         update.callback_query.answer("🚫🚫🚫nombre de tikets insuffisant pour recevoir le bonus , envoyez votre 🔗lien a des 👥amis pour en recevoir gratuitement ❗️ " ,show_alert='true')
      
            
    if plan=='V1':
        arg=round(random.uniform(0.001,0.002),6)
        if row(cid)[6]-80>0:
        	TS= row(cid)[6]-80
        	rtikets(TS,cid)
        	update.callback_query.answer(f"+{arg} btc ✅✅✅✅"
"    -80🎟  🔻")
        	BT=row(cid)[7]+arg
        	rbtc(BT,cid)
        
        else :
         update.callback_query.answer("🚫🚫🚫nombre de tikets insuffisant pour recevoir le bonus , envoyez votre 🔗lien a des 👥amis pour en recevoir gratuitement ❗️ " ,show_alert='true')

                 
                 
         
    if plan=='V2':
        arg=round(random.uniform(0.003,0.004),6)
        if row(cid)[6]-80>0:
        	TS= row(cid)[6]-80
        	rtikets(TS,cid)
        	update.callback_query.answer(f"+{arg} btc ✅✅✅✅"
"    -80🎟  🔻")
        	BT=row(cid)[7]+arg
        	rbtc(BT,cid)
        
        else :
         update.callback_query.answer("🚫🚫🚫nombre de tikets insuffisant pour recevoir le bonus , envoyez votre 🔗lien a des 👥amis pour en recevoir gratuitement ❗️ " ,show_alert='true')
    if plan=='PRO':
        arg=round(random.uniform(0.006,0.011),6)
        if row(cid)[6]-80>0:
        	TS= row(cid)[6]-80
        	rtikets(TS,cid)
        	update.callback_query.answer(f"+{arg} btc ✅✅✅✅"
"    -80🎟  🔻")
        	BT=row(cid)[7]+arg
        	rbtc(BT,cid)
        
        else :
         update.callback_query.answer("🚫🚫🚫nombre de tikets insuffisant pour recevoir le bonus , envoyez votre 🔗lien a des 👥amis pour en recevoir gratuitement ❗️ " ,show_alert='true')
    if plan=='PROMAX':
        arg=round(random.uniform(0.012,0.087),6)
        if row(cid)[6]-80>0:
        	TS= row(cid)[6]-80
        	rtikets(TS,cid)
        	update.callback_query.answer(f"+{arg} btc ✅✅✅✅"
"    -80🎟  🔻")
        	BT=row(cid)[7]+arg
        	rbtc(BT,cid)
        
        else :
         update.callback_query.answer("🚫🚫🚫nombre de tikets insuffisant pour recevoir le bonus , envoyez votre 🔗lien a des 👥amis pour en recevoir gratuitement ❗️ " ,show_alert='true')
 
 
def compte(update:Update,context:CallbackContext):
    cid=update.message.chat.id
    update.message.reply_text(
f"<code>💼informations personnelles :\n"
f"👤Nom d'utilisateur : {update.message.chat.first_name} {update.message.chat.username}\n"
f"🕶id:wmc{update.message.chat.id}\n"
f"❄️solde bitcoin : {row(cid)[7]}btc\n"
f"❄️solde litecoin: {row(cid)[9]}ltc\n"
f"❄️solde ethereum: {row(cid)[8]}eth\n"
f"🎟tikets :{row(cid)[6]}🎟\n"
f"📋plan : {row(cid)[5]}\n"
f"💰total retiré:\n"
f"  🏮bitcoin : {row(cid)[10]}btc\n"
f"  🏮ethereum: {row(cid)[11]}eth\n"
f"  🏮litecoin: {row(cid)[12]}ltc\n"
f"💳total deposé:\n"
f"  🏮bitcoin : {round(row(cid)[13],6)}btc\n"
f"  🏮ethereum: {round(row(cid)[14],6)}eth\n"
f"  🏮litecoin: {round(row(cid)[15],6)}ltc\n</code>"
,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🏦Dépot',callback_data="4")]]),parse_mode=ParseMode.HTML
    )


def depot(update:Update,context:CallbackContext):
    context.bot.sendMessage(text=""
f"🙋‍♂️Pour recharger votre compte \n"
f"vous avez 3 options a savoir:\n"
f"🔴dépôt bitcoin:\n"
f"▫️dépôt min:0.000001 BTC\n"
f"▫️addrèsse 👇:\n\n"
f"\n<code>btc14365dghdstjfvfdeshvG44fS23dF56</code>\n\n\n"
f"▫️bonus:20%\n"
f"⚫️dépôt ethereum:\n"
f"▪️▪️dépôt min:0.000001 ETH\n"
f"▪️▪️addrèsse 👇:\n\n" 
f"\n<code>eth14365dvG44hdjkthfqxbilufS23dF56</code>\n\n\n"
f"▪️▪️bonus:20%\n"
f"⚪️dépôt litecoin:\n"
f"▫️dépôt min:0.000001 LTC\n"
f"▫️addrèsse 👇:\n\n" 
f"\n<code>ltc14365dvfgusghdggffggG44fS23dF56</code>\n\n\n"
f"▫️bonus:20%\n"
f"❗️vous pouvez copier les addrèsses en les selectionents",chat_id=update.callback_query.message.chat.id
,parse_mode=ParseMode.HTML


    )
    update.message.reply_text(
"tu veux acceder au menu?👇"
,reply_markup=ReplyKeyboardMarkup([['🔙RETOUR']],resize_keyboard='true')  )
def retrait(update:Update,context:CallbackContext):
    context.bot.sendMessage(text=''
f"selectionner une crytomonaie pour votre retrait"
,reply_markup=ReplyKeyboardMarkup([['BTC','ETH','LTC'],['🔙RETOUR']],resize_keyboard='true'),
chat_id=update.message.chat.id
    )
def retrait_btc(update:Update,context:CallbackContext):
    cid=update.message.chat.id
    mid=update.message.message_id
    cursor.execute("""
    UPDATE wmc
    SET mid=%s
    WHERE cid=%s
    """,(mid,cid,))
    
    if row(cid)[7]<0.0001:
        
        context.bot.sendMessage(text=''
f"⚠️Vous n'avez pas atteint le montant min pour effectuer cette transaction !\n"
f"NB❗️:montant min:0.0001 btc"
,chat_id=update.message.chat.id
    )
    elif row(cid)[13]<0.0005:
        context.bot.sendMessage(text=''
"⚠️Pour effectuer cette transaction vous devez avoir deposés aumoin "
" 0.0005 btc ",
chat_id=update.message.chat.id
)
    else:
        cid=update.message.chat.id
        mid=update.message.message_id
        context.bot.sendMessage(text=''
"entrez l'addresse bitcoin du destinataire 👇"
,reply_markup=ReplyKeyboardMarkup([['❌annuler']],resize_keyboard='true')
,chat_id=update.message.chat.id

    )
        while row(cid)[4]==update.message.message_id:
        	time.sleep(1)
        	print(str(row(cid)[4])+" "+str(update.message.message_id))

        	

        cid=update.message.chat.id
        mid=update.message.message_id
        cursor.execute("""
        UPDATE wmc
        SET mid=%s
        WHERE cid=%s""",(mid,cid,))
        while len(update.message.text)<28 or update.message.text!='❌annuler' :
                update.message.reply_text("🚫entrez l'addresse bitcoin  valide du destinataire 👇"
,reply_markup=ReplyKeyboardMarkup([['❌annuler']],resize_keyboard='true')
,chat_id=update.message.chat.id)
                while row(cid)[4]==update.message.message_id :
                    time.sleep(0.000000000001)
        cursor.execute("""
            UPDATE wmc
            SET btca
            WHERE cid=%s
            """,(cid,))	
        context.bot.sendMessage(
"🔰entrez le montant!    (min=0.0001 btc)"
,reply_markup=ReplyKeyboardMarkup([['❌annuler']],chat_id=update.callback_query.message.chat_id,resize_keyboard='true')
        )
        cid=update.message.chat.id
        mid=update.message.message_id
        cursor.execute("""
        UPDATE wmc
        SET mid=%s
        WHERE cid=%s""",(mid,cid,))
        if row(cid)[4]==update.message.message_id-2:
                try:
                    int(update.message.text)
                except:
                    update.message.reply_text(' montant invalide!  requette annnulé',reply_markup=ReplyKeyboardMarkup([['❌annuler']],chat_id=update.callback_query.message.chat_id,resize_keyboard='true'))
                else :

                    while update.message.text<0.0001 and row(cid)[7]<update.message.text:
                        update.message.reply_text(
"🔰entrez le montant! le montant min est 0.0001 btc"
,reply_markup=ReplyKeyboardMarkup([['❌annuler']],resize_keyboard='true'))

                        cursor.execute("""
        UPDATE wmc
        SET mid=%s
        WHERE cid=%s""",(mid,cid,))
                        while row(cid)[4]==update.message.message_id:
                            time.sleep(0.000000001)
                    CD=update.message.text
                    rt=row(cid)[7]-CD
                    cursor.execute("""
                    UPDATE wmc
                    SET btc=%s
                    WHERE cid=%s
                    """,(rt,cid,))
                    update.message.reply_text(
f"🧾 DEMANDE APPOUVEE ✅✅✅\n"
f"votre retrait est lancé \n:"
f"🐸somme:{CD} btc\n" 
f"🐸btc  :<code>{row(cid)[16]}</code>\n"
f"🐸status:✅send\n" 
,reply_markup=ReplyKeyboardMarkup([['🏦Distributeur','👤Compte'],['🗣Refferal','🛒Ameliorer','👛Retrait'],['🧮megeboom bonus','💬support 24/7']],resize_keyboard='true'),parse_mode=ParseMode.HTML                  
                    )


def retrait_eth(update:Update,context:CallbackContext):
    cid=update.callback_query.message.chat.id
    if row(cid)[8]<0.001:
        context.bot.sendMessage(text=''
f"⚠️Vous n'avez pas atteint le montant min pour effectuer cette transaction !\n"
f"NB❗️:montant min:0.001 ETH"
,chat_id=update.callback_query.message.chat.id
    )
    if row(cid)[14]<0.005:
        context.bot.sendMessage(text=''
"⚠️Pour effectuer cette transaction vous devez avoir deposés aumoin "
" 0.005 ETH ",
chat_id=update.callback_query.message.chat.id
)
    else:
        cid=update.callback_query.message.chat.id
        mid=update.callback_query.message.message_id
        cursor.execute("""
        UPDATE wmc
        SET mid=%s
        WHERE cid=%s""",(mid,cid,))
        context.bot.sendMessage(text=''
"entrez l'addresse bitcoin du destinataire 👇"
,reply_markup=ReplyKeyboardMarkup([['❌annuler']],resize_keyboard='true')
,chat_id=update.callback_query.message.chat.id

    )
        if row(cid)[4]==update.message.id-2:
            cid=update.message.chat.id
            mid=update.message.id
            cursor.execute("""
        UPDATE wmc
        SET mid=%s
        WHERE cid=%s""",(mid,cid,))
            while len(update.message.text)<28 or update.message.text!='❌annuler' :
                cid=update.message.chat.id
                mid=update.message.id
                cursor.execute("""
        UPDATE wmc
        SET mid=%s
        WHERE cid=%s""",(mid,cid,))
                context.bot.sendMessage(text=''
"🚫entrez l'addresse ethereum  valide du destinataire 👇"
,reply_markup=ReplyKeyboardMarkup([['❌annuler']],resize_keyboard='true')
,chat_id=update.callback_query.message.chat.id)
                while update.message.id-1==row(cid)[4]:
                    cursor.execute("""
        UPDATE wmc
        SET etha=%s
        WHERE cid=%s""",(update.message.text,cid,))
                    update.message.reply_text(
"🔰entrez le montant!"
,reply_markup=ReplyKeyboardMarkup([['❌annuler']],resize_keyboard='true')
        )
        if row(cid)[4]==update.message.id-2:
            cid=update.message.chat.id
            while row(cid)[20]<0.001 :
                cid=update.message.chat.id
                mid=update.message.id
                cursor.execute("""
        UPDATE wmc
        SET mid=%s
        WHERE cid=%s""",(mid,cid,))
                update.message.reply_text(
"🔰entrez le montant! le montant min est 0.001 eth"
,reply_markup=ReplyKeyboardMarkup([['❌annuler']],resize_keyboard='true'))
                while update.message.id-1==row(cid)[4]:
                    time.sleep(1)
            if row(cid)[9]>=float(update.message.text):

                cursor.execute("""
        UPDATE wmc
        SET mt=%s
        WHERE cid=%s""",(update.message.text,cid,))
                update.message.reply_text(
f"🧾 DEMANDE APPOUVEE ✅✅✅\n"
f"votre retrait est lancé \n:"
f"🐸somme:{row(cid)[19]} eth\n" 
f"🐸btc  :<code>{row(cid)[18]}</code>\n"
f"🐸status:✅send\n" 
,reply_markup=ReplyKeyboardMarkup([['🏦Distributeur','👤Compte'],['🗣Refferal','🛒Ameliorer','👛Retrait'],['🧮megeboom bonus','💬support 24/7']],resize_keyboard='true'),parse_mode=ParseMode.HTML          )
            else:
                update.message.reply_text("balance litecoin insuffisante",reply_markup=ReplyKeyboardMarkup([['🏦Distributeur','👤Compte'],['🗣Refferal','🛒Ameliorer','👛Retrait'],['🧮Grandes Taches','💬support 24/7']],resize_keyboard='true'))
def retrait_ltc(update:Update,context:CallbackContext):
    cid=update.callback_query.message.chat.id
    if row(cid)[9]<0.005:
        context.bot.sendMessage(text=''
f"⚠️Vous n'avez pas atteint le montant min pour effectuer cette transaction !\n"
f"NB❗️:montant min:0.005 ltc"
,chat_id=update.callback_query.message.chat.id
    )
    elif row(cid)[15]<0.02:
        context.bot.sendMessage(text=''
"⚠️Pour effectuer cette transaction vous devez avoir deposés aumoin "
" 0.02 ltc ",
chat_id=update.callback_query.message.chat.id
)
    else:
        cid=update.callback_query.message.chat.id
        mid=update.callback_query.message.message_id
        cursor.execute("""
        UPDATE wmc
        SET mid=%s
        WHERE cid=%s""",(mid,cid,))
        context.bot.sendMessage(text=''
"entrez l'addresse litecoin du destinataire 👇"
,reply_markup=ReplyKeyboardMarkup([['❌annuler']],resize_keyboard='true')
,chat_id=update.callback_query.message.chat.id

    )
        if row(cid)[4]==update.message.id-2:
            cid=update.message.chat.id
            mid=update.message.id
            cursor.execute("""
        UPDATE wmc
        SET mid=%s
        WHERE cid=%s""",(mid,cid,))
            while len(update.message.text)<28 or update.message.text!='❌annuler' :
                cid=update.message.chat.id
                mid=update.message.id
                cursor.execute("""
        UPDATE wmc
        SET mid=%s
        WHERE cid=%s""",(mid,cid,))
                context.bot.sendMessage(text=''
"🚫entrez l'addresse litecoin  valide du destinataire 👇"
,reply_markup=ReplyKeyboardMarkup([['❌annuler']],resize_keyboard='true')
,chat_id=update.callback_query.message.chat.id)
                while update.message.id-1==row(cid)[4]:
                    time.sleep(1)
            cursor.execute("""
        UPDATE wmc
        SET ltca=%s
        WHERE cid=%s""",(update.message.text,cid,))
            update.message.reply_text(
"🔰entrez le montant!"
,reply_markup=ReplyKeyboardMarkup([['❌annuler']],resize_keyboard='true')
        )
        if row(update.message.chat.id)[4]==update.message.id-2:
            while row(update.message.chat.id)[20]<0.005 :
                cid=update.message.chat.id
                mid=update.message.id
                cursor.execute("""
        UPDATE wmc
        SET mid=%s
        WHERE cid=%s""",(mid,cid,))
                update.message.reply_text(
"🔰entrez le montant! le montant min est 0.005 ltc"
,reply_markup=ReplyKeyboardMarkup([['❌annuler']],resize_keyboard='true'))
                while update.message.id-1==row(cid)[4]:
                    time.sleep(1)
            if row(cid)[9]>=float(update.message.text):
                cursor.execute("""
        UPDATE wmc
        SET mt=%s
        WHERE cid=%s""",(update.message.text,cid,))
                update.message.reply_text(
f"🧾 DEMANDE APPOUVEE ✅✅✅\n"
f"votre retrait est lancé \n:"
f"🐸somme:{row(cid)[19]} ltc\n" 
f"🐸btc  :<code>{row(cid)[17]}</code>\n"
f"🐸status:✅send\n" 
,reply_markup=ReplyKeyboardMarkup([['🏦Distributeur','👤Compte'],['🗣Refferal','🛒Ameliorer','👛Retrait'],['🧮megeboom bonus','💬support 24/7']],resize_keyboard='true'),parse_mode=ParseMode.HTML          )
            else:
                update.message.reply_text("balance litecoin insuffisante",reply_markup=ReplyKeyboardMarkup([['🏦Distributeur','👤Compte'],['🗣Refferal','🛒Ameliorer','👛Retrait'],['🧮megeboom bonus','💬support 24/7']],resize_keyboard='true'))
def annuler(update:Update,context:CallbackContext):
    update.message.reply_text(
"l 'operation en cour a été arrêtée "
,reply_markup=ReplyKeyboardMarkup([['🏦Distributeur','👤Compte'],['🗣Refferal','🛒Ameliorer','👛Retrait'],['🧮megeboom bonus','💬support 24/7']],resize_keyboard='true')
    )
def ameliorer(update:Update,context:CallbackContext):
	update.message.reply_text(
f"👆ameliorez pour le niveau V1\n"
f"💵prix: $15\n"
f"💎bonus:+10🎟\n"
f"         +rembourse 2%\n"
f"👇cliquez sur une cryptomonaie"
f" pour 💳payez",
reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('BTC',callback_data="9"),InlineKeyboardButton('ETH',callback_data="10"),InlineKeyboardButton('LTC',callback_data="11")]]) )
	update.message.reply_text(
f"👆ameliorez pour le niveau V2\n"
f"💵prix: $25\n"
f"💎bonus:+10🎟\n"
f"         +remboursement 2%\n"
f"👇cliquez sur une cryptomonaie"
f" pour 💳payer",
reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('BTC',callback_data="9"),InlineKeyboardButton('ETH',callback_data="10"),InlineKeyboardButton('LTC',callback_data="11")]]) )
	update.message.reply_text(
f"👆ameliorer pour le niveau PRO\n"
f"💵prix: $60\n"
f"💎bonus:+100🎟\n"
f"         +remboursement 10%\n"
f"👇cliquez sur une cryptomonaie"
f" pour 💳payer",
reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('BTC',callback_data="9"),InlineKeyboardButton('ETH',callback_data="10"),InlineKeyboardButton('LTC',callback_data="11")]])   )
	update.message.reply_text(
f"👆ameliorez pour le niveau PROMAX\n"
f"💵prix: $150\n"
f"💎bonus:+200🎟\n"
f"         +remboursement 15%\n"
f"👇cliquez sur une cryptomonaie"
f" pour 💳payer",
reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('BTC',callback_data="9"),InlineKeyboardButton('ETH',callback_data="10"),InlineKeyboardButton('LTC',callback_data="11")]]) )
	update.message.reply_text(
"tu veux acceder au menu?👇"
,reply_markup=ReplyKeyboardMarkup([['🔙RETOUR']],resize_keyboard='true')  )
 
def refferal(update:Update,context:CallbackContext):
    update.message.reply_text(
"Vous disposez d'un lien de parainage "
"a travers lequel vous recevez des bonus "
" a travers vos refferals 👥 .Ce lien est le suivant:\n"
f"🔗lien: <code>{helpers.create_deep_linked_url(context.bot.username,f'winner{update.message.chat.id}')}</code>\n"
f'👥vous avez deja: 200 refferal(s)\n',parse_mode=ParseMode.HTML
    )
def grandeT(update:Update,context:CallbackContext):
    update.message.reply_text(
"❓nom de la tache?: MICROBOOM!\n"
"🚫contraintes: valide juste pour le 1er depot\n"
"❓comment la realiser ?:\n"
"depose entre $10 et $15 dans ton compte ,tu aura realisé la tache et tu recevra des bonus en plus sur ta recharge \n"
"❓quel est le bonus? :\n"
f"🎁🎁vous recevrez +50🎟  et +5% de votre recharge"
    )
    update.message.reply_text(
"❓nom de la tache?: MINIBOOM!\n"
"🚫contraintes:fonctionne juste 2 fois pour tout les utilisateurs\n"
"❓comment la realiser ?:\n"
"depose entre $18 et $20 dans ton compte ,tu aura realisé la tache et tu recevra des bonus en plus sur ta recharge \n"
"❓quel est le bonus? :\n"
f"🎁🎁vous recevrez +200🎟  et +10% de votre recharge"
    )
    update.message.reply_text(
"❓nom de la tache?: EXBOOM!\n"
"🚫contraintes:aucune\n"
"❓comment la realiser ?:\n"
"depose entre $25 et $50 dans ton compte ,tu aura realisé la tache et tu recevra des bonus en plus sur ta recharge  \n"
"❓quel est le bonus? :\n"
f"🎁🎁vous recevrez +300🎟  et +15% de votre recharge"
    )
    update.message.reply_text(
"❓nom de la tache?: MEGABOOM!\n"
"🚫contraintes:aucune\n"
"❓comment la realiser ?:\n"
"depose entre $100 et $150 dans ton compte ,tu aura realisé la tache et tu recevra des bonus en plus sur ta recharge \n"
"❓quel est le bonus? :\n"
f"🎁🎁vous recevrez +500🎟  et +25% de votre recharge"
    )
    update.message.reply_text(
"❓nom de la tache?: GIGABOOM\n"
"🚫contraintes:aucune \n"
"❓comment la realiser ?:\n"
"depose entre $200 et $300 dans ton compte ,tu aura realisé la tache et tu recevra des bonus en plus sur ta recharge \n"
"❓quel est le bonus? :\n"
f"🎁🎁vous recevrez +800🎟  et +40% de votre recharge"
    )
    update.message.reply_text(
"❓nom de la tache?: EXTRABOOM!\n"
"🚫contraintes:aucune\n"
"❓comment la realiser ?:\n"
"depose entre $350 et $400 dans ton compte ,tu aura realisé la tache et tu recevra des bonus en plus sur ta recharge \n"
"❓quel est le bonus? :\n"
f"🎁🎁vous recevrez +1500🎟  et +50% de votre recharge"
    )
    update.message.reply_text(
"tu veux acceder au menu?👇"
,reply_markup=ReplyKeyboardMarkup([['🔙RETOUR']],resize_keyboard='true')   
)
def support(update:Update,context:CallbackContext):
    cid=update.message.chat.id
    cursor.execute("""
    UPDATE wmc
    SET mid=%s
    WHERE cid=%s
    """,(update.message.message_id,cid,))
    update.message.reply_text(
"faites parvenir vos requettes aux administrateurs en envoyent un message"
,reply_markup=ReplyKeyboardMarkup([['🔙RETOUR']],resize_keyboard='true')
 ) 
    if row(cid)[4]==update.message.id-2:
        context.sendMessage(text=''
f"{update.message.chat.username} - {update.message.chat.first_name} - <code>{update.message.chat.id}</code>\n"+update.messege.text,
reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('reply to user',callback_data='14')]])
,chat_id=admin
        
        )
        update.message.reply_text(
f"votre requette a bien été envoyée ✅"
    ,reply_markup=ReplyKeyboardMarkup([['🏦Distributeur','👤Compte'],['🗣Refferal','🛒Ameliorer','👛Retrait'],['🧮megeboom bonus','💬support 24/7']],resize_keyboard='true')    )
def depot_btc(update:Update,context:CallbackContext):
    context.bot.sendMessage(text=""
"📮envoyez la somme correspondante a l'addresse suivante pour 🔌activer le plan choisis:\n" 
"<code>btcuglsljmoezçavlbnolll523heehhd45</code>"   ,parse_mode=ParseMode.HTML,chat_id=update.callbackmessage.chat.id
    )
def depot_eth(update:Update,context:CallbackContext):
    context.bot.sendMessage(text=""
"📮envoyez la somme correspondante a l'addresse suivante pour 🔌activer le plan choisis:\n" 
"<code>ethuglsljmoezçavlbnolll523heehhd45</code>"   ,parse_mode=ParseMode.HTML,chat_id=update.message.chat.id
    )
def depot_ltc(update:Update,context:CallbackContext):
    context.bot.sendMessage(text=""
"📮envoyez la somme correspondante a l'addresse suivante pour 🔌activer le plan choisis:\n" 
"<code>ltcuglsljmoezçavlbnolll523heehhd45</code>"   ,parse_mode=ParseMode.HTML,chat_id=update.message.chat.id
    )
def retrait1(update:Update,context:CallbackContext):
	context.bot.sendMessage(text=''
f"selectionner une crytomonaie pour votre retrait"
,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('BTC',callback_data="6"),InlineKeyboardButton('ETH',callback_data="7"),InlineKeyboardButton('LTC',callback_data="8")]]),
chat_id=update.message.chat.id
    )
	
def main():
    updater=Updater('1762560403:AAGWkC57kJgn-LXbTVeo7E43wLS0M2St818')
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("^👤Compte$"), compte))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("^BTC"), retrait_btc))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("^🏦Distributeur$"),distributeur))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("^🗣Refferal$"), refferal))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("^🛒Ameliorer$"),ameliorer))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("^👛Retrait$"), retrait))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("^🧮megeboom bonus$"), grandeT))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("^💬support 24/7$"), support))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("^🔙RETOUR"), retour))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("^❌annuler$"), annuler))
    updater.dispatcher.add_handler(CallbackQueryHandler(btc,pattern="^3$"))
    updater.dispatcher.add_handler(CallbackQueryHandler(eth,pattern="^2$"))
    updater.dispatcher.add_handler(CallbackQueryHandler(ltc,pattern="^1$"))
    updater.dispatcher.add_handler(CallbackQueryHandler(depot,pattern="^4$"))
    updater.dispatcher.add_handler(CallbackQueryHandler(retrait,pattern="^5$"))
    updater.dispatcher.add_handler(CallbackQueryHandler(retrait_btc,pattern="^6$"))
    updater.dispatcher.add_handler(CallbackQueryHandler(retrait_ltc,pattern="^7$"))
    updater.dispatcher.add_handler(CallbackQueryHandler(retrait_eth,pattern="^8$"))
    updater.dispatcher.add_handler(CallbackQueryHandler(depot_btc,pattern="^9$"))
    updater.dispatcher.add_handler(CallbackQueryHandler(depot_eth,pattern="^10$"))
    updater.dispatcher.add_handler(CallbackQueryHandler(depot_ltc,pattern="^11$"))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("^🇫🇷Francais$"), francais))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("^🏴󠁧󠁢󠁥󠁮󠁧󠁿english"), english))
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://wmcurrency.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

    print('working...')
    updater.idle()
   
    
if __name__ == '__main__':
    main()

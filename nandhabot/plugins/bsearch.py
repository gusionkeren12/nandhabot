from pyrogram import *
from pyrogram.types import *
from nandhabot import bot as Rias 

from libgen_api import LibgenSearch
prefixes = ["/","!","?","."]

@Rias.on_message(filters.command(["bsearch"] , prefixes))
async def search (client , message:Message):
    global chat_id
    chat_id = message.chat.id
    global s
    s = LibgenSearch()
    bname = message.text
    bookname = bname.replace('/search ' ,"")
    global results
    results = s.search_title(bookname)
    print(bookname)
    global i
    i = 0
    
    item_to_download = results[i]
    download_links = s.resolve_download_links(item_to_download)
    
    data_text = "Title :" + results[i]['Title'] +"\n\nAuthor :" + results[i]['Author'] + "\n\nLanguage :" + results[i]['Language'] + "\n\npublished on :" + results[i]['Year'] + "\n\nsize :" + results[i]['Size']  
    item_to_download = results[i]
    download_links = s.resolve_download_links(item_to_download)
    

    await Rias.send_message(chat_id , text= data_text , reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Next", callback_data="next"),
                    InlineKeyboardButton(text="Mirror1" , url=download_links["GET"]) ,
                    InlineKeyboardButton(text="Mirror2" , url=download_links["Cloudflare"] ),
                    InlineKeyboardButton(text="CANCEL", callback_data="close")


                ]
            ]
        )
    )

@Rias.on_callback_query()
async def cb_handler(Rias, query):
    if query.data == "next":
        await query.answer()
        data_text1 = "Title :" + results[i+1]['Title'] +"\n\nAuthor :" + results[i+1]['Author'] + "\n\nLanguage :" + results[i+1]['Language'] + "\n\npublished on :" + results[i+1]['Year'] + "\n\nsize :" + results[i+1]['Size']
        item_to_download = results[i+1]
        download_links = s.resolve_download_links(item_to_download)
        await query.message.edit_text(text=data_text1 , reply_markup =InlineKeyboardMarkup([[
            InlineKeyboardButton("Next" , callback_data="next1"),
            InlineKeyboardButton(text="Mirror1" , url=download_links["GET"]) ,
            InlineKeyboardButton(text="Mirror2" , url=download_links["Cloudflare"] ),
            InlineKeyboardButton(text="CANCEL", callback_data="close")

            

            
            
                                                                                             ]
                                                                                            ]
                                                                                           )
                                      )
        await Rias(Rias, query.message)
    
    elif query.data == "next1":
        
        await query.answer()
        item_to_download = results[i+2]
        download_links = s.resolve_download_links(item_to_download)
            
        data_text2 = text= "Title :" + results[i+2]['Title'] +"\n\nAuthor :" + results[i+2]['Author'] + "\n\nLanguage :" + results[i+2]['Language'] + "\n\npublished on :" + results[i+2]['Year'] + "\n\nsize :" + results[i+2]['Size']
        await query.message.edit_text(text=data_text2 , reply_markup =InlineKeyboardMarkup([[
                InlineKeyboardButton("Mirror1" ,url=download_links["GET"] ),
                InlineKeyboardButton(text="Mirror2" , url=download_links["Cloudflare"] ),
                InlineKeyboardButton(text="CANCEL", callback_data="close")
                
                                                                                                ]
                                                                                                ]
                                                                                            )
                                        )
        await Rias(Rias, query.message)

        
    elif query.data == "close":
        await query.message.delete()
        await Rias.send_message(text=
        "Process Cancelled..." , chat_id = chat_id)

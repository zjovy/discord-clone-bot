import os
import discord
from openai import AsyncOpenAI
from dotenv import load_dotenv
from data import data_for_training as convo

load_dotenv() # load environmental variables
TOKEN = os.getenv('DISCORD_TOKEN')
GPT_API = os.getenv('OPENAI_API_KEY')

intents = discord.Intents.all()
client = discord.Client(intents=intents) # initialize discord client

openai_client = AsyncOpenAI(api_key=GPT_API) # initialize openai client

async def ask_gpt(prompt): # async function that generates response to a prompt
    
    system_prompt = ( # prompt engineering
        "You are a gamer who loves competitive games. This means that you are a toxic online gamer that banters with other gamers."
        "Don't talk in a helpful, polite manner. You can be rude to the user. Use internet slangs from recent years." 
        "Be sarcastic sometimes when answering questions."
        "Don't use perfect grammar. Use lowercase only and use abbreviations like you for u, idk for I don't know, idc for I don't care etc."
    )
    
    response = await openai_client.chat.completions.create( # generate response
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo"
    )
    return response.choices[0].message.content

@client.event
async def on_ready():
    print(
        f'{client.user} has connected to Discord!'
    )

@client.event
async def on_message(message): # when message gets sent in a discord channel
    if message.author == client.user: # make sure it is not from the bot itself
        return

    if message.content.startswith('!ask'): # make sure there is a command prompt !ask
        prompt = message.content[len('!ask '):]
        
        response = await ask_gpt(prompt) # call gpt async function
        
        await message.channel.send(response) # sends response back in channel
    
client.run(TOKEN) # run bot
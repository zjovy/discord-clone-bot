import os
import discord
import random
from dotenv import load_dotenv
from data import data_for_training as convo

load_dotenv() # load environmental variables
TOKEN = os.getenv('DISCORD_TOKEN') 

intents = discord.Intents.all()

inputs = []
outputs = []
for msg in convo: # imported the dataset I created
    inputs.append(msg['input']) # matches input and output index
    outputs.append(msg['output'])

client = discord.Client(intents=intents) # initialize discord client

@client.event
async def on_ready():
    print(
        f'{client.user} is connected.\n'
    )

@client.event
async def on_message(message): # when message gets sent in a discord channel
    if message.author == client.user:
        return
    
    # if a input contains the user's message
    # add its corresponding output to a list
    matching_responses = [output for input_str, output in zip(inputs, outputs) if input_str in message.content]

    # handle the reponse
    if message.content == 'bot':
        response = "beep beep bop bop"
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException
    elif matching_responses: # randomly pick a matching reponse
        response = random.choice(matching_responses)
        await message.channel.send(response) # send the message in channel
    
@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise    
    
client.run(TOKEN)
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Хей,прочети правилата ,за да не си доведеш перма бан!')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='Prefix [=]'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
 client.run('NzA1NjgwMzUzOTE3OTI3NDU0.XqvORg.UVAu6NvGDDkfR8J2OK5BGeWuK84')
    if message.content == '=gogo':
        await client.send_message(message.channel,'Der Deutsche ist ein heimlicher Fan von 02!')
     if message.content == '=bubabg':
        await client.send_message(message.channel,'Художничката в сървъра! Арт е тя!')
     if message.content == '=ninjax':
        await client.send_message(message.channel,'Minecrafter-чето')
     if message.content == '=mitaka':
        await client.send_message(message.channel,'Програмистчето на сървъра!')
     if message.content == '=help':
        em = discord.Embed(description='=gogo ; =bubabg ; =ninjax ; =mitaka')
        em.set_image(url='')
        await client.send_message(message.channel, embed=em)

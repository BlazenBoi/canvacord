from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageColor
import asyncio
import aiohttp
from random import randint
from io import BytesIO
import discord
from typing import Union

async def getavatar(user: Union[discord.User, discord.Member]) -> bytes:
    session = aiohttp.ClientSession(loop=asyncio.get_event_loop())
    async with session.get(str(user.avatar_url)) as response:
        avatarbytes = await response.read()
    await session.close()
    return avatarbytes

async def getbackground(background):
    session = aiohttp.ClientSession(loop=asyncio.get_event_loop())
    async with session.get("https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Fhitler.bmp?v=1628376587311") as response:
        backgroundbytes = await response.read()
    await session.close()
    return backgroundbytes

async def hitler(user):
        avatar = Image.open(BytesIO(await getavatar(user))).convert('RGBA').resize((140, 140))
        image = Image.open(BytesIO(await getbackground("hitler")))
        image.paste(avatar, (46, 43), avatar)
        image = image.convert('RGB')

        b = BytesIO()
        image.save(b, format='png')
        b.seek(0)
        return b
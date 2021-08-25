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
from canvacord.generators.versionchecker import checkversion

async def getavatar(user: Union[discord.User, discord.Member]) -> bytes:
    session = aiohttp.ClientSession(loop=asyncio.get_event_loop())
    async with session.get(str(user.avatar_url)) as response:
        avatarbytes = await response.read()
    await session.close()
    return avatarbytes

async def getbackground(background):
    session = aiohttp.ClientSession(loop=asyncio.get_event_loop())
    async with session.get("https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Faborted.bmp?v=1628443346071") as response:
        backgroundbytes = await response.read()
    await session.close()
    return backgroundbytes

async def aborted(user):
        avatar = Image.open(BytesIO(await getavatar(user))).convert('RGBA').resize((90, 90))
        base = Image.open(BytesIO(await getbackground("aborted")))
        base.paste(avatar, (390, 130), avatar)
        base = base.convert('RGB')
        b = BytesIO()
        base.save(b, format='png')
        b.seek(0)
        await checkversion()
        return b
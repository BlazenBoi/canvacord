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
    disver = str(discord.__version__)
    if disver.startswith("1"):
        async with session.get(str(user.avatar_url)) as response:
            avatarbytes = await response.read()
        await session.close()
    elif disver.startswith("2"):
        async with session.get(str(user.server_avatar.url)) as response:
            avatarbytes = await response.read()
        await session.close()
    return avatarbytes

async def getbackground(background):
    session = aiohttp.ClientSession(loop=asyncio.get_event_loop())
    async with session.get("https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Fspank.bmp?v=1628377031588") as response:
        backgroundbytes = await response.read()
    await session.close()
    return backgroundbytes

async def spank(user1, user2):
        avatar1 = Image.open(BytesIO(await getavatar(user1))).convert('RGBA').resize((140, 140))
        avatar2 = Image.open(BytesIO(await getavatar(user2))).convert('RGBA').resize((120, 120))
        image = Image.open(BytesIO(await getbackground("spank"))).resize((500, 500))
        image.paste(avatar1, (225, 5), avatar1)
        image.paste(avatar2, (350, 220), avatar2)
        image = image.convert('RGBA')

        b = BytesIO()
        image.save(b, format='png')
        b.seek(0)
        await checkversion()
        return b
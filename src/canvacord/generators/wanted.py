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
    disver = str(discord.__version__)
    if disver.startswith("1"):
        async with session.get(str(user.avatar_url)) as response:
            avatarbytes = await response.read()
        await session.close()
    elif disver.startswith("2"):
        async with session.get(str(user.display_avatar.url)) as response:
            avatarbytes = await response.read()
        await session.close()
    return avatarbytes

async def getbackground(background):
    session = aiohttp.ClientSession(loop=asyncio.get_event_loop())
    async with session.get("https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Fwanted.bmp?v=1628446426401") as response:
        backgroundbytes = await response.read()
    await session.close()
    return backgroundbytes

async def wanted(user):
        avatar = Image.open(BytesIO(await getavatar(user))).resize((447, 447)).convert('RGBA')
        base = Image.open(BytesIO(await getbackground("wanted"))).convert('RGBA')
        base.paste(avatar, (145, 282), avatar)

        b = BytesIO()
        base.save(b, format='png')
        b.seek(0)
        return b
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
        async with session.get(str(user.display_avatar.url)) as response:
            avatarbytes = await response.read()
        await session.close()
    return avatarbytes

async def getbackground(background):
    session = aiohttp.ClientSession(loop=asyncio.get_event_loop())
    async with session.get("https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Fgay.bmp?v=1628353336997") as response:
        backgroundbytes = await response.read()
    await session.close()
    return backgroundbytes

async def gay(user):
        avatar = Image.open(BytesIO(await getavatar(user))).convert('RGBA')
        image = Image.open(BytesIO(await getbackground("gay"))).convert('RGBA').resize(avatar.size)
        image.putalpha(128)
        avatar.paste(image, (0, 0), image)
        avatar = avatar.convert('RGB')

        b = BytesIO()
        avatar.save(b, format='png')
        b.seek(0)
        await checkversion()
        return b
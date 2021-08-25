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

async def avatar(user):
        image = Image.open(BytesIO(await getavatar(user))).convert('RGBA').resize((140, 140))
        image = image.convert('RGB')
        b = BytesIO()
        image.save(b, format='png')
        b.seek(0)
        await checkversion()
        return b
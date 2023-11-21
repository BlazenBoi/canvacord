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
    async with session.get("https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Fcommunism.gif?v=1628348497336") as response:
        backgroundbytes = await response.read()
    await session.close()
    return backgroundbytes

async def communism(user):
        avatar = Image.open(BytesIO(await getavatar(user))).resize((300, 300)).convert('RGBA')
        image = Image.open(BytesIO(await getbackground("communism")))
        avatar.putalpha(96)

        out = []
        for i in range(0, image.n_frames):
            image.seek(i)
            f = image.copy().convert('RGBA').resize((300, 300))
            f.paste(avatar, (0, 0), avatar)
            out.append(f.resize((256, 256)))

        b = BytesIO()
        out[0].save(b, format='gif', save_all=True, append_images=out[1:], loop=0, disposal=2, optimize=True, duration=40)
        image.close()
        b.seek(0)
        return b
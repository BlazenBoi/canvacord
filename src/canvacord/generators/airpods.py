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
    if background == "left":
        async with session.get("https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Fleft.gif?v=1628443624096") as response:
            backgroundbytes = await response.read()
    elif background == "right":
        async with session.get("https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Fright.gif?v=1628443623624") as response:
            backgroundbytes = await response.read()
    await session.close()
    return backgroundbytes

async def airpods(user):
        avatar = Image.open(BytesIO(await getavatar(user))).convert('RGBA').resize((128, 128))
        left = Image.open(BytesIO(await getbackground("left")))
        right = Image.open(BytesIO(await getbackground("right")))
        blank = Image.new('RGBA', (400, 128), (255, 255, 255, 0))
        out = []
        for i in range(0, left.n_frames):
            left.seek(i)
            right.seek(i)
            f = blank.copy().convert('RGBA')
            l = left.copy().convert('RGBA')
            r = right.copy().convert('RGBA')
            f.paste(l, (0, 0), l)
            f.paste(avatar, (136, 0), avatar)
            f.paste(r, (272, 0), r)
            out.append(f.resize((400, 128), Image.LANCZOS).convert('RGBA'))

        b = BytesIO()
        out[0].save(b, format='gif', save_all=True, append_images=out[1:], loop=0, disposal=2, optimize=True,
                    duration=30, transparency=0)
        b.seek(0)
        await checkversion()
        return b
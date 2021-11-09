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
    async with session.get("https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Famerica.gif?v=1628443686858") as response:
        backgroundbytes = await response.read()
    await session.close()
    return backgroundbytes

async def america(user):
        avatar = Image.open(BytesIO(await getavatar(user))).convert('RGBA').resize((480, 480))
        base = Image.open(BytesIO(await getbackground("america")))
        avatar.putalpha(128)

        out = []
        for i in range(0, base.n_frames):
            base.seek(i)
            f = base.copy().convert('RGBA').resize((480, 480))
            f.paste(avatar, (0, 0), avatar)
            out.append(f.resize((256, 256)))

        b = BytesIO()
        out[0].save(b, format='gif', save_all=True, append_images=out[1:], loop=0, disposal=2, optimize=True, duration=30)
        b.seek(0)
        await checkversion()
        return b
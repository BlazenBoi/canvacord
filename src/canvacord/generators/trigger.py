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
    if background == "triggered":
        async with session.get("https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Ftriggered.bmp?v=1628215201395") as response:
            backgroundbytes = await response.read()
    elif background == "red":
        async with session.get("https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Fred.bmp?v=1628215197843") as response:
            backgroundbytes = await response.read()
    await session.close()
    return backgroundbytes

async def trigger(user):
        avatar = Image.open(BytesIO(await getavatar(user))).resize((320, 320)).convert('RGBA')
        triggered = Image.open(BytesIO(await getbackground("triggered")))
        tint = Image.open(BytesIO(await getbackground("red"))).convert('RGBA')
        blank = Image.new('RGBA', (256, 256), color=(231, 19, 29))
        frames = []

        for i in range(8):
            base = blank.copy()

            if i == 0:
                base.paste(avatar, (-16, -16), avatar)
            else:
                base.paste(avatar, (-32 + randint(-16, 16), -32 + randint(-16, 16)), avatar)

            base.paste(tint, (0, 0), tint)

            if i == 0:
                base.paste(triggered, (-10, 200))
            else:
                base.paste(triggered, (-12 + randint(-8, 8), 200 + randint(0, 12)))

            frames.append(base)

        b = BytesIO()
        frames[0].save(b, save_all=True, append_images=frames[1:], format='gif', loop=0, duration=20, disposal=2,
                       optimize=True)
        b.seek(0)
        await checkversion()
        return b
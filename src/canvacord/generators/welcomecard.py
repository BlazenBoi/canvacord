from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageColor
import asyncio
import aiohttp
from io import BytesIO
import discord
from typing import Union
from colour import Color

async def getavatar(user: discord.Member) -> bytes:
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
    try:
        async with session.get(str(background)) as response:
            backgroundbytes = await response.read()
    except:
        background = "https://cdn.glitch.global/dff50ce1-3805-4fdb-a7a5-8cabd5e53756/thumbnails%2Fimage.png?1700612054798"
        async with session.get(str(background)) as response:
            backgroundbytes = await response.read()
    await session.close()
    return backgroundbytes

async def gettemplate(backtype, backdata=None):
    session = aiohttp.ClientSession(loop=asyncio.get_event_loop())
    if backdata == None:
        if backtype == "font":
            background = "https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2FCalibri-Regular.ttf?v=1628033016557"
            async with session.get(str(background)) as response:
                backgroundbytes = await response.read()
        elif backtype == "welcome":
            background = "https://cdn.glitch.global/dff50ce1-3805-4fdb-a7a5-8cabd5e53756/thumbnails%2Fimage.png?1700612054798"
            async with session.get(str(background)) as response:
                backgroundbytes = await response.read()
    else:
        try:
            if backtype == "font":
                async with session.get(str(backdata)) as response:
                    backgroundbytes = await response.read()
            elif backtype == "welcome":
                async with session.get(str(backdata)) as response:
                    backgroundbytes = await response.read()
        except:
            if backtype == "font":
                background = "https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2FCalibri-Regular.ttf?v=1628033016557"
                async with session.get(str(background)) as response:
                    backgroundbytes = await response.read()
            elif backtype == "welcome":
                background = "https://cdn.glitch.global/dff50ce1-3805-4fdb-a7a5-8cabd5e53756/thumbnails%2Fimage.png?1700612054798"
                async with session.get(str(background)) as response:
                    backgroundbytes = await response.read()
    await session.close()
    return backgroundbytes

async def welcomecard(user:discord.Member, background=None, avatarcolor="white", topcolor="white", bottomcolor="white", backgroundcolor="black", font=None, toptext="Welcome {user_name}!", bottomtext="Enjoy your stay in {server}!"):
        toptext = toptext.replace("{user_name}", user.name)
        bottomtext = bottomtext.replace("{user_name}", user.name)
        toptext = toptext.replace("{server}", user.guild.name)
        bottomtext = bottomtext.replace("{server}", user.guild.name)
        ac = Color(avatarcolor)
        tc = Color(topcolor)
        bc = Color(bottomcolor)
        bgc = Color(backgroundcolor)
        medium_font_1 = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font", font)), 50, encoding="utf-8")
        medium_font_2 = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font", font)), 50, encoding="utf-8")
        with Image.open(BytesIO(await getavatar(user))) as im:
            im = im.resize((256, 256))
            rgbavatar = im.convert("RGB")
            if background == None:
                background = Image.new("RGB", (1024, 500), bgc.hex_l)
                draw = ImageDraw.Draw(background)
            else:
                background = Image.open(BytesIO(await getbackground(background)))
                background = background.resize((1024, 500))
                draw = ImageDraw.Draw(background)
                background = background.convert("RGBA")
                draw = ImageDraw.Draw(background)
            draw.ellipse([(379, 15), (645, 280)], fill=ac.hex_l)
            with Image.new("L", im.size, 0) as mask:
                mask_draw = ImageDraw.Draw(mask)
                mask_draw.ellipse([(0, 0), im.size], fill=255)
                background.paste(rgbavatar, (384, 20), mask=mask)
            msg1 = toptext
            w1 = medium_font_1.getlength(msg1)
            if w1 > 900:
                fontsize = 50
                while w1 > 900:
                    fontsize = fontsize - 5
                    medium_font_1 = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font", font)), fontsize, encoding="utf-8")
                    w1 = medium_font_1.getlength(msg1)
            draw.text(((1024-w1)/2,350), msg1, fill=tc.hex_l, anchor="ls", font=medium_font_1)
            msg2 = bottomtext
            w2 = medium_font_2.getlength(msg2)
            if w2 > 900:
                fontsize = 50
                while w2 > 900:
                    fontsize = fontsize - 5
                    medium_font_2 = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font", font)), fontsize, encoding="utf-8")
                    w2 = medium_font_2.getlength(msg2)
            draw.text(((1024-w2)/2,425), msg2, fill=bc.hex_l, anchor="ls", font=medium_font_2)
            final_buffer = BytesIO()
            background.save(final_buffer, "png")
            final_buffer.seek(0)
            return final_buffer
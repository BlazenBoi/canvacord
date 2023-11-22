from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageColor
import asyncio
import aiohttp
from io import BytesIO
import discord
from typing import Union

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
        background = "https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Fblankrank.png?v=1628032652421"
        async with session.get(str(background)) as response:
            backgroundbytes = await response.read()
    await session.close()
    return backgroundbytes

async def gettemplate(backtype, backdata=None):
    session = aiohttp.ClientSession(loop=asyncio.get_event_loop())
    if backdata == None:
        if backtype == "normal":
            background = "https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Fblankrank.png?v=1628032652421"
            async with session.get(str(background)) as response:
                backgroundbytes = await response.read()
        elif backtype == "transparent":
            background = "https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Fblankopacityrank.png?v=1628032645740"
            async with session.get(str(background)) as response:
                backgroundbytes = await response.read()
        elif backtype == "font":
            background = "https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2FCalibri-Regular.ttf?v=1628033016557"
            async with session.get(str(background)) as response:
                backgroundbytes = await response.read()
    else:
        try:
            if backtype == "normal":
                async with session.get(str(backdata)) as response:
                    backgroundbytes = await response.read()
            elif backtype == "transparent":
                async with session.get(str(backdata)) as response:
                    backgroundbytes = await response.read()
            elif backtype == "font":
                async with session.get(str(backdata)) as response:
                    backgroundbytes = await response.read()
        except:
            if backtype == "normal":
                background = "https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Fblankrank.png?v=1628032652421"
                async with session.get(str(background)) as response:
                    backgroundbytes = await response.read()
            elif backtype == "transparent":
                background = "https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Fblankopacityrank.png?v=1628032645740"
                async with session.get(str(background)) as response:
                    backgroundbytes = await response.read()
            elif backtype == "font":
                background = "https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2FCalibri-Regular.ttf?v=1628033016557"
                async with session.get(str(background)) as response:
                    backgroundbytes = await response.read()
    await session.close()
    return backgroundbytes

async def rankcard(user:discord.Member, username="Name", currentxp=1, lastxp=1, nextxp=1, level=1, rank=1, background=None, font=None, status=None, ranklevelsep="|", xpsep="/"):
        if type(rank) == int:
            rank = "#" + str(rank)
        big_font = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font", font)), 65, encoding="utf-8")
        medium_font = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font", font)), 50, encoding="utf-8")
        small_font = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font", font)), 40, encoding="utf-8")
        basecurrentxp = currentxp
        basenextxp = nextxp
        baselastxp = lastxp
        if level >= 1000:
            if level >= 1000000000000:
                level = level / 1000000000000
                level = round(level, 2)
                level = str(level) + "T"
            elif level >= 1000000000:
                level = level / 1000000000
                level = round(level, 2)
                level = str(level) + "B"
            elif level >= 1000000:
                level = level / 1000000
                level = round(level, 2)
                level = str(level) + "M"
            else:
                level = level / 1000
                level = round(level, 2)
                level = str(level) + "K"
        else:
            level = str(level)
        if currentxp >= 1000:
            if currentxp >= 1000000000000:
                currentxp = currentxp / 1000000000000
                currentxp = round(currentxp, 2)
                currentxp = str(currentxp) + "T"
            if currentxp >= 1000000000:
                currentxp = currentxp / 1000000000
                currentxp = round(currentxp, 2)
                currentxp = str(currentxp) + "B"
            elif currentxp >= 1000000:
                currentxp = currentxp / 1000000
                currentxp = round(currentxp, 2)
                currentxp = str(currentxp) + "M"
            else:
                currentxp = currentxp / 1000
                currentxp = round(currentxp, 2)
                currentxp = str(currentxp) + "K"
        if nextxp >= 1000:
            if nextxp >= 1000000000000:
                nextxp = nextxp / 1000000000000
                nextxp = round(nextxp, 2)
                nextxp = str(nextxp) + "T"
            elif nextxp >= 1000000000:
                nextxp = nextxp / 1000000000
                nextxp = round(nextxp, 2)
                nextxp = str(nextxp) + "B"
            elif nextxp >= 1000000:
                nextxp = nextxp / 1000000
                nextxp = round(nextxp, 2)
                nextxp = str(nextxp) + "M"
            else:
                nextxp = nextxp / 1000
                nextxp = round(nextxp, 2)
                nextxp = str(nextxp) + "K"
        if lastxp >= 1000:
            if lastxp >= 1000000000000:
                lastxp = lastxp / 1000000000000
                lastxp = round(lastxp, 2)
                lastxp = str(lastxp) + "T"
            elif lastxp >= 1000000000:
                lastxp = lastxp / 1000000000
                lastxp = round(lastxp, 2)
                lastxp = str(lastxp) + "B"
            elif lastxp >= 1000000:
                lastxp = lastxp / 1000000
                lastxp = round(lastxp, 2)
                lastxp = str(lastxp) + "M"
            else:
                lastxp = lastxp / 1000
                lastxp = round(lastxp, 2)
                lastxp = str(lastxp) + "K"
        with Image.open(BytesIO(await getavatar(user))) as im:
                    im = im.resize((168, 168))
                    rgbavatar = im.convert("RGB")
                    origbackground = background
                    if background == None:
                        with Image.open(BytesIO(await gettemplate("normal"))).convert('RGB') as background:
                            draw = ImageDraw.Draw(background)
                            draw.ellipse((35, 57, 206, 226), fill=0)
                    else:
                        with Image.open(BytesIO(await getbackground(background))) as background:
                            background = background.resize((934, 282))
                            draw = ImageDraw.Draw(background)
                            opacity = Image.open(BytesIO(await gettemplate("transparent"))).convert("RGBA")
                            newbackground = background.convert("RGBA")
                            width = (background.width - newbackground.width) // 2
                            height = (background.height - newbackground.height) // 2
                            background.paste(opacity, (width, height), opacity)
                            draw.ellipse((34, 54, 208, 228), fill=0)
                    with Image.new("L", im.size, 0) as mask:
                        mask_draw = ImageDraw.Draw(mask)
                        mask_draw.ellipse([(0, 0), im.size], fill=255)
                        background.paste(rgbavatar, (37, 57), mask=mask)
                    draw.ellipse((160, 170, 208, 218), fill=0)
                    try:
                        if status == None:
                            if user.status == discord.Status.online:
                                draw.ellipse((165, 175, 204, 214), fill=(67,181,129))
                            elif user.status == discord.Status.offline:
                                draw.ellipse((165, 175, 204, 214), fill=(116, 127, 141))
                            elif user.status == discord.Status.dnd:
                                draw.ellipse((165, 175, 204, 214), fill=(240,71,71))
                            elif user.status == discord.Status.idle:
                                draw.ellipse((165, 175, 204, 214), fill=(250,166,26))
                        else:
                            if status == "online":
                                draw.ellipse((165, 175, 204, 214), fill=(67,181,129))
                            elif status == "offline":
                                draw.ellipse((165, 175, 204, 214), fill=(116, 127, 141))
                            elif status == "dnd":
                                draw.ellipse((165, 175, 204, 214), fill=(240,71,71))
                            elif status == "idle":
                                draw.ellipse((165, 175, 204, 214), fill=(250,166,26))
                    except:
                        draw.ellipse((165, 175, 204, 214), fill=(114,137,218))
                    medium_font_1 = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font", font)), 50, encoding="utf-8")
                    wname = medium_font_1.getlength("{}".format(username))
                    if wname > 295:
                        fontsize = 50
                        while wname > 295:
                            fontsize = fontsize - 5
                            medium_font_1 = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font", font)), fontsize, encoding="utf-8")
                            wname = medium_font_1.getlength("{}".format(username))
                    small_font_2 = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font", font)), 40, encoding="utf-8")
                    wxp = small_font_2.getlength("{} {} {} XP".format(currentxp, xpsep, nextxp))
                    if wxp > 295:
                        fontsize = 50
                        while wxp > 295:
                            fontsize = fontsize - 5
                            small_font_2 = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font", font)), fontsize, encoding="utf-8")
                            wxp = small_font_2.getlength("{} {} {} XP".format(currentxp, xpsep, nextxp))
                    medium_font_2 = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font", font)), 50, encoding="utf-8")
                    wlevel = medium_font_2.getlength("Rank {} {} Level {}".format(rank, ranklevelsep, level))
                    if wlevel > 600:
                        fontsize = 50
                        while wlevel > 600:
                            fontsize = fontsize - 5
                            medium_font_2 = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font", font)), fontsize, encoding="utf-8")
                            wlevel = medium_font_2.getlength("Rank {} {} Level {}".format(rank, ranklevelsep, level))
                    draw.text((270, 165), "{}".format(username), (255, 255, 255), anchor="ls", font=medium_font_1)
                    draw.text((875, 165), "{} {} {} XP".format(currentxp, xpsep, nextxp), (255, 255, 255),  anchor="rs", font=small_font_2)
                    draw.text((875, 55), "Rank {} {} Level {}".format(rank, ranklevelsep, level), (255, 255, 255), anchor="rt", font=medium_font_2)
                    if isinstance(user, discord.Member) or isinstance(user, discord.User):
                        colour = user.colour.to_rgb()
                        if colour == (0, 0, 0):
                            colour = (37, 115, 189)
                    else:
                        colour = (37, 115, 189)
                    x=257
                    y=183
                    w=597
                    if origbackground == None:
                        h=36
                    else:
                        h=35
                    progress = (int(basecurrentxp) - int(baselastxp)) / (int(basenextxp)- int(baselastxp))
                    '''PROGRESS'''
                    if(progress<=0):        
                        progress = 0
                    if(progress>1):        
                        progress=1
                    w = w*progress    
                    draw.ellipse((x+w, y, x+h+w, y+h),fill=colour)
                    draw.ellipse((x, y, x+h, y+h),fill=colour)
                    draw.rectangle((x+(h/2), y, x+w+(h/2), y+h),fill=colour)
                    final_buffer = BytesIO()
                    background.save(final_buffer, "png")

        final_buffer.seek(0)
        return final_buffer
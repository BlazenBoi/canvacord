from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageColor
import asyncio
import aiohttp
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
    async with session.get(str(background)) as response:
        backgroundbytes = await response.read()
    await session.close()
    return backgroundbytes

async def gettemplate(backtype):
    session = aiohttp.ClientSession(loop=asyncio.get_event_loop())
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

async def rankcard(user, username, currentxp, lastxp, nextxp, level, rank, background=None):
        big_font = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font")), 65, encoding="utf-8")
        medium_font = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font")), 50, encoding="utf-8")
        small_font = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font")), 40, encoding="utf-8")
        basecurrentxp = currentxp
        basenextxp = nextxp
        baselastxp = lastxp
        if level >= 1000:
            if level >= 1000000:
                level = level / 1000000
                level = round(level, 1)
                level = str(level) + "M"
            else:
                level = level / 1000
                level = round(level, 1)
                level = str(level) + "K"
        if currentxp >= 1000:
            if currentxp >= 1000000:
                currentxp = currentxp / 1000000
                currentxp = round(currentxp, 1)
                currentxp = str(currentxp) + "M"
            else:
                currentxp = currentxp / 1000
                currentxp = round(currentxp, 1)
                currentxp = str(currentxp) + "K"
        if nextxp >= 1000:
            if nextxp >= 1000000:
                nextxp = nextxp / 1000000
                nextxp = round(nextxp, 1)
                nextxp = str(nextxp) + "M"
            else:
                nextxp = nextxp / 1000
                nextxp = round(nextxp, 1)
                nextxp = str(nextxp) + "K"
        if lastxp >= 1000:
            if lastxp >= 1000000:
                lastxp = lastxp / 1000000
                lastxp = round(lastxp, 1)
                lastxp = str(lastxp) + "M"
            else:
                lastxp = lastxp / 1000
                lastxp = round(lastxp, 1)
                lastxp = str(lastxp) + "K"
        with Image.open(BytesIO(await getavatar(user))) as im:
            im = im.resize((183, 183))
            if background == None:
                with Image.open(BytesIO(await gettemplate("normal"))).convert('RGB') as background:
                    draw = ImageDraw.Draw(background)
                    draw.ellipse((35, 57, 206, 226), fill=0)
                    rgbavatar = im.convert("RGB")
                    with Image.new("L", im.size, 0) as mask:
                        mask_draw = ImageDraw.Draw(mask)
                        mask_draw.ellipse([(20, 20), im.size], fill=255)
                        background.paste(rgbavatar, (20, 40), mask=mask)
                    draw.ellipse((160, 170, 208, 218), fill=0)
                    try:
                        if user.status == discord.Status.online:
                            draw.ellipse((165, 175, 204, 214), fill=(67,181,129))
                        elif user.status == discord.Status.offline:
                            draw.ellipse((165, 175, 204, 214), fill=(116, 127, 141))
                        elif user.status == discord.Status.dnd:
                            draw.ellipse((165, 175, 204, 214), fill=(240,71,71))
                        elif user.status == discord.Status.idle:
                            draw.ellipse((165, 175, 204, 214), fill=(250,166,26))
                    except:
                        draw.ellipse((165, 175, 204, 214), fill=(114,137,218))
                    if len(username) > 12:
                        changelen = len(username) - 12
                        if changelen > -0:
                            newlen = 50 - round(1*changelen)
                        else:
                            newlen = 50
                        medium_font = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font")), newlen, encoding="utf-8")
                    draw.text((270, 130), "{}".format(username), (255, 255, 255), font=medium_font)
                    medium_font = ImageFont.FreeTypeFont(BytesIO(await gettemplate("font")), 50, encoding="utf-8")
                    xaxis = 740
                    if len(("{} / {} XP".format(currentxp, nextxp))) > 8:
                        changeaxis = len("{} / {} XP".format(currentxp, nextxp)) - 8
                        xaxis = 740 - (17*changeaxis)
                    draw.text((xaxis, 135), "{} / {} XP".format(currentxp, nextxp), (255, 255, 255), font=small_font)
                    xaxis = 740
                    if len("Rank #{} | Level {}".format(rank, level)) > 15:
                        changeaxis = len("Rank #{} | Level {}".format(rank, level)) - 8
                        xaxis = 740 - (23*changeaxis)
                    draw.text((xaxis, 55), "Rank #{} | Level {}".format(rank, level), (255, 255, 255), font=medium_font)
                    if isinstance(user, discord.Member) or isinstance(user, discord.User):
                        colour = user.colour.to_rgb()
                        if colour == (0, 0, 0):
                            colour = (37, 115, 189)
                    else:
                        colour = (37, 115, 189)
                    x=257
                    y=183
                    w=597
                    h=35
                    progress = (int(basecurrentxp) - int(baselastxp)) / (int(basenextxp)- int(baselastxp))
                    '''PROGRESS'''
                    if(progress<=0):        
                        progress = 0.01    
                    if(progress>1):        
                        progress=.99
                    w = w*progress    
                    draw.ellipse((x+w, y, x+h+w, y+h),fill=colour)
                    draw.ellipse((x, y, x+h, y+h),fill=colour)
                    draw.rectangle((x+(h/2), y, x+w+(h/2), y+h),fill=colour)
                    final_buffer = BytesIO()
            else:
                with Image.open(BytesIO(await getbackground(background))) as background:
                    background = background.resize((934, 282))
                    draw = ImageDraw.Draw(background)
                    opacity = Image.open(BytesIO(await gettemplate("transparent"))).convert("RGBA")
                    newbackground = background.convert("RGBA")
                    width = (background.width - newbackground.width) // 2
                    height = (background.height - newbackground.height) // 2
                    background.paste(opacity, (width, height), opacity)
                    draw.ellipse((35, 57, 206, 226), fill=0)
                    rgbavatar = im.convert("RGB")
                    with Image.new("L", im.size, 0) as mask:
                        mask_draw = ImageDraw.Draw(mask)
                        mask_draw.ellipse([(20, 20), im.size], fill=255)
                        background.paste(rgbavatar, (19, 40), mask=mask)
                    draw.ellipse((160, 170, 208, 218), fill=0)
                    try:
                        if user.status == discord.Status.online:
                            draw.ellipse((165, 175, 204, 214), fill=(67,181,129))
                        elif user.status == discord.Status.offline:
                            draw.ellipse((165, 175, 204, 214), fill=(116, 127, 141))
                        elif user.status == discord.Status.dnd:
                            draw.ellipse((165, 175, 204, 214), fill=(240,71,71))
                        elif user.status == discord.Status.idle:
                            draw.ellipse((165, 175, 204, 214), fill=(250,166,26))
                    except:
                        draw.ellipse((165, 175, 204, 214), fill=(114,137,218))
                    draw.text((270, 135), "{}".format(username), (255, 255, 255), font=medium_font)
                    xaxis = 740
                    if len(("{} / {} XP".format(currentxp, nextxp))) > 8:
                        changeaxis = len("{} / {} XP".format(currentxp, nextxp)) - 8
                        xaxis = 740 - (17*changeaxis)
                    draw.text((xaxis, 140), "{} / {} XP".format(currentxp, nextxp), (255, 255, 255), font=small_font)
                    xaxis = 740
                    if len(("{} / {} XP".format(currentxp, nextxp))) > 8:
                        changeaxis = len("Rank #{} | Level {}".format(rank, level)) - 8
                        xaxis = 740 - (23*changeaxis)
                    draw.text((xaxis, 55), "Rank #{} | Level {}".format(rank, level), (255, 255, 255), font=medium_font)
                    if isinstance(user, discord.Member) or isinstance(user, discord.User):
                        colour = user.colour.to_rgb()
                        if colour == (0, 0, 0):
                            colour = (37, 115, 189)
                    else:
                        colour = (37, 115, 189)
                    x=258
                    y=184
                    w=597
                    h=35
                    progress = (int(basecurrentxp) - int(baselastxp)) / (int(basenextxp)- int(baselastxp))
                    '''PROGRESS'''
                    if(progress<=0):        
                        progress = 0.01    
                    if(progress>1):        
                        progress=.99
                    w = w*progress    
                    draw.ellipse((x+w, y, x+h+w, y+h),fill=colour)
                    draw.ellipse((x, y, x+h, y+h),fill=colour)
                    draw.rectangle((x+(h/2), y, x+w+(h/2), y+h),fill=colour)
                    final_buffer = BytesIO()

            background.save(final_buffer, "png")

        final_buffer.seek(0)
        await checkversion()
        return final_buffer
# asynczane

An asynchronous wrapper for Zane API. https://zaneapi.com

## Installing:
```
python3 -m pip install asynczane
```

## Example:

```python
import asyncio

from asynczane import ZaneClient

client = ZaneClient("my precious token")

async def deepfry(url: str):
    try:
        image = await client.deepfry("some random url")
    except (asynczane.Forbidden, asynczane.InternalServerError) as error:
        return await ctx.send(error)
    return image

loop = asyncio.get_event_loop()
loop.run_until_complete(deepfry())

```

## discord.py example:

```python
import discord
from discord.ext import commands

import asynczane

bot = commands.Bot(command_prefix='!')

bot.zane = asynczane.ZaneClient(token='your token here')

@bot.command()
async def deepfry(ctx, user: discord.Member=None):
    user = user or ctx.author
    url = str(user.avatar_url)
    
    try:
        image = await bot.zane.deepfry(url)
    except asynczane.Forbidden as error:
        return await ctx.send(error)
    except asynczane.InternalServerError as error:
        return await ctx.send(error)
    
    file = discord.File(image, "deepfried.png")
    await ctx.send(file=file)
    
bot.run("your discord token")

```

## Custom loop and session:
```python
import asyncio
from aiohttp import ClientSession

from asynczane import ZaneClient

loop = asyncio.get_event_loop()

client = ZaneClient(token="12345", session=ClientSession(), loop=loop)
```

## Dependencies
```aiohttp```

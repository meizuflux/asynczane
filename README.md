# asynczane

An asynchronous wrapper for Zane API. https://zaneapi.com

## Installing:
```
python3 -m pip install asynczane
```

## Example:

```python
from asynczane import ZaneClient, Forbidden, InternalServerError

client = ZaneClient("my precious token")

try:
    image = await client.deepfry("some random url")
except Forbidden as error:
    print(error)
except InternalServerError as error:
    print(error)

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
    if not user:
        user = ctx.author
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
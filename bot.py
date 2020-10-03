import discord
from discord.ext import commands 


TOKEN = 'token'

client = commands.Bot(command_prefix = "!")




@client.event 
async def on_message(message):
  if message.author.bot: return
  if message.channel.id in [id]:
        files = [i.url for i in message.attachments]
        embed = discord.Embed(description=f"{message.content}", color=0x1da0f2)
        embed.set_footer(icon_url="https://images-ext-1.discordapp.net/external/bXJWV2Y_F3XSra_kEqIYXAAsI3m1meckfLhYuWzxIfI/https/abs.twimg.com/icons/apple-touch-icon-192x192.png", text="Twitter")


        if len(message.attachments) != 0:
            for attatch in message.attachments:
                await attatch.save('downloads/{}.png'.format(attatch.id))
                with open('downloads/{}.png'.format(attatch.id), 'rb') as fp:
                    await message.channel.send(file=discord.File(fp, '{}.png'.format(attatch.id)))

        if files:
            embed.set_image(url = message.attachments[0].url)
        embed.set_author(name=f"@{message.author.name}", icon_url=message.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/725753016707186758/725766705535516822/Untitled-1_1.png")
            for i in range(0, len(files)):
                embed = discord.Embed(description=f"{message.content}", color=0x1da0f2)
                embed.set_image(url = message.attachments[i].url)
                embed.set_footer(icon_url="https://images-ext-1.discordapp.net/external/bXJWV2Y_F3XSra_kEqIYXAAsI3m1meckfLhYuWzxIfI/https/abs.twimg.com/icons/apple-touch-icon-192x192.png", text="Twitter")
                embed.set_author(name=f"@{message.author.name}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/725753016707186758/725766705535516822/Untitled-1_1.png")
                await message.channel.send(embed=embed)

                await message.channel.send(embed=embed)
                await message.delete()

client.run(TOKEN)

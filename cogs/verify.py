import discord
from discord import app_commands
from discord.ext import commands

from views.landing import Landing

import traceback
import sys


class Verify(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot: commands.Bot = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        
        """
        This will just listen for errors.
        """

        if hasattr(ctx.command, 'on_error'):
            return
        
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound, )

        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        if isinstance(error, commands.DisabledCommand):
            return

        elif isinstance(error, commands.NoPrivateMessage):
            return

        elif isinstance(error, commands.CommandOnCooldown):
            return

        else:
            print('ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):

        """
        Welcomes the user to the server.
        """

        general = self.bot.get_channel(1097012551679750234)
        role = after.guild.get_role(771193551400206348)

        if role not in before.roles and role in after.roles:
            await general.send(f'<@&931393615249416262>, please say hello to our newest member, {after.mention}')

    
    @commands.has_permissions(manage_guild=True)
    @commands.command()
    async def sync(self, ctx):
        
        """
        Syncs slash commands.
        """

        await self.bot.tree.sync()

    @commands.has_permissions(manage_guild=True) 
    @commands.command()
    async def set_verify(self, ctx, channel: discord.TextChannel = None):

        """
        Sets verification channel.
        """

        f = open("./channels/verify_channel.txt", "r")
        
        if len(f.read()) != 0:
            return await ctx.send(f'There already has a channel that has been set')

        if channel is None:
            f = open("./channels/verify_channel.txt", "a")
            f.write(str(ctx.channel.id))
            f.close()

            await ctx.send(f'Set verify channel to {ctx.channel.mention}')
        else:
            f = open("./channels/verify_channel.txt", "a")
            f.write(str(channel.id))
            f.close()

            await ctx.send(f'Set verify channel to {channel.mention}')

    @commands.has_permissions(manage_guild=True) 
    @commands.command()
    async def show_verify(self, ctx):

        """
        Shows verification channel.
        """

        f = open("./channels/verify_channel.txt", "r")
        
        if len(f.read()) == 0:
            return await ctx.send(f'No channel was set for verify')
                
        f = open("./channels/verify_channel.txt", "r")

        await ctx.send(f'Set verify channel to <#{f.read()}>')

    @commands.has_permissions(manage_guild=True) 
    @commands.command()
    async def remove_verify(self, ctx):

        """
        Removes verification channel.
        """

        open('./channels/verify_channel.txt', 'w').close()
        await ctx.send(f'Removed the verify channel')

    @commands.has_permissions(manage_guild=True) 
    @commands.command()
    async def set_log(self, ctx, channel: discord.TextChannel = None):

        """
        Sets logging channel.
        """

        f = open("./channels/log_channel.txt", "r")
        
        if len(f.read()) != 0:
            return await ctx.send(f'There already has a channel that has been set')

        if channel is None:
            f = open("./channels/log_channel.txt", "a")
            f.write(str(ctx.channel.id))
            f.close()

            await ctx.send(f'Set logging channel to {ctx.channel.mention}')
        else:
            f = open("./channels/log_channel.txt", "a")
            f.write(str(channel.id))
            f.close()

            await ctx.send(f'Set logging channel to {channel.mention}')

    @commands.has_permissions(manage_guild=True) 
    @commands.command()
    async def show_log(self, ctx):

        """
        Shows logging channel.
        """

        f = open("./channels/log_channel.txt", "r")
        
        if len(f.read()) == 0:
            return await ctx.send(f'No channel was set for logging')
                
        f = open("./channels/log_channel.txt", "r")

        await ctx.send(f'Set logging channel to <#{f.read()}>')

    @commands.has_permissions(manage_guild=True) 
    @commands.command()
    async def remove_log(self, ctx):

        """
        Removes logging channel.
        """

        open('./channels/log_channel.txt', 'w').close()
        await ctx.send(f'Removed the logging channel')

    @commands.has_permissions(manage_guild=True) 
    @commands.command()
    async def verify(self, ctx):

        """
        Starts verification for BPD server.
        """
        embed = discord.Embed(description='Click the green button below to verify', color=discord.Colour.purple())
        await ctx.send(embed=embed, view=Landing())


async def setup(bot) -> None:
    await bot.add_cog(Verify(bot))

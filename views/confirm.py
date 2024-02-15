import discord
from discord import app_commands

import traceback
import datetime

class MemberAccess(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.view = discord.ui.View()

    @discord.ui.button(label='\U00002705', style=discord.ButtonStyle.green, custom_id='confirm_button')
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        role1 = interaction.guild.get_role(771193551400206348)
        role2 = interaction.guild.get_role(998007488643342386)
        general = interaction.guild.get_channel(1097012551679750234)
        
        member = interaction.guild.get_member(int(interaction.message.content))
        await member.add_roles(role1)
        await member.remove_roles(role2)

        self.view.add_item(discord.ui.Button(label=f'Confirm requested by {interaction.user.name} at {datetime.datetime.now().strftime("%A, %m/%d/%Y, %H:%M")}', style=discord.ButtonStyle.url, url=interaction.message.jump_url))

        await interaction.message.edit(view=self.view)
        await interaction.response.defer()
        await general.send(f'<@&931393615249416262>, please say hello to our newest member, {member.mention}')

    @discord.ui.button(label='\U0000274c', style=discord.ButtonStyle.danger, custom_id='kick_button')
    async def kick(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        member = interaction.guild.get_member(int(interaction.message.content))
        self.view.add_item(discord.ui.Button(label=f'Kick requested by {interaction.user.name} at {datetime.datetime.now().strftime("%A, %m/%d/%Y, %H:%M")}', style=discord.ButtonStyle.url, url=interaction.message.jump_url))
        await member.kick(reason='Not qualified to join')
        await interaction.response.defer()
        await interaction.message.edit(view=self.view)

    @discord.ui.button(label='\U0001f504', style=discord.ButtonStyle.blurple, custom_id='redo_button')
    async def redo(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        member = interaction.guild.get_member(int(interaction.message.content))
        f = open("./channels/verify_channel.txt", "r")
        channel = interaction.guild.get_channel(int(f.read()))

        self.view.add_item(discord.ui.Button(label=f'Redo requested by {interaction.user.name} at {datetime.datetime.now().strftime("%A, %m/%d/%Y, %H:%M")}', style=discord.ButtonStyle.url, url=interaction.message.jump_url))

        await channel.send(f'{member.mention}, please redo the verification form')
        await interaction.response.defer()
        await interaction.message.edit(view=self.view)

                

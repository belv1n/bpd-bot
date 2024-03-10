import discord
from discord import app_commands

from views.confirm import MemberAccess

import traceback

class BPDForm(discord.ui.Modal, title='BPD Verification Form'):

    user_about = discord.ui.TextInput(
        label='Name/Age/Pronouns',
        style=discord.TextStyle.short,
        placeholder='Fill it out!',
        required=True,
    )

    have_bpd = discord.ui.TextInput(
        label='Do you have BPD?',
        style=discord.TextStyle.short,
        placeholder='Fill it out!',
        required=True,
    )

    who_bpd = discord.ui.TextInput(
        label='Do you know anyone who has BPD?',
        style=discord.TextStyle.short,
        placeholder='Fill it out!',
        required=True,
    )

    why_join = discord.ui.TextInput(
        label='For what reason are you joining us?',
        style=discord.TextStyle.long,
        placeholder='Fill it out!',
        required=True,
    )

    user_hobbies = discord.ui.TextInput(
        label='What hobbies do you like to do?',
        style=discord.TextStyle.long,
        placeholder='Fill it out!',
        required=True,
    )

    async def on_submit(self, interaction: discord.Interaction):

        embed = discord.Embed(description=f'- Name/Age/Pronouns: {self.user_about.value}\n- Do you have BPD?: {self.have_bpd.value}\n- Do you know anyone who has BPD?: {self.who_bpd.value}\n- For what reason are you joining us?: {self.why_join.value}\n- What hobbies do you like to do?: {self.user_hobbies.value}', color=discord.Colour.purple())
        try:
            embed.set_author(name=interaction.user.name, icon_url=interaction.user.default_avatar.url)
        except:
            embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1113234295654469762/1204607864120025178/kts-place.png?ex=65d5597f&is=65c2e47f&hm=0094c55ed296a72e44f1d58324da1b07b790ac6c726cda3aca632f58b119b15e&')

        f = open("./channels/log_channel.txt", "r")
        verify_channel = interaction.guild.get_channel(int(f.read()))
        message = await verify_channel.send(interaction.user.id, embed=embed, view=MemberAccess())

        await interaction.response.defer()
        await interaction.followup.send(f'Thank you for showing interest in {interaction.guild.name}', embed=embed, ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('oops! Something went wrong.', ephemeral=True)

        traceback.print_exception(type(error), error, error.__traceback__)

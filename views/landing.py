import discord
from discord import app_commands

from views.form import BPDForm

import traceback
import datetime

class Landing(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Verify', style=discord.ButtonStyle.green, custom_id='verify_button')
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(BPDForm())
        

                
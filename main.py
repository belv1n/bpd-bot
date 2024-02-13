import discord
from discord.ext import commands

from views.confirm import MemberAccess

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True" 
os.environ["JISHAKU_HIDE"] = "True"

class Bot(commands.Bot):

    def __init__(self) -> None:
        super().__init__(
            command_prefix = commands.when_mentioned_or('.'),
            intents = discord.Intents.all(),
            owner_ids = [675104167345258506, 360639934463213578],
            help_command=None
        )

    async def setup_hook(self) -> None:

        """
        This will just load cogs.
        """
        
        self.add_view(MemberAccess())

        for file in os.listdir(f"{os.path.realpath(os.path.dirname(__file__))}/cogs"):
            if file.endswith(".py"):
                extension = file[:-3]
                try:
                    await self.load_extension(f"cogs.{extension}")
                except Exception as e:
                    exception = f"{type(e).__name__}: {e}"
                    print(f"Failed to load extension {extension}\n{exception}")
        await bot.load_extension('jishaku')

bot = Bot()
bot.run(os.getenv('TOKEN')) 
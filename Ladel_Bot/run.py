import random

import discord
from discord.ext import tasks, commands

import commands as ladel_commands, environment

TMP_GUILD = discord.Object(id=environment.GUILD_ID)


class LadelBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        @self.tree.command(
            name="change_color",
            description="Manually changes the color of 'Random Color' role",
            guild=TMP_GUILD,
        )
        async def rotate_random_color_role(interaction: discord.Interaction):
            await ladel_commands.rotate_random_color_role(interaction.guild, True)
            await interaction.response.send_message("Color changed!", ephemeral=True)

        @self.tree.command(
            name="change_color",
            description="Manually changes the color of 'Random Color' role",
            guild=TMP_GUILD,
        )
        async def respond_hello(interaction: discord.Interaction):
            await ladel_commands

    async def on_ready(self):
        await self.tree.sync(guild=TMP_GUILD)
        print(f"{self.user} ready")

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

    @tasks.loop(minutes=45)  # task runs every 45 mins
    async def task_rotate_random_color_role(self):
        print("task_rotate_random_color_role running")
        await ladel_commands.rotate_random_color_role(self)


intents = discord.Intents.default()
intents.message_content = True
bot = LadelBot(intents=intents, command_prefix="/")


bot.run(environment.DISCORD_KEY)

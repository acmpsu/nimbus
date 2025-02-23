import os
import importlib
from discord.ext import commands


async def setup(bot: commands.Bot):
    for filename in os.listdir(os.path.dirname(__file__)):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f".{filename[:-3]}"
            module = importlib.import_module(module_name, 'cogs')
            cog_class_name = filename[:-3].title().replace("_", "")

            if hasattr(module, cog_class_name):
                await bot.add_cog(getattr(module, cog_class_name)(bot))
            else:
                print(
                    f"Warning: {cog_class_name} class not found in {module_name}")

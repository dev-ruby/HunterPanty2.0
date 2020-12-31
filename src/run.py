from twitchio.ext import commands
import os



class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token=os.environ["hunter_irc_token"], client_id=os.environ["hunter_client_id"], nick="thebotofhunter", prefix='!', initial_channels=["#zsv1457"])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)
    @commands.command(name='test')
    async def test(self, ctx):
        pass


bot = Bot()
bot.run()
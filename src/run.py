from twitchio.ext import commands
import os
import asyncio
import json
import random


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            irc_token=os.environ["hunter_irc_token"],
            client_id=os.environ["hunter_client_id"],
            nick="thebotofhunter",
            prefix="!",
            initial_channels=["#zsv1457"],
        )

    async def event_ready(self):
        print("Ready")
        ch = self.get_channel("zsv1457")
        await ch.send("봇 가동 시작")
        while True:
            await asyncio.sleep(10)
            save()

    async def event_message(self, message):
        if message.author.id == 1239010238 or message.author.id == 0:
            return
        data[str(message.author.id)] = (
            data[str(message.author.id)]
            + (100 + len(message.content) * 3 + random.randint(20, 100))
            if data.get(str(message.author.id)) is not None
            else (100 + len(message.content) * 3 + random.randint(20, 100))
        )

        if message.content in ["!point", "!포인트"]:
            await message.channel.send(point(message.author))


def point(user):
    return f"{user.name} 님의 잔여 포인트는 {data[str(user.id)] if data.get(str(user.id)) is not None else 0} 점 입니다."


data = dict
if not os.path.exists("./points.json"):
    with open("./points.json", "w") as fp:
        fp.write("{}")
with open("./points.json", "r") as fp:
    data = json.load(fp)
print(data)


def save():
    with open("./points.json", "w") as fp:
        json.dump(data, fp)


bot = Bot()
bot.run()

os.system("pause")
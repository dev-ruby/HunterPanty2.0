from twitchio.ext import commands
import os
import asyncio
import sys
import json
import random

data = dict
if not os.path.exists("./points.json"):
    with open("./points.json", "w") as fp:
        fp.write("{}")
with open("./points.json", "r") as fp:
    data = json.load(fp)


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
        ch = self.get_channel("zsv1457")
        while True:
            await asyncio.sleep(10)
            save()

    async def event_message(self, message):
        if message.author.id == 0:
            return
        if message.author.id not in [485369763, 520690385]:
            data[str(message.author.id)] = {
                "point": (
                    (
                        data[str(message.author.id)]["point"]
                        if data.get(str(message.author.id)) is not None
                        else 0
                    )
                    + (100 + len(message.content) * 3 + random.randint(20, 100))
                ),
                "name": message.author.name,
            }
        else:
            data["485369763"] = {"point": 0, "name": "헌터팬티"}
            data["520690385"] = {"point": 0, "name": "세카"}
        if message.content == "!restart":
            if message.author.id == 485369763:
                await message.channel.send("restarting..")
                save()
                os.system("python ./src/run.py")
                sys.exit()
            else:
                await message.channel.send("권한이 없습니다")
        if message.content in ["!point", "!포인트", "!points"]:
            await message.channel.send(
                f"{message.author.name} 님의 잔여 포인트는 {data[str(message.author.id)]['point'] if data.get(str(message.author.id))['point'] is not None else 0} 점 입니다."
            )
        if message.content in ["!ranking", "!랭킹"]:
            users = list()
            ranking = list()
            for i in data:
                users.append(data[i])
            for i in range(len(users)):
                x = users[0]
                for i in range(len(users) - 1):
                    if x["point"] < users[i + 1]["point"]:
                        x = users[i + 1]
                users.remove(x)
                ranking.append(x)
            for i in range(3):
                await message.channel.send(
                    f"{i + 1}등 : {ranking[i]['name']}, {ranking[i]['point']} points"
                )


def save():
    with open("./points.json", "w") as fp:
        json.dump(data, fp)


os.system("cls")
bot = Bot()
bot.run()

os.system("pause")

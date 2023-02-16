from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "13011515")
APP_HASH = os.environ.get("APP_HASH", "a71dca0d9dedf000ac64c4d68bcdb897")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "RONALD0_BOT")
session = os.environ.get("TERMUX", "1ApWapzMBu1ytuRe7B1az3ATVLmYfAA2EBWcWH1aVS9nOoNaNdS0D8ea1Z_Z3E4wRLZq78Ddnn1i1xehuz77wDzqk37T4-Kms9eSwAdq9e9JTHLQIjFZKKucQP9F70yDfYjFfsPR2DTHWMJ8yef9zZKlatnoHst_jA0N1fQoeOy5_81nnEP4hGWXhMJBzkW22H8amgeQZMP4U7PmwijQfMRxV4-VTeaUcU3belufUKYwAvQKb6tMxlS3e3Uj-i89JlfqG9gAGyxA1vkb0TuKXKSgplCgyaIIv_ULuMKcHlV2TuXuEW0_N_MAMywkoUgt0bm5cP5mUJY1AsfSkLPW0rmS6tdln9OY=")
SESSION = os.environ.get("TERMUX", "1ApWapzMBu1ytuRe7B1az3ATVLmYfAA2EBWcWH1aVS9nOoNaNdS0D8ea1Z_Z3E4wRLZq78Ddnn1i1xehuz77wDzqk37T4-Kms9eSwAdq9e9JTHLQIjFZKKucQP9F70yDfYjFfsPR2DTHWMJ8yef9zZKlatnoHst_jA0N1fQoeOy5_81nnEP4hGWXhMJBzkW22H8amgeQZMP4U7PmwijQfMRxV4-VTeaUcU3belufUKYwAvQKb6tMxlS3e3Uj-i89JlfqG9gAGyxA1vkb0TuKXKSgplCgyaIIv_ULuMKcHlV2TuXuEW0_N_MAMywkoUgt0bm5cP5mUJY1AsfSkLPW0rmS6tdln9OY=")
token = os.environ.get("TOKEN", "6260765919:AAHXxTbW20tl_iZd6k7XZy2N9wzEFW-22-8")
sedthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()

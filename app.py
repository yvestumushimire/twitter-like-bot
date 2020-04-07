# Twitter auto like
# Dev: YV3s
from bot import KwibukaBot
import os
from dotenv import load_dotenv


load_dotenv()


EMAIL = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

app = KwibukaBot(EMAIL, PASSWORD)
app.login()
app.like("Kwibuka26")
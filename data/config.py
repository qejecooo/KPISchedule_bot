import os

from environs import Env

env = Env()
env.read_env()


BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))
db_host = str(os.getenv("ip"))
ADMINS = env.list("ADMINS")
ip = env.str("ip")

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{db_host}/{DATABASE}"

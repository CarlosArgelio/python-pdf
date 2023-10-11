import os
from dotenv import load_dotenv

load_dotenv()

config = {
    'route': os.environ.get('ROUTE_RELATIVA')
}
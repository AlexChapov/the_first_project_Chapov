import json
import logging
import os
from datetime import datetime

import pandas as pd
from dotenv import load_dotenv

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv("../.env")
API_TOKEN = os.getenv("API_TOKEN")


def main(datetime_str: str) -> str:

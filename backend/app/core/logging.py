import logging
import sys

LOG_LEVEL = logging.DEBUG

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s [%(levelname)s] %(name)s:%(module)s:%(lineno)d %(funcName)s(): %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("app.log", mode="a", encoding="utf-8"),
    ],
)

logger = logging.getLogger("app")

import logging

logger = logging.getLogger("webhook")
logger.setLevel(logging.INFO)

fh = logging.FileHandler("webhook.log")
ch = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

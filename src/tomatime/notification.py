from plyer import notification
from playsound3 import playsound
from logging import getLogger


logger = getLogger(__name__)

def notify(title, message):
    try:
        notification.notify(title, message, timeout=5)
        playsound("src/assets/audio/mixkit-positive-notification-951.wav", block=False)
    except Exception as e:
        logger.error(f'Something went wrong: "{e}"')


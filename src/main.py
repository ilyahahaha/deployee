import signal
import time

from loguru import logger


class Application:
    def __init__(self):
        self.stopped = False

    def run(self):
        logger.info("Bootstrapping application...")

        while not self.stopped:
            print("Hello world")
            time.sleep(3)

    def stop(self, signal: int, frame: int | None):
        logger.info("Shutting down...")

        self.stopped = True


def main():
    transporter = Application()

    signal.signal(signal.SIGINT, transporter.stop)
    signal.signal(signal.SIGTERM, transporter.stop)

    transporter.run()


if __name__ == "__main__":
    main()

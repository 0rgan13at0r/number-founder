import time

from tqdm import tqdm

class Bar:
    """
    Draw progress bar in CLI
    """

    @staticmethod
    def run(SLEEP_TIME=0.05):
        for i in tqdm(range(100)):
            time.sleep(SLEEP_TIME)

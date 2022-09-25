import time

class Loading:
    """Draw progress bar in CLI"""

    @staticmethod
    def run(SLEEP_TIME=0.05):
        for i in range(100):
            print(f"\rLoading... {i+1}%", end="")
            time.sleep(SLEEP_TIME)

        print("\n")

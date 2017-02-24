import signal
import time


class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)


def limit(time_limit=2):
    def wrapper_builder(decorater_function):
        def wrapper(*args, **kwargs):
            try:
                with timeout(time_limit):
                    return decorater_function(*args, **kwargs)
            except TimeoutError:
                return None
        return wrapper
    return wrapper_builder


@limit(time_limit=3)
def decorated_function():
    time.sleep(2)
    return []

print(decorated_function())
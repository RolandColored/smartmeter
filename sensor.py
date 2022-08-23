from abc import ABC


class Sensor(ABC):
    def __init__(self):
        self.counter = 0
        self.name = 'generic'

    def metric_data(self) -> tuple[str, int]:
        return self.name, self.counter

    def cleanup(self) -> None:
        pass

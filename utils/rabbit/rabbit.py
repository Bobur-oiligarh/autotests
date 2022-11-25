import pika as pika

from utils.yaml_reader import YAMLReader


class Rabbit:

    def __init__(self):
        self.exchanges = YAMLReader().rabbit[""]

    def _exchanges(self):
        pass

rmq_parameters = pika.URLParameters(YAMLReader().rabbit[""])

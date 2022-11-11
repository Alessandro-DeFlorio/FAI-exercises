import random
from datetime import datetime
import json


class VanillaRandomSelector:
    def __init__(self, path, sep="\n") -> None:
        already_used =  set()
        with open(path, "r") as f:
            self.content = set([l for l in f.read().split(sep)])

    def give_random(self, n):
        return random.sample(list(self.content), min(len(self.content), n))


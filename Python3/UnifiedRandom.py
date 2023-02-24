import hashlib
import time
import math
import warnings

class UnifiedRandom:
    # UnifiedRandom version 1.00
    # by Michal Obara (mobaradev) mobaradev@yahoo.com http://mobaradev.com
    # MIT License

    def __init__(self, seed = ""):
        if seed == "":
            self.seed = str(int(time.time()))
        else:
            self.seed = seed
        self.index = 0
        self._sign_values = {
            '0': (1/16)/2,
            '1': (1/16 + 2/16)/2,
            '2': (2/16 + 3/16)/2,
            '3': (3/16 + 4/16)/2,
            '4': (4/16 + 5/16)/2,
            '5': (5/16 + 6/16)/2,
            '6': (6/16 + 7/16)/2,
            '7': (7/16 + 8/16)/2,
            '8': (8/16 + 9/16)/2,
            '9': (9/16 + 10/16)/2,
            'a': (10/16 + 11/16)/2,
            'b': (11/16 + 12/16)/2,
            'c': (12/16 + 13/16)/2,
            'd': (13/16 + 14/16)/2,
            'e': (14/16 + 15/16)/2,
            'f': (15/16 + 16/16)/2
        }

    def get_value(self):
        to_hash = self.seed + "-" + str(self.index)
        hash = hashlib.sha256(str(to_hash).encode('utf-8')).hexdigest()
        value = 0

        for i in range(0, 8):
            sign = hash[i]
            sign_value = self._sign_values[sign]

            if i == 0:
                value = sign_value
            else:
                delta = 1
                for j in range(0, i):
                    delta = delta/16

                if self._sign_values[hash[15 - i]] < 0.5:
                    value -= sign_value * delta
                else:
                    value += sign_value * delta

                if value < 0:
                    value = 0

                if value > 1:
                    value = 1

        self.index += 1
        return value

    def get_number(self, min, max):
        # verify and, if possible fix types of min and max arguments
        arguments = [min, max]
        for i in range(len(arguments)):
            if not isinstance(arguments[i], int):
                if isinstance(arguments[i], float):
                    if i == 0:
                        min = int(arguments[i])
                    elif i == 1:
                        max = int(arguments[i])
                    warnings.warn("UnifiedRandom warning: arguments of get_number(min, max) are supposed to be integers. Parsed automatically.")
                else:
                    raise TypeError("UnifiedRandom error: wrong type of get_number(min, max) argument(s). Expected: int, received: " + str(type(arguments[i])))

        value = self.get_value()
        intervals = max - min + 1

        return math.floor(intervals * value) + min

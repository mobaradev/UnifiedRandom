import hashlib
import time
import math

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

    def _get_sign_value(self, sign):
        if sign == '0': return (1/16)/2
        if sign == '1': return (1/16 + 2/16)/2
        if sign == '2': return (2/16 + 3/16)/2
        if sign == '3': return (3/16 + 4/16)/2
        if sign == '4': return (4/16 + 5/16)/2
        if sign == '5': return (5/16 + 6/16)/2
        if sign == '6': return (6/16 + 7/16)/2
        if sign == '7': return (7/16 + 8/16)/2
        if sign == '8': return (8/16 + 9/16)/2
        if sign == '9': return (9/16 + 10/16)/2
        if sign == 'a': return (10/16 + 11/16)/2
        if sign == 'b': return (11/16 + 12/16)/2
        if sign == 'c': return (12/16 + 13/16)/2
        if sign == 'd': return (13/16 + 14/16)/2
        if sign == 'e': return (14/16 + 15/16)/2
        if sign == 'f': return (15/16 + 16/16)/2

    def get_value(self):
        to_hash = self.seed + "-" + str(self.index)
        hash = hashlib.sha256(str(to_hash).encode('utf-8')).hexdigest()
        value = 0

        for i in range(0, 8):
            sign = hash[i]
            sign_value = self._get_sign_value(sign)

            if i == 0:
                value = sign_value
            else:
                delta = 1
                for j in range(0, i):
                    delta = delta/16

                if self._get_sign_value(hash[15 - i]) < 0.5:
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
        value = self.get_value()
        intervals = max - min + 1

        return math.floor(intervals * value) + min

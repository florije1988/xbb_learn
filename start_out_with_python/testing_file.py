# -*- coding: utf-8 -*-
__author__ = 'kiwi'
def flip_coin():
        import random
        face = random.randrange(1, 3)

        if face == 1:
            return 'head'
        elif face == 2:
            return 'tail'
        return 'Error'
print flip_coin()
# -*- coding: utf-8 -*-
__author__ = 'kiwi'


class coin:
    def __init__(self):
        self.flip_result = []

    def flip_coin(self):
        import random
        face = random.randrange(1, 3)
        if face == 1:
            return 'head'
        elif face == 2:
            return 'tail'
        return 'Error'

    def flip_times(self, times):
        if True:
            print 'The raw times is :', times
            for i in range(0, times):
                result = coin.flip_coin(self)
                self.flip_result.append(result)
            return self.flip_result
        else:
            return 'Error on Flip_times'





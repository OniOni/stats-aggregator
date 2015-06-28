import statistics

class BaseStatsAggregator(object):

    def __init__(self, length=500):
        self._stats = {}
        self._supports = []
        self._max_length = length

    def add(self, name, init):
        self._stats[name] = {k: init for k in self._supports}
        self._stats[name]['vals'] = [init]

    def cleanup(self):
        if len(self._stats) > self._max_length:
            self._stats = self._stats[len(self._stats) - self._max_length:]

    def update(self, name, val):
        self._stats[name]['vals'].append(val)

        for k in self._stats[name]:
            if k == 'vals':
                continue

            self._stats[name][k] = getattr(self, k)(name, val)

        self.cleanup()

        return self.stats()

    def stats(self):
        return self._stats


class StatsAggregator(BaseStatsAggregator):

    def __init__(self):
        super(StatsAggregator, self).__init__()
        self._supports = ['mean', 'median']

    def __getattr__(self, name):
        if name in self._supports:
            return lambda k, v: getattr(statistics, name)(self._stats[k]['vals'])
        else:
            raise AttributeError

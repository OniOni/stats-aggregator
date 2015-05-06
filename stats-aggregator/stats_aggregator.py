import statistics

class BaseStatsAggregator(object):

    def __init__(self):
        self._stats = {}
        self._supports = []

    def add(self, name, val, **kwargs):
        self._stats[name] = {k: val for k in kwargs if k in self._supports}
        self._stats[name]['vals'] = [val]

    def update(self, name, val):
        self._stats[name]['vals'].append(val)

        for k in self._stats[name]:
            if k == 'vals':
                continue

            self._stats[name][k] = getattr(self, k)(name, val)

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

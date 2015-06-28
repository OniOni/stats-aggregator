import unittest
import statistics

import stats_aggregator

class TestStatsAggregator(unittest.TestCase):

    def setUp(self):
        self.agr = stats_aggregator.StatsAggregator()

    def test_mean_simple(self):
        data_set = [0]
        self.agr.add('test', 0)

        for i in range(10):
            data_set.append(i)
            self.agr.update('test', i)

            self.assertEqual(statistics.mean(data_set),
                             self.agr.stats()['test']['mean'])

    def test_median_simple(self):
        data_set = [0]
        self.agr.add('test', 0)

        for i in range(10):
            data_set.append(i)
            self.agr.update('test', i)

            self.assertEqual(statistics.median(data_set),
                             self.agr.stats()['test']['median'])

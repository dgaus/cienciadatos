import numpy as np
from scipy import stats


TIMESTAMP_FILE_LOCATION = 'tiempos.txt'


class AthleteTester(object):
    def make_independent_samples_t_test_on(self, sample_1, sample_2):
        return stats.ttest_ind(sample_1, sample_2)

    def make_welch_t_test_on(self, sample_1, sample_2):
        return stats.ttest_ind(sample_1, sample_2, equal_var=False)

    def make_related_samples_t_test_on(self, sample_1, sample_2):
        return stats.ttest_rel(sample_1, sample_2)



import numpy as np
from athlete_tester import AthleteTester
from recorded_athlete_times import RecordedAthleteTimes

recorded_athlete_times = RecordedAthleteTimes()
tester = AthleteTester()
times_for_rainy_days = recorded_athlete_times.times_for_rainy_days()
times_for_cloudy_days = recorded_athlete_times.times_for_cloudy_days()
times_for_sunny_days = recorded_athlete_times.times_for_sunny_days()

"""

Test if athletes are slower on rainy days than on sunny days. We check whether the average expected value
differs significantly between those 2 samples. Null hyphotesis: average times are almost equal or identical.
Since the samples have different variances, we use welcher't test.

"""
assert(np.var(times_for_rainy_days) != np.var(times_for_sunny_days))
indep_test = tester.make_welch_t_test_on(times_for_rainy_days, times_for_sunny_days)
print(indep_test)
# Since the p-value is very small (less than 1%), we can reject the null hypothesis.

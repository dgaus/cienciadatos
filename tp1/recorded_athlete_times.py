TIMESTAMP_FILE_LOCATION = 'tiempos_limpiados.txt'
ORIGINAL_TIMESTAMP_FILE_LOCATION = 'tiempos_originales.txt'

import numpy as np


class RecordedAthleteTimes(object):
    def __init__(self):
        # El formato del array de athlete_times es identico al del archivo (pero sin la primera fila)
        self._recorded_athlete_times = np.loadtxt(fname=TIMESTAMP_FILE_LOCATION, skiprows=1)
        self._original_athlete_times = np.loadtxt(fname=ORIGINAL_TIMESTAMP_FILE_LOCATION, skiprows=1)
        # print(self._recorded_athlete_times)

    def times(self):
        return self._recorded_athlete_times

    def times_for_rainy_days(self):
        return self.times()[:, 3]

    def times_for_cloudy_days(self):
        return self.times()[:, 2]

    def times_for_sunny_days(self):
        return self.times()[:, 1]

    def original_times(self):
        return self._original_athlete_times

    def original_times_for_rainy_days(self):
        return self.original_times()[:, 3]

    def original_times_for_cloudy_days(self):
        return self.original_times()[:, 2]

    def original_times_for_sunny_days(self):
        return self.original_times()[:, 1] 
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt  # Graficos
from athlete_tester import AthleteTester
from recorded_athlete_times import RecordedAthleteTimes

recorded_athlete_times = RecordedAthleteTimes()
tester = AthleteTester()
times_for_rainy_days = recorded_athlete_times.times_for_rainy_days()
times_for_cloudy_days = recorded_athlete_times.times_for_cloudy_days()
times_for_sunny_days = recorded_athlete_times.times_for_sunny_days()

"""

Son los atletas son más lentos en dı́as de lluvia que en dı́as soleados? Usando un related t-test (elegimos ese al tener
2 muestras de la misma poblacion), tratamos de rechazar la hipotesis nula de que ambas muestras tienen identicos
valores promedio (esperados).

"""
rel_test = tester.make_related_samples_t_test_on(times_for_rainy_days, times_for_sunny_days)
print("t-statistic: %s, p-value: %s" % (rel_test[0], rel_test[1]))
# Como el p-valor es muy chico (menor a 1%), podemos rechazar la hipotesis nula.
# Como el t-estadistico es positivo y grande, sabemos que la media para los tiempos medidos en dias lluviosos es
# mayor a la media de los tiempos medidos en dias soleados.
# Podemos entonces concluir que los atletas son mas lentos en dias lluviosos que en dias soleados.

# Scatter plot of the data.
colors = ["red", "blue"]
groups = [u"Días Lluviosos", u"Días Soleados"]
x = np.linspace(0, 12, 12)
figure = plt.figure()
subplot = figure.add_subplot(1, 1, 1, facecolor="1.0")
subplot.scatter(x=x, y=times_for_rainy_days, c=colors[0], label=groups[0])
subplot.scatter(x=x, y=times_for_sunny_days, c=colors[1], label=groups[1])
plt.title(u'Distribución de Tiempos Medidos en Días Lluviosos vs Soleados')
plt.legend(loc=2)
plt.show()

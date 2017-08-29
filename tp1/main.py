# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt  # Graficos
from scipy import stats
from athlete_tester import AthleteTester
from recorded_athlete_times import RecordedAthleteTimes


recorded_athlete_times = RecordedAthleteTimes()
tester = AthleteTester()
times_for_rainy_days = recorded_athlete_times.times_for_rainy_days()
times_for_cloudy_days = recorded_athlete_times.times_for_cloudy_days()
times_for_sunny_days = recorded_athlete_times.times_for_sunny_days()

"""

Evaluando si se deben limpiar los datos. Vemos que hay un outlier en el grafico (189)
Por lo que decidimos eliminar esa fila.
"""
original_times_for_rainy_days = recorded_athlete_times.original_times_for_rainy_days()
original_times_for_cloudy_days = recorded_athlete_times.original_times_for_cloudy_days()
original_times_for_sunny_days = recorded_athlete_times.original_times_for_sunny_days()

colors = ["red", "blue", "green"]
groups = [u"Días Lluviosos", u"Días Soleados", u"Días Soleados"]
x = np.linspace(0, 12, 12)
figure = plt.figure()
subplot = figure.add_subplot(1, 1, 1, facecolor="1.0")
subplot.scatter(x=x, y=original_times_for_rainy_days, c=colors[0], label=groups[0])
subplot.scatter(x=x, y=original_times_for_sunny_days, c=colors[1], label=groups[1])
subplot.scatter(x=x, y=original_times_for_cloudy_days, c=colors[2], label=groups[2])
plt.title(u'Distribución de Tiempos Medidos')
plt.legend(loc=2)
plt.show()

"""

Verificamos normalidad de las muestras.

"""

assert stats.shapiro(times_for_sunny_days)[1] > 0.05
assert stats.shapiro(times_for_rainy_days)[1] > 0.05
assert stats.shapiro(times_for_cloudy_days)[1] > 0.05

"""

Son los atletas son más lentos en dı́as de lluvia que en dı́as soleados? Usando un related t-test (elegimos ese al tener
2 muestras de la misma poblacion), tratamos de rechazar la hipotesis nula de que ambas muestras tienen identicos
valores promedio (esperados).

"""
print("Conclusion 1")
rel_test = tester.make_related_samples_t_test_on(times_for_rainy_days, times_for_sunny_days)

print("Test de muestras apareadas. t-statistic: %s, p-value: %s" % (rel_test[0], rel_test[1]))
# Como el p-valor es muy chico (menor a 1%), podemos rechazar la hipotesis nula.
# Como el t-estadistico es positivo y grande, sabemos que la media para los tiempos medidos en dias lluviosos es
# mayor a la media de los tiempos medidos en dias soleados.
# Podemos entonces concluir que los atletas son mas lentos en dias lluviosos que en dias soleados.

# Scatter plot of the data.
colors = ["red", "blue"]
groups = [u"Días Lluviosos", u"Días Soleados"]
x = np.linspace(0, len(times_for_cloudy_days), len(times_for_cloudy_days))
figure = plt.figure()
subplot = figure.add_subplot(1, 1, 1, facecolor="1.0")
subplot.scatter(x=x, y=times_for_rainy_days, c=colors[0], label=groups[0])
subplot.scatter(x=x, y=times_for_sunny_days, c=colors[1], label=groups[1])
plt.title(u'Distribución de Tiempos Medidos en Días Lluviosos vs Soleados')
plt.legend(loc=2)
plt.show()

"""

Conclusion 2

"""
print("Conclusion 2")
rel_test = tester.make_related_samples_t_test_on(times_for_sunny_days, times_for_cloudy_days)
print("Test de muestras apareadas. t-statistic: %s, p-value: %s" % (rel_test[0], rel_test[1]))
wilco = stats.wilcoxon(times_for_sunny_days, times_for_cloudy_days)
print("Test de Wilcoxon. t-statistic: %s, p-value: %s" % (wilco[0], wilco[1]))

colors = ["red"]
groups = [u"Resta entre Días Soleados y Días Nublados"]
x = np.linspace(0, len(times_for_cloudy_days), len(times_for_cloudy_days))
figure = plt.figure()
subplot = figure.add_subplot(1, 1, 1, facecolor="1.0")
resta = times_for_sunny_days - times_for_cloudy_days
subplot.scatter(x=x, y=resta, c=colors[0], label=groups[0])
plt.title(u'Distribución de la Resta')
plt.ylim(-1, 1)
plt.legend(loc=2)
plt.show()

"""

Conclusion 3

"""

fit = np.polyfit(times_for_sunny_days, times_for_cloudy_days, 1)
fit_fn = np.poly1d(fit)
plt.plot(times_for_sunny_days, times_for_cloudy_days, 'yo', times_for_sunny_days, fit_fn(times_for_sunny_days), '--k', times_for_sunny_days, times_for_sunny_days, '-')

plt.show()

pearson_sunny_rainy = stats.pearsonr(times_for_sunny_days, times_for_rainy_days)
print("pearson_sunny_rainy =", pearson_sunny_rainy)

pearson_sunny_cloudy = stats.pearsonr(times_for_sunny_days, times_for_cloudy_days)
print("pearson_sunny_cloudy =", pearson_sunny_cloudy)

pearson_cloudy_rainy = stats.pearsonr(times_for_cloudy_days, times_for_rainy_days)
print("pearson_cloudy_rainy =", pearson_cloudy_rainy)

fit = np.polyfit(times_for_sunny_days, times_for_rainy_days, 1)
fit_fn = np.poly1d(fit)
plt.plot(times_for_sunny_days, times_for_rainy_days, 'yo', times_for_sunny_days, fit_fn(times_for_sunny_days), '--k', times_for_sunny_days, times_for_sunny_days, '-')
plt.show()


"""

Conclusion 4

"""

no_lluvia = np.append(times_for_sunny_days,times_for_cloudy_days)
lluvia = times_for_rainy_days
dif_media_original = np.mean(lluvia) - np.mean(no_lluvia)
diferencias = []

todos = np.append(lluvia, no_lluvia)
for i in range(1000000):
	perm = np.random.permutation(todos)
	lluvia = perm[:len(lluvia)]
	no_lluvia = perm[len(lluvia):]
	diferencias.append(np.mean(lluvia) - np.mean(no_lluvia))

n, bins, patches = plt.hist(diferencias, bins=100)
plt.axvline(x=dif_media_original, ymin=0, color='red', linewidth=2)

print(len([dif for dif in diferencias if dif > dif_media_original]) * 2)
plt.show()

"""

Los datos obtenidos no discriminan si el entrenamiento sirve mas o menos en el caso de lluvia, solo habla de los tiempos
obtenidos. Un consejo seria separar los atletas en dos grupos g1 y g2. A g1 se lo podria entrenar en dias de lluvia (o simulando
un ambiente de lluvia), mientras que a g2 se lo podria entrenar en dias soleados nublados, evaluando la evolucion en el tiempo
del entrenamiento de los atletas tomando alguna variable de interes (por ejemplo masa muscular). 

"""
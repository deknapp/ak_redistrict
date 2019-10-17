import matplotlib.pyplot as plt

OVER_DEVIATION_LABELS = ['HD7', 'HD8', 'SDD', 'HD9', 'HD10', 'SDE', 'HD11', 'HD12', 'SDF']
OVER_DEVIATION_PERCENTAGES = [8.4, 28.7, 18.5, 5.0, 10.9, 7.9, 9.3, 8.4, 7.4]
x_pos = range(len(OVER_DEVIATION_LABELS))

plt.bar(x_pos, OVER_DEVIATION_PERCENTAGES, align='center', alpha=0.5)
plt.xticks(x_pos, OVER_DEVIATION_LABELS)
plt.xlabel('District')
plt.ylabel('Percent Deviation From Ideal')
plt.title('Districts With High Deviation From Ideal - All in MatSu')
plt.savefig('/Users/nknapp/Desktop/akpirg/high_deviation_from_ideal.png')




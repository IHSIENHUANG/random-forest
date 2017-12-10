import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
FEATURES = [ 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat']


y_pos = np.arange(len(FEATURES))
performance = np.arange(22)
for i in range(0,22):
    performance[i] =i
    y_pos[i] = 20-i
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, FEATURES)
plt.ylabel('Usage')
plt.title('Programming language usage')
 
plt.show()

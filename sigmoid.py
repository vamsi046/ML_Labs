# Sigmoid Function or Logistic Function Characteristic

x = np.linspace(-5,+5,200)
y = 1 / (1 + np.exp(-x))

plt.plot(40+x, y)
plt.xlabel('size of tumour')
plt.ylabel('malignant or benign')
plt.show()

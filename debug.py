# Loss weighting: soft_min_snr and snr
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
sigma_data = 0.5
sigma_values = np.linspace(0, 80, 500)

# Define the function
def _weighting_soft_min_snr(sigma, sigma_data):
    return (sigma * sigma_data) ** 2 / (sigma ** 2 + sigma_data ** 2) ** 2

def _weighting_snr(sigma, sigma_data):
    return sigma_data ** 2 / (sigma ** 2 + sigma_data ** 2)

# Compute the function values
y_values = _weighting_soft_min_snr(sigma_values, sigma_data)

# Plot the curve
plt.figure(figsize=(10, 6))
plt.plot(sigma_values, y_values, label=r'$\frac{(\sigma \cdot \sigma_{data})^2}{(\sigma^2 + \sigma_{data}^2)^2}$')
plt.xlabel(r'$\sigma$')
plt.ylabel('Value')
plt.title(r'Curve of $\frac{(\sigma \cdot \sigma_{data})^2}{(\sigma^2 + \sigma_{data}^2)^2}$ with $\sigma_{data} = 0.5$')
plt.legend()
plt.grid(True)
# plt.show()
plt.savefig('vis/weighting/soft_minsnr.png')

# Compute the function values
y_values = _weighting_snr(sigma_values, sigma_data)

# Plot the curve
plt.figure(figsize=(10, 6))
plt.plot(sigma_values, y_values, label=r'$\frac{(\sigma_{data})^2}{(\sigma^2 + \sigma_{data}^2)}$')
plt.xlabel(r'$\sigma$')
plt.ylabel('Value')
plt.title(r'$\frac{(\sigma_{data})^2}{(\sigma^2 + \sigma_{data}^2)}$ with $\sigma_{data} = 0.5$')
plt.legend()
plt.grid(True)
# plt.show()
plt.savefig('vis/weighting/snr.png')



# Visualize curves of c_skip, c_out, c_inimport numpy as np
import matplotlib.pyplot as plt

# Define the parameters
sigma_data = 0.5
sigma_values = np.linspace(0, 80, 500)

# Define the functions
def c_skip(sigma, sigma_data):
    return sigma_data ** 2 / (sigma ** 2 + sigma_data ** 2)

def c_out(sigma, sigma_data):
    return sigma * sigma_data / (sigma ** 2 + sigma_data ** 2) ** 0.5

def c_in(sigma, sigma_data):
    return 1 / (sigma ** 2 + sigma_data ** 2) ** 0.5

# Compute the function values
c_skip_values = c_skip(sigma_values, sigma_data)
c_out_values = c_out(sigma_values, sigma_data)
c_in_values = c_in(sigma_values, sigma_data)

# Plot the curves
plt.figure(figsize=(12, 8))
plt.plot(sigma_values, c_skip_values, label=r'$c_{skip} = \frac{\sigma_{data}^2}{\sigma^2 + \sigma_{data}^2}$')
plt.plot(sigma_values, c_out_values, label=r'$c_{out} = \frac{\sigma \cdot \sigma_{data}}{(\sigma^2 + \sigma_{data}^2)^{0.5}}$')
plt.plot(sigma_values, c_in_values, label=r'$c_{in} = \frac{1}{(\sigma^2 + \sigma_{data}^2)^{0.5}}$')
plt.xlabel(r'$\sigma$')
plt.ylabel('Value')
plt.title('Curves of $c_{skip}$, $c_{out}$, and $c_{in}$ with $\sigma_{data} = 0.5$')
plt.legend()
plt.grid(True)
# plt.show()
import os
os.makedirs('vis/c_skip_out_in', exist_ok=True)
plt.savefig('vis/c_skip_out_in/c_skip_out_in.png')

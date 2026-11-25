import numpy as np

class MultimodalWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Sinusoidal wave component with varying frequencies and amplitudes
        wave = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.3)
            amp = 1.0 + 0.4 * np.cos(i * 0.7)
            wave += amp * np.sin(freq * x_scaled[i] * np.pi) * np.cos(freq * x_scaled[i] * np.pi * 0.5)
        
        # Radial basis function component with multiple centers
        rbf = 0.0
        for i in range(self.dim):
            for j in range(3):  # Three RBF centers per dimension
                center = np.sin(i * 0.5 + j * 1.2) * 0.8
                width = 0.5 + 0.3 * np.cos(i * 0.3 + j * 0.7)
                strength = 1.0 + 0.5 * np.sin(i * 0.4 + j * 0.9)
                rbf += strength * np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Polynomial interaction terms between dimensions
        poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Higher order polynomial interactions
                poly += (x_scaled[i] * x_scaled[j])**3 + (x_scaled[i]**2 + x_scaled[j]**2) * 0.5
                
        # Cross-term sinusoidal patterns creating additional local optima
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(x_scaled[i] * x_scaled[j] * 2.0) * \
                        np.cos((x_scaled[i] + x_scaled[j]) * 1.5) * \
                        np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Global scaling and combination
        return 0.8 * wave + 1.2 * rbf + 0.6 * poly + 0.4 * cross
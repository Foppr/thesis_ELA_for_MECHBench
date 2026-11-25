import numpy as np

class MultimodalOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Sinusoidal oscillation component with varying frequencies and amplitudes
        oscillation = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.3)
            amp = 1.0 + 0.4 * np.cos(i * 0.7)
            oscillation += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 1.5)
        
        # Radial basis function component with multiple centers
        rbf = 0.0
        for i in range(self.dim):
            for j in range(3):  # Three radial centers per dimension
                center = np.sin(i * 0.5 + j * 1.2) * 0.8
                width = 0.5 + 0.3 * np.cos(i * 0.4 + j * 0.8)
                rbf += np.exp(-width * (x_scaled[i] - center)**2)
        
        # Exponential decay terms with position-dependent rates
        decay = 0.0
        for i in range(self.dim):
            rate = 0.5 + 0.3 * np.sin(i * 0.6)
            decay += np.exp(-rate * np.abs(x_scaled[i]))
        
        # Cross-dimensional interaction terms with varying coupling strengths
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = 0.8 + 0.2 * np.sin(i * 0.3 + j * 0.5)
                interaction += coupling * np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * \
                              (1.0 + 0.3 * np.sin(x_scaled[i] + x_scaled[j]))
        
        # Combined function with modified weights
        return 0.8 * oscillation + 0.6 * rbf + 0.4 * decay + 0.5 * interaction
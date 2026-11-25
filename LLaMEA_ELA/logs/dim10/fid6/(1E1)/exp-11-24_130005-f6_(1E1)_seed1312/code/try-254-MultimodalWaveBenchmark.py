import numpy as np

class MultimodalWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Sinusoidal wave component with multiple frequencies and phases
        wave = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(i * 0.3)
            phase = 0.5 * np.cos(i * 0.7)
            wave += np.sin(freq * x_scaled[i] + phase) * np.cos(freq * x_scaled[i] * 0.8 + phase)
        
        # Radial basis function component with multiple centers
        rbf = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.4) * 0.7
            width = 0.3 + 0.2 * np.cos(i * 0.5)
            rbf += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Polynomial interaction terms between dimensions
        poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                poly += (x_scaled[i]**2 + x_scaled[j]**2) * np.sin(x_scaled[i] * x_scaled[j])
        
        # Cross-term interactions with varying weights
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + abs(i - j))
                cross += weight * np.sin(x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] - x_scaled[j])
        
        # High-frequency oscillation component
        high_freq = 0.0
        for i in range(self.dim):
            freq = 10.0 + 5.0 * np.sin(i * 0.2)
            high_freq += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.3)
        
        # Combined function with carefully balanced weights
        return 0.8 * wave + 1.2 * rbf + 0.6 * poly + 0.4 * cross + 0.7 * high_freq
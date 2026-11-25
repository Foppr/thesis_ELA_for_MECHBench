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
            freq = 2.0 + 0.5 * np.sin(i * 0.3)
            amp = 1.0 + 0.4 * np.cos(i * 0.7)
            wave += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.5)
        
        # Radial basis function component with multiple centers
        rbf = 0.0
        num_centers = min(5, self.dim)
        for i in range(num_centers):
            center = np.sin(i * 0.8) * 0.7
            width = 0.5 + 0.3 * np.cos(i * 0.4)
            rbf += np.exp(-width * (x_scaled[i] - center)**2)
        
        # Polynomial interaction terms between dimensions
        poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                poly += (x_scaled[i]**2 + x_scaled[j]**2) * np.sin(x_scaled[i] * x_scaled[j])
        
        # Cross-term interaction with trigonometric modulation
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] - x_scaled[j])
        
        # Asymmetric penalty terms to create non-symmetrical landscape
        penalty = 0.0
        for i in range(self.dim):
            if x_scaled[i] > 0:
                penalty += 0.3 * x_scaled[i]**3
            else:
                penalty += 0.2 * x_scaled[i]**4
        
        # Combine all components with adjusted weights
        return 1.2 * wave + 0.8 * rbf + 0.6 * poly + 0.4 * cross + 0.5 * penalty
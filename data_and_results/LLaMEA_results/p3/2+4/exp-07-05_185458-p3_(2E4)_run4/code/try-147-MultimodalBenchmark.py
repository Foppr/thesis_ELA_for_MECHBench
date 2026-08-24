import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Periodic radial basis functions with varying frequencies and amplitudes
        rb = 0.0
        for i in range(self.dim):
            freq = 2 * np.pi * (i + 1)
            amp = 1.0 + 0.5 * np.sin(i * np.pi / 4.0)
            center = np.cos(i * np.pi / 3.0)
            rb += amp * np.exp(-5 * (x_norm[i] - center)**2) * np.cos(freq * (x_norm[i] - center))
        
        # Cross-dimensional polynomial coupling with varying exponents
        poly = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            poly += (x_norm[i]**3 + 0.5 * x_norm[i]**5) * (x_norm[j]**2 + 0.3 * x_norm[j]**4)
        
        # Chaotic sine coupling with exponential weighting
        chaos = 0.0
        for i in range(self.dim):
            weight = np.exp(-0.5 * x_norm[i]**2)
            freq = 10 * (i + 1) * np.pi
            phase = np.sin(i * np.pi / 5.0)
            chaos += weight * np.sin(freq * x_norm[i] + phase) * np.cos(5 * x_norm[i])
        
        # High-frequency oscillation component
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(30 * x_norm[i]) * np.cos(25 * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2)
        
        # Novel interaction terms with trigonometric coupling
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(x_norm[i] * x_norm[j]) * np.cos(3 * (x_norm[i] + x_norm[j]))
        
        # Quadratic penalty term for global conditioning
        penalty = 0.1 * np.sum(x_norm**2)
        
        # Combine all components with carefully tuned weights
        return 0.8 * rb + 0.6 * poly + 0.5 * chaos + 0.4 * high_freq + 0.3 * interaction + 0.2 * penalty
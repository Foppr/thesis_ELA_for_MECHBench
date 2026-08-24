import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with shifted center placements
        rb = 0.0
        for i in range(self.dim):
            center = np.sin(i * np.pi / 3.0) * 0.8
            rb += np.exp(-10 * (x_norm[i] - center)**2) * np.cos(15 * (x_norm[i] - center))
        
        # Chaotic cosine modulation with varying frequencies and amplitudes
        chaos = 0.0
        for i in range(self.dim):
            freq = 2**(i % 3 + 3) * np.pi
            amp = 0.7 + 0.3 * np.sin(i * np.pi / 2.5)
            chaos += amp * np.cos(freq * x_norm[i] + np.sin(freq * x_norm[i] + 0.6))
        
        # Asymmetric polynomial interactions with cross-dimensional coupling
        poly = 0.0
        for i in range(self.dim):
            poly += (x_norm[i]**3 + 0.5 * x_norm[i]**5 + 0.2 * x_norm[i]**7) * np.cos(x_norm[(i+1) % self.dim])
        
        # Cross-dimensional coupling with sine-based interaction
        cross = 0.0
        for i in range(self.dim - 1):
            cross += np.sin(x_norm[i] * x_norm[i+1]) * (x_norm[i]**2 + x_norm[i+1]**2 + 0.15)
        
        # Additional chaotic interference with exponential weighting
        interference = 0.0
        for i in range(self.dim):
            interference += np.exp(-0.3 * x_norm[i]**2) * np.sin(30 * x_norm[i] + np.cos(15 * x_norm[i]))
        
        # Modified weighting and added sinusoidal modulation for increased complexity
        return 0.5 * rb + 0.7 * chaos + 0.45 * poly + 0.35 * cross + 0.25 * interference + 0.04 * np.sum(x_norm**2) + 0.02 * np.sin(20 * np.sum(x_norm))
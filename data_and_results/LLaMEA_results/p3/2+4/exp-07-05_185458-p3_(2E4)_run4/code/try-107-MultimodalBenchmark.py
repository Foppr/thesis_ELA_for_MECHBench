import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic center placements
        rb = 0.0
        for i in range(self.dim):
            center = np.sin(i * np.pi / 3.0) * 0.9
            rb += np.exp(-12 * (x_norm[i] - center)**2) * np.cos(18 * (x_norm[i] - center))
        
        # Chaotic cosine modulation with varying frequencies and amplitudes
        chaos = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 2) * np.pi
            amp = 0.6 + 0.4 * np.sin(i * np.pi / 4.0)
            chaos += amp * np.cos(freq * x_norm[i] + np.sin(freq * x_norm[i] * 0.5))
        
        # Asymmetric polynomial interactions with cross-dimensional coupling
        poly = 0.0
        for i in range(self.dim):
            poly += (x_norm[i]**3 + 0.4 * x_norm[i]**5 + 0.15 * x_norm[i]**7) * np.cos(x_norm[(i+1) % self.dim] * 1.2)
        
        # Cross-dimensional coupling with sine-based interaction
        cross = 0.0
        for i in range(self.dim - 1):
            cross += np.sin(x_norm[i] * x_norm[i+1] * 0.8) * (x_norm[i]**2 + x_norm[i+1]**2 * 0.5)
        
        # Additional chaotic interference with exponential weighting
        interference = 0.0
        for i in range(self.dim):
            interference += np.exp(-x_norm[i]**2 * 1.5) * np.sin(25 * x_norm[i] + np.cos(12 * x_norm[i]))
        
        # Final combined function with carefully weighted components
        return 0.9 * rb + 0.5 * chaos + 0.35 * poly + 0.35 * cross + 0.25 * interference + 0.12 * np.sum(x_norm**2)
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial basis function component with chaotic center placements and modified weights
        rb = 0.0
        for i in range(self.dim):
            center = np.sin(i * np.pi / 3.0) * 0.9
            weight = 1.0 + 0.5 * np.sin(i * np.pi / 2.0)
            rb += weight * np.exp(-15 * (x_norm[i] - center)**2) * np.cos(20 * (x_norm[i] - center))
        
        # Enhanced chaotic cosine modulation with varying frequencies, amplitudes, and phase shifts
        chaos = 0.0
        for i in range(self.dim):
            freq = 3**(i % 4 + 1) * np.pi
            amp = 0.7 + 0.3 * np.sin(i * np.pi / 4.0)
            phase = 0.5 * np.cos(i * np.pi / 5.0)
            chaos += amp * np.cos(freq * x_norm[i] + phase + np.sin(freq * x_norm[i]))
        
        # Enhanced asymmetric polynomial interactions with cross-dimensional coupling and modified exponents
        poly = 0.0
        for i in range(self.dim):
            poly += (x_norm[i]**4 + 0.4 * x_norm[i]**6 + 0.15 * x_norm[i]**8) * np.cos(x_norm[(i+1) % self.dim]) * np.sin(x_norm[(i+2) % self.dim])
        
        # Enhanced cross-dimensional coupling with sine-based interaction and additional interaction terms
        cross = 0.0
        for i in range(self.dim - 1):
            cross += np.sin(x_norm[i] * x_norm[i+1]) * (x_norm[i]**3 + x_norm[i+1]**3) + 0.5 * np.cos(x_norm[i] + x_norm[i+1])
        
        # Enhanced chaotic interference with exponential weighting and additional sine modulation
        interference = 0.0
        for i in range(self.dim):
            interference += np.exp(-x_norm[i]**2) * np.sin(25 * x_norm[i] + np.cos(15 * x_norm[i])) + 0.3 * np.cos(30 * x_norm[i])
        
        # Additional high-frequency oscillation component
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(50 * x_norm[i]) * np.cos(40 * x_norm[i])
        
        # Final combined function with carefully weighted components
        return 0.85 * rb + 0.75 * chaos + 0.55 * poly + 0.45 * cross + 0.35 * interference + 0.25 * high_freq + 0.15 * np.sum(x_norm**2)
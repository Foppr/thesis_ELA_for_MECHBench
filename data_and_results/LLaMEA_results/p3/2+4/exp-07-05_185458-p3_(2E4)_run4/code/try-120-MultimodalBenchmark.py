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
            center = np.sin(i * np.pi / 2.7) * 0.85
            weight = 1.2 + 0.4 * np.sin(i * np.pi / 3.0)
            rb += weight * np.exp(-20 * (x_norm[i] - center)**2) * np.cos(25 * (x_norm[i] - center))
        
        # Enhanced chaotic cosine modulation with varying frequencies, amplitudes, and phase shifts
        chaos = 0.0
        for i in range(self.dim):
            freq = 4**(i % 5 + 1) * np.pi
            amp = 0.8 + 0.2 * np.sin(i * np.pi / 3.5)
            phase = 0.6 * np.cos(i * np.pi / 4.5)
            chaos += amp * np.cos(freq * x_norm[i] + phase + np.sin(freq * x_norm[i]))
        
        # Enhanced asymmetric polynomial interactions with cross-dimensional coupling and modified exponents
        poly = 0.0
        for i in range(self.dim):
            poly += (x_norm[i]**5 + 0.5 * x_norm[i]**7 + 0.2 * x_norm[i]**9) * np.cos(x_norm[(i+1) % self.dim]) * np.sin(x_norm[(i+3) % self.dim])
        
        # Enhanced cross-dimensional coupling with sine-based interaction and additional interaction terms
        cross = 0.0
        for i in range(self.dim - 1):
            cross += np.sin(x_norm[i] * x_norm[i+1]) * (x_norm[i]**4 + x_norm[i+1]**4) + 0.6 * np.cos(x_norm[i] + x_norm[i+1]) + 0.2 * np.sin(x_norm[i] + x_norm[i+1] + x_norm[(i+2) % self.dim])
        
        # Enhanced chaotic interference with exponential weighting and additional sine modulation
        interference = 0.0
        for i in range(self.dim):
            interference += np.exp(-x_norm[i]**2) * np.sin(30 * x_norm[i] + np.cos(20 * x_norm[i])) + 0.4 * np.cos(35 * x_norm[i])
        
        # Additional high-frequency oscillation component
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(60 * x_norm[i]) * np.cos(50 * x_norm[i])
        
        # Novel cross-dimensional sine coupling term
        novel_coupling = 0.0
        for i in range(self.dim):
            novel_coupling += np.sin(x_norm[i] * np.cos(x_norm[(i+1) % self.dim])) * np.exp(-0.5 * (x_norm[i] - x_norm[(i+2) % self.dim])**2)
        
        # Final combined function with carefully weighted components
        return 1.0 * rb + 0.8 * chaos + 0.6 * poly + 0.5 * cross + 0.4 * interference + 0.3 * high_freq + 0.2 * novel_coupling + 0.1 * np.sum(x_norm**2)
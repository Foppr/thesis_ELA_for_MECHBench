import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.c = np.random.uniform(0.5, 2.0, dim)
        self.d = np.random.uniform(0.1, 0.5, dim)
        self.alpha = np.random.uniform(0.8, 1.2, dim)
        self.beta = np.random.uniform(0.3, 0.7, dim)
        self.gamma = np.random.uniform(0.1, 0.3, dim)
        self.omega = np.random.uniform(1.0, 3.0, dim)
        self.chaotic_sequence = np.sin(np.arange(100) * 0.1) * 0.5 + 0.5
        
    def f(self, x):
        x_norm = x / 5.0
        t = np.sum(x_norm**2) % 1.0
        
        # Chaotic modulation of frequency components
        freq_mod = 1.0 + 0.3 * self.chaotic_sequence[int(t * 100) % len(self.chaotic_sequence)]
        
        # Asymmetric valley terms with chaotic modulation
        valley_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Asymmetric quadratic with chaotic modulation
            valley_term += (self.c[i] * xi**2 + self.d[i] * xi**3) * freq_mod
            
        # Saddle point landscape with time-variant parameters
        saddle_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Time-variant coefficients for saddle behavior
            coeff = self.alpha[i] + self.beta[i] * np.sin(self.omega[i] * t)
            saddle_term += coeff * xi**2 - self.gamma[i] * xi**4
            
        # Cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim - 1):
            xi, xj = x_norm[i], x_norm[i+1]
            coupling = 0.5 + 0.5 * np.sin(2 * np.pi * t + xi + xj)
            cross_term += coupling * xi * xj
            
        # Polynomial and sinusoidal components for multimodality
        poly_term = 0.1 * np.sum(x_norm**4)
        sin_term = 0.2 * np.sum(np.sin(self.omega * x_norm) * np.cos(self.omega * x_norm))
        
        # Time-variant global minimum shift
        shift = 0.1 * np.sin(2 * np.pi * t)
        shift_term = 0.5 * np.sum((x_norm - shift)**2)
        
        # Combine all terms
        return valley_term + saddle_term + cross_term + poly_term + sin_term + shift_term
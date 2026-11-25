import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # High-order polynomial with chaotic cubic terms
        cubic_poly = np.sum(x_norm**3 + 0.3 * np.sin(3.0 * x_norm) * x_norm**2 + 
                           0.1 * np.cos(2.0 * x_norm) * x_norm**4)
        
        # Embedded sinusoidal modulations with varying frequencies and amplitudes
        sin_mod = np.sum(np.sin(5.0 * x_norm) * np.cos(3.0 * x_norm) * 
                        np.exp(-0.5 * x_norm**2) * (1.0 + 0.2 * np.sin(7.0 * x_norm)))
        
        # Cross-dimensional coupling with chaotic phase shifts
        cross_coupling = 0
        for i in range(self.dim - 1):
            cross_coupling += (x_norm[i] * x_norm[i+1] * 
                             np.sin(2.5 * (x_norm[i] + x_norm[i+1])) * 
                             np.exp(-0.3 * (x_norm[i] - x_norm[i+1])**2))
        
        # Multi-scale chaotic attractor with exponential decay
        attractor = np.sum(np.exp(-2.0 * np.abs(x_norm)) * 
                          np.sin(4.0 * np.pi * x_norm) * 
                          np.cos(1.5 * np.pi * x_norm))
        
        # Asymmetric gradient structure with piecewise polynomial
        asym_grad = 0
        for i in range(self.dim):
            if x_norm[i] >= 0:
                asym_grad += x_norm[i]**3.5 * np.exp(-0.2 * x_norm[i]**2)
            else:
                asym_grad += x_norm[i]**2.5 * np.exp(-0.1 * x_norm[i]**2)
        
        # Combined function with adaptive scaling
        result = 1.5 * cubic_poly + 1.0 * sin_mod + 0.8 * cross_coupling + 0.9 * attractor + 0.7 * asym_grad
        
        # Add controlled noise for robustness
        noise = 0.01 * np.random.rand() * (1.0 + 0.2 * np.abs(np.mean(x_norm)))
        
        return result + noise
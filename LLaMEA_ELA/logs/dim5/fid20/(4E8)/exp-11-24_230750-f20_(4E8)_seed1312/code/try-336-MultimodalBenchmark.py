import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric chaos component with varying frequencies
        chaos_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * x[i])
            chaos_term += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.exp(-0.1 * x[i]**2)
        
        # Radial basis function couplings with adaptive widths
        rbf_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                sigma = 0.5 + 0.3 * np.sin(0.4 * x[i])
                rbf_coupling += np.exp(-0.5 * ((x[i] - x[j])**2) / (sigma**2))
        
        # Adaptive conditioning with dimensionally varying parameters
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.8 * np.cos(0.5 * x[i]) * np.sin(0.3 * x[i])
            conditioning += cond_factor * x[i]**2
        
        # Multi-scale periodic interference patterns
        interference = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(0.6 * x[i])
            interference += scale * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Cross-dimensional harmonic coupling with phase modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                phase_mod = 0.3 * np.sin(0.5 * x[i] + 0.4 * x[j])
                coupling += np.sin(0.8 * (x[i] + x[j]) + phase_mod) * np.cos(0.6 * (x[i] - x[j]))
        
        # Saddle-point structure with dynamic modulation
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                modulator = 0.8 + 0.2 * np.cos(0.4 * x[i]) * np.sin(0.6 * x[i+1])
                saddle += (x[i]**3 - x[i+1]**3) * modulator
        
        # Dimensionally adaptive normalization factor
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return (0.25 * chaos_term + 0.20 * rbf_coupling + 0.15 * conditioning + 
                0.20 * interference + 0.15 * coupling + 0.05 * saddle) * dim_factor
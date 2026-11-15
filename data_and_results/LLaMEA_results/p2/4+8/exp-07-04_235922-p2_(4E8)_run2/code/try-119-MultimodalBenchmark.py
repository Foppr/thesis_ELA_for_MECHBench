import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic sine-wave interactions
        for i in range(self.dim):
            xi = x[i]
            # Use chaotic sine modulation with varying frequencies
            chaotic_term = np.sin(13 * xi) * np.cos(17 * xi) * np.sin(19 * xi) + 0.5 * np.cos(23 * xi) * np.sin(29 * xi)
            result += 0.2 * chaotic_term * (xi**2 + 1)
        
        # Radial harmonic potentials
        radial_potential = 0.0
        for i in range(self.dim):
            radial_potential += (x[i]**2 - 4)**2 * np.exp(-0.1 * x[i]**2)
        result += 0.5 * radial_potential
        
        # Multi-resolution frequency modulation
        freq_mod = 0.0
        for i in range(self.dim):
            freq_mod += (np.sin(3 * x[i]) + 0.5 * np.cos(7 * x[i]) + 0.3 * np.sin(11 * x[i])) * np.exp(-0.05 * x[i]**2)
        result += 0.3 * freq_mod
        
        # Add coupling between dimensions with harmonic interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.sin(2 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.01 * (x[i]**2 + x[j]**2))
        result += 0.4 * coupling
        
        # Add dynamic conditioning based on problem dimensionality
        dynamic_cond = 1.0 + 0.2 * np.sin(0.5 * self.dim) * np.cos(0.3 * self.dim)
        result *= dynamic_cond
        
        # Add noise component with exponential decay
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(31 * x[i]) * np.cos(37 * x[i]) * np.exp(-0.02 * x[i]**2)
        result += 0.02 * noise
        
        return result
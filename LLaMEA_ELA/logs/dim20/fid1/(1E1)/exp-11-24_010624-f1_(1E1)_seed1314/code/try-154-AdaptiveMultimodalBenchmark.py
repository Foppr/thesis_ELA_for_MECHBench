import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive parameters for each dimension
        self.freqs = np.array([1.0 + 0.5 * np.sin(i * 0.5) for i in range(dim)])
        self.ampls = np.array([0.8 + 0.2 * np.cos(i * 0.3) for i in range(dim)])
        self.decays = np.array([0.1 + 0.05 * np.sin(i * 0.4) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Sinusoidal wave component with varying frequencies and amplitudes
        for i in range(self.dim):
            result += self.ampls[i] * np.sin(self.freqs[i] * x[i]) * np.cos(self.freqs[i] * x[i])
            
        # Exponential decay term with dimension-specific decay rates
        for i in range(self.dim):
            result += self.decays[i] * np.exp(-0.5 * (x[i] / 2.0)**2)
            
        # Spherical component with global scaling
        sphere_term = np.sum(x**2)
        result += 0.1 * sphere_term
        
        # Cross-dimensional coupling with adaptive weights
        coupling_weight = 0.05
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = coupling_weight * (x[i] - x[j])**2 * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                result += coupling
                
        # Global scaling factor based on distance from origin
        dist_from_origin = np.sqrt(sphere_term)
        global_scale = 1.0 + 0.2 * np.sin(0.5 * dist_from_origin)
        result *= global_scale
        
        # Add a periodic modulation to increase complexity
        periodic_mod = 0.05 * np.sum(np.sin(3 * x) * np.cos(2 * x))
        result += periodic_mod
        
        return result
import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2) * 0.1
        
        # Add chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            amp = 1.0 / (i + 1)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Radial basis function terms that create multiple valleys
        for i in range(1, min(6, self.dim + 1)):
            center = np.linspace(-4, 4, self.dim)[i-1] if self.dim > 1 else 0.0
            sigma = 0.5 * i
            result += np.exp(-0.5 * ((x[i-1] - center) / sigma)**2) * np.sin(3 * x[i-1])
        
        # Asymmetric saddle points with varying steepness
        saddle_term = 0.0
        for i in range(self.dim):
            if i % 2 == 0:
                saddle_term += (x[i]**4 - 2*x[i]**2) * np.cos(x[i])
            else:
                saddle_term += (x[i]**3 - x[i]) * np.sin(x[i])
        
        result += 0.5 * saddle_term
        
        # Cross-dimensional coupling with chaotic interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                cross_coupling += np.sin(diff) * np.cos(diff * 0.7) * (i + j + 1)
        
        result += 0.3 * cross_coupling
        
        # Add a global chaotic modulation
        chaos_factor = np.prod(np.sin(0.3 * x + 1.0))
        result *= (1.0 + 0.2 * chaos_factor**2)
        
        return result
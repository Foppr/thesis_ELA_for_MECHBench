import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with polynomial growth
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * r**4 + 0.3 * r**3 + 0.1 * r**2
        
        # Sinusoidal perturbations in radial direction
        sin_term = np.sin(5.0 * r) * np.cos(3.0 * r) + 0.5 * np.sin(7.0 * r)
        
        # Cross-dimensional coupling with chaotic interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += (x[i] * x[j])**2 * np.sin(0.5 * (x[i] + x[j]))
        
        # Asymmetric basins with exponential decay
        basin_term = 0.0
        for i in range(self.dim):
            basin_term += np.exp(-0.5 * (x[i] - 1.5)**2) + np.exp(-0.5 * (x[i] + 1.5)**2) + 0.3 * np.exp(-0.5 * (x[i] - 3.0)**2)
        
        # Chaotic component with multiple frequencies
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(2.0 * x[i]) * np.cos(4.0 * x[i]) * np.sin(6.0 * x[i])
        
        # Add a global minimum shift
        shift_term = 0.0
        for i in range(self.dim):
            shift_term += (x[i] - 0.5)**4
        
        # Combine all terms
        result = radial_term + sin_term + coupling_term + basin_term + chaotic_term + 0.01 * shift_term
        
        return result
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic terms with varying scales and asymmetry
        result = 0.0
        for i in range(self.dim):
            result += 0.5 * (x[i] - 1.0)**2 + 0.3 * (x[i] + 1.0)**2 + 0.02 * x[i]**4
        
        # Polynomial interaction terms with asymmetric scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric interaction strength based on indices
                interaction_strength = (i + 1) * (j + 1) * np.exp(0.3 * (i + j))
                result += interaction_strength * (x[i] - x[j])**2
        
        # Trigonometric modulations with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 0.4 * np.sin(2.5 * x[i]) * np.cos(1.2 * x[i]) + 0.1 * np.sin(4.0 * x[i])
        
        # Add complex global minimum with high curvature and saddle points
        result += 0.002 * np.sum(x**2) + 0.0005 * np.sum(x**6) + 0.001 * np.sum(np.abs(x)**3)
        
        # Add periodic component with varying phase shifts
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(3.5 * x[i]) * np.cos(1.8 * x[i]) * np.exp(-0.1 * x[i]**2)
        result += 0.15 * periodic_term
        
        # Add asymmetric basin structure
        basin_term = 0.0
        for i in range(self.dim):
            basin_term += (x[i] - 0.5)**4 + (x[i] + 0.5)**3
        result += 0.05 * basin_term
        
        return result
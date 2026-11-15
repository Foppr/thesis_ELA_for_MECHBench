import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial terms with varying degrees
        result = 0.0
        for i in range(self.dim):
            result += (x[i]**2 - 1.0)**2 + 0.1 * x[i]**4 + 0.01 * x[i]**6
        
        # Asymmetric interaction terms with polynomial scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric interaction based on indices
                asymmetry = 1.0 + 0.1 * (i - j)**2
                result += asymmetry * (x[i]**2 - x[j])**2
        
        # Trigonometric modulation with varying frequencies
        for i in range(self.dim):
            result += 0.5 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) + 0.3 * np.sin(5.0 * x[i])
        
        # Add basin structure with exponential decay
        basin_term = 0.0
        for i in range(self.dim):
            basin_term += np.exp(-0.5 * (x[i] - 2.0)**2) + np.exp(-0.5 * (x[i] + 2.0)**2)
        result += 0.2 * basin_term
        
        # Add a global minimum perturbation
        result += 0.001 * np.sum((x - 1.0)**4)
        
        # Add high-frequency oscillation to increase complexity
        freq_term = 0.0
        for i in range(self.dim):
            freq_term += np.sin(10.0 * x[i]) * np.cos(7.0 * x[i])
        result += 0.15 * freq_term
        
        return result
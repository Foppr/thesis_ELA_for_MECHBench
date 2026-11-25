import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial component with exponential decay
        r_squared = np.sum(x**2)
        result = r_squared * np.exp(-r_squared / 20.0)
        
        # Add multi-frequency chaotic oscillations
        for i in range(self.dim):
            result += 1.5 * np.exp(-0.05 * (x[i] - 2.0)**2) * np.sin(4.0 * x[i]) * np.cos(6.0 * x[i]) * np.sin(2.0 * x[i]**2)
        
        # Add radial symmetry with multiple peaks and varying amplitudes
        r = np.sqrt(r_squared)
        result += 0.8 * np.sin(3.0 * r) * np.exp(-r / 4.0) + 0.3 * np.cos(7.0 * r) * np.exp(-r / 2.0)
        
        # Add coupling terms with varying decay rates and interaction strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                result += 0.4 * np.exp(-dist**2) * np.sin(3.0 * (x[i] + x[j])) * np.cos(5.0 * (x[i] - x[j]))
        
        # Add high-frequency noise and nonlinearity
        result += 0.02 * np.sum(np.sin(15.0 * x) * np.cos(12.0 * x))
        
        # Add a small perturbation term to increase conditioning difficulty
        result += 0.005 * np.sum(x**4)
        
        return result
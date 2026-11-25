import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial component with modified exponential decay
        r_squared = np.sum(x**2)
        result = r_squared * np.exp(-r_squared / 15.0)
        
        # Add multi-frequency chaotic oscillations with altered amplitudes
        for i in range(self.dim):
            result += 2.0 * np.exp(-0.1 * (x[i] - 1.5)**2) * np.sin(5.0 * x[i]) * np.cos(7.0 * x[i]) * np.sin(3.0 * x[i]**2)
        
        # Add radial symmetry with more pronounced peaks and varied amplitudes
        r = np.sqrt(r_squared)
        result += 1.0 * np.sin(4.0 * r) * np.exp(-r / 5.0) + 0.5 * np.cos(8.0 * r) * np.exp(-r / 3.0)
        
        # Add coupling terms with stronger interaction and different decay rates
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.05)
                result += 0.6 * np.exp(-dist**2) * np.sin(4.0 * (x[i] + x[j])) * np.cos(6.0 * (x[i] - x[j]))
        
        # Add high-frequency noise with modified coefficients
        result += 0.03 * np.sum(np.sin(20.0 * x) * np.cos(15.0 * x))
        
        # Add a more significant perturbation term to increase conditioning difficulty
        result += 0.01 * np.sum(x**4)
        
        return result
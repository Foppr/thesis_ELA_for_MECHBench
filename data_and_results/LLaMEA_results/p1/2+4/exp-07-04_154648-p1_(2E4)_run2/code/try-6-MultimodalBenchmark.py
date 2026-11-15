import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        result = 0.0
        
        # Quadratic terms with increasing coefficients
        for i in range(self.dim):
            result += (i + 1) * x[i]**2
        
        # Enhanced sinusoidal perturbations with varying frequencies
        for i in range(self.dim):
            result += 0.2 * np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.sin(2 * x[i])
        
        # Radial component to create symmetric local minima
        r_squared = np.sum(x**2)
        result += 0.1 * np.sin(3 * np.sqrt(r_squared)) * np.cos(2 * np.sqrt(r_squared))
        
        # Cross-term interactions with higher nonlinearity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.02 * x[i] * x[j] * np.sin(2 * (x[i]**2 + x[j]**2))
        
        # Additional high-frequency oscillation for increased complexity
        for i in range(self.dim):
            result += 0.05 * np.sin(10 * x[i]) * np.cos(8 * x[i])
        
        return result
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = np.sum(x**2)
        
        # Add multiple local minima using enhanced sinusoidal terms
        for i in range(self.dim):
            result += 0.3 * np.sin(8 * x[i]) * np.cos(5 * x[i]) * np.sin(3 * x[i])
            
        # Add a more complex saddle point structure with higher-order interactions
        if self.dim >= 2:
            for i in range(self.dim - 1):
                result += 0.15 * (x[i]**3 - x[i+1]**3)**2
                
        # Add a radial component with increased complexity
        r = np.sqrt(np.sum(x**2))
        result += 0.2 * np.sin(12 * r) * np.cos(7 * r) * np.sin(4 * r)
        
        # Add cross-terms to increase landscape complexity
        if self.dim >= 3:
            for i in range(self.dim - 2):
                result += 0.05 * x[i] * x[i+1] * x[i+2] * np.sin(x[i]**2 + x[i+1]**2)
                
        return result
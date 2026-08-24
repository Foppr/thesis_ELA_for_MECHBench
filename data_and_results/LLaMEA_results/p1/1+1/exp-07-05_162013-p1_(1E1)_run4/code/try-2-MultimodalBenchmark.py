import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        result = 0.0
        
        # Quadratic terms with modified coefficients
        for i in range(self.dim):
            result += 0.15 * x[i]**2
            
        # Enhanced sinusoidal perturbations with different frequencies
        for i in range(self.dim):
            result += 0.7 * np.sin(3 * np.pi * x[i] / 5.0) + 0.3 * np.sin(0.5 * np.pi * x[i] / 5.0)
            
        # Additional cross-terms with higher-order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * x[i]**2 * x[j]**2 * np.sin(0.3 * np.pi * x[i] / 5.0) * np.sin(0.3 * np.pi * x[j] / 5.0)
                
        # Cubic interaction terms to increase landscape complexity
        for i in range(self.dim):
            result += 0.05 * x[i]**3 * np.sin(2 * np.pi * x[i] / 5.0)
                
        # Global minimum at origin
        return result
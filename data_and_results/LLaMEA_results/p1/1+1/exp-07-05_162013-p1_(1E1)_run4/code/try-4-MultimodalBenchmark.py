import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        result = 0.0
        
        # Quadratic terms with varying coefficients
        for i in range(self.dim):
            result += 0.1 * x[i]**2
            
        # Sinusoidal perturbations with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 0.8 * np.sin(3 * np.pi * x[i] / 5.0) + 0.3 * np.sin(7 * np.pi * x[i] / 5.0)
            
        # Higher-order polynomial terms to increase complexity
        for i in range(self.dim):
            result += 0.02 * x[i]**4 + 0.01 * x[i]**6
            
        # Enhanced cross-terms with multiple sinusoidal components
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term = x[i] * x[j]
                result += 0.1 * cross_term * np.sin(0.3 * np.pi * x[i] / 5.0) * np.sin(0.7 * np.pi * x[j] / 5.0)
                result += 0.05 * cross_term * np.sin(0.5 * np.pi * x[i] / 5.0) * np.sin(0.9 * np.pi * x[j] / 5.0)
                
        # Additional interaction terms for increased landscape complexity
        for i in range(self.dim):
            result += 0.03 * x[i]**3 * np.sin(2 * np.pi * x[i] / 5.0)
            
        # Global minimum at origin
        return result
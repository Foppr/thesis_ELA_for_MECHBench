import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms with varying frequencies
        for i in range(self.dim):
            result += 0.2 * np.sin(7 * x[i]) * np.cos(4 * x[i])
            
        # Add a more complex multimodal component
        for i in range(self.dim):
            result += 0.15 * np.sin(3 * x[i])**2 * np.cos(5 * x[i])
            
        # Add a global minimum at origin with additional penalty terms for conditioning
        result += 0.02 * np.sum(np.abs(x)**4)
        
        # Add interaction terms between dimensions to increase conditioning
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        return result
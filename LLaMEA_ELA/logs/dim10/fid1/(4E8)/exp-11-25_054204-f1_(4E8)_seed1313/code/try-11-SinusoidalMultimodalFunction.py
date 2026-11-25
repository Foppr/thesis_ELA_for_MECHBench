import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin with quadratic basin
        result = np.sum(x**2) * 0.5
        
        # Add highly oscillatory sinusoidal components with varying frequencies
        for i in range(self.dim):
            result += 0.3 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.sin(3 * x[i])
            
        # Add complex interaction terms between dimensions with multiple frequencies
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for complexity
                result += 0.2 * np.sin(2 * x[i] + 3 * x[j]) * np.cos(5 * x[i] - 2 * x[j]) * np.sin(x[i] * x[j])
                
        # Add higher-order interaction terms for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, min(j+3, self.dim)):
                    result += 0.1 * np.cos(x[i] + x[j] + x[k]) * np.sin(2 * x[i] * x[j])
                    
        # Add a small noise component to further complicate the landscape
        result += 0.05 * np.random.uniform(-1, 1) * np.sum(np.abs(x))
        
        return result
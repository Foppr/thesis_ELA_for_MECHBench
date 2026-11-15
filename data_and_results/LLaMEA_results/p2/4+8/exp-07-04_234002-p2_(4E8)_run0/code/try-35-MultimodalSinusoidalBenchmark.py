import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function with enhanced sinusoidal components
        result = 0.0
        
        # Main sinusoidal contribution with enhanced frequencies and cubic terms
        for i in range(self.dim):
            result += 1.1 * np.sin(1.5 * x[i]) * np.cos(0.7 * x[i]) + 0.25 * x[i]**3 + 0.02 * x[i]**4
            
        # Add interaction terms between dimensions with stronger coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.06 * np.sin(2.0 * x[i]) * np.sin(1.2 * x[j]) + 0.02 * x[i]**2 * x[j]**2
                
        # Add a global scaling factor with higher-order polynomial terms
        x_squared = np.sum(x**2)
        x_fourth = np.sum(x**4)
        x_sixth = np.sum(x**6)
        result = result * (1.0 + 0.3 * x_squared + 0.1 * x_fourth + 0.05 * x_sixth)
        
        # Add a small Gaussian noise term to increase landscape complexity
        noise = 0.001 * np.sum(np.exp(-0.5 * (x / 0.5)**2))
        result += noise
        
        return result
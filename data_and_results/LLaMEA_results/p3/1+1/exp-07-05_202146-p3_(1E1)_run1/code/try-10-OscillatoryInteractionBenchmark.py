import numpy as np

class OscillatoryInteractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term
        result = np.sum(x**2)
        
        # Add exponential interaction terms
        for i in range(self.dim):
            result += 0.3 * np.exp(-0.5 * x[i]**2) * np.sin(3 * x[i])
            
        # Add trigonometric coupling between variables
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                result += 0.2 * coupling * (1 + 0.1 * (x[i]**2 + x[j]**2))
                
        # Add higher-order polynomial chaos with exponential scaling
        for i in range(self.dim):
            result += 0.05 * np.exp(x[i]) + 0.02 * np.exp(2 * x[i]) + 0.01 * np.exp(3 * x[i])
            
        # Add a global minimum enforcing term with logarithmic scaling
        result += 0.005 * np.sum(np.log(1 + np.abs(x)**3))
        
        # Add a complex oscillatory component that depends on all variables
        sum_x = np.sum(x)
        result += 0.5 * np.sin(5 * np.pi * sum_x) * np.cos(4 * np.pi * sum_x) * np.exp(-0.1 * sum_x**2)
        
        # Add a non-separable interaction term that creates multiple local minima
        product_x = np.prod(x)
        result += 0.1 * np.sin(10 * product_x) * np.cos(5 * product_x)
        
        return result
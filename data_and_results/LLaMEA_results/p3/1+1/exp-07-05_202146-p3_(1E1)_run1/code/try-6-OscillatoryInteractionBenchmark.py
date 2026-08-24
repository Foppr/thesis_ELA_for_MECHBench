import numpy as np

class OscillatoryInteractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term
        result = np.sum(x**2)
        
        # Add periodic sinusoidal components with varying frequencies
        for i in range(self.dim):
            freq = 2 ** (i % 3 + 1)
            result += 0.5 * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Add interaction terms with polynomial scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i] * x[j])**2 + (x[i] + x[j])**2
                result += 0.1 * interaction * np.sin(x[i] * x[j])
                
        # Add higher-order polynomial chaos
        for i in range(self.dim):
            result += 0.02 * x[i]**4 + 0.01 * x[i]**5 + 0.005 * x[i]**6
            
        # Add a global minimum enforcing term
        result += 0.001 * np.sum(np.abs(x)**7)
        
        # Add a complex oscillatory component that depends on all variables
        sum_x = np.sum(x)
        result += 0.3 * np.sin(2 * np.pi * sum_x) * np.cos(3 * np.pi * sum_x)
        
        return result
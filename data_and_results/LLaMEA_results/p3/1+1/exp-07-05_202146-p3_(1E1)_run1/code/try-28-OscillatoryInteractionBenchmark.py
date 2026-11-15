import numpy as np

class OscillatoryInteractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term
        result = np.sum(x**2)
        
        # Add stronger periodic sinusoidal components with varying frequencies
        for i in range(self.dim):
            freq = 2 ** (i % 4 + 1)
            result += 0.7 * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Add interaction terms with polynomial scaling and increased weight
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i] * x[j])**2 + (x[i] + x[j])**2
                result += 0.2 * interaction * np.sin(x[i] * x[j])
                
        # Add higher-order polynomial chaos with modified coefficients
        for i in range(self.dim):
            result += 0.03 * x[i]**4 + 0.015 * x[i]**5 + 0.008 * x[i]**6
            
        # Add a global minimum enforcing term with different power
        result += 0.002 * np.sum(np.abs(x)**8)
        
        # Add a complex oscillatory component that depends on all variables with modified parameters
        sum_x = np.sum(x)
        result += 0.4 * np.sin(3 * np.pi * sum_x) * np.cos(2 * np.pi * sum_x)
        
        # Add a cross-term interaction that enhances non-separability
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x[i] * x[j] * np.sin(x[i] + x[j])
        result += 0.15 * cross_term
        
        return result
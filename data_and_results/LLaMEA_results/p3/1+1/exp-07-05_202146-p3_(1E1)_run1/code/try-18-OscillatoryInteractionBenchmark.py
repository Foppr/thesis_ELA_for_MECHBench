import numpy as np

class OscillatoryInteractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term
        result = np.sum(x**2)
        
        # Add periodic sinusoidal components with modified frequencies
        for i in range(self.dim):
            freq = 2 ** (i % 4 + 2)  # Slightly higher base frequencies
            result += 0.3 * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Add interaction terms with modified scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i] * x[j])**2 + (x[i] + x[j])**2
                result += 0.15 * interaction * np.sin(x[i] * x[j] * 0.5)  # Reduced frequency
                
        # Add higher-order polynomial chaos with modified coefficients
        for i in range(self.dim):
            result += 0.01 * x[i]**4 + 0.008 * x[i]**5 + 0.003 * x[i]**6
            
        # Add a global minimum enforcing term with different exponent
        result += 0.002 * np.sum(np.abs(x)**8)
        
        # Add a complex oscillatory component with different structure
        sum_x = np.sum(x)
        result += 0.2 * np.sin(3 * np.pi * sum_x) * np.cos(2 * np.pi * sum_x)
        
        return result
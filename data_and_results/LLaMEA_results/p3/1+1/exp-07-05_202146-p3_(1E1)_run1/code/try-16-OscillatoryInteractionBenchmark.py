import numpy as np

class OscillatoryInteractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term with slight modification
        result = 0.8 * np.sum(x**2)
        
        # Enhanced periodic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2 ** (i % 4 + 1)
            amp = 0.7 + 0.3 * np.sin(i * np.pi / 4)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Stronger interaction terms with higher-order polynomial scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i] * x[j])**3 + (x[i] + x[j])**3
                result += 0.2 * interaction * np.sin(x[i] * x[j] * 0.5)
                
        # Modified higher-order polynomial chaos with different exponents
        for i in range(self.dim):
            result += 0.01 * x[i]**4 + 0.008 * x[i]**5 + 0.003 * x[i]**6
            
        # Adjusted global minimum enforcing term
        result += 0.002 * np.sum(np.abs(x)**8)
        
        # Enhanced complex oscillatory component that depends on all variables
        sum_x = np.sum(x)
        result += 0.4 * np.sin(2 * np.pi * sum_x) * np.cos(3 * np.pi * sum_x) * np.exp(-0.1 * np.abs(sum_x))
        
        # Add a new cross-term interaction that emphasizes dimensionality
        if self.dim > 1:
            cross_term = np.prod(np.sin(x))
            result += 0.15 * cross_term
            
        return result
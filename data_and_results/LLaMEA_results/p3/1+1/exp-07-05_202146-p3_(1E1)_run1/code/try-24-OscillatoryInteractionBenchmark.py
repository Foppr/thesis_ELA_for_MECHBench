import numpy as np

class OscillatoryInteractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term
        result = np.sum(x**2)
        
        # Add exponential sinusoidal components with varying frequencies
        for i in range(self.dim):
            freq = 2 ** (i % 4 + 1)
            result += 0.7 * np.exp(-0.1 * x[i]**2) * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Add interaction terms with exponential scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.exp(0.1 * x[i] * x[j]) * (x[i]**2 + x[j]**2)
                result += 0.15 * interaction * np.sin(x[i] + x[j])
                
        # Add higher-order polynomial chaos with variable coefficients
        for i in range(self.dim):
            result += 0.03 * x[i]**4 + 0.02 * x[i]**5 + 0.01 * x[i]**6 + 0.005 * x[i]**7
            
        # Add a global minimum enforcing term with non-uniform scaling
        result += 0.002 * np.sum(np.abs(x)**8)
        
        # Add a complex oscillatory component that depends on all variables with exponential decay
        sum_x = np.sum(x)
        result += 0.4 * np.sin(3 * np.pi * sum_x) * np.cos(4 * np.pi * sum_x) * np.exp(-0.05 * sum_x**2)
        
        # Add a highly multimodal term with multiple local minima
        for i in range(self.dim):
            result += 0.2 * np.sin(10 * x[i]) * np.cos(5 * x[i]) + 0.1 * np.sin(15 * x[i])
            
        return result
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add trigonometric components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.25 * np.sin(6 * x[i]) * np.cos(4 * x[i]) + 0.12 * np.sin(2.5 * x[i])**2
        
        # Add exponential interactions between variables with modified scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.07 * np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(5 * (x[i] + x[j]))
        
        # Add higher-order polynomial terms with sinusoidal modulation using different exponents
        for i in range(self.dim):
            f_val += 0.03 * (x[i]**6) * np.cos(2.5 * x[i]) + 0.04 * (x[i]**4) * np.sin(1.5 * x[i])
        
        # Add shifted and scaled sinusoidal components to increase local optima density
        for i in range(self.dim):
            f_val += 0.18 * np.exp(-0.15 * (x[i] - 1.5)**2) * np.sin(8 * (x[i] + 1.2))
        
        # Add a global scaling factor based on the sum of absolute values with altered multiplier
        f_val += 0.015 * np.sum(np.abs(x)) * np.sin(0.6 * np.sum(x**2))
        
        return f_val
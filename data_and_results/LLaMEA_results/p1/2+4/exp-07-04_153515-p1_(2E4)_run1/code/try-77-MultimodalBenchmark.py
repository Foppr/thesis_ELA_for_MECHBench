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
            f_val += 0.2 * np.sin(5 * x[i]) * np.cos(3 * x[i]) + 0.1 * np.sin(2 * x[i])**2
        
        # Add enhanced exponential interactions between variables
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.09 * np.exp(-0.35 * (x[i] - x[j])**2) * np.sin(5.5 * (x[i] + x[j]))
        
        # Add higher-order polynomial terms with sinusoidal modulation
        for i in range(self.dim):
            f_val += 0.035 * (x[i]**5) * np.cos(2.2 * x[i]) + 0.045 * (x[i]**3) * np.sin(1.1 * x[i])
        
        # Add shifted and scaled sinusoidal components to increase local optima density
        for i in range(self.dim):
            f_val += 0.21 * np.exp(-0.16 * (x[i] - 2.1)**2) * np.sin(8.2 * (x[i] + 1.1))
        
        # Add a global scaling factor based on the sum of absolute values
        f_val += 0.016 * np.sum(np.abs(x)) * np.sin(0.65 * np.sum(x**2))
        
        return f_val
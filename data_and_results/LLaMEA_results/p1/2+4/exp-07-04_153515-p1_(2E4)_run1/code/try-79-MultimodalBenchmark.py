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
            f_val += 0.3 * np.sin(7 * x[i]) * np.cos(4 * x[i]) + 0.15 * np.sin(3 * x[i])**2
        
        # Add enhanced exponential interactions between variables with stronger coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.12 * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(7 * (x[i] + x[j]))
        
        # Add higher-order polynomial terms with sinusoidal modulation
        for i in range(self.dim):
            f_val += 0.05 * (x[i]**6) * np.cos(3 * x[i]) + 0.06 * (x[i]**4) * np.sin(2 * x[i])
        
        # Add shifted and scaled sinusoidal components to increase local optima density
        for i in range(self.dim):
            f_val += 0.3 * np.exp(-0.2 * (x[i] - 2.5)**2) * np.sin(10 * (x[i] + 1.5))
        
        # Add a global scaling factor based on the sum of absolute values with increased complexity
        f_val += 0.02 * np.sum(np.abs(x)) * np.sin(0.8 * np.sum(x**2)) + 0.01 * np.sum(x**3) * np.cos(0.5 * np.sum(x**2))
        
        # Add cross-dimensional exponential interactions
        f_val += 0.08 * np.exp(-0.2 * np.sum((x - 1.0)**2)) * np.sin(6 * np.sum(x))
        
        # Add a multi-modal sinusoidal component across all dimensions
        f_val += 0.1 * np.sin(12 * np.sum(x)) * np.cos(8 * np.sum(x**2))
        
        return f_val
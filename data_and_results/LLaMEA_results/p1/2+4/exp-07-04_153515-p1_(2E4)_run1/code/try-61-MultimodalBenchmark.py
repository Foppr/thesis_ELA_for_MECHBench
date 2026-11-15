import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add complex trigonometric components with higher frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.3 * np.sin(7 * x[i]) * np.cos(4 * x[i]) + 0.2 * np.sin(3 * x[i])**3 + 0.1 * np.cos(5 * x[i])
        
        # Add stronger exponential interactions between variables
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(6 * (x[i] + x[j])) + 0.05 * np.exp(-0.2 * (x[i] + x[j])**2) * np.cos(3 * (x[i] - x[j]))
        
        # Add higher-order polynomial terms with more complex sinusoidal modulation
        for i in range(self.dim):
            f_val += 0.05 * (x[i]**6) * np.cos(3 * x[i]) + 0.04 * (x[i]**4) * np.sin(2 * x[i]) + 0.03 * (x[i]**2) * np.cos(4 * x[i])
        
        # Add multiple shifted and scaled sinusoidal components to increase local optima density
        for i in range(self.dim):
            f_val += 0.2 * np.exp(-0.15 * (x[i] - 2.5)**2) * np.sin(8 * (x[i] + 1.5)) + 0.1 * np.exp(-0.1 * (x[i] + 2.0)**2) * np.cos(6 * (x[i] - 1.0))
        
        # Add a global scaling factor based on the sum of absolute values and a complex interaction term
        f_val += 0.02 * np.sum(np.abs(x)) * np.sin(0.7 * np.sum(x**2)) + 0.01 * np.sum(x**3) * np.cos(0.3 * np.sum(x**2))
        
        # Add a chaotic-like component with nested sinusoids
        for i in range(self.dim):
            f_val += 0.08 * np.sin(10 * np.sin(5 * x[i])) * np.cos(8 * np.cos(3 * x[i]))
        
        return f_val
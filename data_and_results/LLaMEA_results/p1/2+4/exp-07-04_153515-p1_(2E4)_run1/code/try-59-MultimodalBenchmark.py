import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base function
        f_val = np.sum(x**2)
        
        # Add stronger periodic components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.3 * np.sin(6 * x[i]) * np.cos(4 * x[i]) + 0.15 * np.sin(3 * x[i])**2
        
        # Introduce more complex exponential interactions between variables
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.08 * np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(5 * (x[i] + x[j]))
        
        # Add higher-order polynomial terms with sinusoidal modulation
        for i in range(self.dim):
            f_val += 0.03 * (x[i]**5) * np.cos(3 * x[i]) + 0.02 * (x[i]**3) * np.sin(4 * x[i])
        
        # Incorporate shifted exponential terms to generate multiple local minima
        for i in range(self.dim):
            f_val += 0.15 * np.exp(-0.4 * (x[i] - 2.0)**2) * np.sin(5 * (x[i] - 2.0))
        
        # Add cross-terms to increase landscape complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.04 * np.sin(2 * x[i]) * np.cos(2 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        return f_val
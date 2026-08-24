import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base function
        f_val = np.sum(x**2)
        
        # Add chaotic periodic components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.3 * np.sin(7 * x[i]) * np.cos(5 * x[i]) * np.sin(3 * x[i]) + 0.15 * np.sin(4 * x[i])**3
        
        # Introduce chaotic exponential interactions between variables to create rugged landscape
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.exp(-0.2 * (x[i] - x[j])**2) * np.sin(6 * (x[i] + x[j])) * np.cos(2 * (x[i] - x[j]))
        
        # Add higher-order polynomial terms with chaotic sinusoidal modulation
        for i in range(self.dim):
            f_val += 0.03 * (x[i]**6) * np.cos(3 * x[i]) + 0.02 * (x[i]**4) * np.sin(5 * x[i])
        
        # Incorporate multiple shifted exponential terms to generate dense local minima
        for i in range(self.dim):
            f_val += 0.15 * np.exp(-0.4 * (x[i] - 1.5)**2) * np.sin(5 * (x[i] - 1.5)) + \
                     0.1 * np.exp(-0.3 * (x[i] + 2.0)**2) * np.cos(4 * (x[i] + 2.0))
        
        # Add saddle-point structure via cross-terms
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                f_val += 0.05 * (x[i]**2) * (x[j]**2) * np.sin(2 * (x[i] + x[j]))
        
        # Add a chaotic noise term to increase non-smoothness
        noise = np.sum(0.02 * np.sin(10 * x) * np.cos(8 * x))
        f_val += noise
        
        return f_val
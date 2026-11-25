import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Add radial basis functions with varying centers and widths
        for i in range(self.dim):
            center = 2.0 * np.sin(i * 0.5)
            width = 0.5 + 0.3 * np.cos(i * 0.3)
            f += 2.0 * np.exp(-width * (x[i] - center)**2) * np.sin(3 * x[i])
            
        # Add asymmetric cross-dimensional interactions
        for i in range(self.dim):
            j = (i + 1) % self.dim
            f += 0.5 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
            
        # Add periodic terms with different frequencies and phases
        for i in range(self.dim):
            f += 0.3 * np.sin(2 * np.pi * x[i] / 3.0) * np.cos(4 * np.pi * x[i] / 5.0) + 0.2 * np.sin(6 * x[i])
            
        # Add coupled sinusoidal terms with varying coupling strengths
        for i in range(self.dim):
            f += 0.4 * np.sin(x[i]) * np.cos(2 * x[(i + 1) % self.dim]) * (1 + 0.1 * np.sin(3 * x[i]))
            
        # Add a set of shifted local minima using Gaussian peaks
        for i in range(self.dim):
            f += 0.6 * np.exp(-0.5 * ((x[i] - 1.5)**2 + (x[(i+1)%self.dim] + 1.0)**2)) * np.cos(2 * x[i])
            
        # Add higher-order polynomial interactions
        for i in range(self.dim):
            f += 0.1 * x[i]**4 + 0.05 * x[i]**6
            
        # Add a final chaotic component with exponential decay
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(10 * x[i]) * np.cos(7 * x[(i+2)%self.dim]) * np.exp(-0.05 * x[i]**2)
        f += 0.3 * chaos_term
        
        return f
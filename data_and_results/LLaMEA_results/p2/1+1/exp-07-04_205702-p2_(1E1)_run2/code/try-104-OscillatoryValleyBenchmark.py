import numpy as np

class OscillatoryValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.1 * np.sum(x**2)
        
        # Multiple oscillatory components with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            f2 += np.sin(2.0 * np.pi * x[i]) * np.cos(0.5 * np.pi * x[i])
        
        # Asymmetric valley structure with exponential decay
        f3 = 0.0
        for i in range(self.dim):
            f3 += np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(3.0 * x[i])
        
        # Cross-dimensional interaction terms with varying weights
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f4 += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
        
        # Dynamic scaling based on dimensionality
        dynamic_scale = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Add a global modulating function that changes with dimensionality
        f5 = dynamic_scale * np.prod(np.sin(0.3 * x + 1.0))
        
        # Introduce a noise component that scales with dimensionality
        noise = 0.01 * np.random.rand() * self.dim
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + noise
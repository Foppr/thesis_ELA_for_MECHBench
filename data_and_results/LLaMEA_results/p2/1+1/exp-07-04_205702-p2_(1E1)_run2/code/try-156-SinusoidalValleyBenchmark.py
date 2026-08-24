import numpy as np

class SinusoidalValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global attraction
        f1 = 0.3 * np.sum(x**2)
        
        # Add periodic sinusoidal components to create multiple local minima
        f2 = 0.0
        for i in range(self.dim):
            f2 += np.sin(2.0 * x[i]) * np.cos(0.5 * x[i]) + 0.5 * np.sin(3.0 * x[i])
        
        # Introduce asymmetric valley structure with exponential decay
        f3 = 0.0
        for i in range(self.dim):
            f3 += np.exp(-0.1 * (x[i] - 2.0)**2) * np.sin(1.5 * x[i]) + \
                  np.exp(-0.05 * (x[i] + 2.0)**2) * np.cos(1.0 * x[i])
        
        # Add cross-dimensional interaction terms with varying weights
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f4 += 0.2 * np.sin(x[i] + x[j]) * np.cos(0.3 * x[i] * x[j]) + \
                      0.1 * np.sin(0.5 * x[i] * x[j]) * np.cos(x[i] + x[j])
        
        # Introduce a non-convex component with saddle-like behavior
        f5 = 0.0
        for i in range(self.dim):
            f5 += x[i]**4 - 2.0 * x[i]**2 + 0.5 * x[i]
        
        # Add a component that increases complexity with dimensionality
        f6 = 0.0
        for i in range(self.dim):
            f6 += 0.3 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[i]) * (i + 1)
        
        # Add a noise term to increase robustness
        noise = 0.01 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + noise
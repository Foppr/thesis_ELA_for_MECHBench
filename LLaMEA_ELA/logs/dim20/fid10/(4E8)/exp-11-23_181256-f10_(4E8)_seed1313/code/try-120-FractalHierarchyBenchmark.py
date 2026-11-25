import numpy as np

class FractalHierarchyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial base with varying degrees for multi-scale structure
        poly = np.sum(x_norm**2 + 0.3 * x_norm**4 + 0.05 * x_norm**6)
        
        # Trigonometric component with fractal-like frequency scaling
        trig = np.sum(np.sin(2**np.arange(self.dim) * np.pi * x_norm) + 
                     0.5 * np.cos(2**np.arange(self.dim) * np.pi * x_norm))
        
        # Logarithmic barrier term creating varying conditioning
        log_barrier = np.sum(np.log(1 + 0.1 * x_norm**2) + 
                           0.3 * np.log(1 + 0.05 * np.abs(x_norm)))
        
        # Hierarchical coupling with exponentially weighted interactions
        hierarchical = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.1 * (i - j)**2)
                hierarchical += weight * np.sin(x_norm[i] * x_norm[j])
        
        # Fractal dimensionality scaling term
        fractal = np.sum(np.abs(x_norm)**(1.5 + 0.5 * np.sin(np.pi * x_norm)))
        
        # Combined function with multi-scale complexity and varying curvature
        return 1.2 * poly + 0.8 * trig + 0.6 * log_barrier + 0.4 * hierarchical + 0.3 * fractal
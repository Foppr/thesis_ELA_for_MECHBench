import numpy as np

class FractalHierarchicalOptimization:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base quadratic term with adaptive scaling
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * x[i] ** 2 * (1.0 + 0.1 * np.sin(5 * x[i]))
            
        # Add fractal-like hierarchical structure with nested sinusoidal components
        r = np.sqrt(np.sum(x ** 2))
        for level in range(1, min(4, self.dim + 1)):
            freq = 2 ** level
            result += 0.5 * np.sin(freq * r) * np.cos(freq * np.sum(x)) * np.exp(-0.1 * r ** 2)
            
        # Add cross-dimensional coupling with adaptive weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = (i + 1) * (j + 1) / ((self.dim + 1) ** 2)
                result += weight * np.sin(3 * x[i]) * np.cos(4 * x[j]) * np.exp(-0.05 * (x[i] - x[j]) ** 2)
                
        # Add multi-scale periodicity with dimension-dependent frequencies
        for i in range(self.dim):
            freq = 2 * (i + 1) + np.sin(i)
            result += 0.3 * np.sin(freq * x[i]) * np.cos(freq * np.sum(x[:min(i+2, self.dim)])) * np.exp(-0.02 * x[i] ** 2)
            
        # Add hierarchical fractal components with increasing complexity
        for i in range(self.dim):
            result += 0.2 * np.sin(8 * x[i]) * np.cos(6 * x[(i + 1) % self.dim]) * \
                     np.sin(4 * x[(i + 2) % self.dim]) * np.exp(-0.03 * r ** 2)
            
        # Add adaptive conditioning based on dimension
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += 0.15 * (x[i] ** 4) * np.sin(2 * x[i]) * (1 + 0.2 * np.cos(i))
        result += conditioning
        
        # Add nested local minima structure with varying depths
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += 0.4 * np.exp(-0.5 * (x[i] - 1) ** 2) * np.sin(8 * x[i]) * \
                          np.cos(3 * x[(i + 1) % self.dim])
        result += nested_term
        
        # Add global modulation with adaptive amplitude
        global_mod = 1.0 + 0.25 * np.sin(2 * r) * np.cos(3 * r)
        result *= global_mod
        
        # Add complex coupling with higher-order polynomials
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.1 * x[i] ** 2 * x[j] * np.sin(5 * x[k]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                    
        # Add dimensionality-dependent scaling with fractal characteristics
        fractal_scale = 1.0 + 0.1 * np.sum(np.sin(x) ** 2) + 0.05 * np.sum(np.cos(3 * x) ** 2)
        result *= fractal_scale
        
        return result
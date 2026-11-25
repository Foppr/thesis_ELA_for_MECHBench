import numpy as np

class ChaoticNestedValleys:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Quadratic base with exponential condition number variation
        result = 0.0
        for i in range(self.dim):
            result += (10 ** (3 * i / (self.dim - 1))) * (x[i] ** 2)
            
        # Add chaotic trigonometric modulations with altered frequencies
        for i in range(self.dim):
            result += 0.7 * np.sin(9 * x[i]) * np.cos(13 * x[(i + 1) % self.dim]) * np.tan(0.4 * x[i])
            
        # Radial basis function components with modified fractal-like peaks
        for i in range(self.dim):
            r = np.sqrt(np.sum(x ** 2))
            result += 0.5 * np.exp(-0.2 * (x[i] - r) ** 2) * np.sin(4 * np.pi * r) * np.cos(3 * np.pi * r)
            
        # Add coupling terms with modified chaotic interaction patterns
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.15 * (x[i] ** 2 + x[j] ** 2)) * np.sin(6 * x[i]) * np.cos(8 * x[j])
                result += coupling * np.tan(0.2 * x[i]) * np.sin(0.3 * x[j])
                
        # Add modified quartic and quintic polynomial terms for increased local complexity
        for i in range(self.dim):
            result += 0.12 * (x[i] ** 4) * np.cos(4 * x[i]) + 0.03 * (x[i] ** 5) * np.sin(3 * x[i])
            
        # Add nested chaotic radial component with multiple frequencies
        r = np.sqrt(np.sum(x ** 2))
        result += 0.3 * np.sin(17 * r) * np.cos(9 * r) * np.exp(-0.15 * r)
        
        # Add enhanced chaotic saddle points with sinusoidal perturbations
        for i in range(self.dim):
            result += 0.25 * np.sin(3 * x[i]) * np.cos(4 * x[(i + 2) % self.dim]) * np.tan(0.6 * x[i])
            
        # Add a normalization factor with modified chaotic scaling
        result /= (1.0 + 0.08 * np.sum(x ** 2) + 0.03 * np.sum(np.sin(x) ** 2))
        
        return result
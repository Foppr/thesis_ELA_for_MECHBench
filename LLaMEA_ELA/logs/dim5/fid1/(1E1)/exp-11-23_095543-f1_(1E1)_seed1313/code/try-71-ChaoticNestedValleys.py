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
            
        # Add chaotic trigonometric modulations
        for i in range(self.dim):
            result += 0.8 * np.sin(7 * x[i]) * np.cos(11 * x[(i + 1) % self.dim]) * np.tan(0.5 * x[i])
            
        # Radial basis function components with fractal-like peaks
        for i in range(self.dim):
            r = np.sqrt(np.sum(x ** 2))
            result += 0.6 * np.exp(-0.3 * (x[i] - r) ** 2) * np.sin(3 * np.pi * r) * np.cos(2 * np.pi * r)
            
        # Add coupling terms with chaotic interaction patterns
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.1 * (x[i] ** 2 + x[j] ** 2)) * np.sin(5 * x[i]) * np.cos(7 * x[j])
                result += coupling * np.tan(0.3 * x[i]) * np.sin(0.4 * x[j])
                
        # Add quartic and quintic polynomial terms for increased local complexity
        for i in range(self.dim):
            result += 0.15 * (x[i] ** 4) * np.cos(3 * x[i]) + 0.05 * (x[i] ** 5) * np.sin(2 * x[i])
            
        # Add nested chaotic radial component with multiple frequencies
        r = np.sqrt(np.sum(x ** 2))
        result += 0.4 * np.sin(15 * r) * np.cos(8 * r) * np.exp(-0.2 * r)
        
        # Add chaotic saddle points with sinusoidal perturbations
        for i in range(self.dim):
            result += 0.3 * np.sin(2 * x[i]) * np.cos(3 * x[(i + 2) % self.dim]) * np.tan(0.7 * x[i])
            
        # Add a normalization factor with chaotic scaling
        result /= (1.0 + 0.1 * np.sum(x ** 2) + 0.05 * np.sum(np.sin(x) ** 2))
        
        return result
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
            result += (10 ** (4 * i / (self.dim - 1))) * (x[i] ** 2)
            
        # Add chaotic trigonometric modulations with higher frequency components
        for i in range(self.dim):
            result += 1.2 * np.sin(9 * x[i]) * np.cos(13 * x[(i + 1) % self.dim]) * np.tan(0.6 * x[i])
            
        # Radial basis function components with fractal-like peaks and increased amplitude
        for i in range(self.dim):
            r = np.sqrt(np.sum(x ** 2))
            result += 1.0 * np.exp(-0.4 * (x[i] - r) ** 2) * np.sin(5 * np.pi * r) * np.cos(3 * np.pi * r)
            
        # Add coupling terms with chaotic interaction patterns and stronger coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.2 * (x[i] ** 2 + x[j] ** 2)) * np.sin(7 * x[i]) * np.cos(9 * x[j])
                result += coupling * np.tan(0.4 * x[i]) * np.sin(0.5 * x[j])
                
        # Add quartic and quintic polynomial terms for increased local complexity with higher coefficients
        for i in range(self.dim):
            result += 0.25 * (x[i] ** 4) * np.cos(4 * x[i]) + 0.1 * (x[i] ** 5) * np.sin(3 * x[i])
            
        # Add nested chaotic radial component with multiple frequencies and increased complexity
        r = np.sqrt(np.sum(x ** 2))
        result += 0.6 * np.sin(20 * r) * np.cos(10 * r) * np.exp(-0.3 * r)
        
        # Add chaotic saddle points with sinusoidal perturbations and enhanced nonlinearity
        for i in range(self.dim):
            result += 0.5 * np.sin(3 * x[i]) * np.cos(4 * x[(i + 2) % self.dim]) * np.tan(0.8 * x[i])
            
        # Add a normalization factor with chaotic scaling and increased complexity
        result /= (1.0 + 0.2 * np.sum(x ** 2) + 0.1 * np.sum(np.sin(x) ** 2) + 0.05 * np.sum(np.cos(x) ** 2))
        
        return result
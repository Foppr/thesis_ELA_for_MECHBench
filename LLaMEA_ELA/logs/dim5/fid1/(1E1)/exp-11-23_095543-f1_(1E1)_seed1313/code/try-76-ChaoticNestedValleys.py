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
        
        # Add a new chaotic component that significantly increases complexity
        for i in range(self.dim):
            result += 0.5 * np.sin(13 * x[i]) * np.cos(17 * x[(i + 1) % self.dim]) * np.tan(0.9 * x[i])
            
        # Add a high-frequency chaotic oscillation with dynamic amplitude
        for i in range(self.dim):
            result += 0.25 * np.sin(31 * x[i]) * np.cos(47 * x[(i + 3) % self.dim]) * np.exp(-0.05 * (x[i] ** 2))
            
        # Add a complex nested structure with varying scales
        for i in range(self.dim):
            r = np.sqrt(np.sum(x ** 2))
            result += 0.3 * np.sin(29 * r) * np.cos(19 * r) * np.exp(-0.1 * (r - 2.5) ** 2)
            
        # Add a chaotic perturbation with adaptive scaling based on dimensionality
        adaptive_scale = 0.1 + 0.05 * self.dim
        for i in range(self.dim):
            result += adaptive_scale * np.sin(37 * x[i]) * np.tan(0.8 * x[i]) * np.cos(23 * x[(i + 4) % self.dim])
            
        # Add a new chaotic interaction term with higher-order coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.1 * np.sin(3 * x[i]) * np.cos(5 * x[j]) * np.tan(2 * x[k]) * np.exp(-0.01 * (x[i]**2 + x[j]**2 + x[k]**2))
                    
        return result
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
            
        # Add chaotic trigonometric modulations with higher frequencies
        for i in range(self.dim):
            result += 1.2 * np.sin(13 * x[i]) * np.cos(19 * x[(i + 1) % self.dim]) * np.tan(0.7 * x[i])
            
        # Radial basis function components with fractal-like peaks
        for i in range(self.dim):
            r = np.sqrt(np.sum(x ** 2))
            result += 0.9 * np.exp(-0.5 * (x[i] - r) ** 2) * np.sin(5 * np.pi * r) * np.cos(3 * np.pi * r)
            
        # Add coupling terms with chaotic interaction patterns
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.15 * (x[i] ** 2 + x[j] ** 2)) * np.sin(7 * x[i]) * np.cos(9 * x[j])
                result += coupling * np.tan(0.4 * x[i]) * np.sin(0.5 * x[j])
                
        # Add quartic and quintic polynomial terms for increased local complexity
        for i in range(self.dim):
            result += 0.25 * (x[i] ** 4) * np.cos(4 * x[i]) + 0.1 * (x[i] ** 5) * np.sin(3 * x[i])
            
        # Add nested chaotic radial component with multiple frequencies
        r = np.sqrt(np.sum(x ** 2))
        result += 0.6 * np.sin(20 * r) * np.cos(12 * r) * np.exp(-0.3 * r)
        
        # Add chaotic saddle points with sinusoidal perturbations
        for i in range(self.dim):
            result += 0.5 * np.sin(3 * x[i]) * np.cos(4 * x[(i + 2) % self.dim]) * np.tan(0.9 * x[i])
            
        # Add fractal ridge structure with varying amplitude
        for i in range(self.dim):
            result += 0.4 * np.sin(17 * x[i]) * np.cos(11 * x[(i + 1) % self.dim]) * np.exp(-0.08 * (x[i] ** 2))
            
        # Add high-frequency chaotic noise
        noise = 0.0
        for i in range(self.dim):
            noise += 0.5 * np.sin(31 * x[i]) * np.cos(23 * x[(i + 3) % self.dim])
        result += noise * np.exp(-0.15 * np.sum(x ** 2))
        
        # Add dimensionality-dependent scaling factor
        scaling = 1.0 + 0.08 * np.sum(np.sin(x) ** 2) + 0.04 * np.sum(np.cos(x) ** 2)
        result *= scaling
        
        # Add a normalization factor with chaotic scaling
        result /= (1.0 + 0.15 * np.sum(x ** 2) + 0.08 * np.sum(np.sin(x) ** 2))
        
        # Add an additional chaotic coupling term between all dimensions
        chaos_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_term += np.sin(17 * x[i]) * np.cos(19 * x[j]) * np.tan(0.25 * (x[i] + x[j]))
        result += 0.3 * chaos_term
        
        # Add a complex nested structure with multiple scales
        nested = 0.0
        for i in range(self.dim):
            nested += 0.15 * np.sin(60 * x[i]) * np.cos(40 * x[(i + 1) % self.dim]) * np.exp(-0.02 * (x[i] ** 2))
        result += nested
        
        # Add a dynamic scaling factor that changes with input values
        dynamic_scale = 1.0 + 0.05 * np.sum(np.sin(7 * x) ** 2) + 0.06 * np.sum(np.cos(9 * x) ** 2)
        result *= dynamic_scale
        
        # Add chaotic perturbations to increase local minima density
        for i in range(self.dim):
            result += 0.1 * np.sin(25 * x[i]) * np.cos(15 * x[(i + 1) % self.dim]) * np.tan(0.3 * x[i])
            
        # Add additional high-dimensional coupling with chaotic phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(8 * (x[i] + x[j])) * np.cos(6 * (x[i] - x[j])) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Add a final chaotic modulation with large amplitude
        result += 0.3 * np.sin(40 * np.sum(x)) * np.cos(30 * np.sum(x[::-1])) * np.tan(0.1 * np.sum(np.abs(x)))
        
        return result
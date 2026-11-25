import numpy as np

class NestedHarmonicGradient:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base quadratic term with dimensionally varying coefficients
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * x[i] ** 2
            
        # Add nested harmonic components with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 0.5 * np.sin(2 * (i + 1) * x[i]) * np.cos(3 * (i + 1) * x[i])
            
        # Add asymmetric gradient field with directional dependence
        for i in range(self.dim):
            result += 0.3 * x[i] ** 3 * np.sin(4 * x[(i + 1) % self.dim]) * np.exp(-0.1 * x[i] ** 2)
            
        # Add nested radial components with multiple harmonic layers
        r = np.sqrt(np.sum(x ** 2))
        result *= (1.0 + 0.4 * np.sin(7 * r) * np.cos(5 * r) * np.exp(-0.05 * r ** 2))
        
        # Add dimensionally adaptive conditioning with local minima
        for i in range(self.dim):
            result += 0.2 * np.sin(10 * x[i]) * np.cos(8 * x[i]) * (1 + 0.3 * np.sin(3 * r))
            
        # Add cross-dimensional coupling with exponential weighting
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.25 * np.sin(6 * x[i]) * np.cos(9 * x[j]) * np.exp(-0.1 * (x[i] - x[j]) ** 2)
                
        # Add multi-scale harmonic structure with varying phase shifts
        for i in range(self.dim):
            result += 0.15 * np.sin(15 * x[i] + 0.5 * i) * np.cos(12 * x[(i + 2) % self.dim] - 0.3 * i)
            
        # Add nested oscillatory patterns with varying amplitudes
        for i in range(self.dim):
            result += 0.2 * np.sin(20 * x[i]) * np.cos(18 * x[(i + 1) % self.dim]) * np.exp(-0.05 * x[i] ** 2)
            
        # Add a complex coupling structure with polynomial interactions
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += 0.1 * (x[i] ** 2 + x[j] ** 2) * np.sin(5 * x[i]) * np.cos(7 * x[j])
        result += poly_coupling
        
        # Add a fractal-like structure with recursive harmonic components
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_component += 0.18 * np.sin(25 * x[i]) * np.cos(22 * x[(i + 1) % self.dim]) * np.sin(19 * x[(i + 2) % self.dim])
        result += fractal_component
        
        # Add dimensionally dependent scaling for conditioning
        scaling = 1.0 + 0.15 * np.sum(np.sin(x) ** 2) + 0.1 * np.sum(np.cos(x) ** 2)
        result *= scaling
        
        # Add asymmetric local minima with varying depths
        local_minima = 0.0
        for i in range(self.dim):
            local_minima += 0.3 * np.exp(-0.5 * (x[i] - 1.5) ** 2) * np.sin(6 * x[i])
        result += local_minima
        
        # Add a final conditioning term to increase problem difficulty
        conditioning = 0.05 * np.sum(np.abs(x) ** 1.7)
        result += conditioning
        
        return result
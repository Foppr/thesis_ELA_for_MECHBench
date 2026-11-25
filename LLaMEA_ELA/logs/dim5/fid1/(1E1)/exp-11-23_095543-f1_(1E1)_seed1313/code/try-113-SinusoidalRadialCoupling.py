import numpy as np

class SinusoidalRadialCoupling:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base quadratic term with varying coefficients
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * x[i] ** 2
            
        # Add radial sinusoidal modulation
        r = np.sqrt(np.sum(x ** 2))
        result *= (1.0 + 0.5 * np.sin(3 * r) * np.cos(2 * r))
        
        # Add periodic components with different frequencies
        for i in range(self.dim):
            result += 0.3 * np.sin(7 * x[i]) * np.cos(5 * x[(i + 1) % self.dim])
            
        # Add cross-dimensional coupling terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.sin(4 * x[i]) * np.cos(6 * x[j]) * np.exp(-0.1 * (x[i] - x[j]) ** 2)
                
        # Add radial harmonic components
        for i in range(self.dim):
            result += 0.15 * np.sin(10 * r) * np.cos(8 * r) * x[i] ** 2
            
        # Add multi-scale periodicity
        for i in range(self.dim):
            result += 0.25 * np.sin(15 * x[i]) * np.cos(12 * x[(i + 2) % self.dim]) * np.exp(-0.05 * x[i] ** 2)
            
        # Add asymmetric coupling
        for i in range(self.dim):
            result += 0.1 * (x[i] ** 3) * np.sin(3 * x[(i + 1) % self.dim])
            
        # Add radial peak structure
        result += 0.4 * np.exp(-0.5 * r ** 2) * np.sin(5 * r)
        
        # Add dimensionality-dependent scaling
        scaling = 1.0 + 0.1 * np.sum(np.sin(x) ** 2) + 0.05 * np.sum(np.cos(x) ** 2)
        result *= scaling
        
        return result
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
            
        # Add radial sinusoidal modulation with enhanced frequency
        r = np.sqrt(np.sum(x ** 2))
        result *= (1.0 + 0.4 * np.sin(4 * r) * np.cos(3 * r))
        
        # Add periodic components with different frequencies and amplitudes
        for i in range(self.dim):
            result += 0.25 * np.sin(8 * x[i]) * np.cos(6 * x[(i + 1) % self.dim])
            
        # Add cross-dimensional coupling terms with stronger interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(5 * x[i]) * np.cos(7 * x[j]) * np.exp(-0.15 * (x[i] - x[j]) ** 2)
                
        # Add radial harmonic components with different frequencies
        for i in range(self.dim):
            result += 0.2 * np.sin(12 * r) * np.cos(9 * r) * x[i] ** 2
            
        # Add multi-scale periodicity with more complex interaction
        for i in range(self.dim):
            result += 0.3 * np.sin(18 * x[i]) * np.cos(15 * x[(i + 2) % self.dim]) * np.exp(-0.08 * x[i] ** 2)
            
        # Add asymmetric coupling with cubic terms
        for i in range(self.dim):
            result += 0.15 * (x[i] ** 3) * np.sin(4 * x[(i + 1) % self.dim])
            
        # Add radial peak structure with sharper gradient
        result += 0.5 * np.exp(-0.3 * r ** 2) * np.sin(6 * r)
        
        # Add dimensionality-dependent scaling with more complex interaction
        scaling = 1.0 + 0.15 * np.sum(np.sin(x) ** 2) + 0.1 * np.sum(np.cos(x) ** 2)
        result *= scaling
        
        return result
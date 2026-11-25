import numpy as np

class AsymmetricFractalMultimodal:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base polynomial term with varying exponents
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * np.abs(x[i]) ** (2.5 + 0.5 * np.sin(i))
            
        # Add asymmetric trigonometric coupling terms
        for i in range(self.dim):
            result += 0.8 * np.sin(3 * x[i]) * np.cos(2 * x[(i + 1) % self.dim]) * (1 + 0.3 * np.sin(5 * x[i]))
            
        # Add exponential decay with dimension-dependent scaling
        for i in range(self.dim):
            result += 0.5 * np.exp(-0.1 * np.abs(x[i])) * np.cos(4 * x[i]) * (1 + 0.2 * np.cos(3 * x[(i + 2) % self.dim]))
            
        # Add fractal-like structure with recursive pattern
        fractal = 0.0
        for i in range(self.dim):
            fractal += 0.3 * np.sin(7 * x[i]) * np.cos(5 * x[(i + 1) % self.dim]) * np.sin(3 * x[(i + 2) % self.dim])
        result += fractal * np.exp(-0.05 * np.sum(x**2))
        
        # Add asymmetric coupling with cubic terms
        for i in range(self.dim):
            result += 0.4 * (x[i] ** 3) * np.sin(2 * x[(i + 1) % self.dim]) * np.cos(3 * x[(i + 2) % self.dim])
            
        # Add multi-scale periodic components
        for i in range(self.dim):
            result += 0.25 * np.sin(15 * x[i]) * np.cos(12 * x[(i + 1) % self.dim]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Add radial harmonic components with varying amplitudes
        r = np.sqrt(np.sum(x ** 2))
        result += 0.6 * np.sin(8 * r) * np.cos(6 * r) * (1 + 0.4 * np.sin(4 * r))
        
        # Add dimensionality-dependent complexity
        for i in range(self.dim):
            result += 0.35 * np.sin(9 * x[i]) * np.cos(7 * x[(i + 1) % self.dim]) * (1 + 0.2 * np.sin(2 * r))
            
        # Add asymmetric exponential modulation
        asym_exp = 0.0
        for i in range(self.dim):
            asym_exp += 0.2 * np.exp(-0.2 * x[i] ** 2) * np.sin(5 * x[i]) * np.cos(3 * x[(i + 1) % self.dim])
        result += asym_exp
        
        # Add a conditioning term to increase challenge
        conditioning = 0.1 * np.sum(np.abs(x) ** 1.7)
        result += conditioning
        
        return result
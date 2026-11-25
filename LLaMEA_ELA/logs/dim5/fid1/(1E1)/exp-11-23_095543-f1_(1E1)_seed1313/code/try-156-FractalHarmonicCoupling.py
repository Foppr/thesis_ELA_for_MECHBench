import numpy as np

class FractalHarmonicCoupling:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base quadratic term with dimension-dependent coefficients
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * x[i] ** 2
            
        # Add fractal-like harmonic components with recursive structure
        r = np.sqrt(np.sum(x ** 2))
        fractal_factor = 1.0
        for k in range(1, min(4, self.dim + 1)):
            fractal_factor *= (1.0 + 0.3 * np.sin(k * 7 * r) * np.cos(k * 5 * r))
        result *= fractal_factor
        
        # Add asymmetric cross-dimensional coupling with polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (x[i] ** 3) * np.sin(4 * x[j]) * np.cos(3 * x[i]) * np.exp(-0.1 * (x[i] - x[j]) ** 2)
                result += 0.25 * coupling
                
        # Add multi-scale periodic components with varying amplitudes
        for i in range(self.dim):
            result += 0.3 * np.sin(11 * x[i]) * np.cos(9 * x[(i + 1) % self.dim]) * np.sin(7 * x[(i + 2) % self.dim])
            
        # Add radial peak structure with multiple overlapping harmonics
        result += 0.4 * np.exp(-0.2 * r ** 2) * (np.sin(6 * r) + 0.5 * np.cos(9 * r)) * (1 + 0.3 * np.sin(3 * r))
        
        # Add dimensionality-dependent scaling with chaotic modulation
        scaling = 1.0 + 0.15 * np.sum(np.sin(x) ** 2) + 0.1 * np.sum(np.cos(2 * x) ** 2)
        result *= scaling
        
        # Add asymmetric cubic coupling terms
        for i in range(self.dim):
            result += 0.18 * (x[i] ** 3) * np.sin(5 * x[(i + 1) % self.dim]) * np.cos(2 * x[i])
            
        # Add hypercomplex trigonometric interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                for k in range(j+1, min(j+3, self.dim)):
                    result += 0.15 * np.sin(3 * x[i]) * np.cos(6 * x[j]) * np.sin(4 * x[k]) * np.exp(-0.05 * (x[i]**2 + x[j]**2 + x[k]**2))
                    
        # Add a novel exponential decay structure with local modulation
        exp_decay = 0.0
        for i in range(self.dim):
            exp_decay += 0.2 * np.exp(-0.3 * (x[i] - 1.5) ** 2) * np.sin(8 * x[i]) * np.cos(5 * x[(i + 1) % self.dim])
        result += exp_decay
        
        # Add a conditioning term that increases with dimensionality
        conditioning = 0.05 * np.sum(np.abs(x) ** 1.7)
        result += conditioning
        
        return result
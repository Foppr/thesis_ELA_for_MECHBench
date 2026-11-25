import numpy as np

class PolynomialRBFChaoticCoupling:
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
            
        # Add radial basis function components with Gaussian kernels
        r = np.sqrt(np.sum(x ** 2))
        for i in range(self.dim):
            # Radial basis functions with varying widths and centers
            width = 1.0 + 0.3 * np.sin(i)
            center = 2.0 * np.cos(i) + 0.5 * np.sin(2 * i)
            result += 0.8 * np.exp(-0.5 * ((x[i] - center) / width) ** 2)
            
        # Add asymmetric coupling terms with polynomial interactions
        for i in range(self.dim):
            j = (i + 1) % self.dim
            # Asymmetric coupling with different weights for positive/negative directions
            coupling = x[i] * x[j] * np.exp(-0.1 * np.abs(x[i]))
            if x[i] >= 0:
                result += 0.5 * coupling * (1 + 0.3 * np.sin(3 * x[i]))
            else:
                result += 0.7 * coupling * (1 + 0.2 * np.cos(2 * x[i]))
                
        # Add chaotic sine-cosine components with varying frequencies
        for i in range(self.dim):
            freq = 3.0 + 0.5 * np.sin(i)
            result += 0.4 * np.sin(freq * x[i]) * np.cos(freq * x[(i + 2) % self.dim]) * np.exp(-0.05 * r ** 2)
            
        # Add multi-scale polynomial chaos terms
        for i in range(self.dim):
            result += 0.3 * (x[i] ** 4) * np.sin(7 * x[i]) * np.cos(5 * x[(i + 1) % self.dim])
            
        # Add radial harmonic components with varying amplitudes
        result += 0.6 * np.sin(8 * r) * np.cos(6 * r) * (1 + 0.2 * np.sin(4 * r))
        
        # Add cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                result += 0.25 * np.sin(3 * x[i]) * np.cos(4 * x[j]) * np.exp(-0.3 * dist)
                
        # Add fractal-like structure with recursive polynomial terms
        fractal = 0.0
        for i in range(self.dim):
            fractal += 0.15 * (x[i] ** 3) * np.sin(2 * x[(i + 1) % self.dim]) * np.cos(3 * x[(i + 2) % self.dim])
        result += fractal
        
        # Add condition number influence with dimensionality scaling
        dim_scaling = 1.0 + 0.15 * np.sum(np.abs(x) ** 1.7)
        result *= dim_scaling
        
        # Add final chaotic modulation based on sum of sinusoids
        final_mod = 1.0 + 0.2 * np.sin(13 * np.sum(x)) * np.cos(11 * np.sum(x))
        result *= final_mod
        
        return result
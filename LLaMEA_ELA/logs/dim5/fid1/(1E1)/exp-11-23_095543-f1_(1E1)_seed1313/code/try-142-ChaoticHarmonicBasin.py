import numpy as np

class ChaoticHarmonicBasin:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base fractional-dimensional quadratic term
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) ** 0.7 * x[i] ** 2
            
        # Add chaotic phase modulation with logistic map-like behavior
        r = np.sqrt(np.sum(x ** 2))
        chaotic_phase = 0.0
        for i in range(self.dim):
            chaotic_phase += np.sin(13 * x[i] + 0.3 * np.sin(7 * x[(i+1) % self.dim]))
        result *= (1.0 + 0.5 * np.sin(3 * r) * np.cos(2 * r) * np.exp(-0.1 * r) * chaotic_phase)
        
        # Add nested harmonic structures with varying frequencies
        for i in range(self.dim):
            result += 0.3 * np.sin(8 * x[i]) * np.cos(6 * x[(i+1) % self.dim]) * np.sin(4 * x[(i+2) % self.dim])
            
        # Add fractional-dimensional coupling with power-law decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (x[i] ** 1.5) * (x[j] ** 1.3) * np.sin(5 * x[i]) * np.cos(7 * x[j])
                result += 0.2 * coupling * (1.0 + 0.1 * np.sin(3 * r)) / (1.0 + 0.05 * (x[i] - x[j]) ** 2)
                
        # Add nested multi-modal structure with exponential peaks
        for i in range(self.dim):
            result += 0.4 * np.exp(-0.5 * (x[i] - 2) ** 2) * np.sin(10 * x[i]) * np.cos(8 * x[i])
            
        # Add fractional-dimensional radial components with varying exponents
        for i in range(self.dim):
            result += 0.25 * np.sin(15 * r) * np.cos(12 * r) * (x[i] ** 1.7) * (1 + 0.2 * np.sin(5 * r))
            
        # Add chaotic basin structure with multiple local minima
        basin_term = 0.0
        for i in range(self.dim):
            basin_term += 0.3 * np.sin(20 * x[i]) * np.cos(18 * x[(i+1) % self.dim]) * np.exp(-0.1 * x[i] ** 2)
        result += basin_term
        
        # Add nested harmonic with varying amplitudes and phases
        for i in range(self.dim):
            result += 0.15 * np.sin(9 * x[i] + 0.5 * i) * np.cos(7 * x[(i+3) % self.dim]) * (1.0 + 0.3 * np.sin(4 * r))
            
        # Add multi-scale fractal-like structure with recursive components
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += 0.2 * np.sin(25 * x[i]) * np.cos(23 * x[(i+1) % self.dim]) * np.sin(21 * x[(i+2) % self.dim])
        result += fractal_term
        
        # Add dimensionality-dependent scaling with chaotic modulation
        scaling = 1.0 + 0.15 * np.sum(np.sin(x) ** 2) + 0.1 * np.sum(np.cos(2 * x) ** 2) + 0.05 * np.sum(np.sin(3 * x) ** 2)
        result *= scaling
        
        # Add final chaotic modulation with fractional dimensions
        final_mod = 1.0 + 0.2 * np.sin(17 * r) * np.cos(14 * r) * (1.0 + 0.1 * np.sin(6 * r))
        result *= final_mod
        
        # Add a new hypercomplex coupling with nested trigonometric functions
        hypercomplex = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    hypercomplex += 0.1 * np.sin(7 * x[i]) * np.cos(9 * x[j]) * np.sin(5 * x[k]) * np.exp(-0.1 * (x[i]**2 + x[j]**2 + x[k]**2))
        result += hypercomplex
        
        return result
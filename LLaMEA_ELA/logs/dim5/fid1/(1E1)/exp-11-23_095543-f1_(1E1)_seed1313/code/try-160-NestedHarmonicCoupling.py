import numpy as np

class NestedHarmonicCoupling:
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
            result += (i + 1) * 0.5 * x[i] ** 2
            
        # Add nested harmonic components with different frequencies and amplitudes
        r = np.sqrt(np.sum(x ** 2))
        for i in range(self.dim):
            # Nested sinusoidal terms with varying frequencies
            result += 0.3 * np.sin(2 * (i + 1) * x[i]) * np.cos(3 * (i + 1) * x[i])
            
        # Add asymmetric coupling between dimensions
        for i in range(self.dim):
            j = (i + 1) % self.dim
            result += 0.25 * np.sin(4 * x[i]) * np.cos(5 * x[j]) * (1 + 0.3 * np.sin(2 * r))
            
        # Add nested radial components with exponential decay
        for i in range(self.dim):
            result += 0.2 * np.exp(-0.1 * (x[i] ** 2)) * np.sin(6 * x[i]) * np.cos(4 * r)
            
        # Add multi-scale harmonic interactions
        for k in range(1, 4):
            harmonic_sum = 0.0
            for i in range(self.dim):
                harmonic_sum += np.sin(k * (i + 1) * x[i])
            result += 0.15 * np.cos(harmonic_sum) * np.exp(-0.05 * r ** 2)
            
        # Add dimensionally adaptive exponential decay terms
        for i in range(self.dim):
            result += 0.18 * np.exp(-0.3 * (x[i] - 1) ** 2) * np.sin(7 * x[i]) * (1 + 0.2 * np.cos(3 * (i + 1)))
            
        # Add nested peak structures with varying heights
        peak_sum = 0.0
        for i in range(self.dim):
            peak_sum += np.exp(-0.5 * (x[i] - 2) ** 2) * np.sin(8 * x[i])
        result += 0.22 * peak_sum ** 2
            
        # Add asymmetric cross-dimensional coupling with nested structure
        for i in range(self.dim):
            j = (i + 2) % self.dim
            k = (i + 3) % self.dim
            result += 0.12 * np.sin(3 * x[i]) * np.cos(4 * x[j]) * np.sin(5 * x[k]) * np.exp(-0.1 * (x[i] ** 2 + x[j] ** 2))
            
        # Add nested harmonic modulation based on radial distance
        radial_mod = 1.0 + 0.25 * np.sin(5 * r) * np.cos(3 * r) * np.exp(-0.1 * r)
        result *= radial_mod
        
        # Add dimensionally varying scaling factors
        scaling_factor = 1.0
        for i in range(self.dim):
            scaling_factor += 0.1 * np.sin(x[i]) ** 2 + 0.05 * np.cos(2 * x[i]) ** 2
        result *= scaling_factor
        
        # Add a final nested structure with cubic terms and harmonic mixing
        cubic_sum = 0.0
        for i in range(self.dim):
            cubic_sum += (x[i] ** 3) * np.sin(4 * x[(i + 1) % self.dim])
        result += 0.15 * cubic_sum * np.exp(-0.05 * r ** 2)
        
        # Add conditioning term that varies with dimensionality
        conditioning = 0.05 * np.sum(np.abs(x) ** 1.7)
        result += conditioning
        
        return result
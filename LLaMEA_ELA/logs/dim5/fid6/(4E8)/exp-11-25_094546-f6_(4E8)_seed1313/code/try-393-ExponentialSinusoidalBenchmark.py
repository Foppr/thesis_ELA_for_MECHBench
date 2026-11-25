import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Exponentially decaying sinusoidal waves with radial symmetry
            wave_term = np.exp(-abs(xi) * 0.5) * np.sin(10 * xi + i * 0.3) * np.cos(7 * xi - i * 0.2)
            
            # Radial basis function with adaptive scaling
            radial_basis = 0.0
            for j in range(self.dim):
                if i != j:
                    distance = abs(xi - x_norm[j])
                    radial_basis += np.exp(-distance**2 * 0.3) * np.sin(distance * 5.0 + i * 0.1)
            
            # Adaptive conditioning factor with exponential decay
            condition_factor = 1.0 + 0.5 * np.exp(-i * 0.2) * np.sin(i * 0.7) * np.cos(i * 0.4)
            
            # Multi-scale interference pattern with exponential weighting
            interference = 0.3 * np.exp(-abs(xi) * 0.8) * np.sin(15 * xi + i * 0.25) + \
                          0.2 * np.exp(-abs(xi) * 0.6) * np.cos(12 * xi - i * 0.3) + \
                          0.1 * np.exp(-abs(xi) * 0.4) * np.sin(8 * xi + i * 0.15)
            
            # Combined term with exponential modulation
            term = condition_factor * (wave_term + radial_basis + interference)**2
            
            result += term
            
        # Global scaling factor with exponential decay
        global_scale = 1.0 + 0.3 * np.exp(-self.dim * 0.1) * np.sin(self.dim * 0.5) * np.cos(self.dim * 0.3)
        
        # Cross-dimensional coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.exp(-abs(x_norm[i] - x_norm[j]) * 0.5) * np.sin((x_norm[i] + x_norm[j]) * 3.0)
        
        return global_scale * (result / self.dim + 0.1 * coupling)
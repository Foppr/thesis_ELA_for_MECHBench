import numpy as np

class MultiModalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        radius = np.sqrt(np.sum(x_norm**2))
        
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Radial periodic modulation with dimension-dependent frequency
            radial_freq = 1.0 + 0.3 * np.sin(0.5 * self.dim + i)
            radial_mod = np.sin(radial_freq * radius) * np.cos(0.7 * radius)
            
            # Angular sinusoidal pattern with coupling to other dimensions
            angular_term = 0.0
            for j in range(self.dim):
                if i != j:
                    angular_factor = np.sin(2.5 * (xi - x_norm[j]) + 0.3 * i) * np.cos(1.8 * (xi + x_norm[j]))
                    angular_term += angular_factor / (1.0 + abs(xi - x_norm[j])**1.5)
            
            # Multi-frequency sinusoidal base with varying amplitudes
            base_freq = 3.0 + 0.5 * np.sin(i * 0.7) + 0.3 * np.cos(i * 0.4)
            base_term = np.sin(base_freq * xi) * np.cos(2.1 * xi)
            
            # Cross-dimensional coupling with exponential decay
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = abs(xi - x_norm[j])
                    coupling_factor = np.exp(-dist**2) * np.sin(3.2 * (xi + x_norm[j]))
                    coupling_sum += coupling_factor
            
            # Local quadratic basin with sinusoidal perturbation
            quadratic = 0.5 * xi**2
            perturbation = 0.2 * np.sin(7.0 * xi + 1.3 * i) * np.cos(4.0 * xi - 0.8 * i)
            
            # Combine all terms with dynamic weighting
            weight = 1.0 + 0.25 * np.sin(i * 0.6) * np.cos(self.dim * 0.3) + \
                    0.1 * np.cos(i * 0.4) * np.sin(self.dim * 0.2)
            
            term = weight * (quadratic + base_term + angular_term + coupling_sum + perturbation)**2
            result += radial_mod * term
            
        # Global scaling with multi-fractal characteristics
        global_scale = 1.0 + 0.4 * np.sin(0.3 * self.dim) * np.cos(0.2 * self.dim) + \
                      0.2 * np.sin(0.6 * self.dim**1.5) * np.cos(0.4 * self.dim**1.3)
        
        # Add radial coupling term
        radial_coupling = 0.15 * np.sin(radius * 4.0) * np.cos(radius * 2.0)
        
        return global_scale * (result / self.dim + radial_coupling)
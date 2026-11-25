import numpy as np

class ChaoticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters
        self.chebyshev_coeffs = np.array([1.0, 0.8, 0.6, 0.4, 0.2])
        self.tent_map_params = np.random.uniform(1.5, 3.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Tent map chaotic component
        tent_sum = 0.0
        for i in range(self.dim):
            param = self.tent_map_params[i]
            xi = x[i] / 5.0  # Normalize to [-1, 1]
            if xi < 0.5:
                tent_val = param * xi
            else:
                tent_val = param * (1 - xi)
            tent_sum += tent_val**2
        
        # Spectral decomposition with Chebyshev polynomials
        spectral_sum = 0.0
        for i in range(self.dim):
            xi = x[i] / 5.0  # Normalize to [-1, 1]
            T2 = 2 * xi**2 - 1  # Chebyshev polynomial of degree 2
            T3 = 4 * xi**3 - 3 * xi  # Chebyshev polynomial of degree 3
            spectral_sum += self.chebyshev_coeffs[0] * xi + \
                           self.chebyshev_coeffs[1] * T2 + \
                           self.chebyshev_coeffs[2] * T3
        
        # Adaptive conditioning based on dimensionality
        adapt_factor = 1.0 + 0.5 * np.sin(0.2 * self.dim)
        
        # Cross-dimensional coupling with chaotic interaction
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.abs(x[i] - x[j])
                cross_sum += np.exp(-0.5 * dist**2) * np.sin(3 * (x[i] + x[j]))
        
        # Fractal-like structure with recursive tent maps
        fractal_sum = 0.0
        for i in range(self.dim):
            xi = x[i] / 5.0
            fractal_sum += np.sin(10 * xi) * np.cos(8 * xi) * np.tan(6 * xi)
        
        # Asymmetric basin structure with exponential penalties
        basin_sum = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                basin_sum += 1.5 * np.exp(-0.2 * (x[i] + 5)**2) * (1 + 0.4 * np.sin(8 * x[i]))
            else:
                basin_sum += 1.2 * np.exp(-0.3 * (x[i] - 5)**2) * (1 + 0.3 * np.cos(6 * x[i]))
        
        # High-frequency oscillations with dynamic modulation
        freq_sum = 0.0
        for i in range(self.dim):
            freq_sum += np.sin(20 * x[i]) * np.cos(18 * x[i])
        
        # Add a new component: enhanced multimodality with dynamic conditioning
        multimodal_sum = 0.0
        for i in range(self.dim):
            xi = x[i] / 5.0
            # Add a sinusoidal modulation that varies with dimension
            modulation = 1.0 + 0.3 * np.sin(0.5 * self.dim + xi)
            multimodal_sum += modulation * np.sin(15 * xi) * np.cos(12 * xi)
        
        # Combine all components
        result = (adapt_factor * (tent_sum + spectral_sum + cross_sum) + 
                 0.8 * fractal_sum + basin_sum + 0.5 * freq_sum + 0.3 * multimodal_sum)
        
        # Normalize by dimensionality and add a small constant for better conditioning
        result /= self.dim
        result += 0.01 * np.sum(x**2) / self.dim
        
        return result
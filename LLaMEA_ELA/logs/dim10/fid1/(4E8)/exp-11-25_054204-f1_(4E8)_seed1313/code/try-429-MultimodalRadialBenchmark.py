import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial weights and frequencies
        self.weights = np.random.rand(dim) * 2.0 + 1.0
        self.frequencies = np.random.rand(dim) * 8.0 + 2.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with multiple peaks
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * r**2 + 0.3 * np.sin(3.0 * r) + 0.2 * np.cos(5.0 * r)
        
        # Sinusoidal oscillations in each dimension
        sin_term = np.sum(self.weights * np.sin(self.frequencies * x))
        
        # Polynomial chaos component with mixed exponents
        poly_term = np.sum((x**3) * np.cos(x)) + 0.5 * np.sum((x**5) * np.sin(x/2))
        
        # Radial basis function interaction
        rbf_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                rbf_sum += np.exp(-dist**2 / 2.0) * np.sin(x[i] * x[j])
        
        # Cross-dimensional harmonic interactions
        cross_harmonic = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_harmonic += np.sin(x[i]) * np.cos(x[j]) / (1.0 + abs(i - j))
        
        # Combined fitness with adaptive scaling
        scale = 1.0 + 0.5 * np.log(self.dim + 1)
        
        return scale * (radial_term + sin_term + poly_term + rbf_sum + cross_harmonic)
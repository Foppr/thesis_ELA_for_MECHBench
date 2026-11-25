import numpy as np

class AsymmetricCurvatureBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Periodic exponential barriers with varying frequencies and amplitudes
        barrier_term = np.sum(np.exp(-np.abs(x_norm)) * np.cos(2 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Long-range dependencies through weighted sums with decay functions
        long_range = 0.0
        for i in range(self.dim):
            weight_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    weight = np.exp(-0.1 * distance) / (1.0 + distance)
                    weight_sum += weight * x_norm[j]
            long_range += weight_sum * x_norm[i]
        
        # Asymmetric curvature terms with different exponents for positive and negative directions
        asym_curvature = 0.0
        for i in range(self.dim):
            if x_norm[i] >= 0:
                asym_curvature += x_norm[i]**2.5 * np.sin(4 * x_norm[i])
            else:
                asym_curvature += x_norm[i]**1.8 * np.cos(3 * x_norm[i])
        
        # Multi-scale oscillatory patterns with frequency modulation
        oscillatory = np.sum(np.sin(10 * x_norm + 0.5 * np.sin(20 * x_norm)) * 
                           np.cos(5 * x_norm + 0.3 * np.cos(15 * x_norm)) * 
                           np.exp(-0.2 * np.abs(x_norm)))
        
        # Fractional dimension coupling with non-local interactions
        fractional_coupling = 0.0
        for i in range(self.dim - 1):
            fractional_coupling += (np.abs(x_norm[i] - x_norm[i+1])**1.4 + 
                                 0.3 * np.abs(x_norm[i] + x_norm[i+1])**1.2) * np.exp(-0.1 * (x_norm[i]**2 + x_norm[i+1]**2))
        
        # Add dimensionality scaling and noise
        dim_factor = np.sqrt(self.dim)
        noise = 0.001 * np.random.random()
        
        result = (0.4 * barrier_term + 0.3 * long_range + 0.5 * asym_curvature + 
                 0.6 * oscillatory + 0.4 * fractional_coupling) * dim_factor + noise
        
        return result
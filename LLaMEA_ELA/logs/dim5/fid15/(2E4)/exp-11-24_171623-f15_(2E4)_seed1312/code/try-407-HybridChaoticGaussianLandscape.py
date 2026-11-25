import numpy as np

class HybridChaoticGaussianLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Gaussian peak centers with chaotic distribution
        self.peak_centers = 5.0 * np.random.rand(dim, 15) - 2.5
        self.peak_heights = 2.0 + 8.0 * np.random.rand(15)
        self.peak_widths = 0.5 + 2.5 * np.random.rand(15)
        
        # Trigonometric chaos components with varying frequencies and amplitudes
        self.trig_amplitudes = 1.0 + 4.0 * np.random.rand(dim)
        self.trig_frequencies = 5.0 + 15.0 * np.random.rand(dim)
        self.trig_phases = 2.0 * np.pi * np.random.rand(dim)
        
        # Gradient-based conditioning with adaptive scaling
        self.conditioning_weights = 0.5 + 3.0 * np.random.rand(dim)
        self.conditioning_exponents = 1.0 + 5.0 * np.random.rand(dim)
        
        # Correlation matrix for dimension interactions
        self.correlation_matrix = np.random.rand(dim, dim) - 0.5
        self.correlation_matrix = (self.correlation_matrix + self.correlation_matrix.T) / 2.0
        np.fill_diagonal(self.correlation_matrix, 1.0)
        
        # Chaotic modulation factors
        self.modulation_factors = 0.1 + 0.9 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Gaussian peak component
        gaussian_sum = 0.0
        for k in range(15):
            dist_sq = 0.0
            for i in range(self.dim):
                diff = x_norm[i] - self.peak_centers[i, k]
                dist_sq += diff * diff
            gaussian_sum += self.peak_heights[k] * np.exp(-dist_sq / (2.0 * self.peak_widths[k]**2))
        
        # Trigonometric chaos component
        trig_sum = 0.0
        for i in range(self.dim):
            trig_sum += self.trig_amplitudes[i] * np.sin(self.trig_frequencies[i] * x_norm[i] + self.trig_phases[i])
        
        # Gradient conditioning component
        cond_sum = 0.0
        for i in range(self.dim):
            cond_sum += self.conditioning_weights[i] * np.abs(x_norm[i]) ** self.conditioning_exponents[i]
        
        # Correlated dimension interactions
        corr_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    corr_sum += self.correlation_matrix[i, j] * x_norm[i] * x_norm[j]
        
        # Chaotic modulation
        mod_sum = 0.0
        for i in range(self.dim):
            mod_sum += self.modulation_factors[i] * np.sin(10.0 * x_norm[i])
        
        # Combine all components with dynamic weights
        result = 0.30 * gaussian_sum + 0.25 * trig_sum + 0.20 * cond_sum + 0.15 * corr_sum + 0.10 * mod_sum
        
        # Add penalty for constraint violations and enhanced bias
        penalty = 0.15 * np.sum(np.abs(x_norm)**6) + 0.10 * np.sum(np.cos(5.0 * x_norm))
        
        return result + penalty
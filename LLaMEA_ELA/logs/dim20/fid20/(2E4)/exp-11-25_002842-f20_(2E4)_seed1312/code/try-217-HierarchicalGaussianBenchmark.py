import numpy as np

class HierarchicalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize hierarchical Gaussian process parameters
        self.num_levels = max(2, int(np.log2(dim)) + 1)
        self.level_scales = np.logspace(0, 2, self.num_levels)
        self.correlation_lengths = np.random.uniform(0.5, 3.0, (self.num_levels, dim))
        self.amplitude_scales = np.random.uniform(0.5, 2.0, self.num_levels)
        self.fractal_dimensions = np.random.uniform(1.1, 2.8, self.num_levels)
        self.non_stationary_params = np.random.uniform(-0.5, 0.5, (self.num_levels, dim))
        # Additional spectral components
        self.spectral_centers = np.random.uniform(-np.pi, np.pi, (self.num_levels, dim))
        self.spectral_widths = np.random.uniform(0.1, 1.0, (self.num_levels, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Hierarchical Gaussian process with fractal Brownian motion
        result = 0.0
        for level in range(self.num_levels):
            # Correlation structure with adaptive scaling
            correlation_matrix = np.zeros((self.dim, self.dim))
            for i in range(self.dim):
                for j in range(self.dim):
                    dist = np.abs(x_norm[i] - x_norm[j])
                    corr_val = np.exp(-dist**2 / (2 * self.correlation_lengths[level, i] * self.correlation_lengths[level, j]))
                    correlation_matrix[i, j] = corr_val
            
            # Fractal Brownian motion component with varying Hurst parameters
            hurst = 0.5 + 0.3 * np.sin(level * 0.5)
            fbm_term = np.random.multivariate_normal(np.zeros(self.dim), correlation_matrix)
            
            # Non-stationary spectral components
            spectral_term = 0.0
            for i in range(self.dim):
                freq = self.spectral_centers[level, i] + self.non_stationary_params[level, i] * x_norm[i]
                spectral_term += np.sin(freq * x_norm[i]) * np.exp(-x_norm[i]**2 / (2 * self.spectral_widths[level, i]))
            
            # Combine level components with amplitude scaling
            level_result = self.amplitude_scales[level] * (
                np.sum(fbm_term) + 
                spectral_term * np.sin(self.fractal_dimensions[level] * np.sum(x_norm**2))
            )
            result += level_result * np.exp(-0.5 * self.level_scales[level] * np.sum(x_norm**2))
        
        # Multi-scale coupling terms with modified adaptive weights
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified coupling based on distance and fractal scaling
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling_strength = (1.0 + np.tanh(dist)) * \
                                  np.exp(-dist**2 / (2 * (1.0 + 0.7 * np.sin(x_norm[i]))))
                coupling_terms += coupling_strength * np.cos(5 * (x_norm[i] - x_norm[j]))
        
        # Enhanced harmonic and fractal components
        harmonic_component = 0.0
        for i in range(self.dim):
            harmonic_component += (
                1.2 * np.sin(2 * x_norm[i]) + 
                0.9 * np.cos(3 * x_norm[i]) + 
                0.6 * np.sin(5 * x_norm[i]) + 
                0.3 * np.cos(7 * x_norm[i]) +
                0.4 * np.sin(9 * x_norm[i])
            ) * np.exp(-0.4 * x_norm[i]**2)
        
        # Combine all components
        total = result + 0.4 * coupling_terms + 0.3 * harmonic_component
        
        return total
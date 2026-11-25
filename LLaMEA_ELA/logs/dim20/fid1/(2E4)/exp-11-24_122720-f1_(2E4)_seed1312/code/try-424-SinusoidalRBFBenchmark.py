import numpy as np

class SinusoidalRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced sinusoidal parameters with higher frequency variations
        self.sin_amplitudes = np.random.uniform(0.8, 2.5, dim)
        self.sin_frequencies = np.random.uniform(2.0, 12.0, dim)
        self.sin_phases = np.random.uniform(0, 2*np.pi, dim)
        # Enhanced radial basis function parameters with more centers
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 8))
        self.rbf_widths = np.random.uniform(0.3, 2.5, 8)
        self.rbf_weights = np.random.uniform(-1.5, 1.5, 8)
        # Enhanced cross-dimensional interaction with stronger coupling
        self.interaction_matrix = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Adaptive conditioning and multimodality control
        self.conditioning_factor = np.random.uniform(0.3, 2.5)
        self.multimodal_factor = np.random.uniform(2.0, 4.0)
        # Additional noise parameter to increase complexity
        self.noise_level = np.random.uniform(0.1, 0.5)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal component with harmonic interactions
        sin_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Add harmonic components for increased complexity
            sin_term = self.sin_amplitudes[i] * np.sin(self.sin_frequencies[i] * xi + self.sin_phases[i])
            # Add higher harmonic terms
            sin_term += 0.5 * self.sin_amplitudes[i] * np.sin(2 * self.sin_frequencies[i] * xi + self.sin_phases[i])
            sin_sum += sin_term
        
        # Enhanced radial basis function component with weighted combinations
        rbf_sum = 0
        for i in range(8):  # 8 RBF centers for increased complexity
            rbf_term = 0
            for j in range(self.dim):
                rbf_term += (x[j] - self.rbf_centers[j][i])**2
            # Use different weighting schemes for enhanced landscape complexity
            rbf_sum += self.rbf_weights[i] * np.exp(-rbf_term / (2 * self.rbf_widths[i]**2))
        
        # Enhanced cross-dimensional interaction with quadratic terms
        interaction_sum = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Add quadratic coupling for more complex interactions
                    interaction_sum += self.interaction_matrix[i][j] * x[i] * x[j]
                    # Add cubic terms for additional complexity
                    interaction_sum += 0.1 * self.interaction_matrix[i][j] * x[i]**2 * x[j]
        
        # Add noise component to increase landscape complexity
        noise_component = np.sum(np.random.normal(0, self.noise_level, self.dim) * x)
        
        # Combine all components with enhanced conditioning and multimodality
        result = (0.7 * sin_sum + 
                 1.5 * rbf_sum + 
                 0.4 * interaction_sum + 
                 0.2 * noise_component) * self.conditioning_factor * self.multimodal_factor
        
        return result
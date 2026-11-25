import numpy as np

class SinusoidalRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Sinusoidal parameters
        self.sin_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.sin_frequencies = np.random.uniform(1.0, 8.0, dim)
        self.sin_phases = np.random.uniform(0, 2*np.pi, dim)
        # Radial basis function parameters
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 5))
        self.rbf_widths = np.random.uniform(0.5, 3.0, 5)
        self.rbf_weights = np.random.uniform(-1.0, 1.0, 5)
        # Cross-dimensional interaction coefficients
        self.interaction_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Conditioning and multimodality control
        self.conditioning_factor = np.random.uniform(0.5, 2.0)
        self.multimodal_factor = np.random.uniform(1.5, 3.0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal component
        sin_sum = 0
        for i in range(self.dim):
            xi = x[i]
            sin_term = self.sin_amplitudes[i] * np.sin(self.sin_frequencies[i] * xi + self.sin_phases[i])
            sin_sum += sin_term
        
        # Radial basis function component
        rbf_sum = 0
        for i in range(5):  # 5 RBF centers
            rbf_term = 0
            for j in range(self.dim):
                rbf_term += (x[j] - self.rbf_centers[j][i])**2
            rbf_sum += self.rbf_weights[i] * np.exp(-rbf_term / (2 * self.rbf_widths[i]**2))
        
        # Cross-dimensional interaction
        interaction_sum = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_sum += self.interaction_matrix[i][j] * x[i] * x[j]
        
        # Combine all components with conditioning and multimodality
        result = (0.5 * sin_sum + 
                 1.2 * rbf_sum + 
                 0.3 * interaction_sum) * self.conditioning_factor * self.multimodal_factor
        
        return result
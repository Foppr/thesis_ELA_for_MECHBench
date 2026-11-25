import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Parameters for radial basis functions
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 10))
        self.rbf_weights = np.random.uniform(0.5, 2.0, 10)
        self.rbf_widths = np.random.uniform(0.5, 3.0, 10)
        
        # Sinusoidal components with varying frequencies and amplitudes
        self.sin_frequencies = np.random.uniform(1.0, 10.0, dim)
        self.sin_amplitudes = np.random.uniform(0.5, 2.0, dim)
        
        # Cross-dimensional interaction terms
        self.cross_weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        
        # Conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 5.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Radial basis function components
        for i in range(10):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x_norm[j] - self.rbf_centers[j, i])**2
            f_val += self.rbf_weights[i] * np.exp(-self.rbf_widths[i] * rbf_sum)
        
        # Sinusoidal components
        for i in range(self.dim):
            f_val += self.sin_amplitudes[i] * np.sin(self.sin_frequencies[i] * x_norm[i])**2
        
        # Cross-dimensional interactions
        for i in range(self.dim):
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    interaction_sum += self.cross_weights[i, j] * np.sin(x_norm[i] * x_norm[j])
            f_val += 0.5 * interaction_sum**2
        
        # Conditioning variation across dimensions
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * x_norm[i]**4
        
        # Add a global oscillatory component
        global_osc = np.sin(np.sum(x_norm**2))
        f_val += 0.3 * global_osc**2
        
        # Add noise to increase complexity
        noise = 0.01 * np.sum(np.sin(17 * x_norm) + np.cos(11 * x_norm))
        f_val += noise
        
        return f_val
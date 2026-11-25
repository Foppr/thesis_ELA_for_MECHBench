import numpy as np

class MultiModalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial potential coefficients
        self.poly_degrees = np.random.randint(3, 6, dim)
        self.poly_coefficients = np.random.rand(dim) * 2.0 - 1.0
        # Gaussian noise parameters for each dimension
        self.noise_amplitudes = np.random.rand(dim) * 0.5 + 0.1
        self.noise_frequencies = np.random.rand(dim) * 2.0 + 1.0
        # Ridge shaping parameters
        self.ridge_widths = np.random.rand(dim) * 2.0 + 1.0
        self.ridge_heights = np.random.rand(dim) * 3.0 + 1.0
        # Cross-dimensional coupling with adaptive weights
        self.coupling_weights = np.random.rand(dim, dim) * 0.8 - 0.4
        self.coupling_exponents = np.random.rand(dim, dim) * 2.0 + 1.0
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial potential component
        poly_potential = 0.0
        for i in range(self.dim):
            poly_potential += self.poly_coefficients[i] * (x_norm[i] ** self.poly_degrees[i])
            
        # Gaussian noise injection component
        gaussian_noise = 0.0
        for i in range(self.dim):
            gaussian_noise += self.noise_amplitudes[i] * np.exp(-0.5 * (x_norm[i] * self.noise_frequencies[i])**2)
            
        # Ridge shaping component
        ridge_shaping = 0.0
        for i in range(self.dim):
            ridge_shaping += self.ridge_heights[i] * np.exp(-0.5 * (x_norm[i] / self.ridge_widths[i])**2)
            
        # Cross-dimensional coupling with adaptive interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_coupling += (self.coupling_weights[i, j] * 
                                     (x_norm[i] ** self.coupling_exponents[i, j]) * 
                                     np.sin(x_norm[j]))
        
        # Combined function with adaptive scaling
        return (1.2 * poly_potential + 0.8 * gaussian_noise + 0.6 * ridge_shaping + 
                0.4 * cross_coupling + 1.0)
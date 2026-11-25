import numpy as np

class SinusoidalRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for sinusoidal components
        self.sin_frequencies = np.random.uniform(1.0, 10.0, dim)
        self.sin_amplitudes = np.random.uniform(0.5, 3.0, dim)
        self.sin_phases = np.random.uniform(0, 2*np.pi, dim)
        
        # Initialize radial basis function parameters
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 10))
        self.rbf_widths = np.random.uniform(0.5, 3.0, 10)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, 10)
        
        # Initialize cross-dimensional interaction coefficients
        self.cross_coeffs = np.random.uniform(-1.0, 1.0, (dim, dim))
        
        # Additional noise and scaling parameters
        self.noise_level = np.random.uniform(0.01, 0.5)
        self.scaling_factor = np.random.uniform(0.5, 2.0)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Compute sinusoidal components
        sin_sum = 0.0
        for i in range(self.dim):
            sin_component = self.sin_amplitudes[i] * np.sin(self.sin_frequencies[i] * x_norm[i] + self.sin_phases[i])
            sin_sum += sin_component
        
        # Compute radial basis function components
        rbf_sum = 0.0
        for j in range(10):
            rbf_term = 0.0
            for i in range(self.dim):
                rbf_term += np.exp(-0.5 * ((x_norm[i] - self.rbf_centers[i, j]) / self.rbf_widths[j])**2)
            rbf_sum += self.rbf_weights[j] * rbf_term
        
        # Compute cross-dimensional interactions
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_sum += self.cross_coeffs[i, j] * x_norm[i] * x_norm[j]
        
        # Add noise and scale
        noise = np.random.normal(0, self.noise_level)
        result = self.scaling_factor * (sin_sum + rbf_sum + cross_sum) + noise
        
        return result
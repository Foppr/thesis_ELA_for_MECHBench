import numpy as np

class SinusoidalRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for chaotic sinusoidal components
        self.sin_frequencies = np.random.uniform(5.0, 20.0, dim)
        self.sin_amplitudes = np.random.uniform(2.0, 8.0, dim)
        self.sin_phases = np.random.uniform(0, 4*np.pi, dim)
        
        # Initialize radial basis function parameters
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 15))
        self.rbf_widths = np.random.uniform(0.2, 5.0, 15)
        self.rbf_weights = np.random.uniform(-5.0, 5.0, 15)
        
        # Initialize cross-dimensional interaction coefficients
        self.cross_coeffs = np.random.uniform(-2.0, 2.0, (dim, dim))
        
        # Add fractal noise parameters
        self.fractal_noise = np.random.uniform(0.1, 1.0, dim)
        self.fractal_scale = np.random.uniform(0.5, 3.0)
        
        # Adaptive scaling and additional complexity
        self.scaling_factor = np.random.uniform(1.0, 5.0)
        self.adaptive_exponent = np.random.uniform(1.5, 4.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Compute chaotic sinusoidal components with fractal modulation
        sin_sum = 0.0
        for i in range(self.dim):
            # Add fractal noise component
            fractal_component = self.fractal_noise[i] * np.sin(self.sin_frequencies[i] * x_norm[i] + self.sin_phases[i])
            # Apply adaptive exponent for non-linearity
            sin_component = self.sin_amplitudes[i] * np.sin(self.sin_frequencies[i] * x_norm[i] + self.sin_phases[i]) ** self.adaptive_exponent[i]
            sin_sum += sin_component + fractal_component
        
        # Compute enhanced radial basis function components
        rbf_sum = 0.0
        for j in range(15):
            rbf_term = 0.0
            for i in range(self.dim):
                rbf_term += np.exp(-0.5 * ((x_norm[i] - self.rbf_centers[i, j]) / self.rbf_widths[j])**2)
            rbf_sum += self.rbf_weights[j] * rbf_term
        
        # Compute enhanced cross-dimensional interactions
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_sum += self.cross_coeffs[i, j] * x_norm[i] * x_norm[j]
        
        # Add fractal scaling effect
        result = self.scaling_factor * (sin_sum + rbf_sum + cross_sum) * self.fractal_scale
        
        return result
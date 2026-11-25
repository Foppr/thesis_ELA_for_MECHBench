import numpy as np

class SinusoidalRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for enhanced sinusoidal components with asymmetric modulation
        self.sin_frequencies = np.random.uniform(2.0, 15.0, dim)
        self.sin_amplitudes = np.random.uniform(1.0, 4.0, dim)
        self.sin_phases = np.random.uniform(0, 2*np.pi, dim)
        # Add asymmetric frequency modulation for enhanced complexity
        self.freq_modulation = np.random.uniform(0.5, 2.0, dim)
        
        # Initialize enhanced radial basis function parameters
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 15))
        self.rbf_widths = np.random.uniform(0.3, 2.5, 15)
        self.rbf_weights = np.random.uniform(-3.0, 3.0, 15)
        
        # Initialize enhanced cross-dimensional interaction coefficients
        self.cross_coeffs = np.random.uniform(-2.0, 2.0, (dim, dim))
        
        # Additional adaptive noise and scaling parameters
        self.noise_level = np.random.uniform(0.02, 0.8)
        self.scaling_factor = np.random.uniform(0.3, 2.5)
        self.adaptive_exponent = np.random.uniform(1.5, 3.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Compute enhanced sinusoidal components with asymmetric modulation
        sin_sum = 0.0
        for i in range(self.dim):
            # Apply frequency modulation based on dimension index for more complex structure
            modulated_freq = self.sin_frequencies[i] * (1.0 + 0.3 * np.sin(i * 0.5))
            sin_component = self.sin_amplitudes[i] * np.sin(modulated_freq * x_norm[i] + self.sin_phases[i]) * (1.0 + 0.5 * np.sin(2.0 * x_norm[i]))
            sin_sum += sin_component
        
        # Compute enhanced radial basis function components with clustering effect
        rbf_sum = 0.0
        for j in range(15):
            rbf_term = 0.0
            for i in range(self.dim):
                # Add clustering by using different widths per RBF center
                cluster_width = self.rbf_widths[j] * (1.0 + 0.2 * np.sin(j * 0.7))
                rbf_term += np.exp(-0.5 * ((x_norm[i] - self.rbf_centers[i, j]) / cluster_width)**2)
            rbf_sum += self.rbf_weights[j] * rbf_term
        
        # Compute enhanced cross-dimensional interactions with asymmetric coupling
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Introduce asymmetry in coupling coefficients
                    asym_coeff = self.cross_coeffs[i, j] * (1.0 + 0.2 * np.cos(i * 0.3))
                    cross_sum += asym_coeff * x_norm[i] * x_norm[j] * (1.0 + 0.3 * np.cos(x_norm[i] + x_norm[j]))
        
        # Add adaptive scaling and noise
        noise = np.random.normal(0, self.noise_level)
        result = self.scaling_factor * (sin_sum + rbf_sum + cross_sum) + noise
        
        return result
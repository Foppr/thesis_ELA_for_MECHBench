import numpy as np

class ChaoticSinusoidalRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic sinusoidal components with quantum-like frequency modulation
        self.sin_frequencies = np.random.uniform(1.0, 25.0, dim)
        self.sin_amplitudes = np.random.uniform(0.5, 6.0, dim)
        self.sin_phases = np.random.uniform(0, 2*np.pi, dim)
        # Add chaotic modulation using logistic map for enhanced complexity
        self.chaos_params = np.random.uniform(3.5, 4.0, dim)
        
        # Initialize quantum-inspired radial basis function parameters
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 25))
        self.rbf_widths = np.random.uniform(0.1, 3.0, 25)
        self.rbf_weights = np.random.uniform(-5.0, 5.0, 25)
        
        # Initialize cross-dimensional energy coupling with quantum tunneling effects
        self.cross_coeffs = np.random.uniform(-3.0, 3.0, (dim, dim))
        self.tunneling_coeffs = np.random.uniform(0.1, 1.0, (dim, dim))
        
        # Add adaptive noise parameters with temporal correlation
        self.noise_level = np.random.uniform(0.05, 1.5)
        self.noise_correlation = np.random.uniform(0.3, 0.9)
        self.scaling_factor = np.random.uniform(0.1, 3.0)
        self.adaptive_exponent = np.random.uniform(2.0, 4.0, dim)
        
        # Add chaotic phase shifts for enhanced multimodality
        self.phase_shifts = np.random.uniform(-np.pi, np.pi, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Compute chaotic sinusoidal components with quantum-like modulation
        sin_sum = 0.0
        for i in range(self.dim):
            # Apply chaotic frequency modulation using logistic map
            chaos_factor = self.chaos_params[i]
            modulated_freq = self.sin_frequencies[i] * (1.0 + 0.4 * np.sin(chaos_factor * x_norm[i]))
            sin_component = self.sin_amplitudes[i] * np.sin(modulated_freq * x_norm[i] + self.sin_phases[i] + self.phase_shifts[i])
            # Add quantum-like interference terms
            sin_component += 0.3 * np.sin(2.0 * modulated_freq * x_norm[i] + self.sin_phases[i]) * np.cos(x_norm[i])
            sin_sum += sin_component
        
        # Compute quantum-inspired radial basis function components with enhanced clustering
        rbf_sum = 0.0
        for j in range(25):
            rbf_term = 0.0
            for i in range(self.dim):
                # Add quantum-like tunneling effect to RBF widths
                tunnel_width = self.rbf_widths[j] * (1.0 + 0.3 * np.sin(j * 0.8 + x_norm[i]))
                rbf_term += np.exp(-0.5 * ((x_norm[i] - self.rbf_centers[i, j]) / tunnel_width)**2)
            # Add quantum weight interference
            quantum_weight = self.rbf_weights[j] * (1.0 + 0.2 * np.cos(j * 0.6))
            rbf_sum += quantum_weight * rbf_term
        
        # Compute cross-dimensional energy coupling with quantum tunneling effects
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Introduce quantum tunneling between dimensions
                    tunnel_coeff = self.tunneling_coeffs[i, j] * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2)
                    asym_coeff = self.cross_coeffs[i, j] * (1.0 + 0.3 * np.sin(i * 0.4 + j * 0.3))
                    cross_sum += asym_coeff * x_norm[i] * x_norm[j] * tunnel_coeff
        
        # Add adaptive scaling and chaotic noise with correlation
        noise = np.random.normal(0, self.noise_level)
        # Add temporal correlation to noise
        if hasattr(self, 'prev_noise'):
            noise = 0.5 * noise + 0.5 * self.prev_noise
        self.prev_noise = noise
        
        result = self.scaling_factor * (sin_sum + rbf_sum + cross_sum) + noise
        
        # Add fitness variance control by applying adaptive exponent to final result
        if self.dim > 1:
            variance_factor = np.std(x_norm) * 0.5 + 0.5
            result *= (1.0 + 0.2 * variance_factor)
        
        return result
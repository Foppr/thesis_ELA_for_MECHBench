import numpy as np

class ChaoticSinusoidalRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic sinusoidal components with quantum-inspired frequencies
        self.sin_frequencies = np.random.uniform(1.0, 25.0, dim)
        self.sin_amplitudes = np.random.uniform(0.5, 6.0, dim)
        self.sin_phases = np.random.uniform(0, 2*np.pi, dim)
        # Add hyperchaotic frequency modulation using double golden ratio for enhanced complexity
        self.freq_modulation = np.power(np.full(dim, (3 + np.sqrt(5)) / 2), np.arange(dim))
        
        # Initialize quantum-inspired radial basis function parameters
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 25))
        self.rbf_widths = np.random.uniform(0.1, 4.0, 25)
        self.rbf_weights = np.random.uniform(-5.0, 5.0, 25)
        
        # Initialize ternary cross-dimensional interaction coefficients
        self.cross_coeffs = np.random.uniform(-4.0, 4.0, (dim, dim, dim))
        
        # Additional dynamic noise and scaling parameters
        self.noise_level = np.random.uniform(0.01, 1.5)
        self.scaling_factor = np.random.uniform(0.2, 3.5)
        self.adaptive_exponent = np.random.uniform(2.0, 5.0, dim)
        # Add hyperchaotic phase drift for time-dependent complexity
        self.phase_drift = np.random.uniform(-0.8, 0.8, dim)
        # Add hyperchaotic energy terms
        self.energy_coeffs = np.random.uniform(-2.0, 2.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Compute chaotic sinusoidal components with quantum frequency modulation
        sin_sum = 0.0
        for i in range(self.dim):
            # Apply hyperchaotic frequency modulation with double golden ratio progression
            modulated_freq = self.sin_frequencies[i] * self.freq_modulation[i]
            # Add quantum-like phase drift for enhanced complexity
            quantum_phase = self.sin_phases[i] + self.phase_drift[i] * np.sin(x_norm[i])
            sin_component = self.sin_amplitudes[i] * np.sin(modulated_freq * x_norm[i] + quantum_phase)
            # Add ternary interaction term for enhanced multimodality
            if i > 0:
                sin_component += 0.4 * np.sin(2.5 * x_norm[i-1] * x_norm[i])
            sin_sum += sin_component
        
        # Compute quantum-inspired radial basis function components with dynamic clustering
        rbf_sum = 0.0
        for j in range(25):
            rbf_term = 0.0
            for i in range(self.dim):
                # Dynamic width adjustment based on RBF index and dimension
                dynamic_width = self.rbf_widths[j] * (1.0 + 0.4 * np.sin(j * 0.5 + i * 0.25))
                rbf_term += np.exp(-0.5 * ((x_norm[i] - self.rbf_centers[i, j]) / dynamic_width)**2)
            # Add quantum weight modulation
            quantum_weight = self.rbf_weights[j] * (1.0 + 0.3 * np.cos(j * 0.4))
            rbf_sum += quantum_weight * rbf_term
        
        # Compute ternary cross-dimensional interactions with hyperchaotic coupling
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k:
                        # Introduce ternary hyperchaotic coupling coefficients
                        ternary_coeff = self.cross_coeffs[i, j, k] * (1.0 + 0.2 * np.sin(i * 0.6 + j * 0.4 + k * 0.8))
                        cross_sum += ternary_coeff * x_norm[i] * x_norm[j] * x_norm[k]
        
        # Add hyperchaotic energy terms
        energy_term = 0.0
        for i in range(self.dim):
            energy_term += self.energy_coeffs[i] * np.sin(3.0 * x_norm[i]) * np.cos(2.0 * x_norm[i])
        
        # Add adaptive scaling, dynamic noise, and hyperchaotic exponentiation
        noise = np.random.normal(0, self.noise_level)
        result = self.scaling_factor * (sin_sum + rbf_sum + cross_sum + energy_term) + noise
        
        # Apply hyperchaotic exponentiation for enhanced multimodality
        chaotic_exponent = np.prod(np.abs(x_norm)) if len(x_norm) > 0 else 1.0
        result = result * (1.0 + 0.6 * np.sin(chaotic_exponent))
        
        return result
import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with higher complexity
        self.chebyshev_coeffs = np.random.uniform(-1.0, 1.0, (dim, 7))
        self.chebyshev_degrees = np.random.randint(3, 10, dim)
        # Sinusoidal components with hyperbolic tangent modulations
        self.frequencies = np.random.uniform(2.0, 15.0, dim)
        self.amplitudes = np.random.uniform(1.0, 5.0, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Hyperbolic tangent modulations for additional nonlinearity
        self.tanh_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.tanh_rates = np.random.uniform(0.1, 3.0, dim)
        self.tanh_offsets = np.random.uniform(-2.0, 2.0, dim)
        # Exponential modulations with additional terms
        self.exp_rates = np.random.uniform(0.05, 3.0, dim)
        self.exp_offsets = np.random.uniform(-2.0, 2.0, dim)
        self.exp_scaling = np.random.uniform(0.5, 2.5, dim)
        # Conditioning and scaling with adaptive weights
        self.conditioning = np.random.uniform(1.0, 20.0, dim)
        self.adaptive_weights = np.random.uniform(0.1, 2.0, dim)
        # Cross-dimension coupling with chaotic interaction and higher-order terms
        self.coupling_matrix = np.random.uniform(-1.0, 1.0, (dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0.0)
        # Chaotic base for additional complexity with multiple maps
        self.chaos_seed = np.random.uniform(0.5, 3.0, dim)
        self.chaos_map_params = np.random.uniform(0.1, 2.0, (dim, 3))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1] for periodic components
        normalized_x = x / 5.0
        
        # Compute Chebyshev polynomial components with higher degree terms
        chebyshev_components = np.zeros(self.dim)
        for i in range(self.dim):
            # Evaluate Chebyshev polynomials of different degrees
            T = np.cos(self.chebyshev_degrees[i] * np.arccos(np.clip(normalized_x[i], -1, 1)))
            chebyshev_components[i] = np.sum(self.chebyshev_coeffs[i] * T)
            
        # Compute sinusoidal components with hyperbolic tangent modulations
        sinusoidal_components = np.zeros(self.dim)
        for i in range(self.dim):
            base_term = self.amplitudes[i] * np.sin(
                self.frequencies[i] * normalized_x[i] + self.phases[i]
            )
            tanh_modulation = self.tanh_amplitudes[i] * np.tanh(
                self.tanh_rates[i] * (normalized_x[i] - self.tanh_offsets[i])
            )
            exp_modulation = np.exp(-self.exp_rates[i] * (normalized_x[i] - self.exp_offsets[i])**2)
            sinusoidal_components[i] = base_term * tanh_modulation * exp_modulation * self.conditioning[i]
            
        # Add chaotic component with multiple map types
        chaotic_component = np.zeros(self.dim)
        for i in range(self.dim):
            # Logistic map-like chaotic behavior
            chaos_val = (self.chaos_seed[i] * normalized_x[i] * (1 - normalized_x[i]))
            # Additional chaotic maps for increased complexity
            logistic_map = self.chaos_map_params[i, 0] * normalized_x[i] * (1 - normalized_x[i])
            tent_map = self.chaos_map_params[i, 1] * np.abs(2 * normalized_x[i] - 1)
            sin_map = self.chaos_map_params[i, 2] * np.sin(2 * np.pi * normalized_x[i])
            chaotic_component[i] = np.sin(15 * chaos_val) + 0.5 * np.sin(7 * logistic_map) + 0.3 * np.sin(5 * tent_map) + 0.2 * np.sin(3 * sin_map)
            
        # Combine all components with cross-dimension coupling
        fitness = 0.0
        for i in range(self.dim):
            # Polynomial-like combination of components with higher-order terms
            component_value = (chebyshev_components[i] + 
                              sinusoidal_components[i] + 
                              chaotic_component[i])
            # Add higher-order and non-polynomial terms for increased complexity
            fitness += (component_value**2 + 0.5 * component_value**3 + 
                       0.2 * np.abs(component_value)**1.7 + 
                       0.1 * np.sin(5 * component_value) + 
                       0.05 * np.cos(3 * component_value))
            
        # Cross-dimension coupling with chaotic interaction and higher-order terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term += (self.coupling_matrix[i, j] * 
                                    np.sin(sinusoidal_components[i]) * 
                                    np.cos(chebyshev_components[j]) *
                                    np.exp(-0.1 * (x[i] - x[j])**2))
                    
        # Add final exponential penalty and scaling with adaptive weights
        return fitness + 0.3 * coupling_term + 0.15 * np.sum(np.exp(self.adaptive_weights * 0.5 * x**2))
import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.chebyshev_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))
        self.chebyshev_degrees = np.random.randint(2, 6, dim)
        # Sinusoidal components with varying frequencies and amplitudes
        self.frequencies = np.random.uniform(1.0, 8.0, dim)
        self.amplitudes = np.random.uniform(0.5, 3.0, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Exponential modulations
        self.exp_rates = np.random.uniform(0.1, 2.0, dim)
        self.exp_offsets = np.random.uniform(-1.0, 1.0, dim)
        # Conditioning and scaling
        self.conditioning = np.random.uniform(0.5, 15.0, dim)
        # Cross-dimension coupling with chaotic interaction
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0.0)
        # Chaotic base for additional complexity
        self.chaos_seed = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1] for periodic components
        normalized_x = x / 5.0
        
        # Compute Chebyshev polynomial components
        chebyshev_components = np.zeros(self.dim)
        for i in range(self.dim):
            # Evaluate Chebyshev polynomials of different degrees
            T = np.cos(self.chebyshev_degrees[i] * np.arccos(np.clip(normalized_x[i], -1, 1)))
            chebyshev_components[i] = np.sum(self.chebyshev_coeffs[i] * T)
            
        # Compute sinusoidal components with exponential modulations
        sinusoidal_components = np.zeros(self.dim)
        for i in range(self.dim):
            base_term = self.amplitudes[i] * np.sin(
                self.frequencies[i] * normalized_x[i] + self.phases[i]
            )
            exp_modulation = np.exp(-self.exp_rates[i] * (normalized_x[i] - self.exp_offsets[i])**2)
            sinusoidal_components[i] = base_term * exp_modulation * self.conditioning[i]
            
        # Add chaotic component
        chaotic_component = np.zeros(self.dim)
        for i in range(self.dim):
            # Logistic map-like chaotic behavior
            chaos_val = (self.chaos_seed[i] * normalized_x[i] * (1 - normalized_x[i]))
            chaotic_component[i] = np.sin(10 * chaos_val) if chaos_val != 0 else 0
            
        # Combine all components with cross-dimension coupling
        fitness = 0.0
        for i in range(self.dim):
            # Polynomial-like combination of components
            component_value = (chebyshev_components[i] + 
                              sinusoidal_components[i] + 
                              chaotic_component[i])
            # Add higher-order terms for increased complexity
            fitness += (component_value**2 + 0.3 * component_value**3 + 
                       0.1 * np.abs(component_value)**1.5)
            
        # Cross-dimension coupling with chaotic interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term += (self.coupling_matrix[i, j] * 
                                    np.sin(sinusoidal_components[i]) * 
                                    np.cos(chebyshev_components[j]))
                    
        # Add final exponential penalty and scaling
        return fitness + 0.2 * coupling_term + 0.1 * np.sum(np.exp(0.5 * x**2))
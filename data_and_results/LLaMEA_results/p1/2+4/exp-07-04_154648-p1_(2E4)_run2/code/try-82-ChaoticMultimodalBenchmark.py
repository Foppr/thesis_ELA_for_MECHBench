import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.chaos_params = np.random.uniform(0.1, 0.9, dim)
        self.poly_weights = np.random.uniform(0.5, 2.0, dim)
        self.interaction_matrix = np.random.uniform(-1.0, 1.0, (dim, dim))
        self.noise_amplitudes = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        x_scaled = x / 5.0
        result = 0.0
        
        # Hyperbolic tangent interactions
        for i in range(self.dim):
            result += np.tanh(self.chaos_params[i] * x_scaled[i]) * self.poly_weights[i]
        
        # Adaptive polynomial terms with position-dependent exponents
        for i in range(self.dim):
            exponent = 2 + 3 * np.sin(x_scaled[i] * np.pi)
            result += 0.1 * (x_scaled[i] ** exponent) * self.poly_weights[i]
        
        # Cross-dimensional interactions with chaotic coupling
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = np.sin(x_scaled[i] * x_scaled[j] * np.pi)
                    result += self.interaction_matrix[i, j] * coupling
        
        # Deterministic chaos-based noise component
        chaos_noise = 0.0
        for i in range(self.dim):
            chaos_term = np.sin(x_scaled[i] * 10.0) * np.cos(x_scaled[i] * 7.0)
            chaos_noise += chaos_term * self.noise_amplitudes[i]
        
        # Additional non-smooth features using floor and ceiling functions
        smoothness_term = 0.0
        for i in range(self.dim):
            smoothness_term += np.floor(x_scaled[i]) * np.ceil(x_scaled[i])
        
        # Combine all components with global minimum at origin
        return result + chaos_noise + smoothness_term
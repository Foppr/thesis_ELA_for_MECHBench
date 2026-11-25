import numpy as np

class PolynomialChaosSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial chaos coefficients
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 10))
        self.chaos_orders = np.random.randint(2, 6, dim)
        # Saddle point configuration
        self.saddle_points = np.random.uniform(-3.0, 3.0, (dim, 8))
        self.saddle_weights = np.random.uniform(0.5, 2.0, (dim, 8))
        # Adaptive noise parameters
        self.noise_amplitude = np.random.uniform(0.1, 1.0, dim)
        self.noise_frequency = np.random.uniform(0.5, 3.0, dim)
        self.noise_decay = np.random.uniform(0.9, 0.99, dim)
        # Dynamic landscape parameters
        self.dynamical_exponent = np.random.uniform(1.5, 4.0, dim)
        self.interaction_strength = np.random.uniform(0.1, 2.0, (dim, dim))
        self.resonance_freq = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component
        poly_term = 0.0
        for i in range(self.dim):
            term = 0.0
            for j in range(min(10, self.chaos_orders[i] + 3)):
                term += self.poly_coeffs[i, j] * (x[i] ** j)
            poly_term += term
            
        # Saddle point dynamics component
        saddle_term = 0.0
        for i in range(self.dim):
            min_dist = float('inf')
            for k in range(8):
                dist = np.abs(x[i] - self.saddle_points[i, k])
                if dist < min_dist:
                    min_dist = dist
            # Saddle point attraction with weighted influence
            saddle_term += self.saddle_weights[i, 0] * np.exp(-min_dist**2) + \
                          self.saddle_weights[i, 1] * np.sin(self.resonance_freq[i] * x[i])
            
        # Adaptive noise component
        noise_term = 0.0
        for i in range(self.dim):
            noise = self.noise_amplitude[i] * np.sin(self.noise_frequency[i] * x[i]) * \
                   np.exp(-self.noise_decay[i] * np.abs(x[i]))
            noise_term += noise
            
        # Dynamical interaction component
        dynamic_term = 0.0
        for i in range(self.dim):
            interaction = 0.0
            for j in range(self.dim):
                if i != j:
                    interaction += self.interaction_strength[i, j] * np.sin(x[i] - x[j])
            dynamic_term += (x[i]**self.dynamical_exponent[i]) + interaction
            
        # Combine all components with adaptive weights
        total = 0.4 * poly_term + 0.3 * saddle_term + 0.2 * noise_term + 0.1 * dynamic_term
        
        return total
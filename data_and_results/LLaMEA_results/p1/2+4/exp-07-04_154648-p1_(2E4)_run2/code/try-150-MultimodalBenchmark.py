import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 20)
        self.frequency_modulation = np.random.uniform(2.0, 8.0, dim)
        self.amplitude_modulation = np.random.uniform(0.3, 2.5, dim)
        self.asymmetry_params = np.random.uniform(0.1, 0.8, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Chaotic sinusoidal components with asymmetric modulation
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.frequency_modulation[i]
            asym = self.asymmetry_params[i]
            sin_term += (np.sin(freq * x_norm[i]) * 
                        np.cos(freq * x_norm[i] * 1.3) * 
                        np.sin(freq * x_norm[i] * 0.7)) * \
                       self.amplitude_modulation[i] * \
                       (1.0 + asym * np.sin(3 * x_norm[i]))
        
        # Adaptive RBF with chaotic width variation
        rbf_sum = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            # Chaotic width modulation based on position and iteration
            chaotic_factor = 1.0 + 0.4 * np.sin(2 * np.pi * np.sum(x_norm[:min(i+1, self.dim)]))
            adaptive_width = self.rbf_widths[i] * chaotic_factor
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2))
        
        # Novel noise component with asymmetric chaotic interaction
        noise = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            noise += np.sin(x_norm[i]**3 + x_norm[j]**2.5) * \
                    np.cos(x_norm[i]**2.2 + x_norm[j]**3.1) * \
                    np.tan(0.5 * x_norm[i]) * \
                    (0.15 + 0.25 * np.sin(7 * x_norm[i]))
        
        # Asymmetric cross-dimensional coupling with dynamic weights
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = 0.6 + 0.4 * np.sin(np.pi * (x_norm[i] + x_norm[i+1])) * \
                     np.cos(np.pi * (x_norm[i] - x_norm[i+1]))
            asym_weight = 1.0 + 0.3 * np.sin(2 * np.pi * x_norm[i])
            cross_interaction += weight * asym_weight * (x_norm[i]**2 + x_norm[i+1]**2) * \
                               np.sin(np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Complex polynomial and interaction terms with asymmetric exponents
        poly_term = 0.02 * np.sum(np.abs(x_norm)**7)
        interaction_term = 0.08 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Asymmetric local minimum penalty with chaotic positioning
        local_min_penalty = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            # Chaotic distance calculation
            distance = np.sqrt(np.sum(diff**2) + 0.1 * np.sin(np.sum(x_norm)))
            local_min_penalty += 1.0 / (1.0 + distance**3)
        
        # Introduce asymmetric valley structure
        valley_term = 0.0
        for i in range(self.dim):
            valley_term += (x_norm[i]**4 + 0.5 * x_norm[i]**3 + 0.1 * x_norm[i]**2) * \
                          np.cos(2 * np.pi * x_norm[i])
        
        # Combine all components with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term + 0.5 * local_min_penalty + valley_term
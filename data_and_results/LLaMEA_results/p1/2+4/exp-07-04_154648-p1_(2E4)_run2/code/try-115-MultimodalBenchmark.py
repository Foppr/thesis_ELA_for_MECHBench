import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 20)
        self.frequency_modulation = np.random.uniform(2.0, 8.0, dim)
        self.amplitude_modulation = np.random.uniform(0.3, 2.5, dim)
        self.interaction_weights = np.random.uniform(0.1, 1.5, (dim, dim))
        self.chaotic_params = np.random.uniform(0.5, 3.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Chaotic sinusoidal components with dynamic parameters
        sin_term = 0.0
        for i in range(self.dim):
            chaotic_factor = np.sin(self.chaotic_params[i] * x_norm[i])
            sin_term += (np.sin(self.frequency_modulation[i] * x_norm[i] * chaotic_factor) * 
                        np.cos(self.frequency_modulation[i] * x_norm[i] * 1.5 * chaotic_factor)) * \
                       self.amplitude_modulation[i]
        
        # Adaptive RBF with chaotic width modulation
        rbf_sum = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            # Widths vary based on chaotic function of position
            adaptive_width = self.rbf_widths[i] * (1.0 + 0.5 * np.sin(3.0 * np.sum(np.abs(x_norm))))
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2))
        
        # Novel noise component with multi-scale chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x_norm[i]**3 + x_norm[(i+1) % self.dim]**2 + 
                           0.3 * np.sin(7 * x_norm[i])) * \
                    np.cos(x_norm[i]**2 + x_norm[(i+1) % self.dim]**3 + 
                           0.4 * np.cos(5 * x_norm[(i+1) % self.dim])) * \
                    (0.15 + 0.25 * np.sin(8 * x_norm[i]))
        
        # Cross-dimensional coupling with chaotic interaction weights
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    weight = self.interaction_weights[i, j] * (1.0 + 0.3 * np.sin(4.0 * (x_norm[i] + x_norm[j])))
                    cross_interaction += weight * np.sin(np.pi * (x_norm[i] + x_norm[j])) * \
                                       (x_norm[i]**2 + x_norm[j]**2)
        
        # Additional polynomial and interaction terms for increased complexity
        poly_term = 0.02 * np.sum(x_norm**7)
        interaction_term = 0.08 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Introduce a new term that penalizes proximity to previous local minima with chaotic penalty
        # to increase challenge for optimization algorithms
        local_min_penalty = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            distance = np.sqrt(np.sum(diff**2))
            penalty_factor = 1.0 + 0.5 * np.sin(5.0 * distance)
            local_min_penalty += penalty_factor / (1.0 + distance**2)
        
        # Add a global scaling factor that varies with problem dimension
        dimension_factor = 1.0 + 0.1 * np.log(self.dim)
        
        # Combine all components with global minimum at origin
        return dimension_factor * (sin_term + rbf_sum + noise + cross_interaction + 
                                 poly_term + interaction_term + 0.3 * local_min_penalty)
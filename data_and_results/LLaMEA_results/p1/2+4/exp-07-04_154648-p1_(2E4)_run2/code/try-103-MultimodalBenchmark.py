import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 20)
        self.frequency_modulation = np.random.uniform(2.0, 10.0, dim)
        self.amplitude_modulation = np.random.uniform(0.3, 3.0, dim)
        self.chaotic_params = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Enhanced chaotic sinusoidal components
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += (np.sin(self.frequency_modulation[i] * x_norm[i]) * 
                        np.cos(self.frequency_modulation[i] * x_norm[i] * 1.7) * 
                        np.sin(self.frequency_modulation[i] * x_norm[i] * 0.8)) * \
                       self.amplitude_modulation[i] * \
                       (1.0 + 0.3 * np.sin(3.0 * x_norm[i]))
        
        # Dynamic RBF with chaotic width modulation and multiple peaks
        rbf_sum = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            adaptive_width = self.rbf_widths[i] * (1.0 + 0.5 * np.abs(x_norm).mean() + 
                                                  0.2 * np.sin(2.0 * np.sum(x_norm)))
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2)) * \
                       (1.0 + 0.1 * np.sin(5.0 * np.sum(diff**2)))
        
        # Novel chaotic noise with multi-scale modulation
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x_norm[i]**3 + x_norm[(i+1) % self.dim]**2 + 
                           self.chaotic_params[i] * np.sin(10 * x_norm[i])) * \
                    np.cos(x_norm[i]**2 + x_norm[(i+1) % self.dim]**3 + 
                           self.chaotic_params[(i+2) % self.dim] * np.cos(7 * x_norm[i])) * \
                    (0.15 + 0.25 * np.sin(7 * x_norm[i]) * np.cos(4 * x_norm[(i+1) % self.dim]))
        
        # Cross-dimensional coupling with chaotic interaction weights
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = 0.6 + 0.4 * np.sin(np.pi * (x_norm[i] + x_norm[i+1]) * 
                                      (1.0 + 0.3 * np.sin(5 * x_norm[i])))
            cross_interaction += weight * (x_norm[i]**3 + x_norm[i+1]**3) * \
                               np.sin(np.pi * (x_norm[i] + x_norm[i+1]) * 
                                      (1.0 + 0.2 * np.cos(3 * x_norm[i+1])))
        
        # Additional high-order polynomial and interaction terms
        poly_term = 0.02 * np.sum(x_norm**8)
        interaction_term = 0.08 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Novel penalty term with chaotic local minima avoidance
        local_min_penalty = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            distance = np.sqrt(np.sum(diff**2))
            penalty_factor = 1.0 + 0.5 * np.sin(10 * distance)
            local_min_penalty += penalty_factor / (1.0 + distance**3)
        
        # Add a global conditioning term that varies based on position
        conditioning = 1.0 + 0.3 * np.sin(2.0 * np.sum(x_norm**2))
        
        # Combine all components with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term + 0.7 * local_min_penalty + conditioning
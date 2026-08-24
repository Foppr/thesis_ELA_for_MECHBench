import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 20)
        self.frequency_modulation = np.random.uniform(2.0, 10.0, dim)
        self.amplitude_modulation = np.random.uniform(0.3, 3.0, dim)
        self.fractal_exponent = np.random.uniform(0.3, 0.7, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Enhanced chaotic sinusoidal components with fractal modulation
        sin_term = 0.0
        for i in range(self.dim):
            base_freq = self.frequency_modulation[i]
            fractal_freq = base_freq * (1.0 + 0.5 * np.sin(10 * x_norm[i]) * np.cos(7 * x_norm[i]))
            sin_term += (np.sin(fractal_freq * x_norm[i]) * 
                        np.cos(fractal_freq * x_norm[i] * 1.3) * 
                        np.sin(fractal_freq * x_norm[i] * 0.7)) * \
                       self.amplitude_modulation[i]
        
        # Adaptive RBF with fractal-like width variation
        rbf_sum = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            # Fractal-inspired width variation
            adaptive_width = self.rbf_widths[i] * (1.0 + 0.4 * np.sin(3 * np.sum(np.abs(diff))))
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2))
        
        # Novel fractal noise component with chaotic interaction
        noise = 0.0
        for i in range(self.dim):
            pos1 = x_norm[i]
            pos2 = x_norm[(i+1) % self.dim]
            pos3 = x_norm[(i+2) % self.dim]
            noise += np.sin(pos1**3 + pos2**2 + pos3**1.5) * \
                    np.cos(pos1**2 + pos2**3 + pos3**1.2) * \
                    np.sin(5 * pos1 + 3 * pos2) * \
                    (0.15 + 0.25 * np.sin(8 * pos1 + 4 * pos2))
        
        # Cross-dimensional coupling with fractal interaction weights
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = 0.6 + 0.4 * np.sin(np.pi * (x_norm[i] + x_norm[i+1]) * 2.0)
            cross_interaction += weight * (x_norm[i]**2 + x_norm[i+1]**2) * \
                               np.sin(np.pi * (x_norm[i] + x_norm[i+1]) * 1.5)
        
        # Additional high-order polynomial and fractal interaction terms
        poly_term = 0.02 * np.sum(np.abs(x_norm)**7)
        interaction_term = 0.08 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Fractal penalty term that penalizes proximity to previous local minima
        local_min_penalty = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            distance = np.sqrt(np.sum(diff**2))
            local_min_penalty += 1.0 / (1.0 + distance**3)
        
        # Add fractal dimensionality effect
        fractal_dim_effect = 0.0
        for i in range(self.dim):
            fractal_dim_effect += np.sin(x_norm[i] * 10.0) * np.cos(x_norm[i] * 7.0) * \
                                np.sin(x_norm[i] * 3.0) * self.fractal_exponent[i]
        
        # Combine all components with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term + 0.6 * local_min_penalty + 0.1 * fractal_dim_effect
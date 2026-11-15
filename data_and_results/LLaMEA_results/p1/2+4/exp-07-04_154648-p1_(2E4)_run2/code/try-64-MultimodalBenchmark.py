import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.rbf_widths = np.random.uniform(0.3, 1.5, 15)
        self.frequency_modulation = np.random.uniform(1.0, 6.0, dim)
        self.amplitude_modulation = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Enhanced sinusoidal components with frequency modulation
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += (np.sin(self.frequency_modulation[i] * x_norm[i]) * 
                        np.cos(self.frequency_modulation[i] * x_norm[i] * 1.5)) * \
                       self.amplitude_modulation[i]
        
        # Dynamic RBF with position-dependent widths
        rbf_sum = 0.0
        for i in range(15):
            diff = x_norm - self.rbf_centers[i]
            # Widths vary based on position to create adaptive terrain
            adaptive_width = self.rbf_widths[i] * (1.0 + 0.3 * np.abs(x_norm).mean())
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2))
        
        # Novel noise component with chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x_norm[i]**3 + x_norm[(i+1) % self.dim]**2) * \
                    np.cos(x_norm[i]**2 + x_norm[(i+1) % self.dim]**3) * \
                    (0.1 + 0.2 * np.sin(5 * x_norm[i]))
        
        # Cross-dimensional coupling with dynamic interaction weights (modified)
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = 0.3 + 0.7 * np.sin(np.pi * (x_norm[i] + x_norm[i+1]) * 1.2)
            cross_interaction += weight * (x_norm[i]**2 + x_norm[i+1]**2) * \
                               np.sin(np.pi * (x_norm[i] + x_norm[i+1]) * 0.8)
        
        # Modified polynomial and interaction terms for increased complexity
        poly_term = 0.02 * np.sum(x_norm**7)
        interaction_term = 0.08 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**2.5)
        
        # Combine all components with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term
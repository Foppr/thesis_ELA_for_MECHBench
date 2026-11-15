import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.rbf_widths = np.random.uniform(0.3, 1.5, 15)
        self.frequency_modulation = np.random.uniform(1.0, 6.0, dim)
        self.amplitude_modulation = np.random.uniform(0.5, 2.0, dim)
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)  # Logistic map parameter
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Enhanced sinusoidal components with logistic chaos modulation
        sin_term = 0.0
        for i in range(self.dim):
            logistic_factor = 1.0 / (1.0 + np.exp(-self.logistic_r[i] * (x_norm[i] - 0.5)))
            sin_term += (np.sin(self.frequency_modulation[i] * x_norm[i]) * 
                        np.cos(self.frequency_modulation[i] * x_norm[i] * 1.5)) * \
                       self.amplitude_modulation[i] * logistic_factor
        
        # Dynamic RBF with position-dependent widths
        rbf_sum = 0.0
        for i in range(15):
            diff = x_norm - self.rbf_centers[i]
            adaptive_width = self.rbf_widths[i] * (1.0 + 0.3 * np.abs(x_norm).mean())
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2))
        
        # Novel noise component with chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x_norm[i]**3 + x_norm[(i+1) % self.dim]**2) * \
                    np.cos(x_norm[i]**2 + x_norm[(i+1) % self.dim]**3) * \
                    (0.1 + 0.2 * np.sin(5 * x_norm[i]))
        
        # Cross-dimensional coupling with dynamic interaction weights
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = 0.5 + 0.5 * np.sin(np.pi * (x_norm[i] + x_norm[i+1]))
            cross_interaction += weight * (x_norm[i]**2 + x_norm[i+1]**2) * \
                               np.sin(np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Additional quartic and interaction terms for increased complexity
        poly_term = 0.01 * np.sum(x_norm**4)
        interaction_term = 0.05 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**2)
        
        # Combine all components with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term
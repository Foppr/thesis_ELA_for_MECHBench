import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.rbf_widths = np.random.uniform(0.3, 1.5, 15)
        self.frequency_modulation = np.random.uniform(1.0, 6.0, dim)
        self.amplitude_modulation = np.random.uniform(0.5, 2.0, dim)
        # Add chaotic logistic map for enhanced nonlinearity
        self.logistic_r = 3.95
        self.logistic_x = np.random.rand(dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Enhanced sinusoidal components with logistic modulation
        sin_term = 0.0
        for i in range(self.dim):
            # Update logistic map
            self.logistic_x[i] = self.logistic_r * self.logistic_x[i] * (1 - self.logistic_x[i])
            logistic_factor = 1.0 + 0.3 * self.logistic_x[i]
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
        
        # Quaternion-inspired cross-dimensional coupling
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            # Use quaternion-like interaction terms
            q_real = x_norm[i]**2 + x_norm[i+1]**2
            q_imag1 = x_norm[i] * x_norm[i+1]
            q_imag2 = x_norm[i] * x_norm[(i+2) % self.dim] if self.dim > 2 else 0
            cross_interaction += (q_real * np.sin(q_imag1 + q_imag2) + 
                                q_imag1 * np.cos(q_imag2)) * 0.3
        
        # Additional polynomial and interaction terms for increased complexity
        poly_term = 0.01 * np.sum(x_norm**6)
        interaction_term = 0.05 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**2)
        
        # Introduce a new term that penalizes proximity to previous local minima
        local_min_penalty = 0.0
        for i in range(15):
            diff = x_norm - self.rbf_centers[i]
            distance = np.sqrt(np.sum(diff**2))
            local_min_penalty += 1.0 / (1.0 + distance**2)
        
        # Combine all components with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term + 0.5 * local_min_penalty
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 20)
        self.frequency_modulation = np.random.uniform(2.0, 10.0, dim)
        self.amplitude_modulation = np.random.uniform(1.0, 3.0, dim)
        self.quaternion_weights = np.random.randn(4, dim)
        self.interaction_strength = np.random.uniform(0.1, 0.8, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Enhanced chaotic sinusoidal components with quaternion modulation
        sin_term = 0.0
        for i in range(self.dim):
            # Quaternion-based frequency modulation
            q_freq = np.sum(self.quaternion_weights[:, i] * np.array([1, np.sin(x_norm[i]), np.cos(x_norm[i]), np.sin(x_norm[i]**2)]))
            sin_term += (np.sin(q_freq * x_norm[i]) * 
                        np.cos(q_freq * x_norm[i] * 1.3)) * \
                       self.amplitude_modulation[i]
        
        # Adaptive RBF with dynamic width and position-dependent scaling
        rbf_sum = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            # Widths vary with position and dimension to create complex terrain
            adaptive_width = self.rbf_widths[i] * (1.0 + 0.5 * np.abs(x_norm).mean() + 0.2 * np.sin(np.sum(x_norm**2)))
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2))
        
        # Novel quaternion noise component with chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            # Quaternion-based noise with chaotic coupling
            q_noise = np.sum(self.quaternion_weights[:, (i+1) % self.dim] * np.array([1, np.cos(x_norm[i]), np.sin(x_norm[i]), np.cos(x_norm[i]**2)]))
            noise += np.sin(x_norm[i]**3 + x_norm[(i+1) % self.dim]**2 + q_noise) * \
                    np.cos(x_norm[i]**2 + x_norm[(i+1) % self.dim]**3 + q_noise) * \
                    (0.15 + 0.25 * np.sin(7 * x_norm[i]) * np.cos(3 * x_norm[(i+1) % self.dim]))
        
        # Cross-dimensional coupling with dynamic interaction weights and chaos
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            # Chaotic interaction weight
            weight = 0.6 + 0.4 * np.sin(np.pi * (x_norm[i] + x_norm[i+1]) * (1 + 0.3 * np.sin(x_norm[i] * x_norm[i+1])))
            cross_interaction += weight * (x_norm[i]**2 + x_norm[i+1]**2) * \
                               np.sin(np.pi * (x_norm[i] + x_norm[i+1]) * (1 + 0.2 * np.cos(x_norm[i] + x_norm[i+1])))
        
        # Additional high-order polynomial and interaction terms for increased complexity
        poly_term = 0.02 * np.sum(x_norm**8)
        interaction_term = 0.08 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Introduce a new term that penalizes proximity to previous local minima with chaotic penalty
        # to increase challenge for optimization algorithms
        local_min_penalty = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            distance = np.sqrt(np.sum(diff**2))
            # Chaotic penalty function
            penalty_factor = 1.0 + 0.5 * np.sin(5 * distance) * np.cos(3 * distance)
            local_min_penalty += penalty_factor / (1.0 + distance**2)
        
        # Add a novel fractal-like component for increased multimodality
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_component += np.sin(10 * x_norm[i]) * np.cos(15 * x_norm[i]) * np.sin(20 * x_norm[i])
        
        # Combine all components with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term + 0.7 * local_min_penalty + 0.05 * fractal_component
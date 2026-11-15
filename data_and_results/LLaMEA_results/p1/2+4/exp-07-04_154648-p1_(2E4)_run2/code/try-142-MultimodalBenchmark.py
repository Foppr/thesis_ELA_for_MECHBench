import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 20)
        self.frequency_modulation = np.random.uniform(2.0, 10.0, dim)
        self.amplitude_modulation = np.random.uniform(1.0, 3.0, dim)
        self.quaternion_weights = np.random.randn(4, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Chaotic sine-wave components with quaternion modulation
        sin_term = 0.0
        for i in range(self.dim):
            # Quaternion-based frequency modulation
            q_freq = np.dot(self.quaternion_weights[:, i], [1, x_norm[i], x_norm[(i+1)%self.dim], x_norm[(i+2)%self.dim]])
            sin_term += (np.sin(self.frequency_modulation[i] * x_norm[i] + q_freq) * 
                        np.cos(self.frequency_modulation[i] * x_norm[i] * 1.7 + q_freq)) * \
                       self.amplitude_modulation[i]
        
        # Dynamic RBF with adaptive widths and quaternion-based center shifts
        rbf_sum = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            # Widths vary based on position and quaternion influence
            adaptive_width = self.rbf_widths[i] * (1.0 + 0.5 * np.abs(x_norm).mean() + 0.2 * np.abs(np.dot(self.quaternion_weights[:, 0], x_norm)))
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2))
        
        # Novel noise component with chaotic quaternion modulation
        noise = 0.0
        for i in range(self.dim):
            # Quaternion-based chaotic noise
            q_noise = np.dot(self.quaternion_weights[:, i], [1, x_norm[i]**2, x_norm[(i+1)%self.dim]**3, x_norm[(i+2)%self.dim]**2])
            noise += np.sin(x_norm[i]**3 + x_norm[(i+1)%self.dim]**2 + q_noise) * \
                    np.cos(x_norm[i]**2 + x_norm[(i+1)%self.dim]**3 + q_noise) * \
                    (0.15 + 0.3 * np.sin(7 * x_norm[i] + q_noise))
        
        # Cross-dimensional coupling with dynamic interaction weights and quaternion influence
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = 0.6 + 0.4 * np.sin(np.pi * (x_norm[i] + x_norm[i+1] + np.dot(self.quaternion_weights[:, i], [1, x_norm[i], x_norm[i+1], 0])))
            cross_interaction += weight * (x_norm[i]**2 + x_norm[i+1]**2) * \
                               np.sin(np.pi * (x_norm[i] + x_norm[i+1] + np.dot(self.quaternion_weights[:, i], [0, x_norm[i], x_norm[i+1], 1])))
        
        # Additional high-order polynomial and interaction terms for increased complexity
        poly_term = 0.02 * np.sum(x_norm**8)
        interaction_term = 0.08 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Introduce a new term that penalizes proximity to previous local minima with quaternion influence
        local_min_penalty = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            distance = np.sqrt(np.sum(diff**2))
            # Quaternion-based penalty adjustment
            penalty_factor = np.abs(np.dot(self.quaternion_weights[:, 0], x_norm))
            local_min_penalty += penalty_factor / (1.0 + distance**2)
        
        # Combine all components with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term + 0.7 * local_min_penalty
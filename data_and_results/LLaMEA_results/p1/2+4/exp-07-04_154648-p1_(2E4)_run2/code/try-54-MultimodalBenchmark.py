import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 20)
        self.frequency_modulation = np.random.uniform(2.0, 10.0, dim)
        self.amplitude_modulation = np.random.uniform(0.3, 3.0, dim)
        self.quaternion_weights = np.random.uniform(-1.0, 1.0, (4, dim))
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Enhanced sinusoidal components with chaotic frequency modulation
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.frequency_modulation[i] * (1.0 + 0.3 * np.sin(7.0 * x_norm[i]))
            sin_term += (np.sin(freq * x_norm[i]) * 
                        np.cos(freq * x_norm[i] * 1.7)) * \
                       self.amplitude_modulation[i]
        
        # Adaptive RBF with quaternion-based position-dependent widths
        rbf_sum = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            # Quaternion-based adaptive widths
            adaptive_width = self.rbf_widths[i] * (1.0 + 0.4 * np.abs(np.dot(self.quaternion_weights[0], x_norm)))
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2))
        
        # Novel quaternion noise component with chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            q = np.array([x_norm[i], x_norm[(i+1) % self.dim], x_norm[(i+2) % self.dim], x_norm[(i+3) % self.dim]])
            noise += np.sin(np.dot(q, self.quaternion_weights[0])) * \
                    np.cos(np.dot(q, self.quaternion_weights[1])) * \
                    (0.15 + 0.25 * np.sin(3.0 * x_norm[i]))
        
        # Cross-dimensional coupling with dynamic interaction weights based on chaos
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = 0.6 + 0.4 * np.sin(np.pi * (x_norm[i] + x_norm[i+1] + 0.5 * np.sin(5.0 * x_norm[i])))
            cross_interaction += weight * (x_norm[i]**2 + x_norm[i+1]**2) * \
                               np.sin(np.pi * (x_norm[i] + x_norm[i+1] + 0.3 * np.cos(3.0 * x_norm[i+1])))
        
        # Additional high-order polynomial and interaction terms for increased complexity
        poly_term = 0.02 * np.sum(x_norm**8)
        interaction_term = 0.08 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Combine all components with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term
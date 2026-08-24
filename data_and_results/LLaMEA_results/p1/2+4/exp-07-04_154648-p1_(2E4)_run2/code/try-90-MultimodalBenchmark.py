import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 20)
        self.frequency_modulation = np.random.uniform(2.0, 10.0, dim)
        self.amplitude_modulation = np.random.uniform(0.3, 3.0, dim)
        self.quaternion_weights = np.random.randn(4, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Chaotic sine-wave components with quaternion modulation
        sin_term = 0.0
        for i in range(self.dim):
            q = np.dot(self.quaternion_weights[:, i], [1, x_norm[i], x_norm[(i+1)%self.dim], x_norm[(i+2)%self.dim]])
            sin_term += (np.sin(self.frequency_modulation[i] * x_norm[i]) * 
                        np.cos(self.frequency_modulation[i] * x_norm[i] * 1.7) * 
                        np.sin(q)) * self.amplitude_modulation[i]
        
        # Adaptive RBF with chaotic width variation
        rbf_sum = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            # Chaotic width modulation based on position and iteration
            chaotic_factor = 1.0 + 0.5 * np.sin(3.14159 * np.sum(x_norm) * (i % 7))
            adaptive_width = self.rbf_widths[i] * chaotic_factor
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2))
        
        # Novel quaternion-based noise with chaotic coupling
        noise = 0.0
        for i in range(self.dim):
            q_real = np.dot(self.quaternion_weights[0, :], x_norm)
            q_imag = np.dot(self.quaternion_weights[1, :], x_norm)
            q_j = np.dot(self.quaternion_weights[2, :], x_norm)
            q_k = np.dot(self.quaternion_weights[3, :], x_norm)
            noise += np.sin(q_real**3 + q_imag**2) * np.cos(q_j**2 + q_k**3) * \
                    (0.15 + 0.25 * np.sin(7 * x_norm[i]) * np.cos(4 * x_norm[(i+1)%self.dim]))
        
        # Cross-dimensional coupling with chaotic interaction weights
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = 0.6 + 0.4 * np.sin(np.pi * (x_norm[i] + x_norm[i+1]) * (i % 5 + 1))
            cross_interaction += weight * (x_norm[i]**2 + x_norm[i+1]**2) * \
                               np.sin(np.pi * (x_norm[i] + x_norm[i+1]) * 1.3)
        
        # Additional high-order polynomial and chaotic interaction terms
        poly_term = 0.02 * np.sum(x_norm**8)
        interaction_term = 0.08 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Combine all components with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term
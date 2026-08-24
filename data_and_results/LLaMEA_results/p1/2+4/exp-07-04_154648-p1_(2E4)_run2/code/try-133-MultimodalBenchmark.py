import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 20)
        self.frequency_modulation = np.random.uniform(2.0, 8.0, dim)
        self.amplitude_modulation = np.random.uniform(0.3, 2.5, dim)
        self.quaternion_weights = np.random.uniform(-1.0, 1.0, (dim, 4))
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Chaotic sine waves with quaternion-inspired coupling
        sin_term = 0.0
        for i in range(self.dim):
            # Quaternion-inspired interaction terms
            quat_interaction = 0.0
            for j in range(4):
                quat_interaction += self.quaternion_weights[i, j] * np.sin((j+1) * x_norm[i])
            sin_term += (np.sin(self.frequency_modulation[i] * x_norm[i]) * 
                        np.cos(self.frequency_modulation[i] * x_norm[i] * 1.7)) * \
                       self.amplitude_modulation[i] + quat_interaction * 0.1
        
        # Adaptive RBF with chaotic width modulation
        rbf_sum = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            # Chaotic width modulation based on position and iteration
            chaotic_factor = 1.0 + 0.5 * np.sin(3.0 * np.sum(x_norm**2))
            adaptive_width = self.rbf_widths[i] * chaotic_factor
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2))
        
        # Novel chaotic noise with dynamic phase coupling
        noise = 0.0
        for i in range(self.dim):
            phase_coupling = np.sin(x_norm[i] * x_norm[(i+1) % self.dim] * 2.0)
            noise += np.sin(x_norm[i]**3 + x_norm[(i+1) % self.dim]**2) * \
                    np.cos(x_norm[i]**2 + x_norm[(i+1) % self.dim]**3) * \
                    (0.15 + 0.25 * np.sin(7 * x_norm[i]) * phase_coupling)
        
        # Cross-dimensional coupling with dynamic weights and chaos
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            # Chaos-driven weight modulation
            weight = 0.6 + 0.4 * np.sin(np.pi * (x_norm[i] + x_norm[i+1]) * 1.5)
            cross_interaction += weight * (x_norm[i]**2 + x_norm[i+1]**2) * \
                               np.sin(np.pi * (x_norm[i] + x_norm[i+1]) * 1.3)
        
        # Polynomial and interaction terms with higher-order exponents
        poly_term = 0.03 * np.sum(x_norm**9)  # Increased exponent
        interaction_term = 0.1 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3.0)  # Changed exponent and coefficient
        
        # Add a global scaling factor and chaotic offset
        global_scale = 1.0 + 0.2 * np.sin(np.sum(x_norm**2))
        
        return (sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term) * global_scale
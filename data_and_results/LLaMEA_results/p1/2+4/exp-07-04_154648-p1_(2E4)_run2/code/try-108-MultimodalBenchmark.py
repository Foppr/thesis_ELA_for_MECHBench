import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (25, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 25)
        self.frequency_modulation = np.random.uniform(0.5, 8.0, dim)
        self.amplitude_modulation = np.random.uniform(0.3, 2.5, dim)
        self.quaternion_weights = np.random.randn(4, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Chaotic sinusoidal components with quaternion modulation
        sin_term = 0.0
        for i in range(self.dim):
            # Quaternion-based frequency modulation
            q_freq = np.dot(self.quaternion_weights[:, i], 
                           [1, np.sin(x_norm[i]), np.cos(x_norm[i]), np.sin(x_norm[i]**2)])
            sin_term += (np.sin(q_freq * x_norm[i]) * 
                        np.cos(q_freq * x_norm[i] * 1.7)) * \
                       self.amplitude_modulation[i]
        
        # Multi-scale RBF with chaotic width variations
        rbf_sum = 0.0
        for i in range(25):
            diff = x_norm - self.rbf_centers[i]
            # Chaotic width modulation based on position and iteration
            chaotic_factor = 1.0 + 0.5 * np.sin(10 * np.sum(x_norm**2))
            adaptive_width = self.rbf_widths[i] * chaotic_factor * (1.0 + 0.2 * np.abs(x_norm).mean())
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2))
        
        # Novel quaternion noise component with dynamic phase coupling
        noise = 0.0
        for i in range(self.dim):
            # Quaternion-based phase coupling
            phase = np.dot(self.quaternion_weights[:, i], 
                          [x_norm[i], x_norm[(i+1) % self.dim], 
                           x_norm[(i+2) % self.dim], x_norm[(i+3) % self.dim]])
            noise += np.sin(phase**3 + phase**2) * \
                    np.cos(phase**2 + phase**3) * \
                    (0.15 + 0.25 * np.sin(7 * x_norm[i]))
        
        # Cross-dimensional coupling with chaotic interaction weights
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            # Chaotic weight modulation
            weight = 0.6 + 0.4 * np.sin(3 * np.pi * (x_norm[i] + x_norm[i+1]) + 
                                       2 * np.cos(5 * x_norm[i]))
            cross_interaction += weight * (x_norm[i]**2 + x_norm[i+1]**2) * \
                               np.sin(2 * np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Enhanced polynomial and interaction terms with fractional exponents
        poly_term = 0.03 * np.sum(np.abs(x_norm)**8.5)  # Increased exponent
        interaction_term = 0.1 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3.2)  # Higher exponent
        
        # Additional chaotic coupling term
        chaotic_coupling = 0.05 * np.sum(np.sin(2 * np.pi * x_norm) * 
                                        np.cos(3 * np.pi * x_norm) * 
                                        np.tan(0.5 * np.pi * x_norm))
        
        # Combine all components with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term + chaotic_coupling
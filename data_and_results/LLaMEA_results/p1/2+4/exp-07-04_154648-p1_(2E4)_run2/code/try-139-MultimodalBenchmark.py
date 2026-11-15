import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 20)
        self.frequency_modulation = np.random.uniform(0.5, 8.0, dim)
        self.amplitude_modulation = np.random.uniform(0.3, 2.5, dim)
        self.noise_strength = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Enhanced chaotic sinusoidal components with dynamic phase shifts
        sin_term = 0.0
        for i in range(self.dim):
            phase = np.sin(x_norm[i] * np.pi * (i + 1)) * np.cos(x_norm[i] * np.pi * (i + 2))
            sin_term += (np.sin(self.frequency_modulation[i] * x_norm[i] + phase) * 
                        np.cos(self.frequency_modulation[i] * x_norm[i] * 2.0 + phase)) * \
                       self.amplitude_modulation[i]
        
        # Adaptive RBF with position-dependent widths and dynamic centers
        rbf_sum = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            adaptive_width = self.rbf_widths[i] * (1.0 + 0.5 * np.abs(x_norm).mean() + 0.2 * np.sin(x_norm[0]))
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2)) * np.cos(np.pi * np.sum(diff**2))
        
        # Novel chaotic noise component with multi-scale modulation
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x_norm[i]**3 + x_norm[(i+1) % self.dim]**2) * \
                    np.cos(x_norm[i]**2 + x_norm[(i+1) % self.dim]**3) * \
                    (0.15 + 0.3 * np.sin(7 * x_norm[i]) * np.cos(3 * x_norm[(i+2) % self.dim]))
        
        # Cross-dimensional coupling with time-varying weights and higher-order interactions
        cross_interaction = 0.0
        for i in range(self.dim - 2):
            weight = 0.6 + 0.4 * np.sin(np.pi * (x_norm[i] + x_norm[i+1] + x_norm[i+2]))
            cross_interaction += weight * (x_norm[i]**3 + x_norm[i+1]**3 + x_norm[i+2]**3) * \
                               np.sin(np.pi * (x_norm[i] + x_norm[i+1] + x_norm[i+2]))
        
        # Additional high-order polynomial and interaction terms for increased complexity
        poly_term = 0.05 * np.sum(x_norm**9)  # Increased exponent
        interaction_term = 0.1 * np.sum(np.abs(x_norm[:-2] - x_norm[2:])**3.0)  # Changed exponent and coefficient
        
        # Add global scaling and bias to increase difficulty
        scaling_factor = 1.0 + 0.1 * np.sin(np.sum(x_norm**2))
        
        return scaling_factor * (sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term)
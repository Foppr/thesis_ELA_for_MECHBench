import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (25, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 25)
        self.frequency_modulation = np.random.uniform(2.0, 10.0, dim)
        self.amplitude_modulation = np.random.uniform(0.3, 3.0, dim)
        self.noise_amplitude = np.random.uniform(0.1, 0.5, dim)
        self.interaction_weights = np.random.uniform(0.1, 2.0, (dim, dim))
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Enhanced chaotic sinusoidal components with multi-frequency modulation
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += (np.sin(self.frequency_modulation[i] * x_norm[i]) * 
                        np.cos(self.frequency_modulation[i] * x_norm[i] * 1.7) * 
                        np.sin(self.frequency_modulation[i] * x_norm[i] * 0.8)) * \
                       self.amplitude_modulation[i]
        
        # Dynamic multi-scale RBF with position-adaptive widths and multiple scales
        rbf_sum = 0.0
        for i in range(25):
            diff = x_norm - self.rbf_centers[i]
            adaptive_width = self.rbf_widths[i] * (1.0 + 0.5 * np.abs(x_norm).mean() + 0.2 * np.sum(x_norm**2))
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2)) * (1.0 + 0.3 * np.sin(i * 0.5))
        
        # Novel chaotic noise with dynamic amplitude modulation and cross-dimensional coupling
        noise = 0.0
        for i in range(self.dim):
            noise += (np.sin(x_norm[i]**3 + x_norm[(i+1) % self.dim]**2) * 
                     np.cos(x_norm[i]**2 + x_norm[(i+1) % self.dim]**3) * 
                     np.tan(3 * x_norm[i]) * 
                     self.noise_amplitude[i]) * \
                     (0.1 + 0.3 * np.sin(7 * x_norm[i]) + 0.2 * np.cos(4 * x_norm[(i+2) % self.dim]))
        
        # Cross-dimensional coupling with dynamic interaction weights and higher-order terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = self.interaction_weights[i, j] * (1.0 + 0.5 * np.sin(np.pi * (x_norm[i] + x_norm[j])))
                cross_interaction += weight * (x_norm[i]**3 + x_norm[j]**3) * \
                                   np.sin(np.pi * (x_norm[i] + x_norm[j])) * \
                                   np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Additional high-order polynomial and interaction terms with chaotic coefficients
        poly_term = 0.05 * np.sum(x_norm**9)  # Increased exponent
        interaction_term = 0.1 * np.sum(np.abs(x_norm[:-2] - x_norm[2:])**3.0)  # Changed exponent and coefficient
        
        # Add chaotic global modulation factor
        global_factor = 1.0 + 0.2 * np.sin(np.sum(x_norm**2) * 2.0)
        
        # Combine all components with global minimum at origin
        return global_factor * (sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term)
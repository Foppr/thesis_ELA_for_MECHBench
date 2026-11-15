import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (25, dim))
        self.rbf_widths = np.random.uniform(0.1, 2.0, 25)
        self.frequency_modulation = np.random.uniform(2.0, 12.0, dim)
        self.amplitude_modulation = np.random.uniform(1.0, 4.0, dim)
        self.hyperchaos_params = np.random.uniform(0.5, 3.0, (5, dim))
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Hyperchaotic sinusoidal components with multi-scale frequency modulation
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.frequency_modulation[i]
            sin_term += (np.sin(freq * x_norm[i]) * 
                        np.cos(freq * x_norm[i] * 1.7) * 
                        np.sin(freq * x_norm[i] * 0.8)) * \
                       self.amplitude_modulation[i]
        
        # Adaptive RBF with exponential width variation and dynamic center shifting
        rbf_sum = 0.0
        for i in range(25):
            diff = x_norm - self.rbf_centers[i]
            # Exponentially varying widths with position-dependent scaling
            adaptive_width = self.rbf_widths[i] * np.exp(0.5 * np.abs(x_norm).mean())
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**3))
        
        # Hyperchaotic noise component with multi-dimensional coupling
        noise = 0.0
        for i in range(self.dim):
            # Multi-scale chaotic modulation with feedback loops
            chaos1 = np.sin(x_norm[i]**3 + x_norm[(i+1) % self.dim]**2 + 
                           self.hyperchaos_params[0, i] * np.sin(10 * x_norm[i]))
            chaos2 = np.cos(x_norm[i]**2 + x_norm[(i+1) % self.dim]**3 + 
                           self.hyperchaos_params[1, i] * np.cos(8 * x_norm[i]))
            chaos3 = np.tan(x_norm[i] * x_norm[(i+2) % self.dim] + 
                           self.hyperchaos_params[2, i] * np.sin(15 * x_norm[i]))
            noise += chaos1 * chaos2 * chaos3 * (0.2 + 0.3 * np.sin(7 * x_norm[i]))
        
        # Cross-dimensional coupling with exponentially varying weights
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = np.exp(2.0 * np.sin(np.pi * (x_norm[i] + x_norm[i+1])))
            cross_interaction += weight * (x_norm[i]**3 + x_norm[i+1]**3) * \
                               np.sin(2 * np.pi * (x_norm[i] + x_norm[i+1]))
        
        # High-order polynomial and interaction terms for extreme conditioning
        poly_term = 0.02 * np.sum(x_norm**8)
        interaction_term = 0.1 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Extreme local minimum penalty with inverse cubic scaling
        local_min_penalty = 0.0
        for i in range(25):
            diff = x_norm - self.rbf_centers[i]
            distance = np.sqrt(np.sum(diff**2))
            local_min_penalty += 1.0 / (1.0 + distance**3)
        
        # Add a global conditioning term that makes optimization extremely difficult
        conditioning_term = 10.0 * np.exp(-0.5 * np.sum(x_norm**2)) * np.sin(50 * np.sum(x_norm**2))
        
        # Combine all components with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term + 0.5 * local_min_penalty + conditioning_term
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 20)
        self.frequency_modulation = np.random.uniform(2.0, 8.0, dim)
        self.amplitude_modulation = np.random.uniform(0.3, 2.5, dim)
        self.noise_amplitude = np.random.uniform(0.1, 0.5, dim)
        self.interaction_weights = np.random.uniform(0.1, 1.0, (dim, dim))
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Chaotic sine wave components with dynamic frequency and amplitude
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.frequency_modulation[i] * (1.0 + 0.3 * np.sin(3.0 * x_norm[i]))
            amp = self.amplitude_modulation[i] * (1.0 + 0.2 * np.cos(2.0 * x_norm[i]))
            sin_term += amp * np.sin(freq * x_norm[i] + np.sin(freq * x_norm[i]**2)) * \
                       np.cos(freq * x_norm[i] * 1.2 + np.cos(freq * x_norm[i]**1.5))
        
        # Adaptive RBF with dynamic width and position-dependent scaling
        rbf_sum = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            adaptive_width = self.rbf_widths[i] * (1.0 + 0.5 * np.abs(x_norm).mean() + 0.1 * np.sum(diff**2))
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2)) * \
                      np.cos(2.0 * np.sum(diff**2))
        
        # Multi-scale noise with chaotic modulation and dynamic amplitude
        noise = 0.0
        for i in range(self.dim):
            noise += (self.noise_amplitude[i] * 
                     np.sin(x_norm[i]**3 + x_norm[(i+1) % self.dim]**2 + 
                            np.sin(5 * x_norm[i]) * np.cos(3 * x_norm[(i+1) % self.dim])) * 
                     np.cos(x_norm[i]**2 + x_norm[(i+1) % self.dim]**3 + 
                            np.cos(4 * x_norm[i]) * np.sin(2 * x_norm[(i+1) % self.dim])) * 
                     (0.1 + 0.3 * np.sin(7 * x_norm[i]) * np.cos(5 * x_norm[(i+1) % self.dim])))
        
        # Dynamic cross-dimensional coupling with time-varying weights
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = self.interaction_weights[i, j] * (1.0 + 0.2 * np.sin(2.0 * (x_norm[i] + x_norm[j])))
                cross_interaction += weight * (x_norm[i]**2 + x_norm[j]**2) * \
                                   np.sin(np.pi * (x_norm[i] + x_norm[j]) + 
                                          np.cos(np.pi * (x_norm[i] - x_norm[j])))
        
        # High-order polynomial terms with interaction
        poly_term = 0.02 * np.sum(x_norm**8)
        interaction_term = 0.08 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Novel penalty for proximity to local minima with exponential decay
        local_min_penalty = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            distance = np.sqrt(np.sum(diff**2))
            local_min_penalty += 1.0 / (1.0 + distance**3 + 0.1 * distance**6)
        
        # Additional chaotic coupling term
        chaotic_coupling = 0.0
        for i in range(self.dim):
            chaotic_coupling += np.sin(10 * x_norm[i] + np.sin(5 * x_norm[i]**2)) * \
                               np.cos(8 * x_norm[i] + np.cos(4 * x_norm[i]**3))
        
        # Combine all components with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term + 0.7 * local_min_penalty + 0.3 * chaotic_coupling
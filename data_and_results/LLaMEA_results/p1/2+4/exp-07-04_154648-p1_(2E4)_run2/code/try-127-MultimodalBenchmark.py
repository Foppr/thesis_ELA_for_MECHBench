import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 20)
        self.frequency_modulation = np.random.uniform(2.0, 8.0, dim)
        self.amplitude_modulation = np.random.uniform(0.3, 2.5, dim)
        self.memory_weights = np.random.uniform(-0.5, 0.5, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Chaotic sine-wave components with memory effects
        sin_term = 0.0
        for i in range(self.dim):
            # Memory-based frequency modulation
            freq = self.frequency_modulation[i] * (1.0 + 0.3 * np.sin(x_norm[i] * 2.0 + self.memory_weights[i]))
            sin_term += (np.sin(freq * x_norm[i] + self.phase_shifts[i]) * 
                        np.cos(freq * x_norm[i] * 1.3 + self.phase_shifts[i] * 1.7)) * \
                       self.amplitude_modulation[i]
        
        # Adaptive RBF with dynamic width and position-dependent weights
        rbf_sum = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            # Widths vary based on position and dimension
            adaptive_width = self.rbf_widths[i] * (1.0 + 0.4 * np.abs(x_norm).mean() + 0.2 * np.sin(x_norm[0] if self.dim > 0 else 0))
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2)) * (1.0 + 0.1 * np.sin(i * 0.5))
        
        # Novel chaotic noise component with dynamic phase coupling
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x_norm[i]**3 + x_norm[(i+1) % self.dim]**2 + 
                           0.5 * np.sin(x_norm[i] * 3.0)) * \
                    np.cos(x_norm[i]**2 + x_norm[(i+1) % self.dim]**3 + 
                           0.3 * np.cos(x_norm[i] * 2.0)) * \
                    (0.15 + 0.25 * np.sin(7 * x_norm[i] + 0.5 * np.cos(x_norm[(i+2) % self.dim])))
        
        # Cross-dimensional coupling with dynamic interaction weights and memory
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            # Memory-dependent weight
            weight = 0.6 + 0.4 * np.sin(np.pi * (x_norm[i] + x_norm[i+1]) + self.memory_weights[i])
            cross_interaction += weight * (x_norm[i]**2 + x_norm[i+1]**2) * \
                               np.sin(np.pi * (x_norm[i] + x_norm[i+1]) + self.phase_shifts[i])
        
        # Additional high-order polynomial and interaction terms
        poly_term = 0.02 * np.sum(x_norm**8)
        interaction_term = 0.08 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Memory-based local minimum penalty with dynamic scaling
        local_min_penalty = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            distance = np.sqrt(np.sum(diff**2))
            # Dynamic penalty scaling based on memory weights
            penalty_scale = 1.0 + 0.3 * np.sin(self.memory_weights[i % self.dim])
            local_min_penalty += penalty_scale / (1.0 + distance**2)
        
        # Introduce a new term that creates fitness valleys and plateaus
        valley_term = 0.0
        for i in range(self.dim):
            valley_term += np.sin(3 * x_norm[i]) * np.cos(2 * x_norm[i]) * \
                          (0.5 + 0.5 * np.sin(x_norm[i] * 5.0))
        
        # Combine all components with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term + 0.6 * local_min_penalty + 0.3 * valley_term
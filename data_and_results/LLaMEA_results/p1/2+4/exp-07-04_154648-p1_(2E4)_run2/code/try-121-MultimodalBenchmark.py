import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 20)
        self.frequency_modulation = np.random.uniform(2.0, 10.0, dim)
        self.amplitude_modulation = np.random.uniform(0.3, 3.0, dim)
        self.gradient_weights = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Chaotic sinusoidal components with dynamic frequency and amplitude
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.frequency_modulation[i] * (1.0 + 0.3 * np.sin(x_norm[i] * 7.0))
            amp = self.amplitude_modulation[i] * (1.0 + 0.2 * np.cos(x_norm[i] * 5.0))
            sin_term += amp * np.sin(freq * x_norm[i] + np.sin(x_norm[i] * 3.0)) * \
                       np.cos(freq * x_norm[i] * 1.2 + np.cos(x_norm[i] * 4.0))
        
        # Adaptive RBF with gradient-dependent widths and position-aware centers
        rbf_sum = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            adaptive_width = self.rbf_widths[i] * (1.0 + 0.5 * np.linalg.norm(diff))
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2)) * \
                      np.exp(-0.1 * np.sum(np.abs(diff)))
        
        # Novel chaotic noise with gradient modulation
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x_norm[i]**3 + x_norm[(i+1) % self.dim]**2) * \
                    np.cos(x_norm[i]**2 + x_norm[(i+1) % self.dim]**3) * \
                    (0.15 + 0.3 * np.sin(7 * x_norm[i]) * np.cos(3 * x_norm[i]))
        
        # Cross-dimensional coupling with gradient-weighted interactions
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = self.gradient_weights[i] * (1.0 + 0.5 * np.sin(np.pi * (x_norm[i] + x_norm[i+1])))
            cross_interaction += weight * (x_norm[i]**3 + x_norm[i+1]**3) * \
                               np.sin(np.pi * (x_norm[i] + x_norm[i+1])) * \
                               np.cos(np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Additional high-order polynomial and directional interaction terms
        poly_term = 0.02 * np.sum(x_norm**8)
        interaction_term = 0.1 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Gradient-based penalty to discourage movement in certain directions
        gradient_penalty = 0.0
        for i in range(self.dim):
            grad = np.abs(x_norm[i] - np.mean(x_norm)) * self.gradient_weights[i]
            gradient_penalty += grad * np.exp(-0.5 * grad**2)
        
        # Enhanced local minimum penalty with directional bias
        local_min_penalty = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            distance = np.sqrt(np.sum(diff**2))
            local_min_penalty += 1.0 / (1.0 + distance**3) * \
                               np.exp(-0.5 * np.sum(np.abs(diff)))
        
        # Combine all components with global minimum at origin and increased conditioning
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term + gradient_penalty + 0.3 * local_min_penalty
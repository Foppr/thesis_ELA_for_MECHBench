import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 20)
        self.frequency_modulation = np.random.uniform(2.0, 10.0, dim)
        self.amplitude_modulation = np.random.uniform(1.0, 3.0, dim)
        self.quaternion_weights = np.random.uniform(-1.0, 1.0, (4, dim))
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Chaotic sine-wave components with quaternion modulation
        sin_term = 0.0
        for i in range(self.dim):
            q = np.array([x_norm[i], x_norm[(i+1) % self.dim], x_norm[(i+2) % self.dim], x_norm[(i+3) % self.dim]])
            q = q * self.quaternion_weights[:, i]
            sin_term += (np.sin(self.frequency_modulation[i] * x_norm[i]) * 
                        np.cos(self.frequency_modulation[i] * x_norm[i] * 2.0)) * \
                       self.amplitude_modulation[i] * np.sum(q**2)
        
        # Dynamic RBF with adaptive widths and position-dependent scaling
        rbf_sum = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            adaptive_width = self.rbf_widths[i] * (1.0 + 0.5 * np.abs(x_norm).mean() + 0.2 * np.sin(x_norm[0]))
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2)) * (1.0 + 0.1 * np.sin(i * x_norm[0]))
        
        # Novel quaternion-based noise with chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            q_real = np.sin(x_norm[i]**3 + x_norm[(i+1) % self.dim]**2) * \
                    np.cos(x_norm[i]**2 + x_norm[(i+1) % self.dim]**3)
            q_imag = np.sin(x_norm[i]**2 + x_norm[(i+1) % self.dim]**3) * \
                    np.cos(x_norm[i]**3 + x_norm[(i+1) % self.dim]**2)
            noise += q_real * q_imag * (0.15 + 0.25 * np.sin(7 * x_norm[i] + 3 * x_norm[(i+1) % self.dim]))
        
        # Cross-dimensional coupling with dynamic interaction weights and chaotic phase shifts
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = 0.6 + 0.4 * np.sin(np.pi * (x_norm[i] + x_norm[i+1]) + 2 * np.sin(x_norm[i]))
            cross_interaction += weight * (x_norm[i]**2 + x_norm[i+1]**2) * \
                               np.sin(np.pi * (x_norm[i] + x_norm[i+1]) + 3 * np.cos(x_norm[i]))
        
        # Additional high-order polynomial and interaction terms for increased complexity
        poly_term = 0.02 * np.sum(x_norm**8)
        interaction_term = 0.08 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Combine all components with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + interaction_term
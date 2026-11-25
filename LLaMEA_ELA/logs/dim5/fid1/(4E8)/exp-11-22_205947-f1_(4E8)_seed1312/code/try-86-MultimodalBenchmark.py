import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine-cosine map with multiple attractors and time-delayed feedback
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Chaotic feedback with multiple sinusoidal modulations
            feedback = np.sin(17 * np.pi * xi) * np.cos(11 * np.pi * xi) * np.sin(13 * np.pi * xi)
            chaotic_val = 3.999 * xi * (1 - xi) + 0.3 * feedback
            chaotic_term += chaotic_val * np.sin(29 * np.pi * xi)**2
        
        # Multi-modal radial basis function with dynamic centers and varying widths
        rbf_term = 0.0
        centers = np.linspace(-0.7, 0.7, min(7, self.dim))
        widths = np.linspace(0.08, 0.5, min(7, self.dim))
        for i in range(self.dim):
            rbf_sum = 0.0
            for j, (center, width) in enumerate(zip(centers, widths)):
                dist = abs(x_norm[i] - center)
                rbf_sum += np.exp(-dist**2 / (2 * width**2)) * (1 + 0.6 * np.sin(19 * np.pi * x_norm[i] + j))
            rbf_term += rbf_sum
        
        # Non-separable high-frequency trigonometric interactions with dynamic coupling
        trig_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Reduced coupling for better conditioning
                freq_i = 7 + i % 8
                freq_j = 6 + j % 7
                # Dynamic amplitude modulation with chaotic feedback
                amp_mod = 1 + 0.3 * np.sin(11 * np.pi * x_norm[i]) * np.cos(9 * np.pi * x_norm[j])
                trig_interaction += amp_mod * np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j]) * \
                                  (1 + 0.2 * np.sin(13 * np.pi * (x_norm[i] + x_norm[j])))
        
        # Polynomial and exponential mix with asymmetric curvature and dynamic scaling
        poly_exp_term = 0.0
        for i in range(self.dim):
            # Asymmetric polynomial with dynamic exponential decay and chaotic modulation
            mod = 1 + 0.15 * np.sin(17 * np.pi * x_norm[i])
            poly_exp_term += (mod * (x_norm[i]**5 + 0.7 * x_norm[i]**3 - 0.2 * x_norm[i]**2)) * \
                            np.exp(-0.8 * x_norm[i]**2)
        
        # Cross-dimensional coupling with chaotic weights and multiple interaction modes
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic weight based on both variables and their interactions
                weight = 0.6 * (1 + np.sin(x_norm[i]) * np.cos(x_norm[j]) * 
                               np.sin(4 * np.pi * (x_norm[i] + x_norm[j])) * 
                               np.cos(2 * np.pi * (x_norm[i] - x_norm[j])))
                coupling_term += weight * (x_norm[i]**2 + x_norm[j]**2) * \
                               np.sin(9 * np.pi * (x_norm[i] - x_norm[j])) * \
                               np.cos(6 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Global modulation with chaotic sine-cosine combinations
        global_mod = 0.7 * np.sin(23 * np.pi * np.sum(x_norm**2)) + 0.4 * np.cos(19 * np.pi * np.prod(x_norm)) + \
                     0.2 * np.sin(13 * np.pi * np.mean(x_norm**3))
        
        # Combine all terms with enhanced scaling and global modulation
        result = 1.2 * chaotic_term + 0.9 * rbf_term + 0.6 * trig_interaction + \
                 0.5 * poly_exp_term + 0.4 * coupling_term + global_mod
        
        return result
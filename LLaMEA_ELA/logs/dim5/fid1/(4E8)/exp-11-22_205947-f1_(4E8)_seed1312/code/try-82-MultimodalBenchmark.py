import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine-based map with dynamic coupling and multiple attractors
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-attractor chaotic component with dynamic modulation
            mod1 = 1 + 0.3 * np.sin(17 * np.pi * xi)
            mod2 = 1 + 0.2 * np.cos(19 * np.pi * xi)
            chaotic_val = mod1 * np.sin(23 * np.pi * xi) * mod2 * np.cos(13 * np.pi * xi)
            chaotic_term += chaotic_val * (1 + 0.4 * np.sin(7 * np.pi * xi)**2)
        
        # Modified radial basis function with adaptive centers and widths
        rbf_term = 0.0
        num_centers = min(7, self.dim)
        centers = np.linspace(-0.9, 0.9, num_centers)
        widths = np.linspace(0.08, 0.5, num_centers)
        for i in range(self.dim):
            rbf_sum = 0.0
            for j, (center, width) in enumerate(zip(centers, widths)):
                dist = abs(x_norm[i] - center)
                rbf_sum += np.exp(-dist**2 / (2 * width**2)) * (1 + 0.3 * np.sin(19 * np.pi * x_norm[i] + j))
            rbf_term += rbf_sum
        
        # Enhanced trigonometric coupling with dynamic amplitude and phase modulation
        trig_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                freq_i = 6 + (i % 7)
                freq_j = 5 + (j % 6)
                # Dynamic amplitude modulation with chaotic feedback
                amp_mod = 1 + 0.3 * np.sin(11 * np.pi * x_norm[i]) * np.cos(9 * np.pi * x_norm[j])
                phase_mod = 1 + 0.2 * np.sin(15 * np.pi * (x_norm[i] + x_norm[j]))
                trig_term += amp_mod * np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j]) * phase_mod
        
        # Polynomial-exponential hybrid with asymmetric curvature and dynamic scaling
        poly_exp_term = 0.0
        for i in range(self.dim):
            # Asymmetric polynomial with exponential decay and chaotic modulation
            mod = 1 + 0.25 * np.sin(15 * np.pi * x_norm[i])
            poly_exp_term += (mod * (x_norm[i]**5 + 0.7 * x_norm[i]**3 - 0.4 * x_norm[i]**2)) * \
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
                               np.sin(8 * np.pi * (x_norm[i] - x_norm[j])) * \
                               np.cos(6 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Global modulation with enhanced chaotic sine-cosine combinations
        global_mod = 0.7 * np.sin(25 * np.pi * np.sum(x_norm**2)) + 0.4 * np.cos(21 * np.pi * np.prod(x_norm)) + \
                     0.2 * np.sin(15 * np.pi * np.mean(x_norm**3))
        
        # Combine all terms with refined scaling and global modulation
        result = 1.2 * chaotic_term + 0.9 * rbf_term + 0.8 * trig_term + \
                 0.7 * poly_exp_term + 0.6 * coupling_term + global_mod
        
        return result
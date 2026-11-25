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
            mod1 = 1 + 0.35 * np.sin(19 * np.pi * xi)
            mod2 = 1 + 0.25 * np.cos(21 * np.pi * xi)
            chaotic_val = mod1 * np.sin(25 * np.pi * xi) * mod2 * np.cos(15 * np.pi * xi)
            chaotic_term += chaotic_val * (1 + 0.45 * np.sin(9 * np.pi * xi)**2)
        
        # Modified radial basis function with adaptive centers and widths
        rbf_term = 0.0
        num_centers = min(7, self.dim)
        centers = np.linspace(-0.8, 0.8, num_centers)
        widths = np.linspace(0.09, 0.55, num_centers)
        for i in range(self.dim):
            rbf_sum = 0.0
            for j, (center, width) in enumerate(zip(centers, widths)):
                dist = abs(x_norm[i] - center)
                rbf_sum += np.exp(-dist**2 / (2 * width**2)) * (1 + 0.35 * np.sin(21 * np.pi * x_norm[i] + j))
            rbf_term += rbf_sum
        
        # Enhanced trigonometric coupling with dynamic amplitude and phase modulation
        trig_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                freq_i = 7 + (i % 8)
                freq_j = 6 + (j % 7)
                # Dynamic amplitude modulation with chaotic feedback
                amp_mod = 1 + 0.35 * np.sin(13 * np.pi * x_norm[i]) * np.cos(11 * np.pi * x_norm[j])
                phase_mod = 1 + 0.25 * np.sin(17 * np.pi * (x_norm[i] + x_norm[j]))
                trig_term += amp_mod * np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j]) * phase_mod
        
        # Polynomial-exponential hybrid with asymmetric curvature and dynamic scaling
        poly_exp_term = 0.0
        for i in range(self.dim):
            # Asymmetric polynomial with exponential decay and chaotic modulation
            mod = 1 + 0.3 * np.sin(17 * np.pi * x_norm[i])
            poly_exp_term += (mod * (x_norm[i]**5 + 0.75 * x_norm[i]**3 - 0.45 * x_norm[i]**2)) * \
                            np.exp(-0.85 * x_norm[i]**2)
        
        # Cross-dimensional coupling with chaotic weights and multiple interaction modes
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic weight based on both variables and their interactions
                weight = 0.65 * (1 + np.sin(x_norm[i]) * np.cos(x_norm[j]) * 
                               np.sin(5 * np.pi * (x_norm[i] + x_norm[j])) * 
                               np.cos(3 * np.pi * (x_norm[i] - x_norm[j])))
                coupling_term += weight * (x_norm[i]**2 + x_norm[j]**2) * \
                               np.sin(9 * np.pi * (x_norm[i] - x_norm[j])) * \
                               np.cos(7 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Global modulation with enhanced chaotic sine-cosine combinations
        global_mod = 0.75 * np.sin(27 * np.pi * np.sum(x_norm**2)) + 0.45 * np.cos(23 * np.pi * np.prod(x_norm)) + \
                     0.25 * np.sin(17 * np.pi * np.mean(x_norm**3))
        
        # Combine all terms with refined scaling and global modulation
        result = 1.3 * chaotic_term + 0.95 * rbf_term + 0.85 * trig_term + \
                 0.75 * poly_exp_term + 0.65 * coupling_term + global_mod
        
        return result
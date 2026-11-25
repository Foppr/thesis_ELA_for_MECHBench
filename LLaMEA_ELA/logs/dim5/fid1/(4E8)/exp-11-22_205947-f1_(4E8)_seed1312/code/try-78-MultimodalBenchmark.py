import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map component with enhanced ergodicity
        logistic_term = 0.0
        r = 3.999  # Slightly increased chaos parameter
        for i in range(self.dim):
            xi = x_norm[i]
            logistic_val = r * xi * (1 - xi)
            logistic_term += logistic_val * np.sin(19 * np.pi * xi) ** 2
        
        # Multi-modal radial basis function with dynamic centers and widths
        rbf_term = 0.0
        centers = np.linspace(-0.85, 0.85, min(6, self.dim))
        widths = np.linspace(0.12, 0.45, min(6, self.dim))
        for i in range(self.dim):
            rbf_sum = 0.0
            for j, (center, width) in enumerate(zip(centers, widths)):
                dist = abs(x_norm[i] - center)
                rbf_sum += np.exp(-dist**2 / (2 * width**2)) * (1 + 0.35 * np.sin(19 * np.pi * x_norm[i] + j))
            rbf_term += rbf_sum
        
        # Non-separable high-frequency trigonometric interactions with improved coupling
        trig_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended coupling
                freq_i = 7 + i % 8
                freq_j = 6 + j % 7
                amp_mod = 1 + 0.35 * np.sin(10 * np.pi * x_norm[i]) * np.cos(8 * np.pi * x_norm[j])
                trig_interaction += amp_mod * np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j]) * \
                                  (1 + 0.3 * np.sin(13 * np.pi * (x_norm[i] + x_norm[j])))
        
        # Polynomial and exponential mix with improved asymmetry
        poly_exp_term = 0.0
        for i in range(self.dim):
            poly_exp_term += (x_norm[i]**5 + 0.75 * x_norm[i]**3 - 0.28 * x_norm[i]**2) * np.exp(-0.75 * x_norm[i]**2)
        
        # Cross-dimensional coupling with enhanced dynamic weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.6 * (1 + np.sin(x_norm[i]) * np.cos(x_norm[j]) * np.sin(5 * np.pi * (x_norm[i] + x_norm[j])))
                coupling_term += weight * (x_norm[i]**2 + x_norm[j]**2) * \
                               np.sin(9 * np.pi * (x_norm[i] - x_norm[j])) * \
                               np.cos(6 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Global modulation with stronger influence
        global_mod = 0.7 * np.sin(25 * np.pi * np.sum(x_norm**2)) + 0.4 * np.cos(20 * np.pi * np.prod(x_norm))
        
        # Combine all terms with updated scaling factors
        result = 0.85 * logistic_term + 0.65 * rbf_term + 0.55 * trig_interaction + \
                 0.45 * poly_exp_term + 0.35 * coupling_term + global_mod
        
        return result
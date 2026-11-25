import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of squares term
        sum_sq = np.sum(x_norm**2)
        
        # Chaotic tent map dynamics for enhanced complexity
        tent_map = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            if xi < 0.5:
                tent_map += 2 * xi
            else:
                tent_map += 2 * (1 - xi)
        
        # Radial basis function component with multiple centers
        rbf_term = 0.0
        centers = np.linspace(-0.8, 0.8, 5)
        for i in range(self.dim):
            min_dist = np.min(np.abs(x_norm[i] - centers))
            rbf_term += np.exp(-5 * min_dist**2)
        
        # Enhanced sinusoidal interactions with chaotic frequency modulation
        sin_term = 0.0
        for i in range(self.dim):
            freq_mod = 1 + 0.5 * np.sin(30 * x_norm[i])
            sin_term += (np.sin(freq_mod * 20 * np.pi * x_norm[i]) + 
                        0.3 * np.sin(40 * freq_mod * np.pi * x_norm[i])) * np.exp(-0.5 * (x_norm[i] - 0.2)**2)
        
        # Modified polynomial terms with non-separable interactions
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x_norm[i] - 0.1)**2 * (1 + 0.7 * np.sin(10 * np.pi * x_norm[i])**2) + \
                        0.4 * (x_norm[i] + 0.15)**4 + \
                        0.2 * (x_norm[i] - 0.3)**6
        
        # Non-separable trigonometric interactions with chaotic coupling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1 + 0.3 * np.sin(25 * x_norm[i]) * np.cos(15 * x_norm[j])
                interaction_term += coupling * np.sin(12 * np.pi * x_norm[i]) * np.sin(6 * np.pi * x_norm[j]) * \
                                  (1 + 0.2 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Additional harmonic term with chaotic modulation
        harmonic_term = 0.0
        for i in range(self.dim):
            mod_freq = 1 + 0.4 * np.sin(40 * x_norm[i])
            harmonic_term += 0.2 * np.sin(mod_freq * 25 * np.pi * x_norm[i]) * np.cos(mod_freq * 12 * np.pi * x_norm[i])
        
        # Combine all terms with optimized weights
        result = sum_sq + 0.8 * sin_term + 0.35 * poly_term + 0.2 * interaction_term + \
                0.25 * harmonic_term + 0.15 * tent_map + 0.1 * rbf_term
        
        return result
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map component for ergodic behavior
        logistic_term = 0.0
        r = 3.99  # Chaos parameter
        for i in range(self.dim):
            xi = x_norm[i]
            # Logistic map with dynamic parameter
            logistic_val = r * xi * (1 - xi)
            logistic_term += logistic_val * np.sin(17 * np.pi * xi) ** 2
        
        # Multi-modal radial basis function component with multiple centers and varying widths
        rbf_term = 0.0
        centers = np.linspace(-0.9, 0.9, min(7, self.dim))
        widths = np.linspace(0.1, 0.5, min(7, self.dim))
        for i in range(self.dim):
            rbf_sum = 0.0
            for j, (center, width) in enumerate(zip(centers, widths)):
                dist = abs(x_norm[i] - center)
                rbf_sum += np.exp(-dist**2 / (2 * width**2)) * (1 + 0.4 * np.sin(17 * np.pi * x_norm[i] + j))
            rbf_term += rbf_sum
        
        # Non-separable high-frequency trigonometric interactions with dynamic coupling
        trig_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling
                freq_i = 6 + i % 7
                freq_j = 5 + j % 6
                # Dynamic amplitude modulation
                amp_mod = 1 + 0.3 * np.sin(9 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[j])
                trig_interaction += amp_mod * np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j]) * \
                                  (1 + 0.25 * np.sin(11 * np.pi * (x_norm[i] + x_norm[j])))
        
        # Polynomial and exponential mix with asymmetric curvature
        poly_exp_term = 0.0
        for i in range(self.dim):
            # Asymmetric polynomial with exponential decay
            poly_exp_term += (x_norm[i]**5 + 0.7 * x_norm[i]**3 - 0.25 * x_norm[i]**2) * np.exp(-0.8 * x_norm[i]**2)
        
        # Cross-dimensional coupling with dynamic weights based on position and interaction strength
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic weight based on both variables and their interactions
                weight = 0.5 * (1 + np.sin(x_norm[i]) * np.cos(x_norm[j]) * np.sin(4 * np.pi * (x_norm[i] + x_norm[j])))
                coupling_term += weight * (x_norm[i]**2 + x_norm[j]**2) * \
                               np.sin(8 * np.pi * (x_norm[i] - x_norm[j])) * \
                               np.cos(5 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Add a global modulation term to increase complexity
        global_mod = 0.6 * np.sin(22 * np.pi * np.sum(x_norm**2)) + 0.35 * np.cos(17 * np.pi * np.prod(x_norm))
        
        # Combine all terms with adaptive scaling and global modulation
        result = 0.8 * logistic_term + 0.6 * rbf_term + 0.5 * trig_interaction + \
                 0.4 * poly_exp_term + 0.3 * coupling_term + global_mod
        
        return result
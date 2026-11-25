import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic tent map component for ergodic behavior
        tent_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Tent map with parameter control
            if xi < 0.5:
                tent_val = 2 * xi
            else:
                tent_val = 2 * (1 - xi)
            tent_term += tent_val * np.sin(10 * np.pi * xi) ** 2
        
        # Radial basis function component with multiple centers
        rbf_term = 0.0
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        for i in range(self.dim):
            min_dist = float('inf')
            for center in centers:
                dist = abs(x_norm[i] - center)
                if dist < min_dist:
                    min_dist = dist
            rbf_term += np.exp(-5 * min_dist**2) * (1 + 0.3 * np.sin(12 * np.pi * x_norm[i]))
        
        # Non-separable trigonometric interactions with varying frequencies
        trig_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                freq_i = 3 + i % 5
                freq_j = 2 + j % 4
                trig_interaction += np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j]) * \
                                  (1 + 0.2 * np.sin(7 * np.pi * (x_norm[i] + x_norm[j])))
        
        # Polynomial and exponential mix for varied curvature
        poly_exp_term = 0.0
        for i in range(self.dim):
            poly_exp_term += (x_norm[i]**3 + 0.5 * x_norm[i]**2) * np.exp(-0.5 * x_norm[i]**2)
        
        # Cross-dimensional coupling with dynamic weights based on position
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic weight based on both variables
                weight = 0.3 * (1 + np.sin(x_norm[i]) * np.cos(x_norm[j]))
                coupling_term += weight * (x_norm[i]**2 + x_norm[j]**2) * \
                               np.sin(5 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Combine all terms with adaptive scaling
        result = 0.6 * tent_term + 0.4 * rbf_term + 0.3 * trig_interaction + \
                 0.25 * poly_exp_term + 0.15 * coupling_term
        
        return result
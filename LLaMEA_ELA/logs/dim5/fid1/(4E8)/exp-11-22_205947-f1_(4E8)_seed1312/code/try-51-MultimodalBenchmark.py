import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic tent map component for ergodic behavior with enhanced nonlinearity
        tent_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Tent map with parameter control and additional nonlinearities
            if xi < 0.5:
                tent_val = 2 * xi
            else:
                tent_val = 2 * (1 - xi)
            tent_term += tent_val * np.sin(15 * np.pi * xi) ** 3
        
        # Radial basis function component with multiple centers and enhanced locality
        rbf_term = 0.0
        centers = np.linspace(-0.9, 0.9, min(7, self.dim))
        for i in range(self.dim):
            min_dist = float('inf')
            for center in centers:
                dist = abs(x_norm[i] - center)
                if dist < min_dist:
                    min_dist = dist
            rbf_term += np.exp(-8 * min_dist**2) * (1 + 0.4 * np.sin(15 * np.pi * x_norm[i]))
        
        # Non-separable trigonometric interactions with stronger coupling and frequency variation
        trig_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling range
                freq_i = 4 + i % 6
                freq_j = 3 + j % 5
                trig_interaction += np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j]) * \
                                  (1 + 0.3 * np.sin(9 * np.pi * (x_norm[i] + x_norm[j])) + 
                                   0.2 * np.cos(11 * np.pi * (x_norm[i] - x_norm[j])))
        
        # Enhanced polynomial and exponential mix with varied curvature
        poly_exp_term = 0.0
        for i in range(self.dim):
            poly_exp_term += (x_norm[i]**4 + 0.6 * x_norm[i]**3 + 0.3 * x_norm[i]**2) * np.exp(-0.7 * x_norm[i]**2)
        
        # Cross-dimensional coupling with dynamic weights based on position and interaction strength
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic weight based on both variables with additional interaction
                weight = 0.4 * (1 + np.sin(x_norm[i]) * np.cos(x_norm[j]) * np.sin(2 * x_norm[i] + x_norm[j]))
                coupling_term += weight * (x_norm[i]**2 + x_norm[j]**2) * \
                               np.sin(7 * np.pi * (x_norm[i] - x_norm[j])) * \
                               (1 + 0.2 * np.cos(5 * np.pi * (x_norm[i] + x_norm[j])))
        
        # Combine all terms with adaptive scaling for better balance
        result = 0.7 * tent_term + 0.3 * rbf_term + 0.4 * trig_interaction + \
                 0.3 * poly_exp_term + 0.2 * coupling_term
        
        return result
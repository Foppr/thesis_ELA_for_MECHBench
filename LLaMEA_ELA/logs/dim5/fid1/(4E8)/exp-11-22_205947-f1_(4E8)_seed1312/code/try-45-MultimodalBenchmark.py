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
        tent_term = 0.0
        for i in range(self.dim):
            # Tent map with parameter 1.5 for chaos
            tent_val = 1.5 * np.abs(x_norm[i])
            if x_norm[i] > 0.5:
                tent_val = 1.5 * (1 - np.abs(x_norm[i]))
            tent_term += tent_val * np.sin(20 * np.pi * x_norm[i])
        
        # Radial basis function component with multiple centers
        rbf_term = 0.0
        centers = np.linspace(-0.8, 0.8, 5)
        for i in range(self.dim):
            min_dist = float('inf')
            for center in centers:
                dist = np.abs(x_norm[i] - center)
                if dist < min_dist:
                    min_dist = dist
            rbf_term += np.exp(-5 * min_dist**2)
        
        # Non-separable trigonometric interactions with chaotic coupling
        trig_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling through sine of sum
                coupling = np.sin(15 * np.pi * (x_norm[i] + x_norm[j]))
                trig_interaction += coupling * np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Modified polynomial with multiple local minima
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x_norm[i] - 0.2)**4 + 0.8 * (x_norm[i] + 0.3)**6 + 0.5 * np.sin(10 * np.pi * x_norm[i])**2
        
        # Enhanced sinusoidal interactions with varying frequencies
        sin_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 8 + 4 * np.sin(x_norm[i])
                freq_j = 6 + 3 * np.cos(x_norm[j])
                sin_interaction += np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j]) * (1 + 0.3 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Combine all terms with optimized weights
        result = 0.5 * sum_sq + 0.4 * tent_term + 0.3 * rbf_term + 0.25 * trig_interaction + 0.35 * poly_term + 0.2 * sin_interaction
        
        return result
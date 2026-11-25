import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal modulations with chaotic phase interactions
        chaotic_term = 0
        for i in range(self.dim):
            phase = np.sin(x_norm[i] * np.pi) * np.cos(x_norm[i] * np.pi / 2)
            chaotic_term += np.sin(12 * x_norm[i] + phase) * np.cos(6 * x_norm[i] - phase)
        
        # Saddle-point interactions with varying curvature
        saddle_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x_norm[i] - x_norm[j])
                saddle_term += (x_norm[i]**2 - x_norm[j]**2) * np.exp(-distance**2)
        
        # Gradient-based attraction fields with repulsion centers
        attraction_term = 0
        for i in range(self.dim):
            attraction_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    attraction_sum += (x_norm[j] / (distance**2 + 0.1)) * np.exp(-distance)
            attraction_term += attraction_sum
        
        # Polynomial chaos with mixed even/odd terms (modified exponents)
        poly_term = 0
        for i in range(self.dim):
            if i % 2 == 0:
                poly_term += x_norm[i]**7 - 2.5*x_norm[i]**4 + 1.5*x_norm[i]**2
            else:
                poly_term += x_norm[i]**6 - 3.2*x_norm[i]**3 + 2.1*x_norm[i]
        
        # Cross-dimensional coupling with hyperbolic interactions (modified)
        cross_term = 0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                cross_term += np.tanh(x_norm[i]) * np.log(np.abs(x_norm[i+1]) + 1.5) * \
                             (x_norm[i]**3 + x_norm[i+1]**3)
        
        # Combine all terms with dynamic weights
        result = 0.25 * chaotic_term + 0.3 * saddle_term + 0.15 * attraction_term + \
                 0.2 * poly_term + 0.1 * cross_term
        
        # Add a conditioning term to control the landscape difficulty (increased)
        conditioning = 0.02 * np.sum(x_norm**4)
        
        return result + conditioning
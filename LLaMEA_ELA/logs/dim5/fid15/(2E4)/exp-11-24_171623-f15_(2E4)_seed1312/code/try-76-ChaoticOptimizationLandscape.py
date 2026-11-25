import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic dynamics with fractal-like modulation
        chaotic_term = 0
        for i in range(self.dim):
            phase = np.sin(x_norm[i] * np.pi) * np.cos(x_norm[i] * np.pi / 2)
            chaotic_term += np.sin(20 * x_norm[i] + phase) * np.cos(12 * x_norm[i] - phase) * \
                           np.exp(-np.abs(x_norm[i]))
        
        # Fractal-like saddle-point interactions with varying curvature
        saddle_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.01)
                saddle_term += (x_norm[i]**3 - x_norm[j]**3) * np.exp(-distance**3)
        
        # Gradient-based attraction fields with repulsion centers and non-linear coupling
        attraction_term = 0
        for i in range(self.dim):
            attraction_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    attraction_sum += (x_norm[j] / (distance**2 + 0.1)) * \
                                    np.exp(-distance**1.5) * np.sin(5 * distance)
            attraction_term += attraction_sum
        
        # Polynomial chaos with mixed even/odd terms and fractional exponents
        poly_term = 0
        for i in range(self.dim):
            if i % 2 == 0:
                poly_term += x_norm[i]**11 - 4.0*x_norm[i]**6 + 3.0*x_norm[i]**3
            else:
                poly_term += x_norm[i]**9 - 4.5*x_norm[i]**5 + 3.5*x_norm[i]**2
        
        # Cross-dimensional coupling with hyperbolic and logarithmic interactions (restructured)
        cross_term = 0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                cross_term += np.tanh(x_norm[i]) * np.log(np.abs(x_norm[i+1]) + 1.5) * \
                             (x_norm[i]**5 + x_norm[i+1]**5) * np.exp(-np.abs(x_norm[i] - x_norm[i+1]))
        
        # Fractal curvature enhancement with multi-scale interactions
        fractal_term = 0
        for i in range(self.dim):
            fractal_term += (x_norm[i]**8 + 0.5*x_norm[i]**4) * np.sin(10 * x_norm[i])
        
        # Combine all terms with dynamic weights
        result = 0.25 * chaotic_term + 0.20 * saddle_term + 0.15 * attraction_term + \
                 0.25 * poly_term + 0.10 * cross_term + 0.05 * fractal_term
        
        # Add a conditioning term to control the landscape difficulty (improved)
        conditioning = 0.05 * np.sum(x_norm**8)
        
        return result + conditioning
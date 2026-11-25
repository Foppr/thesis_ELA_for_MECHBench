import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic phase interactions with higher frequency components
        chaotic_term = 0
        for i in range(self.dim):
            phase1 = np.sin(20 * x_norm[i]) * np.cos(15 * x_norm[i])
            phase2 = np.sin(8 * x_norm[i]**3) * np.cos(4 * x_norm[i]**2)
            chaotic_term += np.sin(25 * x_norm[i] + phase1) * np.cos(10 * x_norm[i] - phase2) + \
                           np.sin(15 * x_norm[i] + phase2) * np.cos(20 * x_norm[i] - phase1)
        
        # Multi-scale saddle-point interactions with varying coupling strengths
        saddle_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x_norm[i] - x_norm[j])
                coupling = np.exp(-distance**3) * (1 + 0.5 * np.sin(5 * distance))
                saddle_term += (x_norm[i]**3 - x_norm[j]**3) * coupling
        
        # Complex gradient attraction with multiple repulsion centers and dynamic weights
        attraction_term = 0
        for i in range(self.dim):
            attraction_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    weight = 1.0 / (distance**2 + 0.05)
                    attraction_sum += (x_norm[j] * weight) * np.exp(-distance**2)
            attraction_term += attraction_sum
        
        # Modified polynomial chaos with fractional exponents and cross-terms
        poly_term = 0
        for i in range(self.dim):
            if i % 3 == 0:
                poly_term += x_norm[i]**8.5 - 3.0*x_norm[i]**5.2 + 2.0*x_norm[i]**3.7
            elif i % 3 == 1:
                poly_term += x_norm[i]**9.3 - 2.8*x_norm[i]**4.1 + 1.8*x_norm[i]**2.9
            else:
                poly_term += x_norm[i]**7.7 - 3.5*x_norm[i]**6.4 + 2.2*x_norm[i]**4.3
        
        # Novel cross-dimensional coupling with hyperbolic and trigonometric interactions
        cross_term = 0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                interaction = np.tanh(x_norm[i]) * np.sinh(x_norm[i+1]) * \
                             (np.cos(x_norm[i]**2) + np.sin(x_norm[i+1]**2))
                cross_term += interaction
        
        # Additional high-frequency modulation and conditioning
        mod_term = 0
        for i in range(self.dim):
            mod_term += np.sin(50 * x_norm[i]) * np.cos(30 * x_norm[i]) * \
                       np.exp(-x_norm[i]**2)
        
        # Combine all terms with adjusted weights and increased conditioning
        result = 0.3 * chaotic_term + 0.25 * saddle_term + 0.18 * attraction_term + \
                 0.22 * poly_term + 0.05 * cross_term + 0.02 * mod_term
        
        # Enhanced conditioning term with quartic and quintic components
        conditioning = 0.05 * np.sum(x_norm**5) + 0.03 * np.sum(x_norm**6)
        
        return result + conditioning
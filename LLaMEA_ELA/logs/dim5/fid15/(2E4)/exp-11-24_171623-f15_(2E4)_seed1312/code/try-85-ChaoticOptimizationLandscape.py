import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic oscillations with fractal-like frequency modulation
        chaotic_term = 0
        for i in range(self.dim):
            freq_mod = np.sin(x_norm[i] * np.pi * 3) * np.cos(x_norm[i] * np.pi * 1.5)
            chaotic_term += np.sin(20 * x_norm[i] + freq_mod) * np.cos(12 * x_norm[i] - freq_mod) * \
                           np.exp(-np.abs(x_norm[i]))
        
        # Multi-scale saddle-point interactions with dynamic curvature
        saddle_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.01)
                curvature = np.sin(distance * np.pi) * (1 + 0.5 * np.sin(x_norm[i] * x_norm[j]))
                saddle_term += (x_norm[i]**2 - x_norm[j]**2) * curvature * np.exp(-distance**2)
        
        # Adaptive attraction fields with time-varying repulsion centers
        attraction_term = 0
        for i in range(self.dim):
            attraction_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    weight = 1.0 / (distance**2 + 0.05)
                    attraction_sum += (x_norm[j] * weight) * np.exp(-distance * 0.5)
            attraction_term += attraction_sum
        
        # Mixed polynomial chaos with dynamic exponents and fractal scaling
        poly_term = 0
        for i in range(self.dim):
            exponent = 5 + 4 * np.sin(i * np.pi / self.dim)
            if i % 3 == 0:
                poly_term += x_norm[i]**exponent - 2.5*x_norm[i]**(exponent/2) + 1.5*x_norm[i]
            elif i % 3 == 1:
                poly_term += x_norm[i]**(exponent*1.2) - 3.2*x_norm[i]**(exponent/1.8) + 2.1*x_norm[i]**0.7
            else:
                poly_term += x_norm[i]**(exponent*0.8) - 2.8*x_norm[i]**(exponent/2.5) + 1.8*x_norm[i]**1.3
        
        # Dynamic cross-dimensional coupling with hyperbolic and logarithmic interactions
        cross_term = 0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                coupling = np.tanh(x_norm[i] * x_norm[i+1]) * np.log(np.abs(x_norm[i]) + np.abs(x_norm[i+1]) + 1.5)
                cross_term += coupling * (x_norm[i]**5 + x_norm[i+1]**3)
        
        # Combine all terms with adaptive weights
        result = 0.28 * chaotic_term + 0.22 * saddle_term + 0.19 * attraction_term + \
                 0.24 * poly_term + 0.07 * cross_term
        
        # Adaptive conditioning term with fractal-like scaling
        conditioning = 0.05 * np.sum(np.abs(x_norm)**7) * (1 + 0.3 * np.sin(np.sum(x_norm**2)))
        
        return result + conditioning
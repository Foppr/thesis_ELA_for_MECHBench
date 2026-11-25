import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Fractional Brownian motion-like correlation term
        fbm_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = abs(x_scaled[i] - x_scaled[j])
                fbm_term += (distance ** 1.3) * np.sin(5.0 * distance)
        
        # Nested sinusoidal patterns with varying amplitudes and frequencies
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += (
                2.0 * np.sin(8.0 * x_scaled[i]) * 
                np.cos(3.0 * x_scaled[i]**2) + 
                1.5 * np.sin(12.0 * x_scaled[i]) * 
                np.cos(7.0 * x_scaled[i]**3) +
                0.8 * np.sin(15.0 * x_scaled[i]) * 
                np.cos(11.0 * x_scaled[i]**4)
            )
        
        # Asymmetric basin structure with exponential decay
        basin_term = 0.0
        for i in range(self.dim):
            if x_scaled[i] >= 0:
                basin_term += np.exp(-x_scaled[i]**2) * (1.0 + 0.5 * np.sin(4.0 * x_scaled[i]))
            else:
                basin_term += np.exp(-x_scaled[i]**2) * (1.0 + 0.3 * np.cos(6.0 * x_scaled[i]))
        
        # Chaotic component with logistic map-like behavior
        chaotic_term = 0.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            chaotic_term += (r * abs(x_scaled[i]) * (1 - abs(x_scaled[i])) + 
                           0.2 * np.sin(10.0 * x_scaled[i]) * np.cos(5.0 * x_scaled[i]))
        
        # Cross-dimensional interaction with asymmetric weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i % 2 == 0:
                    cross_term += (x_scaled[i] * x_scaled[j] * 
                                 np.sin(3.0 * (x_scaled[i] + x_scaled[j])) + 
                                 0.5 * np.cos(2.0 * (x_scaled[i] - x_scaled[j])))
                else:
                    cross_term += (x_scaled[i] * x_scaled[j] * 
                                 np.cos(4.0 * (x_scaled[i] + x_scaled[j])) + 
                                 0.3 * np.sin(1.5 * (x_scaled[i] - x_scaled[j])))
        
        # Combine all terms with optimized weights
        return 0.7 * fbm_term + 0.6 * nested_term + 0.8 * basin_term + 0.5 * chaotic_term + 0.4 * cross_term + 3.2
import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r_values = np.linspace(3.5, 4.0, dim)
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Chaotic logistic map component for each dimension
        chaotic_term = 0.0
        for i in range(self.dim):
            r = self.r_values[i]
            x_i = x_scaled[i]
            # Logistic map: x_{n+1} = r * x_n * (1 - x_n)
            chaotic_val = r * x_i * (1 - x_i)
            chaotic_term += chaotic_val ** 2
        
        # Fractional Brownian motion-like roughness with Hurst parameter
        fbm_term = 0.0
        hurst = 0.3
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Distance-based correlation with fractional scaling
                dist = abs(x_scaled[i] - x_scaled[j])
                corr = dist ** (2 * hurst)
                fbm_term += corr * np.sin(5 * (x_scaled[i] + x_scaled[j]))
        
        # Saddle-point dominant component with multiple interacting peaks
        saddle_term = 0.0
        for i in range(self.dim):
            # Quadratic saddle with sinusoidal modulation
            saddle_term += (x_scaled[i]**2 - 1)**2 * np.cos(3 * x_scaled[i])
            
        # Cross-dimensional interaction with polynomial and trigonometric mixing
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Mixed polynomial-trigonometric interaction
                poly_interaction = (x_scaled[i]**3 + x_scaled[j]**2) * 0.5
                trig_interaction = np.sin(x_scaled[i] * x_scaled[j]) * 0.3
                cross_term += (poly_interaction + trig_interaction) * (i + j + 1)
        
        # Add a global periodic modulation based on sum of all dimensions
        coord_sum = np.sum(x_scaled)
        global_mod = 1.0 + 0.2 * np.sin(2 * coord_sum) * np.cos(3 * coord_sum)
        
        # Combine all terms with different weights and add constant offset
        result = chaotic_term + fbm_term + saddle_term + cross_term + global_mod + 3.0
        
        return result
import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial basin term - attracts points towards center
        radial_term = np.sum(x_scaled**2)
        
        # Sinusoidal oscillations in multiple directions
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5 * np.pi * x_scaled[i]) * np.cos(3 * np.pi * x_scaled[i])
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(min(5, self.dim)):  # Limit to first 5 dimensions for chaos
            if i == 0:
                chaotic_term += np.sin(10 * x_scaled[i]) * np.cos(7 * x_scaled[i])
            else:
                chaotic_term += np.sin(8 * x_scaled[i-1] + 3 * x_scaled[i]) * np.cos(5 * x_scaled[i])
        
        # Combine all terms with different weights
        return 0.5 * radial_term + 0.3 * sin_term + 0.2 * chaotic_term + 1.0
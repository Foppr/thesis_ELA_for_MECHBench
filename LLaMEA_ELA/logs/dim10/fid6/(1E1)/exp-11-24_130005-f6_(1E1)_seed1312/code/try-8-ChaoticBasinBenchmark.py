import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial basin term - attracts points towards center
        radial_term = np.sum(x_scaled**2)
        
        # Sinusoidal oscillations in multiple directions with higher frequency
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(10 * np.pi * x_scaled[i]) * np.cos(6 * np.pi * x_scaled[i])
        
        # Chaotic component using coupled sine waves for enhanced complexity
        chaotic_term = 0.0
        for i in range(min(7, self.dim)):  # Use more dimensions for chaos
            if i == 0:
                chaotic_term += np.sin(15 * x_scaled[i]) * np.cos(12 * x_scaled[i])
            else:
                chaotic_term += np.sin(11 * x_scaled[i-1] + 7 * x_scaled[i]) * np.cos(9 * x_scaled[i])
        
        # Cross-term interactions between dimensions
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += np.sin(4 * np.pi * x_scaled[i]) * np.cos(4 * np.pi * x_scaled[i+1])
        
        # Combine all terms with different weights
        return 0.4 * radial_term + 0.35 * sin_term + 0.2 * chaotic_term + 0.05 * cross_term + 1.0
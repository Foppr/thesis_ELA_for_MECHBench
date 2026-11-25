import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.a = 3.9
        self.b = 0.5
        self.c = 2.0
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Normalize input to [-1, 1] for chaotic map
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Chaotic map component using logistic map
        chaotic_sum = 0.0
        r = self.a
        for i in range(self.dim):
            if i < len(x_norm):
                # Logistic map: x_{n+1} = r * x_n * (1 - x_n)
                chaotic_val = x_norm[i]
                for _ in range(10):  # Iterate to reach chaotic regime
                    chaotic_val = r * chaotic_val * (1 - chaotic_val)
                chaotic_sum += chaotic_val ** 2
        
        # Polynomial basin component
        poly_basin = np.sum(x**4) + 0.5 * np.sum(x**2)
        
        # Sinusoidal oscillation component
        sin_term = 0.0
        for i in range(self.dim):
            if i < len(x):
                sin_term += np.sin(self.c * x[i]) * np.cos(self.b * x[i])
        
        # Cross-term interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i < len(x) and j < len(x):
                    cross_term += (x[i] - x[j])**2 * np.sin(x[i] + x[j])
        
        # Combine all components with different weights
        return 0.3 * chaotic_sum + 0.4 * poly_basin + 0.2 * sin_term + 0.1 * cross_term
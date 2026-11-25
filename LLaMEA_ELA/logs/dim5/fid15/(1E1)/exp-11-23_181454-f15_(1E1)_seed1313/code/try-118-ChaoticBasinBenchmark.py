import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Normalize input to [-1, 1] for chaotic behavior
        x_norm = x / 5.0
        
        # Radial basin term with chaotic sinusoidal modulation
        r = np.sqrt(np.sum(x_norm**2))
        basin_term = r**2 + 0.1 * np.sin(10 * r) * np.cos(5 * r)
        
        # Multiple sinusoidal oscillations creating complex landscape
        oscillation_term = 0.0
        for i in range(self.dim):
            oscillation_term += np.sin((i + 1) * x[i]) * np.cos((i + 1) * x[i])
            
        # Add chaotic modulation based on all dimensions
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += np.sin(2**i * x[i]) * np.cos(3**i * x[i])
            
        # Global minimum at origin with varying difficulty
        global_min = 0.5 * (np.sum(x**2) + 0.1 * np.sum(np.sin(x)))
        
        return basin_term + oscillation_term + chaotic_mod + global_min
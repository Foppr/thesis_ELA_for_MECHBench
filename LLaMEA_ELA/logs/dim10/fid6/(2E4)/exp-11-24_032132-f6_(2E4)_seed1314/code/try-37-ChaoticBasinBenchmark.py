import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Global minimum at origin
        global_min = 0.0
        
        # Radial basin term with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = r**2 * (1 + 0.1 * np.sin(10 * r))
        
        # Sinusoidal oscillations in multiple directions
        oscillation_term = 0.0
        for i in range(self.dim):
            oscillation_term += np.sin(x[i]) * np.cos(2 * x[i])
        
        # Add a chaotic component based on all dimensions
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(x[i] * np.pi / 2) * np.cos(x[i] * np.pi)
            
        return radial_term + oscillation_term + chaotic_component
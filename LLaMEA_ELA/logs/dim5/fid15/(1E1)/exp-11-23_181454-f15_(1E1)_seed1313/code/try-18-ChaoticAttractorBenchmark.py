import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Define the global minimum at the center
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Normalize input to [-1, 1] for internal calculations
        x_norm = x / 5.0
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            # Create a chaotic sequence that depends on all dimensions
            if i == 0:
                chaotic_term += np.sin(10 * x_norm[i]) * np.cos(5 * x_norm[i])
            else:
                chaotic_term += np.sin(10 * x_norm[i] + chaotic_term) * np.cos(5 * x_norm[i-1])
        
        # Nested attractor terms with different scales
        attractor_term = 0.0
        for i in range(self.dim):
            # Multiple nested attractors with varying strengths and positions
            attractor_term += (x_norm[i] - np.sin(x_norm[i]))**2 + \
                             0.5 * (x_norm[i] - np.cos(x_norm[i]))**2 + \
                             0.1 * (x_norm[i] - np.tan(x_norm[i]))**2
        
        # Sinusoidal modulation that creates a complex, oscillating landscape
        modulation_term = 0.0
        for i in range(self.dim):
            modulation_term += np.sin(2 * np.pi * x_norm[i]) * \
                              np.cos(3 * np.pi * x_norm[i]) * \
                              np.exp(-0.1 * np.sum(x_norm**2))
        
        # Combine all terms with different weights
        result = 2.0 * attractor_term + 0.5 * chaotic_term + 0.3 * modulation_term
        
        # Add a small penalty for being far from the global minimum
        distance_penalty = 0.1 * np.sum((x - self.global_min)**2)
        
        return result + distance_penalty
import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Fractal-like component with recursive self-similarity
        fractal_term = 0.0
        for i in range(self.dim):
            # Nested sinusoidal components with varying frequencies and amplitudes
            fractal_term += (np.sin(2**i * x[i]) * np.cos(3**i * x[i]) + 
                           0.5 * np.sin(5**i * x[i]) * np.cos(7**i * x[i]) +
                           0.2 * np.sin(11**i * x[i]) * np.cos(13**i * x[i]))
        
        # Chaotic gradient modulation using logistic map-like behavior
        chaotic_mod = 1.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            # Simulate chaotic dynamics with feedback from all dimensions
            chaotic_input = np.sum(x_scaled[:i+1]) if i > 0 else x_scaled[i]
            chaotic_mod *= (1 + 0.4 * np.sin(r * chaotic_input * (1 - chaotic_input)))
        
        # Interference pattern with multiple wave sources
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                interference_term += (np.sin(2 * dist) * np.cos(3 * dist) + 
                                   0.3 * np.sin(5 * dist) * np.cos(7 * dist) +
                                   0.1 * np.sin(9 * dist) * np.cos(11 * dist))
        
        # Multi-scale peak structure with varying heights and widths
        peak_term = 0.0
        for i in range(self.dim):
            # Multiple peaks at different scales
            peak_term += (np.exp(-0.5 * (x[i] - 2)**2) + 
                         0.7 * np.exp(-0.3 * (x[i] + 1)**2) +
                         0.4 * np.exp(-0.1 * (x[i] - 3)**2) +
                         0.2 * np.exp(-0.05 * (x[i] + 4)**2))
        
        # Self-similar structure with recursive scaling
        self_similar = 0.0
        for i in range(self.dim):
            # Apply transformation that creates similar patterns at different scales
            scaled_x = x[i] / (1 + np.abs(x[i]))
            self_similar += (np.sin(10 * scaled_x) + 
                           0.5 * np.sin(20 * scaled_x) + 
                           0.2 * np.sin(40 * scaled_x))
        
        # Combined with a global periodic modulation
        coord_sum = np.sum(x_scaled)
        global_mod = 1.0 + 0.3 * np.sin(2 * coord_sum) * np.cos(3 * coord_sum)
        
        # Final combination with different weights
        return (fractal_term * chaotic_mod + 
                interference_term * 0.5 + 
                peak_term * 0.8 + 
                self_similar * 0.3 + 
                global_mod * 0.2 + 10.0)
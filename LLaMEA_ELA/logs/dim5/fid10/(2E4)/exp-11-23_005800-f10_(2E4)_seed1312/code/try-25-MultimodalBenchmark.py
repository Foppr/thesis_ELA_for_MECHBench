import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic barrier penalty term
        barrier_penalty = 0
        for i in range(self.dim):
            barrier_penalty += -np.log(25 - x[i]**2) * np.exp(-0.1 * abs(x[i]))
        
        # Multi-scale sinusoidal oscillation with dynamic frequencies
        sin_component = 0
        for i in range(self.dim):
            freq = 1 + 0.3 * np.sin(0.5 * i) + 0.2 * np.cos(0.7 * i)
            scale = 1 + 0.5 * np.sin(0.4 * i)
            sin_component += scale * np.sin(freq * np.pi * x[i]) * np.cos(freq * np.pi * x[i] / 3)
        
        # Chaotic feedback with exponential coupling
        chaotic_mod = 0
        for i in range(self.dim):
            if i == 0:
                chaotic_mod += x[i] * np.exp(-0.2 * abs(x[i]))
            else:
                chaotic_mod += x[i] * np.sin(0.5 * x[i-1]) + 0.3 * np.exp(-0.1 * abs(x[i])) * x[i-1]
        
        # Quadratic cross-dimensional interaction with adaptive weights
        cross_term = 0
        for i in range(self.dim - 1):
            weight = 0.5 + 0.5 * np.sin(0.3 * i)
            cross_term += weight * (x[i] - x[i+1])**2 * np.exp(-0.1 * abs(x[i] + x[i+1]))
        
        # Combine all components with varying amplitudes
        return 1.2 * barrier_penalty + 2.0 * sin_component + 0.5 * chaotic_mod + 1.0 * cross_term + 2.5 * self.dim
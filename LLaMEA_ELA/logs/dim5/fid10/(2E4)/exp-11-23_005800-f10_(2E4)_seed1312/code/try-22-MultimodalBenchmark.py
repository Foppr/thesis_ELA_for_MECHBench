import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial penalty with variable exponents
        poly_penalty = 0
        for i in range(self.dim):
            poly_penalty += (x[i]**6 - 12 * x[i]**4 + 45 * x[i]**2 - 30) * np.exp(-0.15 * abs(x[i]))
        
        # Enhanced sinusoidal component with frequency modulation
        sin_component = 0
        for i in range(self.dim):
            freq = 2.5 + 0.3 * np.sin(0.4 * i)
            sin_component += np.sin(freq * np.pi * x[i]) * np.cos(freq * np.pi * x[i] / 3)
        
        # Chaotic modulation with feedback connections - slightly modified
        chaotic_mod = 0
        for i in range(self.dim):
            if i == 0:
                chaotic_mod += x[i] * np.sin(0.5 * x[i])
            else:
                chaotic_mod += x[i] * np.sin(0.2 * x[i-1]) + x[i-1] * np.cos(0.6 * x[i])
        
        # Cross-dimensional interaction term
        cross_term = 0
        for i in range(self.dim - 1):
            cross_term += (x[i] - x[i+1])**2 * np.sin(0.3 * np.pi * (x[i] + x[i+1]))
        
        # Combine all components with optimized weights
        return 0.4 * poly_penalty + 1.2 * sin_component + 0.15 * chaotic_mod + 0.9 * cross_term + 3.5 * self.dim
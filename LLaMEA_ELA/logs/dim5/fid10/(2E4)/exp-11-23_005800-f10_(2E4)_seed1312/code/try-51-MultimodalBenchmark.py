import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial penalty with variable exponents and Gaussian attraction
        poly_penalty = 0
        for i in range(self.dim):
            term = x[i]**6 - 12 * x[i]**4 + 45 * x[i]**2 - 30
            gaussian_attraction = np.exp(-0.15 * abs(x[i]))
            poly_penalty += term * gaussian_attraction
        
        # Modified sinusoidal component with frequency modulation and phase shifts
        sin_component = 0
        for i in range(self.dim):
            freq = 2.5 + 0.3 * np.sin(0.4 * i)
            phase = 0.2 * np.cos(0.3 * i)
            sin_component += np.sin(freq * np.pi * x[i] + phase) * np.cos(freq * np.pi * x[i] / 2 + phase)
        
        # Chaotic modulation with feedback connections and dynamic coupling
        chaotic_mod = 0
        for i in range(self.dim):
            if i == 0:
                chaotic_mod += x[i] * np.sin(0.35 * x[i])
            else:
                chaotic_mod += x[i] * np.sin(0.3 * x[i-1]) + x[i-1] * np.cos(0.4 * x[i]) + 0.12 * x[i-1] * np.sin(0.4 * x[i-1])
        
        # Cross-dimensional interaction term with enhanced coupling
        cross_term = 0
        for i in range(self.dim - 1):
            diff = x[i] - x[i+1]
            cross_term += diff**2 * np.sin(0.5 * np.pi * (x[i] + x[i+1])) * np.exp(-0.15 * abs(diff))
        
        # Additional interaction term for higher dimensional complexity
        high_dim_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_dim_interaction += (x[i] * x[j]) / (1 + 0.5 * abs(x[i] - x[j]))
        
        # Combine all components with optimized weights
        return 0.6 * poly_penalty + 1.3 * sin_component + 0.25 * chaotic_mod + 1.1 * cross_term + 0.7 * high_dim_interaction + 3.5 * self.dim
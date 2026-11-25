import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial penalty terms with higher degree
        poly_penalty = np.sum(0.5 * x**6 - 3 * x**4 + 5 * x**2)
        
        # Sinusoidal oscillation component with increased frequency and interaction
        sin_component = 0
        for i in range(self.dim):
            sin_component += np.sin(5 * np.pi * x[i]) * np.cos(3 * np.pi * x[i]) + 0.5 * np.sin(2 * np.pi * x[i])
        
        # Chaotic modulation with altered logistic-like behavior and cross-dimensional interaction
        chaotic_mod = 0
        for i in range(self.dim):
            if i == 0:
                chaotic_mod += x[i] * np.sin(x[i] * 0.7)
            else:
                chaotic_mod += x[i] * np.sin(x[i-1] * 0.4) + x[i-1] * np.cos(x[i] * 0.5)
        
        # Add cross-dimensional interaction term
        cross_term = 0
        for i in range(self.dim - 1):
            cross_term += (x[i] - x[i+1])**2 * np.sin(np.pi * (x[i] + x[i+1]))
        
        # Combine all components with adjusted weights
        return 0.3 * poly_penalty + 1.5 * sin_component + 0.2 * chaotic_mod + 0.1 * cross_term + 3 * self.dim
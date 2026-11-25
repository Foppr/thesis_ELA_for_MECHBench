import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Define chaotic parameters
        self.a = 3.9
        self.b = 0.5
        self.c = 0.1
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Normalize input to [-1, 1] for chaotic map
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Chaotic logistic map component
        chaotic_sum = 0.0
        for i in range(self.dim):
            if i == 0:
                chaotic_sum += self.a * x_norm[i] * (1 - x_norm[i])
            else:
                chaotic_sum += self.a * x_norm[i-1] * (1 - x_norm[i-1])
        
        # Fractal-like structure with nested minima
        fractal_term = 0.0
        for i in range(self.dim):
            # Nested sinusoidal components with varying frequencies
            freq = 2**(i % 4 + 1)
            fractal_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Attractor basin with multiple local minima
        attractor_term = 0.0
        for i in range(1, self.dim):
            attractor_term += (x[i] - x[i-1])**2 + self.b * (x[i] - np.sin(x[i-1]))**2
        
        # Add a global minimum at the origin with additional penalty
        penalty = 0.0
        if np.linalg.norm(x) < 0.5:
            penalty = 0.1 * np.exp(-np.sum(x**2) / 0.1)
        
        # Combine all components with varying weights
        result = 0.3 * chaotic_sum + 0.4 * fractal_term + 0.2 * attractor_term - penalty
        
        return result
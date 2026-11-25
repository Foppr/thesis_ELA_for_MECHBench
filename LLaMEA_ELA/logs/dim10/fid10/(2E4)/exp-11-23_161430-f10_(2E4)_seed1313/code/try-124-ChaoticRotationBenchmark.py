import numpy as np

class ChaoticRotationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate rotation angles for each dimension
        self.angles = np.pi * np.sin(np.arange(dim) * 0.7 + 1.0)
        # Polynomial weights and chaotic modulation factors
        self.poly_weights = 1.0 + 0.5 * np.cos(np.arange(dim) * 1.3 + 0.5)
        self.chaos_mod = 0.8 + 0.4 * np.sin(np.arange(dim) * 1.1 + 0.3)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to input vector
        rotated_x = np.zeros_like(x)
        for i in range(self.dim):
            rotated_x[i] = np.sum(x * np.sin(self.angles[i] * np.arange(self.dim) + self.angles[i]))
        
        # Polynomial component with chaotic modulation
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += self.poly_weights[i] * (rotated_x[i]**4 - 6*rotated_x[i]**2 + 9) * \
                         np.exp(-0.1 * rotated_x[i]**2)
        
        # Sinusoidal component with multiple frequencies
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(i * 0.8 + self.chaos_mod[i])
            sin_term += np.sin(freq * rotated_x[i]) * np.cos(freq * rotated_x[i]**2)
        
        # Chaotic interaction term
        chaos_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            chaos_term += np.sin(3.0 * rotated_x[i] + 0.5 * np.cos(rotated_x[j])) * \
                          np.exp(-0.2 * (rotated_x[i] - rotated_x[j])**2)
        
        # Combined function value
        result = 0.1 * np.sum(rotated_x**2) + 0.3 * poly_term + 0.4 * sin_term + 0.2 * chaos_term
        
        return result
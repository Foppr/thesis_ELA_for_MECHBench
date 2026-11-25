import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with fractal-like scaling
        r = np.sqrt(np.sum(x**2))
        radial_term = r * np.sin(10 * r) * np.cos(5 * r)
        
        # Multi-scale sinusoidal modulation with chaotic frequency ratios
        modulated_sum = 0.0
        frequencies = [1.0, 1.618, 2.718, 3.142, 4.236]  # Golden ratio and transcendental constants
        for i in range(min(self.dim, len(frequencies))):
            freq = frequencies[i % len(frequencies)]
            modulated_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.sin(0.1 * x[i]**2)
        
        # Rotational symmetry breaking with polynomial weights
        rotation_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = np.arctan2(x[j], x[i])
                rotation_term += (x[i]**2 + x[j]**2) * np.sin(3 * angle) * np.cos(2 * angle)
        
        # Adaptive conditioning based on dimensionality and position
        condition_factor = 1.0 + 0.3 * np.sin(self.dim * 0.7) + 0.2 * np.cos(r * 0.3)
        
        # Multi-scale interference pattern using wavelets
        interference = 0.0
        for i in range(self.dim):
            interference += np.exp(-0.5 * (x[i] - np.sin(i))**2) * np.sin(10 * x[i])
        
        # Slight mutation: altered interaction and scaling coefficients
        return condition_factor * (radial_term + 0.7 * modulated_sum + 0.3 * rotation_term + 0.2 * interference)
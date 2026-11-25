import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial_decay = np.exp(-r / 5.0)
        
        # Trigonometric oscillations in multiple dimensions
        trig_sum = 0
        for i in range(self.dim):
            trig_sum += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
            
        # Chaotic modulation using a tent map-like behavior
        chaotic_mod = 0
        for i in range(self.dim):
            if i == 0:
                chaotic_mod += np.abs(x[i] - 2.5) * np.sin(x[i] * 0.7)
            else:
                chaotic_mod += np.abs(x[i] - x[i-1]) * np.cos(x[i] * 0.9)
        
        # Polynomial penalty term for conditioning
        poly_penalty = np.sum(0.1 * x**6 - 2 * x**4 + 5 * x**2)
        
        # Combine all components with different weights
        return 3 * radial_decay + 1.5 * trig_sum + 0.3 * chaotic_mod + 0.1 * poly_penalty + 2 * self.dim
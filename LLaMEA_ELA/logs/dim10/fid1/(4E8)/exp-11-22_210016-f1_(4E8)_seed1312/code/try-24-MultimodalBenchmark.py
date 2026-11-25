import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 5.0) * (1.0 + 0.5 * np.sin(r))
        
        # Trigonometric wave interference in multiple directions
        wave_term = 0.0
        for i in range(self.dim):
            wave_term += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            wave_term += np.sin(5.0 * x[i]) * np.cos(4.0 * x[i])
        
        # Cross-dimensional interaction with chaotic coupling
        chaos_term = 0.0
        for i in range(self.dim - 1):
            chaos_term += np.sin(x[i] * x[i+1]) * np.exp(-abs(x[i] - x[i+1]))
        
        # Additional chaotic sinusoidal modulation based on angular position
        angle_mod = np.sum(np.arctan2(x[1:], x[:-1]) ** 2)
        angular_term = 0.3 * np.sin(angle_mod) * np.cos(angle_mod)
        
        # Combine all terms with different weights
        result = radial_term + wave_term + 0.5 * chaos_term + angular_term
        
        return result
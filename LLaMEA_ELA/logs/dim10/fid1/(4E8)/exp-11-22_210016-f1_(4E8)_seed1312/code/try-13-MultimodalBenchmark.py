import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_normalized**2)
        
        # Multiple sinusoidal components with different frequencies and amplitudes
        f2 = np.sum(np.sin(3 * np.pi * x_normalized) ** 2)
        f3 = np.sum(np.cos(7 * np.pi * x_normalized) ** 2)
        f4 = np.sum(np.sin(11 * np.pi * x_normalized) ** 2)
        
        # Add a complex interaction term that creates intricate local minima
        interaction = np.sum(np.sin(2 * np.pi * x_normalized) * np.cos(4 * np.pi * x_normalized))
        
        # Create a landscape with multiple valleys and ridges using polynomial combinations
        f5 = np.sum((x_normalized**4 - 2*x_normalized**2)**2)
        
        # Add a global scaling factor to control the difficulty
        difficulty_factor = 2.0
        
        # Combine all components with different weights
        result = difficulty_factor * (f1 + 0.3 * f2 + 0.4 * f3 + 0.2 * f4 + 0.1 * f5 + 0.05 * interaction)
        
        # Add a small random perturbation to make it non-deterministic
        noise = 0.01 * np.random.random()
        
        return result + noise
import numpy as np

class NestedParabolicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        self.conditioning = 10.0
        self.periodicity = 2.0 * np.pi
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        result = 0.0
        
        # Nested parabolic valleys with varying scales
        for i in range(self.dim):
            xi = x[i]
            
            # Main parabolic component with adaptive conditioning
            main_term = self.conditioning * (xi - self.global_min[i])**2
            
            # Nested smaller valleys
            nested_valley = 0.0
            for j in range(1, 4):  # Three levels of nesting
                scale = 0.5**j
                freq = 2**(j-1)
                offset = scale * np.sin(xi * freq)
                nested_valley += scale * (xi - offset)**2
            
            # Periodic boundary effects
            periodic_effect = np.sin(xi / self.periodicity) * np.cos(xi / (self.periodicity * 0.5))
            
            # Combine components
            result += main_term + nested_valley + 0.1 * periodic_effect
        
        # Add interaction terms between dimensions
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited cross-dimensional interaction
                interaction_term += 0.3 * np.sin(x[i] * x[j]) * (x[i]**2 + x[j]**2)
        
        return result + interaction_term
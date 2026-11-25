import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.a = 3.9
        self.b = 1.2
        self.c = 3.0
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basin term - encourages convergence to origin with increased curvature
        radial_term = 0.3 * np.sum(x**2)
        
        # Chaotic sinusoidal modulations - creates complex landscape with higher frequency
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Apply chaotic map to each dimension
            chaotic_component = self.a * xi * (1 - xi)  # Logistic map
            # Add sinusoidal modulation based on chaotic output with modified frequency
            chaotic_term += np.sin(chaotic_component * self.b + i * 0.5) * np.cos(xi * self.c + i * 0.3)
        
        # Add interaction terms between dimensions for non-separability with enhanced coupling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += (x[i] - x[j])**2 * np.sin(x[i] + x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Combine all terms with proper scaling
        return radial_term + 0.7 * chaotic_term + 0.1 * interaction_term
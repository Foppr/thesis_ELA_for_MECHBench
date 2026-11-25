import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.a = 3.9
        self.b = 0.5
        self.c = 2.0
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basin term - encourages convergence to origin
        radial_term = 0.1 * np.sum(x**2)
        
        # Chaotic sinusoidal modulations - creates complex landscape
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Apply chaotic map to each dimension
            chaotic_component = self.a * xi * (1 - xi)  # Logistic map
            # Add sinusoidal modulation based on chaotic output
            chaotic_term += np.sin(chaotic_component * self.b + i) * np.cos(xi * self.c)
        
        # Add interaction terms between dimensions for non-separability
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += (x[i] - x[j])**2 * np.sin(x[i] + x[j])
        
        # Combine all terms with proper scaling
        return radial_term + 0.5 * chaotic_term + 0.05 * interaction_term
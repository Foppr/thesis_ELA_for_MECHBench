import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.a = 3.9
        self.b = 1.5
        self.c = 2.5
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial basin term with higher curvature and conditioning
        radial_term = 0.5 * np.sum(x**2) + 0.1 * np.sum(x**4)
        
        # Chaotic sinusoidal modulations with increased frequency and chaos intensity
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Apply chaotic map to each dimension
            chaotic_component = self.a * xi * (1 - xi)  # Logistic map
            # Add sinusoidal modulation based on chaotic output with higher frequency
            chaotic_term += np.sin(chaotic_component * self.b + i * 0.7) * np.cos(xi * self.c + i * 0.4)
        
        # Enhanced interaction terms between dimensions for greater non-separability and conditioning
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Increased coupling strength and added exponential decay
                interaction_term += (x[i] - x[j])**2 * np.sin(x[i] + x[j]) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Add cross-terms for even higher non-separability
        cross_term = 0.0
        for i in range(self.dim):
            cross_term += x[i] * np.sin(x[i] * self.b) * np.cos(x[i] * self.c)
            
        # Combine all terms with proper scaling
        return radial_term + 0.8 * chaotic_term + 0.15 * interaction_term + 0.05 * cross_term
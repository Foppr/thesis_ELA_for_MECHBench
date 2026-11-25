import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.a = 3.8
        self.b = 0.7
        self.c = 1.5
        self.d = 0.3
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basin term - encourages convergence to origin with modified scaling
        radial_term = 0.15 * np.sum(x**2)
        
        # Chaotic sinusoidal modulations - creates complex landscape with enhanced chaos
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Apply chaotic map to each dimension with modified logistic map
            chaotic_component = self.a * xi * (1 - xi)  # Logistic map
            # Add sinusoidal modulation based on chaotic output with additional phase
            chaotic_term += np.sin(chaotic_component * self.b + i * self.d) * np.cos(xi * self.c + i * 0.1)
        
        # Enhanced interaction terms between dimensions for non-separability
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use a more complex interaction term with mixed powers and trigonometric functions
                diff = x[i] - x[j]
                sum_val = x[i] + x[j]
                interaction_term += (diff**2 + 0.5 * sum_val**2) * np.sin(diff * sum_val)
        
        # Add a small noise component to improve robustness
        noise_term = 0.01 * np.sum(np.sin(x * 0.5))
        
        # Combine all terms with proper scaling
        return radial_term + 0.6 * chaotic_term + 0.08 * interaction_term + noise_term
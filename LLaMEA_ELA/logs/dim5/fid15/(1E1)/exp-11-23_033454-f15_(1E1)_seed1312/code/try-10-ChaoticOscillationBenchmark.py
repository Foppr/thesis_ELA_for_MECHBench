import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.constants = np.random.uniform(0.5, 2.0, dim)
        self.amplitudes = np.random.uniform(1.0, 3.0, dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basin term pulling towards origin
        radial_term = 0.1 * np.sum(x**2)
        
        # Sinusoidal oscillation terms creating chaotic behavior
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += self.amplitudes[i] * np.sin(self.constants[i] * x[i])
            sin_term += self.amplitudes[i] * np.cos(self.constants[i] * x[i] * 0.5)
        
        # Cross-terms creating complex interactions between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.3 * np.sin(x[i] * x[j]) * (1.0 + 0.1 * (x[i]**2 + x[j]**2))
        
        # Add chaotic scaling factor
        chaos_factor = 1.0 + 0.5 * np.sin(np.sum(x**2) / 10.0)
        
        return chaos_factor * (radial_term - sin_term + cross_term)
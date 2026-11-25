import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Central attracting force term
        central_force = 0.5 * np.sum(x**2)
        
        # Chaotic sinusoidal waves with exponentially decaying amplitudes
        wave_term = 0.0
        for i in range(self.dim):
            # Exponentially decaying amplitude
            amp = np.exp(-0.1 * i)
            # Sinusoidal component with varying frequency
            freq = 2.0 + 0.5 * i
            wave_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Add a chaotic component using sine of squared coordinates
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(x[i]**2) * np.exp(-0.01 * x[i]**2)
            
        # Combine all terms with different weights
        result = central_force + 0.3 * wave_term + 0.2 * chaotic_term
        
        # Add a small noise term to make it non-deterministic
        noise = 0.001 * np.sum(np.random.randn(self.dim) * x)
        
        return result + noise
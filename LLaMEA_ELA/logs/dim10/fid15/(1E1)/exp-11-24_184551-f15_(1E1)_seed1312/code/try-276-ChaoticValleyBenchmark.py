import numpy as np

class ChaoticValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Base polynomial penalty term
        poly_term = np.sum(x**4) * 0.01
        
        # Sinusoidal wave components creating chaotic valleys
        wave_term = 0.0
        for i in range(self.dim):
            wave_term += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            
        # Additional chaotic component with varying frequencies
        chaos_term = 0.0
        for i in range(self.dim):
            freq = (i + 1) * 0.5
            chaos_term += np.sin(freq * x[i] + np.cos(freq * x[i]))
            
        # Combine all terms with different weights
        return poly_term - wave_term * 0.5 - chaos_term * 0.3
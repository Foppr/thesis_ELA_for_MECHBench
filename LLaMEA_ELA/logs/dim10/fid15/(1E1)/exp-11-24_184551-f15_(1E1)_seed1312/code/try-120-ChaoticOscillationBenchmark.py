import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        result = 0.0
        
        # Add sinusoidal oscillations with varying frequencies
        for i in range(self.dim):
            # Use each dimension with different frequency and amplitude
            freq = 2 * np.pi * (i + 1)
            amp = 1.0 / (i + 1)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Add exponential barrier terms to create sharp transitions
        barrier_penalty = 0.0
        for i in range(self.dim):
            # Create barriers at -4, -2, 0, 2, 4 with increasing steepness
            barrier_positions = [-4.0, -2.0, 0.0, 2.0, 4.0]
            for pos in barrier_positions:
                distance = abs(x[i] - pos)
                # Exponential barrier that becomes very steep near positions
                barrier_penalty += np.exp(5.0 * (1.0 - distance)) if distance < 1.0 else 0.0
        
        # Add quadratic basin term to encourage convergence
        basin_term = 0.1 * np.sum(x**2)
        
        # Add noise term for non-triviality
        noise = 0.01 * np.sum(np.sin(10 * x))
        
        return result + barrier_penalty + basin_term + noise
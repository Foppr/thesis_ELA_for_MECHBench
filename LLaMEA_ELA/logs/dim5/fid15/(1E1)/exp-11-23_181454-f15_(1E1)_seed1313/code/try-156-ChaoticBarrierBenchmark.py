import numpy as np

class ChaoticBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute barrier positions for each dimension
        self.barrier_positions = np.linspace(-4.0, 4.0, 9)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Sinusoidal oscillation term creating many local minima
        oscillation = np.sum(np.sin(5.0 * x) * np.cos(3.0 * x))
        
        # Exponential barrier terms that become very steep near boundaries
        barriers = 0.0
        for i in range(self.dim):
            # Create exponential barriers at positions -4, -3, ..., 4
            for pos in self.barrier_positions:
                barriers += np.exp(2.0 * (abs(x[i] - pos) - 0.5))
        
        # Add a chaotic component using logistic map-like behavior
        chaotic = 0.0
        if self.dim >= 2:
            # Use first two dimensions for chaotic interaction
            x1, x2 = x[0], x[1]
            # Logistic map inspired term
            chaotic = np.sin(100 * (x1**2 + x2**2)) * np.exp(-0.1 * (x1**2 + x2**2))
        
        # Combine all components with different weights
        result = 0.5 * oscillation + 0.3 * barriers + 0.2 * chaotic
        
        # Add a small noise term to make it more realistic
        noise = 0.001 * np.sum(np.random.randn(self.dim))
        
        return result + noise
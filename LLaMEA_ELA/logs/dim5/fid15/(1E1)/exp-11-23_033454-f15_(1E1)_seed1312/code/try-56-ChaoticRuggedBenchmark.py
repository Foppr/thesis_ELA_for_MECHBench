import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute barrier positions for different dimensions
        self.barrier_positions = []
        if dim >= 2:
            # Create a set of barrier positions in the search space
            for i in range(min(5, dim)):
                pos = np.random.uniform(-4.0, 4.0, dim)
                self.barrier_positions.append(pos)
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation term - creates many local minima
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Exponential barrier terms - create rugged landscape
        barrier_term = 0.0
        for pos in self.barrier_positions:
            dist = np.sum((x - pos)**2)
            barrier_term += np.exp(-dist / 2.0) * 0.5
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        if self.dim >= 2:
            for i in range(self.dim - 1):
                chaotic_term += (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
        
        # Combine all terms with different weights
        result = 0.3 * sin_term + 0.4 * barrier_term + 0.3 * chaotic_term
        
        # Add a small random perturbation to make it non-deterministic
        noise = 0.01 * np.random.random()
        
        return result + noise
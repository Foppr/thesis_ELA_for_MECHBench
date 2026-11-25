import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute barrier positions for 2D case
        if dim == 2:
            self.barrier_positions = []
            for i in range(-4, 5):
                for j in range(-4, 5):
                    self.barrier_positions.append([i, j])
        else:
            self.barrier_positions = [[0.0] * dim]
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation term - creates many local minima
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Exponential barrier term - creates rugged landscape with steep walls
        barrier_term = 0.0
        if self.dim == 2:
            for pos in self.barrier_positions:
                dist = np.sqrt((x[0] - pos[0])**2 + (x[1] - pos[1])**2)
                barrier_term += np.exp(-dist**2 / 0.3) * 2.0
        else:
            # For higher dimensions, use a more complex barrier structure
            for i in range(0, self.dim, 2):
                if i + 1 < self.dim:
                    dist = np.sqrt((x[i] - 1.0)**2 + (x[i+1] - 1.0)**2)
                    barrier_term += np.exp(-dist**2 / 0.5) * 1.5
                    dist = np.sqrt((x[i] + 1.0)**2 + (x[i+1] + 1.0)**2)
                    barrier_term += np.exp(-dist**2 / 0.5) * 1.5
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        if self.dim >= 2:
            for i in range(self.dim - 1):
                chaotic_term += (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
        
        # Combine all terms with different weights
        result = 0.5 * sin_term + 0.3 * barrier_term + 0.2 * chaotic_term
        
        # Add small random noise for additional challenge
        noise = 0.01 * np.random.random()
        
        return result + noise
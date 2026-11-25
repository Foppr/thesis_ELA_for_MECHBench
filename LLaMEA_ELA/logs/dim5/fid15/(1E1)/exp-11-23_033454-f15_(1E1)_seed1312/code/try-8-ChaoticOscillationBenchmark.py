import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.omega = 2 * np.pi * np.random.uniform(0.5, 2.0, dim)
        self.amplitude = np.random.uniform(0.5, 2.0, dim)
        self.phase = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial basin term - creates a smooth central attraction
        basin_term = 0.1 * np.sum(x**4)
        
        # Chaotic sinusoidal oscillation term - creates complex landscape
        oscillation_term = 0.0
        for i in range(self.dim):
            oscillation_term += self.amplitude[i] * np.sin(self.omega[i] * x[i] + self.phase[i])
            oscillation_term += 0.5 * self.amplitude[i] * np.sin(2 * self.omega[i] * x[i] + self.phase[i])
        
        # Add coupling between dimensions for increased complexity
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += 0.3 * np.sin(x[i] * x[j]) * (1 + 0.1 * (x[i]**2 + x[j]**2))
        
        # Add a small random component to prevent exact replication
        random_component = 0.01 * np.random.random()
        
        return basin_term - oscillation_term + coupling_term + random_component
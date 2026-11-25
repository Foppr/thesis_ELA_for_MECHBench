import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r = 3.9  # Logistic map parameter for chaos
        self.penalty_weight = 10.0
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spherical component
        sphere = np.sum(x_norm**2)
        
        # Chaotic component using logistic map
        chaotic = 0.0
        for i in range(self.dim):
            # Use each dimension as initial condition for logistic map
            xi = x_norm[i]
            # Apply logistic map iterations to generate chaos
            for _ in range(10):  # Iterate to reach chaotic regime
                xi = self.r * xi * (1 - xi)
            chaotic += xi**2
        
        # Add penalty for being far from origin to encourage convergence
        penalty = self.penalty_weight * np.sum(np.abs(x_norm)**3)
        
        return sphere + 0.5 * chaotic + penalty
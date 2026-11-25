import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with multiple local minima
        radial = np.sum(x_normalized**2)
        
        # Sinusoidal oscillations in multiple directions
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(2 * np.pi * x_normalized[i]) * np.cos(3 * np.pi * x_normalized[i])
            
        # Asymmetric saddle points with varying weights
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = (i + 1) * (j + 1)
                saddle += weight * (x_normalized[i]**2 - x_normalized[j]**2) * np.exp(-0.5 * (x_normalized[i] - x_normalized[j])**2)
        
        # Radial basis function component with varying widths
        rbf = 0.0
        for i in range(self.dim):
            rbf += np.exp(-5.0 * (x_normalized[i] - 0.3)**2) + np.exp(-3.0 * (x_normalized[i] + 0.4)**2)
            
        # Chaotic modulation using logistic map
        chaotic = 0.0
        r = 3.9
        for i in range(self.dim):
            x_prev = 0.5
            for _ in range(10):
                x_prev = r * x_prev * (1 - x_prev)
            chaotic += np.sin(x_normalized[i] * x_prev * 10) * np.cos(x_normalized[i] * x_prev * 7)
            
        # Cross-term interactions with exponential decay
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                cross += np.exp(-dist * 2.0) * np.sin(5 * (x_normalized[i] + x_normalized[j]))
        
        # Final combined function with adaptive weights
        return (0.25 * radial + 0.3 * sinusoidal + 0.15 * saddle + 
                0.1 * rbf + 0.15 * chaotic + 0.05 * cross)
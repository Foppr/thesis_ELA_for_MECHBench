import numpy as np

class ChaoticNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r = 3.9
        self.tau = 0.5
        self.alpha = 0.1
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic neural network component with time-delayed feedback
        chaotic_sum = 0
        for i in range(self.dim):
            # Simulate chaotic dynamics using logistic map
            chaotic_val = self.r * x[i] * (1 - x[i])
            
            # Add time-delayed feedback effect
            if i >= 2:
                delayed = x[i-2] * np.exp(-self.tau * abs(x[i-2]))
                chaotic_val += self.alpha * delayed
            
            chaotic_sum += chaotic_val**2
        
        # Adaptive basin-hopping landscape
        basin_sum = 0
        for i in range(self.dim):
            # Multiple local minima with varying depths
            depth = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            center = 2.0 * np.cos(i * np.pi / (self.dim + 2))
            basin_sum += depth * (x[i] - center)**2
            
        # Fractional polynomial modulation
        poly_mod = 0
        for i in range(self.dim):
            power = 1.5 + 0.5 * np.sin(i * np.pi / (self.dim + 3))
            poly_mod += np.abs(x[i])**power
        
        # Cross-term coupling with dynamic weights
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.sin(i * j / (self.dim + 1)) * np.cos(i + j)
                cross_sum += weight * x[i] * x[j]
        
        # Global scaling and normalization
        scale_factor = 0.5 + 0.5 * np.sin(self.dim * np.pi / 8)
        
        return scale_factor * (chaotic_sum + basin_sum + poly_mod + cross_sum)
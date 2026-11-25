import numpy as np

class ChaoticNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r = 3.9
        self.tau = 0.3
        self.alpha = 0.2
        
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
        
        # Enhanced basin-hopping landscape with dynamic centers and depths
        basin_sum = 0
        for i in range(self.dim):
            # Dynamic depth and center based on position
            depth = 1.5 + 0.8 * np.sin(i * np.pi / (self.dim + 1))
            center = 2.5 * np.cos(i * np.pi / (self.dim + 3)) + 0.5 * np.sin(i * np.pi / (self.dim + 2))
            basin_sum += depth * (x[i] - center)**2
            
        # Fractional polynomial modulation with dynamic exponents
        poly_mod = 0
        for i in range(self.dim):
            power = 1.2 + 0.8 * np.sin(i * np.pi / (self.dim + 4))
            poly_mod += np.abs(x[i])**power
        
        # Enhanced cross-term coupling with adaptive weights
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic weight based on both indices and values
                weight = np.sin(i * j / (self.dim + 2)) * np.cos(i + j) * (1 + 0.3 * np.sin(x[i] + x[j]))
                cross_sum += weight * x[i] * x[j]
        
        # Add noise component to increase ruggedness
        noise = 0.1 * np.sum(np.sin(x * 10))
        
        # Global scaling and normalization
        scale_factor = 0.7 + 0.3 * np.sin(self.dim * np.pi / 10)
        
        return scale_factor * (chaotic_sum + basin_sum + poly_mod + cross_sum) + noise
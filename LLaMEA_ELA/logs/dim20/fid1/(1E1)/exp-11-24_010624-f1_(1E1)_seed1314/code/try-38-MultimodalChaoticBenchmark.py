import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive parameters for each dimension
        self.adaptive_params = np.array([1.0 + 0.5 * np.sin(i * 0.5) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential decay component with adaptive scaling
        for i in range(self.dim):
            exp_term = self.adaptive_params[i] * np.exp(-0.1 * x[i]**2) * np.cos(2 * x[i])
            result += exp_term
            
        # Trigonometric coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling range
                coupling = np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
                result += 0.2 * coupling
                
        # Adaptive curvature with polynomial modulation
        for i in range(self.dim):
            curvature = 0.1 * x[i]**4 * np.sin(3 * x[i]) * self.adaptive_params[i]
            result += curvature
            
        # Multi-scale sinusoidal modulation
        for i in range(self.dim):
            scale_mod = np.sin(0.2 * x[i]) + 0.5 * np.sin(0.8 * x[i]) + 0.3 * np.sin(1.5 * x[i])
            result += 0.05 * scale_mod
            
        # Add global rotation and scaling effect
        rotation_matrix = np.random.rand(self.dim, self.dim) * 2 - 1
        rotated_x = np.dot(rotation_matrix, x)
        global_effect = np.sum(rotated_x**2) * 0.01
        result += global_effect
        
        # Add noise to increase irregularity
        noise = 0.02 * np.sum(np.sin(x * 5))
        result += noise
        
        return result
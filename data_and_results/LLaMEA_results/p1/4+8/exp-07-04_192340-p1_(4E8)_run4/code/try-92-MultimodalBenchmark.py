import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute a more complex rotation matrix with orthogonalization
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add a larger random shift to increase asymmetry
        self.shift = np.random.uniform(-1.0, 1.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Compute the multimodal function with enhanced chaotic and barrier components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with stronger variation
            result += (x_rot[i] ** 2) * (i + 1) * 0.7
            # Composite sinusoidal components with higher frequency interactions
            result += 5 * np.sin(x_rot[i] * (i + 1) * np.pi / 2) * np.cos(x_rot[i] * (i + 1) * np.pi / 4)
            # Logarithmic barrier with increased influence
            log_term = np.log(1 + np.abs(x_rot[i]) ** 3)
            result += log_term * (i + 1) * 0.25
            # Chaotic component with exponential decay - slightly modified frequency
            chaotic = np.sin(np.pi * x_rot[i] * np.sin(x_rot[i] * 1.5)) * np.exp(-0.15 * np.abs(x_rot[i]))
            result += chaotic * (i + 1) * 0.12
            # Additional exponential decay term to encourage convergence
            exp_term = np.exp(-0.5 * x_rot[i] ** 2)
            result += exp_term * (i + 1) * 0.06
        
        # Add a strong penalty for large values to enforce boundary adherence
        result += 0.015 * np.sum(np.abs(x_rot) ** 4)
        
        return result
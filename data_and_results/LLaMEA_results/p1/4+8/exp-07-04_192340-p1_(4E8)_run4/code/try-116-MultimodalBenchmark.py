import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add a small random shift to make the function less symmetric
        self.shift = np.random.uniform(-0.5, 0.5, dim)
        # Global optimum at origin in rotated space
        self.optimum = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Compute the multimodal function with exponential and trigonometric components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with varying coefficients
            result += (x_rot[i] ** 2) * (i + 1) * 0.5
            # Trigonometric coupling terms
            result += 2 * np.sin(x_rot[i] * (i + 1)) * np.cos(x_rot[i] * (i + 1) * 0.5)
            # Exponential decay term to encourage convergence
            exp_term = np.exp(-0.1 * np.abs(x_rot[i]))
            result += exp_term * (i + 1) * 0.3
            # Additional coupling between dimensions
            if i > 0:
                coupling = np.sin(x_rot[i-1] * x_rot[i]) * 0.2
                result += coupling
        
        # Dynamic penalty based on proximity to global optimum
        distance_to_opt = np.linalg.norm(x_rot - self.optimum)
        penalty = 10 * np.exp(-distance_to_opt / 2.0)
        result += penalty
        
        return result
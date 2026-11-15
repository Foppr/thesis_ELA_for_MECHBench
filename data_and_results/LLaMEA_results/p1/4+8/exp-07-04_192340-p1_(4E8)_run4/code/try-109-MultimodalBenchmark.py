import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add a small random shift to make the function less symmetric
        self.shift = np.random.uniform(-0.5, 0.5, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Compute the multimodal function with polynomial, trigonometric, and exponential components
        result = 0.0
        for i in range(self.dim):
            # Polynomial term with varying exponents
            result += (x_rot[i] ** 3) * (i + 1) * 0.1
            # Trigonometric components with varying frequencies
            result += 2 * np.sin(x_rot[i] * (i + 1)) * np.cos(x_rot[i] * (i + 1) * 2)
            # Exponential barrier to prevent divergence
            exp_term = np.exp(-0.1 * np.abs(x_rot[i]))
            result += exp_term * (i + 1) * 0.2
            # Additional chaotic component using a sine of sine
            chaotic = np.sin(np.sin(x_rot[i] * (i + 1)))
            result += chaotic * (i + 1) * 0.05
            # Mixed polynomial and trigonometric term
            result += 0.5 * (x_rot[i] ** 2) * np.cos(x_rot[i] * (i + 1) * 0.5)
        
        # Add a penalty for large values to encourage convergence
        result += 0.001 * np.sum(np.abs(x_rot) ** 4)
        
        return result
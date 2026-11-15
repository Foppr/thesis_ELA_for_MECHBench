import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for rotation-invariance
        self.rotation = np.random.rand(dim, dim)
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Normalize the rotation matrix
        self.rotation = self.rotation / (np.linalg.norm(self.rotation) + 1e-8)
        # Add a small random shift to make the function less symmetric
        self.shift = np.random.uniform(-0.5, 0.5, dim)
        # Adaptive noise parameter
        self.noise_level = np.random.uniform(0.1, 0.5)
        # Saddle-point control parameter
        self.saddle_param = np.random.uniform(0.5, 2.0)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Compute the multimodal function with hybrid exponential-logarithmic components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with varying coefficients
            result += (x_rot[i] ** 2) * (i + 1) * 0.1
            # Exponential-logarithmic interaction term
            exp_log_term = np.exp(-np.abs(x_rot[i])) * np.log(1 + np.abs(x_rot[i]))
            result += exp_log_term * (i + 1) * 0.2
            # Saddle-point structure using hyperbolic functions
            saddle = np.sinh(x_rot[i] * self.saddle_param) * np.cosh(x_rot[i] * self.saddle_param)
            result += saddle * (i + 1) * 0.15
            # Adaptive noise component
            noise = np.random.normal(0, self.noise_level) * np.sin(x_rot[i] * np.pi * (i + 1))
            result += noise * (i + 1) * 0.05
            # Composite exponential term for ruggedness
            exp_term = np.exp(-0.5 * (x_rot[i] ** 2)) * np.sin(x_rot[i] * np.pi * (i + 1))
            result += exp_term * (i + 1) * 0.1
            # Additional logarithmic barrier to prevent divergence
            log_barrier = np.log(1 + np.abs(x_rot[i]))
            result += log_barrier * (i + 1) * 0.08
        
        # Add a penalty for large values to encourage convergence
        result += 0.001 * np.sum(np.abs(x_rot) ** 3)
        
        return result
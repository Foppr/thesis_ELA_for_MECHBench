import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add a small random shift to make the function less symmetric
        self.shift = np.random.uniform(-0.5, 0.5, dim)
        # Saddle point configuration
        self.saddle_points = np.random.uniform(-3, 3, (dim, 5))
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Compute the multimodal function with exponential and polynomial components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with varying coefficients
            result += (x_rot[i] ** 2) * (i + 1) * 0.5
            # Exponential decay terms with different scales
            result += 2 * np.exp(-0.5 * (x_rot[i] ** 2)) * (i + 1) * 0.1
            # Polynomial interactions
            result += 0.5 * (x_rot[i] ** 4) * (i + 1) * 0.01
            # Saddle point clustering component
            saddle_contribution = 0.0
            for j in range(5):
                dist = np.abs(x_rot[i] - self.saddle_points[i, j])
                saddle_contribution += np.exp(-dist * 0.5) * (j + 1) * 0.05
            result += saddle_contribution
        
        # Add a dynamic penalty based on landscape curvature
        curvature_penalty = 0.0
        for i in range(self.dim):
            # Estimate local curvature using finite differences
            h = 1e-4
            second_diff = (np.exp(-0.5 * (x_rot[i] + h)**2) - 2 * np.exp(-0.5 * (x_rot[i])**2) + np.exp(-0.5 * (x_rot[i] - h)**2)) / (h ** 2)
            curvature_penalty += np.abs(second_diff) * (i + 1) * 0.01
        
        result += curvature_penalty
        
        return result
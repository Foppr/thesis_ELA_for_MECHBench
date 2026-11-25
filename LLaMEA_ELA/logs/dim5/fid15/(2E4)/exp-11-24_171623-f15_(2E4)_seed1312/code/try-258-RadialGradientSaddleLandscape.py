import numpy as np

class RadialGradientSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-3.0, 3.0, (15, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 15)
        # Gradient field parameters
        self.grad_magnitudes = np.random.uniform(1.0, 5.0, 10)
        self.grad_directions = np.random.rand(10, dim)
        self.grad_directions = self.grad_directions / np.linalg.norm(self.grad_directions, axis=1, keepdims=True)
        # Saddle point clusters
        self.saddle_centers = np.random.uniform(-4.0, 4.0, (8, dim))
        self.saddle_strengths = np.random.uniform(0.5, 3.0, 8)
        self.saddle_eigenvals = np.random.uniform(-2.0, 2.0, (8, dim))
        # Adaptive conditioning
        self.conditioning_factors = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Normalize to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(len(self.rbf_centers)):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            diff = x_norm - center
            rbf_sum += np.exp(-np.sum(diff**2) / (2 * width**2))
        
        # Gradient field component with adaptive magnitudes
        grad_sum = 0.0
        for i in range(len(self.grad_magnitudes)):
            direction = self.grad_directions[i]
            magnitude = self.grad_magnitudes[i]
            proj = np.dot(x_norm, direction)
            grad_sum += magnitude * proj * np.exp(-0.5 * np.sum((x_norm - 0.5 * direction)**2))
        
        # Saddle point clusters with eigenvalue-based potential
        saddle_sum = 0.0
        for i in range(len(self.saddle_centers)):
            center = self.saddle_centers[i]
            strength = self.saddle_strengths[i]
            eigenvals = self.saddle_eigenvals[i]
            diff = x_norm - center
            # Quadratic form with eigenvalues
            quad_form = np.sum(eigenvals * diff**2)
            saddle_sum += strength * np.exp(-0.5 * quad_form)
        
        # Combine components with adaptive conditioning
        result = 0.3 * rbf_sum + 0.4 * grad_sum - 0.3 * saddle_sum
        
        # Adaptive conditioning factor
        cond_factor = np.prod(1.0 + self.conditioning_factors * np.abs(x_norm))
        
        # Add global penalty and conditioning
        penalty = 0.1 * np.sum(np.abs(x_norm)**3)
        return result * cond_factor + penalty + 0.05 * np.sum(x_norm**6)
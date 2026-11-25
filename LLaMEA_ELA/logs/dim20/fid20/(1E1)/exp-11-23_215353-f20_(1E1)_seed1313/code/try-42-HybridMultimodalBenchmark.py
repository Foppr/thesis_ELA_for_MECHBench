import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for dimensionality
        self.rotation_matrix = np.random.rand(dim, dim) - 0.5
        self.rotation_matrix = np.linalg.qr(self.rotation_matrix)[0]
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to introduce non-separability
        x_rot = self.rotation_matrix @ x
        
        # Sinusoidal component with multiple frequencies
        sin_component = np.sum(np.sin(2 * np.pi * x_rot) + 
                              0.5 * np.sin(4 * np.pi * x_rot) + 
                              0.3 * np.sin(6 * np.pi * x_rot))
        
        # Polynomial distortion with mixed exponents
        poly_component = np.sum((x_rot**4 + 0.7 * x_rot**3 - 0.5 * x_rot**2 + 0.2 * x_rot)**1.8)
        
        # Radial basis function component with dynamic scaling
        rbfs = []
        centers = np.linspace(-5, 5, min(10, self.dim))
        for i in range(min(10, self.dim)):
            center = centers[i] if self.dim > 1 else 0
            rbfs.append(np.exp(-0.5 * (x_rot - center)**2 / (0.5 + 0.5 * i)))
        rbf_component = np.sum(rbfs)
        
        # Dynamic scaling based on input magnitude
        scale_factor = 1.0 + 0.3 * np.mean(np.abs(x_rot))
        
        # Combine components with adaptive weights
        return scale_factor * (0.4 * sin_component + 0.35 * poly_component - 0.25 * rbf_component) + 2.1
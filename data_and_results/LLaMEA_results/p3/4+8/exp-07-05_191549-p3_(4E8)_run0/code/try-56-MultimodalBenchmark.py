import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for dimensionality
        self.rotation_matrix = np.random.rand(dim, dim) - 0.5
        self.rotation_matrix = np.linalg.qr(self.rotation_matrix)[0]
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to create rotation-invariance challenge
        x_rot = self.rotation_matrix @ x
        
        # Base quadratic term
        f1 = np.sum(x_rot**2)
        
        # Composite sinusoidal interference with varying frequencies
        f2 = 0.3 * np.sum(np.sin(5.0 * x_rot) * np.cos(3.0 * x_rot) * np.sin(2.0 * x_rot))
        
        # Chaotic component using sine of exponential
        f3 = 0.25 * np.sum(np.sin(np.exp(x_rot)) * np.cos(np.exp(0.5 * x_rot)))
        
        # Nested optima with radial scaling
        f4 = 0.2 * np.sum((x_rot**2 + 1.0)**2 * np.sin(10.0 * x_rot))
        
        # Adaptive conditioning based on variable magnitude
        f5 = 0.1 * np.sum(np.abs(x_rot) * np.sin(4.0 * x_rot))
        
        # Combine all terms
        return f1 + f2 + f3 + f4 + f5
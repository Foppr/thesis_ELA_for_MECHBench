import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for dimensionality
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        np.fill_diagonal(self.rotation, 1.0)
        self.rotation = self.rotation / np.linalg.norm(self.rotation, axis=1, keepdims=True)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Apply rotation to create anisotropic structure
        x_rot = np.dot(self.rotation, x_norm)
        
        # Hyperellipsoid terms with varying eccentricities
        f1 = np.sum((x_rot**2) * (1 + 0.5 * np.sin(3 * x_rot))**2)
        
        # Embedded sine-wave interference for multimodality
        f2 = np.sum(np.sin(10 * x_rot + np.sin(5 * x_rot))**2)
        
        # Cross-dimensional coupling with exponential decay
        f3 = np.sum(np.exp(-0.1 * np.abs(x_rot[:-1] - x_rot[1:])) * (x_rot[:-1]**2 + x_rot[1:]**2))
        
        # Asymmetric polynomial terms with chaotic modulation
        f4 = np.sum((x_rot**3 + 0.3 * x_rot**5 + 0.1 * x_rot**7) * np.cos(2 * np.pi * x_rot))
        
        # Additional noise-like term with controlled randomness
        noise = np.sin(7 * x_rot + np.cos(4 * x_rot)) * 0.05
        f5 = np.sum(noise**2)
        
        # Combine all components with weighted contributions
        return 0.8 * f1 + 0.6 * f2 + 0.3 * f3 + 0.2 * f4 + 0.1 * f5
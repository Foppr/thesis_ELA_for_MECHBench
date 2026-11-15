import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize rotation matrix and conditioning parameters
        np.random.seed(42)  # For reproducibility
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        self.conditioning = np.random.uniform(1, 100, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Apply rotation and conditioning
        x_rot = self.rotation_matrix @ x_norm
        x_cond = x_rot * np.sqrt(self.conditioning)
        
        # Spherical component
        f1 = np.sum(x_cond**2)
        
        # Saddle component with multiple peaks
        f2 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Gaussian peaks with random centers and widths
        peaks = np.random.randn(5, self.dim)
        widths = np.random.uniform(0.5, 2.0, 5)
        gaussian = 0.0
        for i in range(5):
            center = peaks[i]
            width = widths[i]
            gaussian += np.exp(-np.sum(((x_norm - center) / width)**2) / 2)
        f3 = -gaussian
        
        # Cross-dimensional interaction terms
        interaction = 0.0
        for i in range(self.dim - 1):
            interaction += (x_norm[i]**2 + x_norm[i+1]**2) * np.sin(5 * np.pi * (x_norm[i] + x_norm[i+1]))
        f4 = interaction
        
        # Adaptive noise component
        noise = np.random.normal(0, 0.1, self.dim)
        f5 = np.sum(noise * x_norm)
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5
import numpy as np

class RotatedSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation_matrix = np.random.rand(dim, dim) - 0.5
        self.rotation_matrix = np.dot(self.rotation_matrix, self.rotation_matrix.T)
        np.fill_diagonal(self.rotation_matrix, 1.0)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to the input vector
        x_rotated = np.dot(self.rotation_matrix, x)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Sum of sinusoidal terms with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            xi = x_rotated[i]
            freq = 2 * np.pi * (i + 1) * (1.0 + 0.5 * np.sin(i))
            amp = 1.0 + 0.3 * np.cos(i)
            f2 += amp * np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Add noise component to increase irregularity
        noise = 0.1 * np.sum(np.random.rand(self.dim) * np.sin(10.0 * x))
        
        # Polynomial corruption with non-integer powers
        f3 = 0.05 * np.sum((x**3.7 + 0.9 * x**2.8 + 0.6 * x**1.9 + 0.3 * x**1.2) / self.dim)
        
        # Saddle point structure with exponential interference
        f4 = 0.15 * np.sum(np.exp(-0.2 * np.abs(x)) * np.sin(8.0 * x) * np.cos(5.0 * x))
        
        # Asymmetric multimodal structure with varying curvature
        f5 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.1 - 0.5 * x**2.3 + 0.2 * x) / self.dim)
        
        # Combine all components
        return f1 + f2 + noise + f3 + f4 + f5
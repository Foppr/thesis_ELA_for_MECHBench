import numpy as np

class AsymmetricRotatedEllipsoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix and scaling factors
        np.random.seed(42)  # For reproducibility
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        self.scales = np.logspace(0, 2, dim)  # Scales from 1 to 100
    
    def f(self, x):
        # Apply rotation and scaling
        x_rot = self.rotation_matrix @ x
        x_scaled = x_rot * self.scales
        
        # Ellipsoidal basin term
        ellipsoid = np.sum(x_scaled**2)
        
        # Asymmetric saddle points with sinusoidal modulation
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i]**2 - 10 * np.cos(0.5 * x[i]))**2
        
        # Cross-term interaction with rotation
        cross = 0.0
        for i in range(self.dim - 1):
            cross += (x_rot[i] * x_rot[i+1]) * np.sin(0.3 * (x_rot[i] + x_rot[i+1]))
        
        # High-frequency oscillation to increase conditioning
        high_freq = np.sum(np.sin(10 * x)**2)
        
        # Add noise to increase ruggedness
        noise = 0.1 * np.sum(np.random.randn(self.dim) * x)
        
        # Combine all components
        return 0.5 * ellipsoid + 1.2 * saddle + 0.8 * cross + 1.0 * high_freq + noise
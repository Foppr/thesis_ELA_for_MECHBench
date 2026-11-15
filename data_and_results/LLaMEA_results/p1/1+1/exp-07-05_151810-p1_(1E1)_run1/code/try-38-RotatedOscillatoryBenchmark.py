import numpy as np

class RotatedOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrix
        self.rotation_matrix = np.random.rand(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation
        x_rot = self.rotation_matrix @ x
        
        # Periodic oscillation component
        periodic = np.sum(np.sin(2.0 * np.pi * x_rot) * np.cos(2.0 * np.pi * x_rot))
        
        # Gaussian peaks with varying heights and widths
        gaussian_peaks = np.sum(0.5 * np.exp(-0.5 * (x_rot - 1.0)**2) + 0.3 * np.exp(-0.5 * (x_rot + 1.0)**2))
        
        # Saddle-point basin component
        saddle = np.sum(0.1 * x_rot**2 - 0.01 * x_rot**4)
        
        # Cross-shaped attraction wells
        cross_wells = np.sum(np.abs(x_rot) - 0.5 * np.abs(x_rot)**0.5)
        
        # High-frequency noise component
        noise = np.sum(0.05 * np.sin(10.0 * x_rot) * np.cos(10.0 * x_rot))
        
        # Combine all components
        result = periodic + gaussian_peaks + saddle + cross_wells + noise
        
        return result
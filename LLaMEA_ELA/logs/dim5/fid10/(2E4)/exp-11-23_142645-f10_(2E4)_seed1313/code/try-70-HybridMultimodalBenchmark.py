import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for dynamic conditioning
        self.rotation_matrix = np.random.rand(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical component
        spherical = np.sum(x**2)
        
        # Step function component with varying thresholds
        step = 0.0
        for i in range(self.dim):
            threshold = 2.0 * np.sin(i * 0.5) + 1.0
            step += np.floor(np.abs(x[i]) / (threshold + 0.1)) * (i + 1)
        
        # Gaussian peaks with dynamic positions and widths
        gaussian = 0.0
        num_peaks = min(5, self.dim)
        for i in range(num_peaks):
            peak_pos = 3.0 * np.sin(i * 0.7) + 2.0 * np.cos(i * 0.9)
            width = 0.5 + 0.5 * np.sin(i * 0.3)
            gaussian += np.exp(-0.5 * ((x[i % self.dim] - peak_pos) / width)**2)
        
        # Dynamic rotation component
        rotated_x = self.rotation_matrix @ x
        rotation_component = np.sum(rotated_x**4) / (self.dim + 1.0)
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combine all components with dynamic weights
        weight_spherical = 0.5 + 0.2 * np.sin(np.sum(x) * 0.2)
        weight_step = 0.3 + 0.1 * np.cos(np.sum(x) * 0.1)
        weight_gaussian = 0.2 + 0.1 * np.sin(np.sum(x) * 0.3)
        
        return (condition_factor * 
                (weight_spherical * spherical + 
                 weight_step * step + 
                 weight_gaussian * gaussian) + 
                0.1 * rotation_component + 
                0.05 * np.sum(np.abs(x)**3))
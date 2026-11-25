import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for dimensionality
        self.rotation_matrix = np.random.rand(dim, dim) - 0.5
        self.rotation_matrix = np.linalg.qr(self.rotation_matrix)[0]
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Apply rotation to create non-separable structure
        x_rotated = self.rotation_matrix @ x_norm
        
        # Ellipsoid component with varying condition numbers
        ellipsoid = np.sum((x_rotated**2) * np.exp(np.arange(self.dim) * 0.5))
        
        # Periodic noise component with multiple frequencies and amplitudes
        periodic_noise = 0
        frequencies = [1.0, 2.0, 3.0, 4.0]
        amplitudes = [0.5, 0.3, 0.2, 0.1]
        for freq, amp in zip(frequencies, amplitudes):
            periodic_noise += amp * np.sin(freq * np.pi * x_norm)
        
        # Saddle-point repulsion with varying strength
        saddle_repulsion = 0
        for i in range(self.dim - 1):
            saddle_repulsion += (x_norm[i]**2 - x_norm[i+1]**2)**2
        
        # Cross-term coupling with trigonometric modulation
        cross_coupling = 0
        for i in range(self.dim - 2):
            cross_coupling += np.sin(2.0 * np.pi * (x_norm[i] + x_norm[i+1] + x_norm[i+2]))
        
        # Asymmetric gradient component with exponential decay
        asym_gradient = np.sum(np.abs(x_norm) * np.exp(-0.5 * x_norm**2) * 
                              np.sin(3.0 * np.pi * x_norm))
        
        # Combined function with adaptive scaling
        result = ellipsoid + periodic_noise + saddle_repulsion + cross_coupling + asym_gradient
        
        # Add controlled noise for robustness
        noise = 0.1 * np.random.rand() * (1.0 + 0.1 * np.abs(np.mean(x_norm)))
        
        return result + noise
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for dimensionality
        self.rotation_matrix = np.random.rand(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Apply rotation to decorrelate dimensions
        x_rot = self.rotation_matrix @ x_norm
        
        # Saddle-point structure with harmonic coupling
        saddle = np.sum(x_rot**2 * np.cos(3 * np.pi * x_rot))
        
        # Multi-scale spectral components with varying frequencies
        spectral = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            spectral += np.sin(freq * np.pi * x_rot[i]) * np.cos(freq * np.pi * x_rot[i])
        
        # Chaotic modulation based on radial distance and dimensionality
        r = np.sqrt(np.sum(x_rot**2))
        chaotic_mod = np.sin(10 * r) * np.cos(7 * r) * (1 + 0.3 * np.sin(self.dim * r))
        
        # Banding effect with periodic interference patterns
        banding = 0.0
        for i in range(self.dim):
            banding += np.sin(8 * np.pi * x_rot[i]) * np.cos(5 * np.pi * x_rot[i])
        
        # Combine all terms with adaptive scaling
        total = saddle + 0.5 * spectral + 0.3 * chaotic_mod + 0.2 * banding
        
        # Add dimensionality-dependent conditioning
        condition = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return condition * total
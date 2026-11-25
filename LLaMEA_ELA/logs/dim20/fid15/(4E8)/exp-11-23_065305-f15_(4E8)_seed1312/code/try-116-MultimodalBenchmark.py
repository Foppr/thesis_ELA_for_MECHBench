import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Rotation matrix for subspace interaction
        rotation = np.eye(self.dim)
        if self.dim > 1:
            for i in range(0, self.dim-1, 2):
                angle = np.pi / 4 * (i % 7) 
                rotation[i:i+2, i:i+2] = [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
        
        x_rot = rotation @ x
        
        # Composite sinusoidal terms with varying frequencies and phases
        sin_term = np.sum(np.sin(2 * x_rot) + 0.5 * np.sin(5 * x_rot) + 0.3 * np.sin(8 * x_rot)) / self.dim
        
        # Polynomial interaction with mixed degrees
        poly_term = np.sum(x_rot**2 + 0.1 * x_rot**4 + 0.01 * x_rot**6) / self.dim
        
        # Multi-scale exponential decay with chaotic modulation
        exp_decay = np.sum(np.exp(-x_rot**2 / (2 * self.dim)) * 
                          np.exp(-0.5 * (x_rot - 1)**2 / self.dim) * 
                          np.exp(-0.3 * (x_rot + 1)**2 / self.dim)) / self.dim
        
        # Cross-dimensional coupling with phase shifts
        cross_coupling = 0.2 * np.sum(np.sin(x_rot[:-1] + x_rot[1:]) * 
                                    np.cos(0.5 * x_rot[:-1] - 0.3 * x_rot[1:])) / (self.dim - 1)
        
        # Asymmetric polynomial potential with different scaling per dimension
        asym_poly = np.sum(np.abs(x_rot)**3 + 0.2 * np.abs(x_rot)**5 + 0.05 * np.abs(x_rot)**7) / self.dim
        
        # Chaotic radial component with multiple frequency harmonics
        radius = np.sqrt(np.sum(x_rot**2))
        radial_component = 0.15 * (np.sin(3 * radius) + 0.5 * np.sin(7 * radius) + 
                                 0.3 * np.sin(11 * radius)) * np.exp(-radius / 3)
        
        # Subspace interaction with different scaling factors
        subspace_interaction = 0.1 * np.sum(np.sin(x_rot[::2])**2 + 0.5 * np.cos(x_rot[1::2])**2) / (self.dim // 2)
        
        # High-frequency chaotic modulation
        chaotic_mod = 0.05 * np.sum(np.sin(13 * x_rot) * np.cos(9 * x_rot) * 
                                  np.exp(-x_rot**2)) / self.dim
        
        # Combined result with global scaling
        result = (sin_term + poly_term + exp_decay + cross_coupling + 
                 asym_poly + radial_component + subspace_interaction + chaotic_mod)
        
        return float(result)
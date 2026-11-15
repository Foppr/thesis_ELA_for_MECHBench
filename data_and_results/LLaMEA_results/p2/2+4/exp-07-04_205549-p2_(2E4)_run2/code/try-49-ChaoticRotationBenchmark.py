import numpy as np

class ChaoticRotationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for conditioning
        np.random.seed(42)
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Apply rotation to introduce dimension coupling
        x_rot = self.rotation_matrix @ x_norm
        
        # Base quadratic term with conditioning
        base = np.sum(x_rot**2)
        
        # Hybrid exponential-sinusoidal components
        hybrid = 0.0
        for i in range(self.dim):
            # Exponential decay with sinusoidal modulation
            exp_term = np.exp(-0.5 * x_rot[i]**2)
            sin_term = np.sin(10 * np.pi * x_rot[i])
            hybrid += exp_term * sin_term
            
        # Chaotic component with multiple frequencies
        chaotic = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 2)
            chaotic += np.sin(freq * x_rot[i]) * np.cos(freq * x_rot[i]) * np.exp(-0.3 * x_rot[i]**2)
            
        # Dynamic conditioning based on distance from origin
        dist = np.sqrt(np.sum(x_rot**2))
        dynamic_cond = 0.5 * dist * np.sin(15 * dist)
        
        # Cross-dimensional interaction with exponential coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.exp(-2.0 * (x_rot[i]**2 + x_rot[j]**2)) * np.sin(20 * (x_rot[i] - x_rot[j]))
                
        # Multimodal penalty with varying scales
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.3 * (np.sin(12 * x_rot[i]) + 0.5 * np.sin(24 * x_rot[i])) * np.exp(-0.4 * x_rot[i]**2)
            
        # Global minimum enhancement
        global_min = 0.1 * np.sum(np.sin(5 * x_rot)**2)
        
        return base + hybrid + chaotic + dynamic_cond + cross_interaction + penalty + global_min
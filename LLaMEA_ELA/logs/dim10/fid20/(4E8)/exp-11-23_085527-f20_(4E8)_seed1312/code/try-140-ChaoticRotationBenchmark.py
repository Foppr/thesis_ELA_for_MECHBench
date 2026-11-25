import numpy as np

class ChaoticRotationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for chaos induction
        np.random.seed(42)
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
    
    def f(self, x):
        # Apply rotation to introduce non-separability and chaos
        x_rotated = self.rotation_matrix @ x
        
        # Scale to [-1, 1] for stable computation
        x_scaled = x_rotated / 5.0
        
        # Polynomial base with mixed degrees
        poly_term = np.sum(x_scaled**2) + 0.5 * np.sum(x_scaled**4) + 0.1 * np.sum(x_scaled**6)
        
        # Sinusoidal modulation with chaotic frequency coupling
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2 * np.pi * (1 + 0.3 * np.sin(i * 1.7) + 0.2 * np.cos(i * 2.3))
            sin_term += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Cross-term interactions with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = (x_scaled[i]**2 + x_scaled[j]**2)
                exp_decay = np.exp(-dist / 2.0)
                interaction = np.sin(3 * x_scaled[i] * x_scaled[j]) * np.cos(2 * x_scaled[i] * x_scaled[j])
                cross_term += exp_decay * interaction
        
        # Chaotic component with recursive coupling
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(x_scaled[i] + 0.5 * np.sin(x_scaled[(i+1) % self.dim])) * \
                      np.cos(x_scaled[i] + 0.3 * np.cos(x_scaled[(i+2) % self.dim]))
        
        # Combine all components with adaptive weights
        return 3.0 * poly_term + 2.5 * sin_term + 1.8 * cross_term + 1.2 * chaotic
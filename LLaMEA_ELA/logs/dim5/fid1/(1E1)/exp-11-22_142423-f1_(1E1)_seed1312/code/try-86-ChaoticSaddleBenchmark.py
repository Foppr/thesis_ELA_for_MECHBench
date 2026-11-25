import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for chaotic mixing
        np.random.seed(42)
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation for chaotic mixing
        x_rot = self.rotation_matrix @ x
        
        # Base quadratic term with varying weights
        f = 0.5 * np.sum(x_rot**2)
        
        # Add chaotic saddle points with sinusoidal modulation
        for i in range(self.dim):
            f += 0.3 * np.sin(7 * x_rot[i]) * np.cos(5 * x_rot[(i + 1) % self.dim]) * (1 + 0.2 * np.sin(3 * x_rot[i]))
            
        # Add multi-scale oscillations with different frequencies
        for i in range(self.dim):
            f += 0.15 * np.sin(12 * x_rot[i]) * np.cos(9 * x_rot[(i + 2) % self.dim]) * np.sin(6 * x_rot[(i + 3) % self.dim])
            
        # Introduce irregular penalty terms with exponential growth
        f += 0.2 * np.sum(np.exp(0.1 * np.abs(x_rot)) - 1)
        
        # Add cubic interactions to create saddle points
        for i in range(self.dim):
            f += 0.1 * x_rot[i]**3 * x_rot[(i + 1) % self.dim] * (1 + 0.1 * np.sin(4 * x_rot[i]))
            
        # Include cross-dimensional coupling with varying strengths
        for i in range(self.dim):
            f += 0.25 * np.cos(8 * x_rot[i]) * np.sin(6 * x_rot[(i + 3) % self.dim]) * (1 + 0.15 * np.cos(2 * x_rot[(i + 2) % self.dim]))
            
        # Add perturbed hyperbolic terms to create complex curvature
        f += 0.1 * np.sum(np.tanh(x_rot)**2)
        
        # Final chaotic modulation with non-uniform scaling
        for i in range(self.dim):
            f *= 1 + 0.05 * np.sin(10 * x_rot[i]) * np.cos(7 * x_rot[(i + 1) % self.dim])
            
        return f
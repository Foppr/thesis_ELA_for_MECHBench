import numpy as np

class ChaoticRotationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        np.random.seed(42)
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        # Clip input to domain [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation
        x_rot = self.rotation_matrix @ x
        
        # Base quadratic term with conditioning
        result = np.sum(x_rot**2) * (1.0 + 0.1 * np.linalg.norm(x_rot))
        
        # Add composite sinusoidal modulations with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2 ** (i % 5 + 1)
            amp = 1.0 + 0.2 * np.sin(i)
            result += amp * np.sin(freq * x_rot[i]) * np.cos(freq * x_rot[i] * 0.3)
            
        # Add saddle-point structure with exponential scaling
        for i in range(self.dim):
            result += 0.5 * np.exp(-0.1 * (x_rot[i] - 2.0)**2) * (x_rot[i] - 2.0)**4
            
        # Add cross-dimensional coupling with rotation-aware interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(0.5 * (x_rot[i] + x_rot[j])) * np.cos(0.3 * (x_rot[i] - x_rot[j]))
                result += 0.05 * interaction
                
        # Add chaotic component with nested frequency modulation
        chaotic = 0.08 * np.sum(np.sin(10 * np.sin(5 * x_rot)) * np.cos(7 * x_rot))
        result += chaotic
        
        # Add a non-uniform penalty term to increase conditioning difficulty
        penalty = 0.2 * np.sum(np.abs(x_rot)**3.5)
        result += penalty
        
        return result
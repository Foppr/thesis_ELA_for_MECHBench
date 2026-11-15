import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Global minimum at the center
        self.global_min = np.zeros(dim)
        # Random rotation matrix for orientation
        self.rotation = np.random.rand(dim, dim)
        self.rotation, _ = np.linalg.qr(self.rotation)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to the input
        x_rot = self.rotation @ x
        
        # Base quadratic term with rotation
        f1 = np.sum((x_rot - self.global_min)**2)
        
        # Sinusoidal interference with varying frequencies and amplitudes
        f2 = np.sum(np.sin(2 * x_rot) + 0.5 * np.sin(5 * x_rot) + 0.3 * np.sin(8 * x_rot))
        
        # Polynomial coupling with cross-terms
        f3 = np.sum(x_rot**4 + 0.5 * x_rot**3 + 0.2 * x_rot**2)
        
        # Exponential barrier terms
        f4 = np.sum(np.exp(0.2 * np.abs(x_rot)) * np.cos(x_rot))
        
        # Fractal-like component using recursive sine
        fractal = 0.0
        for i in range(1, self.dim + 1):
            fractal += np.sin(2**i * x_rot[i-1]) / (2**i)
        f5 = fractal
        
        # Chaotic modulation with perturbed global minimum
        f6 = np.sum(np.sin(x_rot * np.cos(x_rot)) * np.exp(-0.1 * x_rot**2))
        
        # Cross-dimensional interaction with dynamic weights
        f7 = 0.0
        for i in range(self.dim - 1):
            f7 += (x_rot[i] - x_rot[i+1])**2 * np.sin(x_rot[i] + x_rot[i+1])
            
        # Combine all components with dynamic weights
        return 0.15 * f1 + 0.20 * f2 + 0.15 * f3 + 0.15 * f4 + 0.10 * f5 + 0.15 * f6 + 0.10 * f7
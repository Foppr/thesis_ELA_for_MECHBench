import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Quadratic base with varying coefficients
        f1 = np.sum(0.5 * (x_normalized**2) + 0.5 * (x_normalized**4))
        
        # Chaotic sine coupling with varying frequencies and phases
        f2 = np.sum(np.sin(13 * x_normalized + np.sin(7 * x_normalized)) * np.exp(-0.5 * np.abs(x_normalized)))
        
        # Radial basis interaction term with multiple peaks
        f3 = 0.8 * np.sum(np.exp(-np.sum((x_normalized[:, None] - x_normalized[None, :])**2, axis=0) / (2 * 0.2**2)))
        
        # Asymmetric polynomial scaling to create rugged terrain
        f4 = 0.3 * np.sum(np.where(x_normalized > 0, x_normalized**3, -0.5 * x_normalized**3))
        
        # Additional exponential barrier term
        f5 = 0.1 * np.sum(np.exp(-0.1 * np.abs(x_normalized)) * np.sin(5 * x_normalized)**2)
        
        # Combined function with enhanced complexity and non-smooth regions
        return f1 + f2 + f3 + f4 + f5 + 0.05 * np.sum(np.abs(x_normalized)**5)
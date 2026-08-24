import numpy as np

class PolynomialSpiralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients for varying dimensions
        self.coeffs = np.random.randn(dim, 5)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component
        f1 = 0.0
        for i in range(self.dim):
            for j in range(5):
                f1 += self.coeffs[i, j] * np.polyval([1, 0, 1], x_norm[i]) ** j
        
        # Adaptive conditioning term
        f2 = np.sum((x_norm ** 2) * (1 + 0.5 * np.sin(3 * np.pi * x_norm)))
        
        # Spiral structure with multiple rotations
        spiral_term = 0.0
        for i in range(self.dim - 1):
            dx = x_norm[i+1] - x_norm[i]
            dy = x_norm[i+1] + x_norm[i]
            spiral_term += np.sin(2 * np.pi * np.sqrt(dx**2 + dy**2)) * np.exp(-0.1 * (dx**2 + dy**2))
        
        # Global multimodal component with varying scales
        f4 = np.sum(np.sin(10 * x_norm) * np.cos(5 * x_norm) * np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Combine all components
        return 0.3 * f1 + 1.2 * f2 + 0.8 * spiral_term + 1.5 * f4
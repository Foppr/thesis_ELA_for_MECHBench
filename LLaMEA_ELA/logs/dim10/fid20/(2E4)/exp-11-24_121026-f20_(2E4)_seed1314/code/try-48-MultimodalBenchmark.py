import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic term with conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic tent map component with varying parameter
        tent_map = np.zeros_like(x_norm)
        for i in range(self.dim):
            if x_norm[i] < 0.5:
                tent_map[i] = 2 * x_norm[i]
            else:
                tent_map[i] = 2 * (1 - x_norm[i])
        
        f2 = np.sum(tent_map**4)
        
        # Radial basis function with multiple centers
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        rbf_sum = 0.0
        for i in range(len(centers)):
            rbf_sum += np.exp(-np.sum((x_norm - centers[i])**2) / 0.1)
        f3 = -rbf_sum
        
        # Mixed polynomial and trigonometric terms for additional complexity
        f4 = np.sum(x_norm**5 * np.sin(5 * np.pi * x_norm))
        
        # Add a global repulsion term to prevent easy convergence
        f5 = 0.3 * np.sum(np.abs(x_norm)**0.3)
        
        # Additional high-frequency component for increased complexity
        f6 = 0.2 * np.sum(np.sin(18 * x_norm) * np.cos(7 * x_norm**2))
        
        # Add a fourth-order polynomial with random coefficients for extra ruggedness
        f7 = 0.08 * np.sum((x_norm**4 - 0.4 * x_norm**3 + 0.2 * x_norm**2 - 0.1 * x_norm)**2)
        
        # Add a sinusoidal modulation based on the sum of dimensions
        f8 = 0.15 * np.sin(np.sum(x_norm) * np.pi / 2)
        
        return f1 + 0.3 * f2 + 0.25 * f3 + 0.15 * f4 + 0.08 * f5 + 0.06 * f6 + 0.05 * f7 + 0.04 * f8
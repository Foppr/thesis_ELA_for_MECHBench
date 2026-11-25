import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal modulation with multiple frequencies and amplitudes
        sin_modulation = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) * 
                               np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm))
        
        # Radial basis function component with varying widths and centers
        rbf = 0.0
        for i in range(self.dim):
            rbf += np.exp(-0.5 * (x_norm[i] - 0.5)**2 / 0.1**2) + \
                   np.exp(-0.5 * (x_norm[i] + 0.3)**2 / 0.2**2) + \
                   np.exp(-0.5 * (x_norm[i] - 0.8)**2 / 0.15**2)
        
        # Asymmetric saddle point structure with exponential scaling
        saddle = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**2 * 
                       np.exp(-0.3 * (x_norm[:-1] + x_norm[1:])**2))
        
        # Non-separable polynomial interactions with cross-dimensional coupling
        poly_interaction = np.sum((x_norm[:-1]**3 + x_norm[1:]**3) * 
                                (x_norm[:-1]**2 + x_norm[1:]**2) * 
                                np.exp(-0.2 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Chaotic repulsive force field with fractal-like behavior
        chaotic_repulsion = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                chaotic_repulsion += 0.5 * np.sin(10 * dist) * np.exp(-dist**2)
        
        # Additional high-frequency oscillatory component
        high_freq = 0.3 * np.sum(np.sin(15 * np.pi * x_norm) * 
                               np.cos(17 * np.pi * x_norm) * 
                               np.sin(19 * np.pi * x_norm))
        
        # Add noise term with controlled variance
        noise = 0.1 * np.random.normal(0, 1)
        
        return sin_modulation + rbf + saddle + poly_interaction + chaotic_repulsion + high_freq + noise
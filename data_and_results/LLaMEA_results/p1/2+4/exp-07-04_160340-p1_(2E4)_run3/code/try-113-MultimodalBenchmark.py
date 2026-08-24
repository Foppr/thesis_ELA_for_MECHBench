import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5]
        x = x / 5.0
        
        # Fractal component using recursive sine waves
        fractal = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Create fractal-like behavior with nested sine waves
            for k in range(1, 6):
                fractal += np.sin(2**(k+1) * np.pi * xi) / (2**k)
        
        # Polynomial base with varying curvature
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Chaotic perturbation using tent map
        chaotic = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Tent map: chaotic dynamics with parameter 2.0
            if xi < 0.5:
                chaotic += 2.0 * xi
            else:
                chaotic += 2.0 * (1.0 - xi)
        
        # Nested minima with exponential decay
        nested = 0.0
        for i in range(1, 8):
            # Create nested minima at different scales
            scale = 1.0 / (2.0**i)
            center = np.full(self.dim, scale)
            # Randomly perturb centers for complexity
            np.random.seed(i)
            center = center + np.random.uniform(-scale/2, scale/2, self.dim)
            
            # Distance to center
            dist = np.sum((x - center)**2)
            # Add exponentially decaying minimum
            nested += np.exp(-dist / (2.0 * scale**2)) / (i**2)
        
        # Combine all components
        result = polynomial + fractal + 0.5 * chaotic - nested
        
        # Add a global scaling factor to ensure proper fitness range
        result = result * (1.0 + 0.1 * np.sum(x**2))
        
        return result
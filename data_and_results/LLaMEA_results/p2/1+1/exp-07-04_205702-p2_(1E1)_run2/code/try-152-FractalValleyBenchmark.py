import numpy as np

class FractalValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrices for different dimensions
        self.rotations = []
        for i in range(4):
            angle = np.pi * i / 8
            c, s = np.cos(angle), np.sin(angle)
            rot = np.array([[c, -s], [s, c]])
            full_rot = np.eye(self.dim)
            full_rot[:2, :2] = rot
            self.rotations.append(full_rot)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply multiple rotation transformations
        rotated_x = [self.rotations[i % len(self.rotations)] @ x for i in range(4)]
        
        # Base fractal-like term with multiple scales
        f1 = 0.0
        for i, rx in enumerate(rotated_x):
            scale = 2.0 ** (i - 1)
            f1 += scale * np.sum(np.sin(scale * rx)**2 + np.cos(scale * rx)**2)
        
        # Add dynamic conditioning with sine modulation
        f2 = 0.0
        for i in range(self.dim):
            cond = 1.0 + 0.5 * np.sin(0.3 * i)
            f2 += cond * (x[i]**2 + 0.1 * np.sin(10 * x[i])**2)
        
        # Introduce valley-like structure with multiple basins
        f3 = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi, xj = x[i], x[i+1]
                f3 += 0.5 * (xi**2 + xj**2) * np.exp(-0.1 * (xi - xj)**2)
        
        # Add fractal-like interaction terms
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                f4 += 0.3 * np.sin(dist)**3 * np.cos(dist)**2
        
        # Add noise and scaling for robustness
        noise = 0.01 * np.random.rand()
        
        # Combine all components with dynamic weights
        weights = [0.8, 0.1, 0.05, 0.05]
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4 + noise
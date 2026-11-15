import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.wave_frequencies = np.random.uniform(1.0, 3.0, dim)
        self.decay_rates = np.random.uniform(0.5, 2.0, dim)
        self.basin_centers = np.random.uniform(-5, 5, (4, dim))
        self.basin_radii = np.random.uniform(1.0, 2.5, 4)
        self.rotation_matrices = [np.random.rand(dim, dim) for _ in range(3)]
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        f_val = np.sum(x**2)
        
        # Add exponential decay interactions
        for i in range(self.dim):
            f_val += 0.3 * np.exp(-self.decay_rates[i] * np.abs(x[i])) * np.sin(self.wave_frequencies[i] * x[i])
        
        # Add trigonometric wave patterns with rotation
        for i in range(3):
            rotated_x = self.rotation_matrices[i] @ x
            wave_sum = np.sum(np.sin(self.wave_frequencies * rotated_x) * np.cos(self.wave_frequencies * rotated_x))
            f_val += 0.2 * wave_sum
        
        # Add probabilistic basin attraction regions
        for i in range(4):
            dist = np.linalg.norm(x - self.basin_centers[i])
            if dist < self.basin_radii[i]:
                f_val += 0.4 * np.exp(-0.5 * (dist / self.basin_radii[i])**2) * np.sin(2 * np.pi * dist)
        
        # Add cross-dimensional polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term = (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
                f_val += 0.1 * poly_term
        
        # Add a global oscillatory modulation
        norm = np.linalg.norm(x)
        f_val += 0.25 * np.sin(0.5 * norm) * np.cos(0.3 * norm) * np.exp(-0.1 * norm)
        
        return f_val
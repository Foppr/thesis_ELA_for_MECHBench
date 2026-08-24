import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.poly_coeffs = np.random.uniform(-1, 1, (5, dim))
        self.wave_freqs = np.random.uniform(1, 6, dim)
        self.basin_centers = np.random.uniform(-5, 5, (4, dim))
        self.basin_radii = np.random.uniform(0.5, 2.0, 4)
        self.basin_weights = np.random.uniform(0.5, 2.0, 4)
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        f_val = 0.0
        
        # Polynomial chaos expansion terms
        for i in range(5):
            term = 1.0
            for j in range(self.dim):
                term *= np.polyval(self.poly_coeffs[i], x[j])
            f_val += 0.1 * term
        
        # Trigonometric wave interactions
        for i in range(self.dim):
            wave = np.sin(self.wave_freqs[i] * x[i]) * np.cos(self.wave_freqs[i] * x[i])
            f_val += 0.2 * wave
        
        # Adaptive basin structure
        for i in range(4):
            dist = np.linalg.norm(x - self.basin_centers[i])
            if dist < self.basin_radii[i]:
                f_val += self.basin_weights[i] * np.exp(-dist**2 / (2 * self.basin_radii[i]**2))
        
        # Cross-variable coupling with dynamic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(3 * x[i]) * np.cos(2 * x[j]) + np.cos(4 * x[i]) * np.sin(5 * x[j])
                f_val += 0.15 * coupling * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Global scaling with dynamic frequency modulation
        norm = np.linalg.norm(x)
        f_val += 0.3 * np.sin(2 * norm) * np.cos(1.5 * norm) * (1 + 0.2 * np.sin(0.5 * norm))
        
        return f_val
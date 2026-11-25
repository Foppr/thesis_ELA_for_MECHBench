import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-based recursive sine-wave interactions
        fractal_sine = 0.0
        for i in range(self.dim):
            fractal_sine += np.sin(2 ** (i + 1) * x[i]) * np.cos(2 ** (i + 1) * x[i])
        
        # Self-similar basin structures with varying scales
        basin_structure = 0.0
        for i in range(self.dim):
            scale = 2.0 ** (i % 3)
            basin_structure += (x[i] ** 2) * np.exp(-0.5 * (x[i] / scale) ** 2)
        
        # Logarithmic barrier penalties with nested complexity
        log_barrier = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                log_barrier += np.log(1 + np.exp(5.0 * (np.abs(x[i]) - 4.0))) * np.sin(x[i])
            else:
                log_barrier += 0.5 * (x[i] ** 2) * np.cos(3 * x[i])
        
        # Nested polynomial-trigonometric interactions
        nested_poly_trig = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-term interaction
                nested_poly_trig += (x[i] ** 3) * np.sin(x[j]) * np.cos(x[i] * x[j])
        
        # Multi-scale Gaussian peaks with varying heights and widths
        gaussian_peaks = 0.0
        centers = np.linspace(-4.5, 4.5, 9)
        for center in centers:
            gaussian_peaks += np.exp(-0.5 * np.sum((x - center) ** 2) / (0.5 + 0.2 * np.abs(center))) * np.sin(2 * np.pi * np.sum((x - center) ** 2))
        
        # Cross-term exponential attraction basins with fractal scaling
        cross_attraction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j]) ** 2 + 1e-8)
                cross_attraction += np.exp(-dist) * np.sin(3 * np.pi * dist) * (1.0 + 0.1 * np.sin(dist))
        
        # Combined fitness with adjusted weights
        return 0.3 * fractal_sine + 0.25 * basin_structure + 0.2 * log_barrier + 0.1 * nested_poly_trig + 0.1 * gaussian_peaks + cross_attraction
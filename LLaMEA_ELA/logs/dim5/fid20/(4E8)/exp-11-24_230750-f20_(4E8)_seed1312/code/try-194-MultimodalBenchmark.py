import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similar structure using iterative scaling
        fractal = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Apply multiple scales of sinusoidal modulation
            scale_factors = [1.0, 0.5, 0.25]
            for scale in scale_factors:
                fractal += np.sin(scale * xi) * np.cos(scale * xi) * np.exp(-scale * np.abs(xi))
        
        # Adaptive radial symmetry with varying influence radii
        radial = 0.0
        centers = np.linspace(-4, 4, 7)
        for center in centers:
            dist = np.sum((x - center) ** 2)
            radial += np.exp(-0.1 * dist) * np.sin(3 * np.pi * dist) * np.cos(3 * np.pi * dist)
        
        # Mixed polynomial-trigonometric interactions
        poly_trig = 0.0
        for i in range(self.dim):
            poly_trig += (x[i] ** 4 - 2 * x[i] ** 2 + 1) * np.sin(5 * x[i]) * np.cos(5 * x[i])
        
        # Cross-term coupling with exponentially decaying interactions
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.exp(-0.5 * (x[i] - x[j]) ** 2) * np.sin(x[i] + x[j])
        
        # Boundary-adaptive penalty with logarithmic scaling
        boundary = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                boundary += np.log(1 + np.abs(x[i]) - 4.5) * (np.abs(x[i]) - 4.5)
        
        # Combined fitness function with dynamic weighting
        return 0.3 * fractal + 0.25 * radial + 0.2 * poly_trig + 0.15 * cross + 0.1 * boundary
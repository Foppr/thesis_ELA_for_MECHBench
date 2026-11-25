import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic fractal structure with recursive sine-wave patterns
        fractal = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple chaotic scales with varying frequencies
            scales = [1.0, 0.7, 0.4, 0.2]
            for scale in scales:
                fractal += np.sin(scale * xi**3) * np.cos(scale * xi**2) * np.exp(-scale * np.abs(xi))
        
        # Dynamic radial symmetry with non-uniform influence
        radial = 0.0
        centers = np.linspace(-4.8, 4.8, 9)
        for center in centers:
            dist = np.sum((x - center)**2)
            radial += np.exp(-0.05 * dist) * np.sin(4 * np.pi * dist**0.7) * np.cos(2 * np.pi * dist**0.5)
        
        # Mixed high-order polynomial-trigonometric interactions
        poly_trig = 0.0
        for i in range(self.dim):
            poly_trig += (x[i]**6 - 3*x[i]**4 + 3*x[i]**2 - 1) * np.sin(7*x[i]) * np.cos(7*x[i])
        
        # Exponentially decaying cross-term coupling with chaotic modulation
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                cross += np.exp(-dist**2) * np.sin(3*(x[i] + x[j])) * np.cos(5*(x[i] - x[j]))
        
        # Boundary-adaptive penalty with hyperbolic scaling
        boundary = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.7:
                boundary += np.log(1 + (np.abs(x[i]) - 4.7)**2) * (np.abs(x[i]) - 4.7)**3
        
        # Additional chaotic coupling terms
        chaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos += np.sin(2 * np.pi * x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Combined fitness function with enhanced dynamic weighting
        return 0.25 * fractal + 0.2 * radial + 0.25 * poly_trig + 0.15 * cross + 0.1 * boundary + 0.05 * chaos
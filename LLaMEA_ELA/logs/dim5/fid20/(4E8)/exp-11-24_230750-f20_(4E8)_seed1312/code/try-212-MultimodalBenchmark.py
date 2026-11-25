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
            # Multiple chaotic scales with varying frequencies (mutated)
            scales = [1.2, 0.6, 0.3, 0.15]
            for scale in scales:
                fractal += np.sin(scale * xi**3) * np.cos(scale * xi**2) * np.exp(-scale * np.abs(xi))
        
        # Dynamic radial symmetry with non-uniform influence (mutated)
        radial = 0.0
        centers = np.linspace(-4.8, 4.8, 9)
        for center in centers:
            dist = np.sum((x - center)**2)
            radial += np.exp(-0.07 * dist) * np.sin(5 * np.pi * dist**0.7) * np.cos(3 * np.pi * dist**0.5)
        
        # Mixed high-order polynomial-trigonometric interactions (mutated)
        poly_trig = 0.0
        for i in range(self.dim):
            poly_trig += (x[i]**7 - 4*x[i]**5 + 6*x[i]**3 - 4*x[i]) * np.sin(8*x[i]) * np.cos(6*x[i])
        
        # Exponentially decaying cross-term coupling with chaotic modulation (mutated)
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                cross += np.exp(-dist**2.5) * np.sin(4*(x[i] + x[j])) * np.cos(6*(x[i] - x[j]))
        
        # Boundary-adaptive penalty with hyperbolic scaling (mutated)
        boundary = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.6:
                boundary += np.log(1 + (np.abs(x[i]) - 4.6)**2) * (np.abs(x[i]) - 4.6)**3
        
        # Additional chaotic coupling terms (mutated)
        chaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos += np.sin(2.5 * np.pi * x[i] * x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2))
        
        # Combined fitness function with enhanced dynamic weighting (mutated)
        return 0.3 * fractal + 0.18 * radial + 0.27 * poly_trig + 0.12 * cross + 0.08 * boundary + 0.05 * chaos
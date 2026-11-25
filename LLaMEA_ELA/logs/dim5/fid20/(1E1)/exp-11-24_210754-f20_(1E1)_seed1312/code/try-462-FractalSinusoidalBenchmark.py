import numpy as np

class FractalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with fractal-like scaling
        r = np.sqrt(np.sum(x**2) / self.dim)
        
        # Multi-scale sinusoidal modulation with decreasing amplitudes
        f1 = 0.3 * np.sum(np.sin(10.0 * x) * np.cos(7.0 * x) * np.exp(-0.1 * r))
        
        # Self-similar fractal structure with recursive scaling
        f2 = 0.25 * np.sum(np.sin(20.0 * np.sin(5.0 * x)) * np.cos(15.0 * np.cos(3.0 * x)))
        
        # Radial symmetry with varying curvature
        f3 = 0.2 * np.sum((r**2.5 + 0.5 * r**1.8 + 0.1 * r**0.9) / self.dim)
        
        # Gradient-guided basin hopping with directional coupling
        f4 = 0.15 * np.sum(np.sin(12.0 * x) * np.cos(9.0 * x) * np.exp(-0.2 * np.abs(x)))
        
        # Multi-modal structure with asymmetric peaks and valleys
        f5 = 0.1 * np.sum((np.sin(8.0 * x)**2 + 0.3 * np.cos(6.0 * x)**2) / self.dim)
        
        # Cross-dimensional coupling with exponential decay
        f6 = 0.12 * np.sum(np.exp(-0.5 * np.abs(x[:-1] - x[1:])) * np.sin(14.0 * (x[:-1] + x[1:])))
        
        # Asymmetric saddle points with chaotic perturbations
        f7 = 0.08 * np.sum(np.sin(25.0 * x) * np.cos(22.0 * x) * np.tan(0.5 * x))
        
        # Final combination with adaptive weighting
        return f1 + f2 + f3 + f4 + f5 + f6 + f7
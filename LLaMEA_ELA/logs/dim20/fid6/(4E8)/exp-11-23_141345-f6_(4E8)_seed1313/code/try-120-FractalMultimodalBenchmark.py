import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal scaling with multiple resolution levels
        fractal_term = np.sum(np.sin(x) * np.cos(2.0 * x) * np.sin(4.0 * x) * (1.0 + 0.2 * np.sin(8.0 * x)))
        
        # Multi-scale radial symmetry with varying frequencies
        radial_term = np.sum((x**2 + 1.0)**(-1.5) * np.cos(3.0 * np.arctan2(x[1:], x[:-1])) * (1.0 + 0.3 * np.sin(5.0 * x)))
        
        # Long-range coupling with power-law decay
        long_range = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                long_range += (1.0 / (1.0 + distance**2)) * np.sin(2.0 * (x[i] + x[j]))
        
        # Self-similar structure with recursive scaling
        self_similar = np.sum(np.sin(3.0 * x) * np.cos(6.0 * x) * np.sin(12.0 * x) * (1.0 + 0.15 * np.cos(24.0 * x)))
        
        # Scale-invariant curvature with variable smoothness
        curvature = np.sum(np.abs(x)**(1.7 + 0.3 * np.sin(7.0 * x)) * np.exp(-0.1 * x**2))
        
        # Asymmetric multimodal components with chaotic modulation
        asym_term = np.sum(np.sin(x) * np.cos(1.5 * x) * (1.0 + 0.25 * np.sin(3.0 * x)) * np.exp(-0.05 * x**2))
        
        # Combined function with varying weights based on dimensionality
        weight_fractal = 0.25
        weight_radial = 0.20
        weight_long = 0.15
        weight_self = 0.20
        weight_curvature = 0.10
        weight_asym = 0.10
        
        return (weight_fractal * fractal_term + 
                weight_radial * radial_term + 
                weight_long * long_range + 
                weight_self * self_similar + 
                weight_curvature * curvature + 
                weight_asym * asym_term)
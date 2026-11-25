import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with varying degrees
        f1 = np.sum(x_norm**4)
        
        # Multiple sine waves with different frequencies and amplitudes
        f2 = np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm) + np.sin(5 * x_norm**2) * np.cos(3 * x_norm**3))
        
        # Exponential decay modulated by trigonometric functions
        f3 = np.sum(np.exp(-np.abs(x_norm)) * np.sin(np.pi * x_norm * np.cos(2 * x_norm)))
        
        # Dynamic phase shift based on dimensionality
        phase_shift = np.sum(np.sin(self.dim * x_norm) * np.cos(self.dim * x_norm**2))
        
        # Logarithmic scaling with trigonometric modulation
        f4 = np.sum(np.log(np.abs(x_norm) + 1.1) * np.sin(3 * np.pi * x_norm))
        
        # Adaptive interaction term with exponential weighting
        f5 = np.sum(np.exp(-0.5 * x_norm**2) * np.cos(4 * np.pi * x_norm) * np.sin(2 * np.pi * x_norm))
        
        # Fractal-like recursive structure using sine and cosine compositions
        fractal = np.sum(np.sin(np.pi * x_norm * np.sin(3 * np.pi * x_norm)) * np.cos(np.pi * x_norm * np.cos(5 * np.pi * x_norm)))
        
        # Multi-scale periodic components with varying periods
        f6 = np.sum(np.sin(15 * x_norm) + np.cos(12 * x_norm) + np.sin(8 * x_norm**2))
        
        # Combined weighted sum with dynamic scaling factor
        scale_factor = 1.0 + 0.3 * np.std(x_norm) + 0.2 * np.mean(np.abs(x_norm))
        
        return scale_factor * (0.6 * f1 + 0.4 * f2 - 0.3 * f3 + 0.2 * phase_shift + 0.15 * f4 + 0.1 * f5 + 0.08 * fractal + 0.05 * f6) + 0.03 * np.sum(x_norm**6)
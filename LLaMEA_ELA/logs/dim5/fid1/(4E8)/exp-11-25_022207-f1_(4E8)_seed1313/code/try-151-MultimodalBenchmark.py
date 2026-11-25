import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map modulation for non-linearity
        chaos_mod = np.sum(4 * x_norm * (1 - x_norm))
        
        # Multi-scale Gaussian peaks with varying heights and widths
        peaks = 0
        scales = [0.5, 1.0, 2.0]
        heights = [1.0, 0.5, 0.3]
        for i, (scale, height) in enumerate(zip(scales, heights)):
            peaks += height * np.exp(-0.5 * np.sum(((x_norm - np.sin(i)) / scale)**2))
        
        # Gradient-asymmetric corridor structure
        asym_corridor = np.sum(np.abs(x_norm) * np.exp(-0.1 * x_norm**2) * 
                              np.sin(3 * np.pi * x_norm) * 
                              np.cos(2 * np.pi * x_norm))
        
        # Polynomial coupling with trigonometric modulation
        poly_coupling = np.sum((x_norm[:-1]**2 + x_norm[1:]**2)**3 * 
                              np.cos(4 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                              np.exp(-0.3 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Saddle-point repulsion with exponential decay
        saddle_repulse = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**2 * 
                               np.exp(-0.5 * (x_norm[:-1] + x_norm[1:])**2) * 
                               np.sin(5 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Fractal-like chaotic component
        fractal = np.sum(np.sin(10 * np.pi * x_norm) * 
                        np.cos(7 * np.pi * x_norm) * 
                        np.exp(-0.2 * np.abs(x_norm)) * 
                        np.tan(0.3 * x_norm))
        
        # Combined function with chaotic noise
        result = chaos_mod + peaks + asym_corridor + poly_coupling + saddle_repulse + fractal
        
        # Add small random perturbation for robustness
        noise = 0.05 * np.random.rand()
        
        return result + noise
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map modulation for non-linearity with altered coefficient
        chaos_mod = np.sum(3.5 * x_norm * (1 - x_norm))
        
        # Multi-scale Gaussian peaks with varying heights and widths
        peaks = 0
        scales = [0.4, 1.2, 1.8]
        heights = [1.2, 0.6, 0.25]
        for i, (scale, height) in enumerate(zip(scales, heights)):
            peaks += height * np.exp(-0.5 * np.sum(((x_norm - np.sin(i * 0.5)) / scale)**2))
        
        # Gradient-asymmetric corridor structure with modified frequency
        asym_corridor = np.sum(np.abs(x_norm) * np.exp(-0.15 * x_norm**2) * 
                              np.sin(4 * np.pi * x_norm) * 
                              np.cos(1.5 * np.pi * x_norm))
        
        # Polynomial coupling with trigonometric modulation and altered exponent
        poly_coupling = np.sum((x_norm[:-1]**3 + x_norm[1:]**3)**2 * 
                              np.cos(3 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                              np.exp(-0.25 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Saddle-point repulsion with exponential decay and modified frequency
        saddle_repulse = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**3 * 
                               np.exp(-0.4 * (x_norm[:-1] + x_norm[1:])**2) * 
                               np.sin(4 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Fractal-like chaotic component with altered frequencies
        fractal = np.sum(np.sin(9 * np.pi * x_norm) * 
                        np.cos(6 * np.pi * x_norm) * 
                        np.exp(-0.25 * np.abs(x_norm)) * 
                        np.tan(0.25 * x_norm))
        
        # Combined function with chaotic noise
        result = chaos_mod + peaks + asym_corridor + poly_coupling + saddle_repulse + fractal
        
        # Add small random perturbation for robustness
        noise = 0.03 * np.random.rand()
        
        return result + noise
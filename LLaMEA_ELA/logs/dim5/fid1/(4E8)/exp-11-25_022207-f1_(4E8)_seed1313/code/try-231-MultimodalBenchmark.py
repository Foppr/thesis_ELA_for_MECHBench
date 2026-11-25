import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic modulation with sine-cosine coupling and dynamic scaling
        chaos_mod = np.sum(np.sin(4.1 * np.pi * x_norm) * np.cos(2.9 * np.pi * x_norm) * 
                          np.exp(-0.31 * x_norm**2) * np.tan(0.71 * x_norm))
        
        # Multi-scale Gaussian peaks with varying heights, widths, and phase shifts
        peaks = 0
        scales = [0.42, 1.15, 1.95]
        heights = [2.3, 1.1, 0.37]
        phases = [0.31, 0.71, 1.11]
        for i, (scale, height, phase) in enumerate(zip(scales, heights, phases)):
            peaks += height * np.exp(-0.5 * np.sum(((x_norm - np.sin(i * phase)) / scale)**2))
        
        # Gradient-asymmetric corridor structure with dynamic frequency and amplitude
        asym_corridor = np.sum(np.abs(x_norm) * np.exp(-0.17 * x_norm**2) * 
                              np.sin(5.1 * np.pi * x_norm) * 
                              np.cos(2.7 * np.pi * x_norm) * 
                              np.tan(0.51 * x_norm))
        
        # Increased polynomial coupling with enhanced trigonometric modulation and altered exponent
        poly_coupling = np.sum((x_norm[:-1]**4.1 + x_norm[1:]**4.1)**2 * 
                              np.cos(4.1 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                              np.exp(-0.51 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Perturbed saddle-point repulsion with exponential decay and enhanced frequency
        saddle_repulse = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**4.1 * 
                               np.exp(-0.51 * (x_norm[:-1] + x_norm[1:])**2) * 
                               np.sin(5.1 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Fractal-like chaotic component with enhanced complexity and dynamic scaling
        fractal = np.sum(np.sin(9.1 * np.pi * x_norm) * 
                        np.cos(5.7 * np.pi * x_norm) * 
                        np.exp(-0.31 * np.abs(x_norm)) * 
                        np.tan(0.51 * x_norm) * 
                        np.cos(1.9 * np.pi * x_norm))
        
        # Dynamic scaling component with adaptive noise
        dynamic_scale = np.sum(np.sin(3.1 * x_norm) * np.cos(1.7 * x_norm) * 
                              (1.0 + 0.25 * np.random.rand()))
        
        # Combined function with enhanced chaotic noise and modular structure
        result = chaos_mod + peaks + asym_corridor + poly_coupling + saddle_repulse + fractal + dynamic_scale
        
        # Add adaptive random perturbation for robustness
        noise = 0.05 * np.random.rand() * (1.0 + 0.25 * np.abs(np.mean(x_norm)))
        
        return result + noise
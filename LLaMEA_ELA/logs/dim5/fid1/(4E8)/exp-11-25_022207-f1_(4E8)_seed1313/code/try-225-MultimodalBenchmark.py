import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic modulation with improved frequency control and dynamic scaling
        chaos_mod = np.sum(np.sin(4.1 * np.pi * x_norm) * np.cos(2.9 * np.pi * x_norm) * 
                          np.exp(-0.31 * x_norm**2) * np.tan(0.58 * x_norm))
        
        # Multi-scale Gaussian peaks with optimized heights, widths, and phase shifts
        peaks = 0
        scales = [0.42, 1.15, 1.95]
        heights = [2.3, 1.1, 0.35]
        phases = [0.31, 0.71, 1.11]
        for i, (scale, height, phase) in enumerate(zip(scales, heights, phases)):
            peaks += height * np.exp(-0.5 * np.sum(((x_norm - np.sin(i * phase)) / scale)**2))
        
        # Gradient-asymmetric corridor structure with improved frequency and amplitude
        asym_corridor = np.sum(np.abs(x_norm) * np.exp(-0.17 * x_norm**2) * 
                              np.sin(5.1 * np.pi * x_norm) * 
                              np.cos(2.7 * np.pi * x_norm) * 
                              np.tan(0.51 * x_norm))
        
        # Enhanced polynomial coupling with modified exponent and trigonometric modulation
        poly_coupling = np.sum((x_norm[:-1]**4.1 + x_norm[1:]**4.1)**2 * 
                              np.cos(4.1 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                              np.exp(-0.51 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Refined saddle-point repulsion with improved exponential decay and frequency
        saddle_repulse = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**4.1 * 
                               np.exp(-0.51 * (x_norm[:-1] + x_norm[1:])**2) * 
                               np.sin(5.1 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Enhanced fractal-like chaotic component with better complexity control
        fractal = np.sum(np.sin(9.1 * np.pi * x_norm) * 
                        np.cos(5.7 * np.pi * x_norm) * 
                        np.exp(-0.31 * np.abs(x_norm)) * 
                        np.tan(0.51 * x_norm) * 
                        np.cos(1.9 * np.pi * x_norm))
        
        # Improved dynamic scaling component with reduced noise impact
        dynamic_scale = np.sum(np.sin(3.1 * x_norm) * np.cos(1.7 * x_norm) * 
                              (1.0 + 0.15 * np.random.rand()))
        
        # Combined function with refined chaotic noise and modular structure
        result = chaos_mod + peaks + asym_corridor + poly_coupling + saddle_repulse + fractal + dynamic_scale
        
        # Reduced adaptive random perturbation for better consistency
        noise = 0.03 * np.random.rand() * (1.0 + 0.15 * np.abs(np.mean(x_norm)))
        
        return result + noise
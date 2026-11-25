import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic modulation with dynamic frequency and amplitude scaling
        chaos_mod = np.sum(np.sin(3.7 * np.pi * x_norm) * np.cos(2.3 * np.pi * x_norm) * 
                          np.exp(-0.41 * x_norm**2) * np.tan(0.68 * x_norm))
        
        # Multi-scale Gaussian peaks with varying heights, widths, and phase shifts
        peaks = 0
        scales = [0.38, 1.12, 1.95]
        heights = [2.1, 1.25, 0.42]
        phases = [0.29, 0.75, 1.15]
        for i, (scale, height, phase) in enumerate(zip(scales, heights, phases)):
            peaks += height * np.exp(-0.5 * np.sum(((x_norm - np.sin(i * phase)) / scale)**2))
        
        # Gradient-asymmetric corridor structure with modified frequency and amplitude
        asym_corridor = np.sum(np.abs(x_norm) * np.exp(-0.21 * x_norm**2) * 
                              np.sin(4.8 * np.pi * x_norm) * 
                              np.cos(3.1 * np.pi * x_norm) * 
                              np.tan(0.49 * x_norm))
        
        # Enhanced polynomial coupling with trigonometric modulation and altered exponents
        poly_coupling = np.sum((x_norm[:-1]**3.8 + x_norm[1:]**3.8)**2.3 * 
                              np.cos(3.8 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                              np.exp(-0.48 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Perturbed saddle-point repulsion with exponential decay and enhanced frequency
        saddle_repulse = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**3.8 * 
                               np.exp(-0.48 * (x_norm[:-1] + x_norm[1:])**2) * 
                               np.sin(4.8 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Fractal-like chaotic component with enhanced complexity and dynamic scaling
        fractal = np.sum(np.sin(8.7 * np.pi * x_norm) * 
                        np.cos(6.1 * np.pi * x_norm) * 
                        np.exp(-0.35 * np.abs(x_norm)) * 
                        np.tan(0.48 * x_norm) * 
                        np.cos(2.1 * np.pi * x_norm))
        
        # Dynamic scaling component with adaptive noise
        dynamic_scale = np.sum(np.sin(3.3 * x_norm) * np.cos(1.9 * x_norm) * 
                              (1.0 + 0.3 * np.random.rand()))
        
        # Combined function with enhanced chaotic noise and modular structure
        result = chaos_mod + peaks + asym_corridor + poly_coupling + saddle_repulse + fractal + dynamic_scale
        
        # Add adaptive random perturbation for robustness
        noise = 0.04 * np.random.rand() * (1.0 + 0.3 * np.abs(np.mean(x_norm)))
        
        return result + noise
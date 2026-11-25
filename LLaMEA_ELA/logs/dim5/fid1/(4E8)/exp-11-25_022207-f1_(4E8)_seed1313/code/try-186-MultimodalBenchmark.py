import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic modulation with logistic map and sine coupling
        chaos_mod = np.sum(3.9 * x_norm * (1 - x_norm) * np.sin(2.7 * x_norm))
        
        # Multi-scale Gaussian peaks with varying heights, widths, and phase shifts
        peaks = 0
        scales = [0.4, 1.2, 1.8]
        heights = [1.4, 0.6, 0.25]
        phases = [0.3, 0.7, 1.1]
        for i, (scale, height, phase) in enumerate(zip(scales, heights, phases)):
            peaks += height * np.exp(-0.5 * np.sum(((x_norm - np.sin(i * phase)) / scale)**2))
        
        # Gradient-asymmetric corridor structure with modified frequency and amplitude
        asym_corridor = np.sum(np.abs(x_norm) * np.exp(-0.2 * x_norm**2) * 
                              np.sin(5.0 * np.pi * x_norm) * 
                              np.cos(1.5 * np.pi * x_norm))
        
        # Enhanced polynomial coupling with trigonometric modulation and altered exponent
        poly_coupling = np.sum((x_norm[:-1]**4 + x_norm[1:]**4)**2 * 
                              np.cos(3.5 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                              np.exp(-0.3 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Perturbed saddle-point repulsion with exponential decay and modified frequency
        saddle_repulse = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**4 * 
                               np.exp(-0.5 * (x_norm[:-1] + x_norm[1:])**2) * 
                               np.sin(4.5 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Fractal-like chaotic component with altered frequencies and amplitude scaling
        fractal = np.sum(np.sin(10.0 * np.pi * x_norm) * 
                        np.cos(6.5 * np.pi * x_norm) * 
                        np.exp(-0.3 * np.abs(x_norm)) * 
                        np.tan(0.3 * x_norm))
        
        # Additional chaotic modulation with wavelet-like structure
        wavelet_mod = np.sum(np.sin(7.0 * x_norm) * np.cos(4.0 * x_norm) * 
                            np.exp(-0.15 * x_norm**2))
        
        # Combined function with adaptive noise and scaling factor
        result = 0.8 * chaos_mod + 1.2 * peaks + 0.6 * asym_corridor + 1.0 * poly_coupling + 0.9 * saddle_repulse + 0.7 * fractal + 0.5 * wavelet_mod
        
        # Add adaptive random perturbation for robustness
        noise = 0.02 * np.random.rand() * (1.0 + 0.3 * np.abs(np.mean(x_norm)))
        
        return result + noise
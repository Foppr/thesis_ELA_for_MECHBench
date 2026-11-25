import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Nested chaotic modulation with multi-frequency coupling and adaptive scaling
        chaos_mod = np.sum(np.sin(7.3 * np.pi * x_norm) * np.cos(3.9 * np.pi * x_norm) * 
                          np.exp(-0.45 * x_norm**2) * np.tan(1.2 * x_norm) * 
                          np.sin(2.1 * np.pi * np.sum(x_norm**2)))
        
        # Multi-scale Gaussian peaks with dynamic heights, widths, and phase shifts
        peaks = 0
        scales = [0.35, 0.92, 1.68, 2.15]
        heights = [3.1, 1.7, 0.85, 0.22]
        phases = [0.27, 0.68, 1.05, 1.42]
        for i, (scale, height, phase) in enumerate(zip(scales, heights, phases)):
            peaks += height * np.exp(-0.5 * np.sum(((x_norm - np.sin(i * phase)) / scale)**2))
        
        # Gradient-asymmetric corridor structure with modified frequency and amplitude
        asym_corridor = np.sum(np.abs(x_norm) * np.exp(-0.25 * x_norm**2) * 
                              np.sin(6.8 * np.pi * x_norm) * 
                              np.cos(3.4 * np.pi * x_norm) * 
                              np.tan(0.65 * x_norm) * 
                              np.cos(1.3 * np.pi * x_norm))
        
        # Increased polynomial coupling with enhanced trigonometric modulation and altered exponent
        poly_coupling = np.sum((x_norm[:-1]**5.3 + x_norm[1:]**5.3)**2.7 * 
                              np.cos(5.3 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                              np.exp(-0.62 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Perturbed saddle-point repulsion with exponential decay and enhanced frequency
        saddle_repulse = np.sum((x_norm[:-1]**3 - x_norm[1:]**3)**3.8 * 
                               np.exp(-0.65 * (x_norm[:-1] + x_norm[1:])**2) * 
                               np.sin(6.1 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Fractal-like chaotic component with enhanced complexity and dynamic scaling
        fractal = np.sum(np.sin(11.2 * np.pi * x_norm) * 
                        np.cos(7.8 * np.pi * x_norm) * 
                        np.exp(-0.42 * np.abs(x_norm)) * 
                        np.tan(0.68 * x_norm) * 
                        np.cos(2.3 * np.pi * x_norm) * 
                        np.sin(1.7 * np.pi * np.mean(x_norm)))
        
        # Dynamic scaling component with adaptive noise and phase coupling
        dynamic_scale = np.sum(np.sin(4.3 * x_norm) * np.cos(2.1 * x_norm) * 
                              (1.0 + 0.35 * np.random.rand()) * 
                              np.cos(1.5 * np.pi * np.mean(x_norm)))
        
        # Phase-coupled oscillator structure with adaptive frequencies
        phase_coupling = np.sum(np.sin(2.7 * np.pi * x_norm) * 
                               np.cos(1.9 * np.pi * x_norm) * 
                               np.exp(-0.38 * (x_norm - np.mean(x_norm))**2) * 
                               np.tan(0.45 * x_norm))
        
        # Combined function with enhanced chaotic noise and modular structure
        result = chaos_mod + peaks + asym_corridor + poly_coupling + saddle_repulse + fractal + dynamic_scale + phase_coupling
        
        # Add adaptive random perturbation for robustness
        noise = 0.08 * np.random.rand() * (1.0 + 0.35 * np.abs(np.mean(x_norm)))
        
        return result + noise
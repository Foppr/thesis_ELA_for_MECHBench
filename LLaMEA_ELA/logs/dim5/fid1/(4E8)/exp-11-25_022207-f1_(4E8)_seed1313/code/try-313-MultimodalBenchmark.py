import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal harmonic coupling with dynamic frequency modulation and phase locking
        fractal_harmonic = np.sum(np.sin(7.8 * np.pi * x_norm) * 
                                 np.cos(6.2 * np.pi * x_norm) * 
                                 np.exp(-0.4 * np.abs(x_norm)) * 
                                 np.tan(1.1 * x_norm) * 
                                 np.cos(3.9 * np.pi * x_norm) * 
                                 np.sin(2.8 * np.pi * x_norm))
        
        # Multi-scale asymmetric Gaussian peaks with dynamic amplitude and frequency
        peaks = 0
        scales = [0.6, 1.7, 2.9]
        heights = [3.2, 2.5, 1.2]
        phases = [0.7, 1.3, 2.1]
        for i, (scale, height, phase) in enumerate(zip(scales, heights, phases)):
            peaks += height * np.exp(-0.5 * np.sum(((x_norm - np.sin(i * phase + 1.5)) / scale)**2))
        
        # Asymmetric gradient corridor with multi-frequency harmonic modulation
        asym_corridor = np.sum(np.abs(x_norm)**1.6 * np.exp(-0.35 * x_norm**2) * 
                              np.sin(6.8 * np.pi * x_norm) * 
                              np.cos(4.3 * np.pi * x_norm) * 
                              np.tan(0.8 * x_norm) * 
                              np.sin(2.3 * np.pi * x_norm))
        
        # Enhanced polynomial coupling with dynamic exponent and phase-shifted trigonometric terms
        poly_coupling = np.sum((x_norm[:-1]**5.2 + x_norm[1:]**5.2)**3.2 * 
                              np.cos(5.2 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                              np.exp(-0.65 * (x_norm[:-1] - x_norm[1:])**2) * 
                              np.sin(3.5 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Saddle-point repulsion with multi-scale fractal coupling and dynamic exponential decay
        saddle_repulse = np.sum((x_norm[:-1]**3.2 - x_norm[1:]**3.2)**3.8 * 
                               np.exp(-0.68 * (x_norm[:-1] + x_norm[1:])**2) * 
                               np.sin(6.5 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               np.cos(2.3 * np.pi * (x_norm[:-1] + x_norm[1:])))
        
        # Dynamic chaotic modulation with multi-scale frequency coupling and adaptive scaling
        chaos_mod = np.sum(np.sin(5.9 * np.pi * x_norm) * 
                          np.cos(4.8 * np.pi * x_norm) * 
                          np.exp(-0.28 * x_norm**2) * 
                          np.tan(0.6 * x_norm) * 
                          np.sin(1.9 * np.pi * x_norm) * 
                          np.cos(3.3 * np.pi * x_norm))
        
        # Enhanced fractal-like gradient structure with asymmetric coupling and dynamic phase modulation
        fractal_gradient = np.sum(np.sin(8.5 * np.pi * x_norm) * 
                                 np.cos(5.2 * np.pi * x_norm) * 
                                 np.exp(-0.38 * np.abs(x_norm)) * 
                                 np.tan(0.4 * x_norm) * 
                                 np.sin(2.7 * np.pi * x_norm) * 
                                 np.cos(4.2 * np.pi * x_norm))
        
        # Combined function with enhanced chaotic noise and modular structure
        result = fractal_harmonic + peaks + asym_corridor + poly_coupling + saddle_repulse + chaos_mod + fractal_gradient
        
        # Add adaptive random perturbation for robustness
        noise = 0.065 * np.random.rand() * (1.0 + 0.35 * np.abs(np.mean(x_norm)))
        
        return result + noise
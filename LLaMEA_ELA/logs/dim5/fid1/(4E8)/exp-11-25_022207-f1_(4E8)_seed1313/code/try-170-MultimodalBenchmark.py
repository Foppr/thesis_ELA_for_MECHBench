import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like periodic component with varying frequency scales
        fractal_periodic = np.sum(np.sin(2 ** (np.arange(self.dim) + 1) * np.pi * x_norm) * 
                                 np.cos(3 ** (np.arange(self.dim) + 1) * np.pi * x_norm) * 
                                 (1 + 0.3 * np.sin(5 * np.pi * x_norm)))
        
        # Asymmetric saddle-point structure with harmonic coupling
        asym_saddle = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**3 * 
                            np.exp(-0.5 * (x_norm[:-1] + x_norm[1:])**2) * 
                            np.sin(4 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                            (1 + 0.2 * np.cos(7 * np.pi * x_norm[:-1])))
        
        # Multi-scale harmonic coupling with dynamic amplitude modulation
        harmonic_coupling = np.sum(np.sin(8 * np.pi * x_norm) * 
                                  np.cos(6 * np.pi * x_norm) * 
                                  np.exp(-0.3 * np.abs(x_norm)) * 
                                  (1 + 0.4 * np.sin(12 * np.pi * x_norm)) * 
                                  (1 + 0.3 * np.cos(9 * np.pi * x_norm)))
        
        # Chaotic gradient modulation using tent map-like behavior
        chaotic_gradient = np.sum(np.tan(2 * np.pi * x_norm) * 
                                 np.exp(-0.4 * (x_norm**2).sum()) * 
                                 (1 + 0.5 * np.sin(13 * np.pi * x_norm)) * 
                                 np.cos(3 * np.pi * x_norm.sum()))
        
        # Multi-scale polynomial interactions with fractal-like scaling
        poly_fractal = np.sum((x_norm[:-1]**3 + x_norm[1:]**3)**2 * 
                             np.exp(-0.6 * (x_norm[:-1] - x_norm[1:])**2) * 
                             (1 + 0.3 * np.cos(11 * np.pi * x_norm[:-1])) * 
                             (1 + 0.2 * np.sin(15 * np.pi * x_norm[1:])))
        
        # Asymmetric repulsive force field with harmonic perturbations
        repulsion_field = np.sum(np.exp(-2 * (x_norm**2).sum()) * 
                                np.sin(5 * np.pi * x_norm) * 
                                np.cos(2 * np.pi * x_norm.sum()) * 
                                (1 + 0.3 * np.sin(14 * np.pi * x_norm)) * 
                                (1 + 0.2 * np.cos(8 * np.pi * x_norm)))
        
        # Adaptive noise component with chaotic modulation
        adaptive_noise = 0.15 * np.random.normal(0, 1) * (1 + 0.4 * np.sin(19 * np.pi * x_norm[0] if len(x_norm) > 0 else 0))
        
        # High-frequency chaotic oscillation with exponential decay
        high_freq_osc = np.sum(np.sin(30 * np.pi * x_norm) * 
                              np.cos(25 * np.pi * x_norm) * 
                              np.exp(-0.2 * (x_norm**2).sum()) * 
                              (1 + 0.6 * np.sin(35 * np.pi * x_norm)) * 
                              np.tan(0.8 * x_norm))
        
        # Fractional polynomial coupling with multi-dimensional interaction
        fractional_coupling = np.sum((np.abs(x_norm[:-1])**1.5 + np.abs(x_norm[1:])**1.5)**2 * 
                                    np.exp(-0.4 * (x_norm[:-1] - x_norm[1:])**2) * 
                                    (1 + 0.3 * np.cos(10 * np.pi * x_norm[:-1])) * 
                                    (1 + 0.2 * np.sin(16 * np.pi * x_norm[1:])))
        
        # Combined chaotic modulation with fractal-like structure
        final_modulation = np.sum(np.sin(20 * np.pi * x_norm) * 
                                 np.cos(17 * np.pi * x_norm) * 
                                 np.tan(1.5 * x_norm) * 
                                 (1 + 0.5 * np.sin(28 * np.pi * x_norm)) * 
                                 np.exp(-0.3 * (x_norm**2).sum()) * 
                                 np.cos(11 * np.pi * x_norm.sum()))
        
        return fractal_periodic + asym_saddle + harmonic_coupling + chaotic_gradient + poly_fractal + repulsion_field + adaptive_noise + high_freq_osc + fractional_coupling + final_modulation
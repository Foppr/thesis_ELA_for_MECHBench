import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Gaussian radial basis components with varying widths and centers
        gauss_radial = np.sum(np.exp(-0.5 * np.sum((x_norm[:, None] - np.linspace(-0.8, 0.8, self.dim))**2, axis=0)) * 
                             np.cos(3 * np.pi * x_norm) * 
                             np.sin(2 * np.pi * x_norm))
        
        # Sinusoidal modulation with adaptive frequency and amplitude
        sin_mod = np.sum(np.sin(4 * np.pi * x_norm) * 
                        np.cos(5 * np.pi * x_norm) * 
                        (1 + 0.3 * np.sin(7 * np.pi * x_norm)) * 
                        np.exp(-0.2 * np.abs(x_norm)))
        
        # Adaptive polynomial coupling with dynamic scaling
        poly_coupling = np.sum((x_norm[:-1]**2 + x_norm[1:]**2)**3 * 
                              np.exp(-0.4 * (x_norm[:-1] - x_norm[1:])**2) * 
                              (1 + 0.2 * np.cos(9 * np.pi * x_norm[:-1])) * 
                              (1 + 0.1 * np.sin(11 * np.pi * x_norm[1:])))
        
        # Chaotic perturbation with logistic map dynamics
        chaotic_perturb = np.sum(np.sin(6 * np.pi * x_norm) * 
                                np.cos(8 * np.pi * x_norm) * 
                                (1 + 0.4 * np.sin(13 * np.pi * x_norm)) * 
                                np.exp(-0.3 * (x_norm**2).sum()))
        
        # Adaptive noise component with dynamic variance
        adaptive_noise = 0.1 * np.random.normal(0, 1) * (1 + 0.2 * np.sin(17 * np.pi * x_norm[0] if len(x_norm) > 0 else 0))
        
        # Saddle-point structure with enhanced gradient variations
        saddle_structure = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**2 * 
                                 np.cos(0.5 * (x_norm[:-1] + x_norm[1:])) * 
                                 np.exp(-0.5 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                                 (1 + 0.3 * np.sin(10 * np.pi * x_norm[:-1])))
        
        # Fractional polynomial interactions with dynamic scaling
        frac_poly = np.sum((x_norm[:-1]**1.5 + x_norm[1:]**1.5)**4 * 
                          np.exp(-0.6 * (x_norm[:-1] - x_norm[1:])**2) * 
                          (1 + 0.25 * np.cos(12 * np.pi * x_norm[:-1])) * 
                          (1 + 0.2 * np.sin(14 * np.pi * x_norm[1:])))
        
        # Multi-scale sinusoidal modulation with varying frequencies
        multi_scale = np.sum(np.sin(3 * np.pi * x_norm) * 
                            np.cos(4 * np.pi * x_norm) * 
                            np.sin(5 * np.pi * x_norm) * 
                            (1 + 0.2 * np.cos(6 * np.pi * x_norm)) * 
                            np.exp(-0.1 * (x_norm**2).sum()))
        
        # Enhanced gradient structure with multiple interacting components
        enhanced_grad = np.sum(np.sin(7 * np.pi * x_norm) * 
                              np.cos(9 * np.pi * x_norm) * 
                              (1 + 0.3 * np.sin(11 * np.pi * x_norm)) * 
                              np.exp(-0.25 * np.abs(x_norm)) * 
                              (1 + 0.15 * np.cos(13 * np.pi * x_norm.sum())))
        
        # Combined objective function
        return gauss_radial + sin_mod + poly_coupling + chaotic_perturb + adaptive_noise + saddle_structure + frac_poly + multi_scale + enhanced_grad
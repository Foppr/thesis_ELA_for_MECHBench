import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with multiple peaks and valleys
        radial = np.sum(np.exp(-5 * (x_norm**2).sum()) * np.cos(3 * np.pi * x_norm.sum()))
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_mod = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) * 
                        (1 + 0.3 * np.sin(6 * np.pi * x_norm)))
        
        # Asymmetric cubic interactions with cross-dimensional coupling
        asym_cubic = np.sum(x_norm**3 * (1 + 0.2 * np.sin(5 * x_norm)) * 
                           np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Saddle point structure with perturbed harmonic potential
        saddle = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**2 * 
                       np.cos(0.5 * (x_norm[:-1] + x_norm[1:])) * 
                       np.exp(-0.3 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Cross-dimensional polynomial coupling with exponential scaling
        poly_coupling = np.sum((x_norm[:-1]**2 + x_norm[1:]**2)**3 * 
                              np.exp(-0.4 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Additional noise for robustness testing
        noise = 0.1 * np.random.normal(0, 1)
        
        return radial + sin_mod + asym_cubic + saddle + poly_coupling + noise
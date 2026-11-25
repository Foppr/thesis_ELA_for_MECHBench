import numpy as np

class ChaoticAsymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic oscillation component with non-linear coupling
        chaotic_osc = np.sum(np.sin(13 * x_norm) * np.cos(7 * x_norm) * 
                            (1 + 0.3 * np.sin(5 * x_norm)) * 
                            (1 + 0.2 * np.cos(3 * x_norm)))
        
        # Asymmetric Gaussian valleys with position-dependent variance
        asym_gauss = np.sum(np.exp(-0.5 * ((x_norm - 0.3)**2) / (0.3 + 0.2 * np.sin(4 * x_norm))) + 
                           np.exp(-0.5 * ((x_norm + 0.3)**2) / (0.4 + 0.1 * np.cos(6 * x_norm))))
        
        # Saddle point structure with cross-dimensional interaction
        saddle_points = np.sum((x_norm[:-1]**2 - x_norm[1:]**2) * 
                              (1 + 0.2 * np.sin(3 * x_norm[:-1])) * 
                              (1 + 0.1 * np.cos(2 * x_norm[1:])))
        
        # Dynamic conditioning with time-like parameter
        dynamic_cond = np.sum((1 + 0.5 * np.sin(8 * x_norm)) * 
                             np.exp(-0.4 * np.abs(x_norm)**1.7) * 
                             (1 + 0.3 * np.cos(5 * x_norm)))
        
        # Discontinuous regions with step-like transitions
        discontinuous = np.sum(np.floor(2 * np.sin(9 * x_norm)) * 
                              np.exp(-0.3 * x_norm**2) * 
                              (1 + 0.25 * np.sin(7 * x_norm)))
        
        # Multi-scale fractal-like correlation with varying roughness
        fractal_corr = np.sum(np.abs(x_norm[:-1] - x_norm[1:])**(0.7 + 0.3 * np.sin(4 * x_norm[:-1])) * 
                              (1 + 0.2 * np.cos(5 * x_norm[1:])))
        
        # Combined landscape with mixed smooth and discontinuous regions
        return 2.0 * (chaotic_osc + asym_gauss + saddle_points + 
                     dynamic_cond + discontinuous + fractal_corr)
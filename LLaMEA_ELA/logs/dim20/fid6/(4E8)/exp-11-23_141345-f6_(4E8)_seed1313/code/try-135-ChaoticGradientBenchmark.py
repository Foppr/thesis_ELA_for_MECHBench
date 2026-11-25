import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient oscillations with logistic map modulation
        chaotic_term = np.sum(np.sin(2.0 * np.pi * x) * np.cos(1.5 * np.pi * x) * 
                             (1.0 + 0.3 * np.sin(3.0 * x)) * np.exp(-0.1 * np.abs(x)))
        
        # Radial asymmetry with modified Euclidean distances
        radial_asymmetry = np.sum(np.exp(-0.5 * (x**2 + 0.2 * x**4)) * 
                                 np.sin(2.0 * x) * np.cos(1.2 * x) * 
                                 (1.0 + 0.1 * np.sin(4.0 * x)))
        
        # Adaptive cross-dimensional interference with dynamic scaling
        cross_interference = np.sum(np.exp(-0.3 * np.abs(x[:-1] - x[1:])) * 
                                   (x[:-1]**3 + x[1:]**3) * 
                                   np.sin(2.5 * x[:-1]) * np.cos(1.8 * x[1:]) * 
                                   (1.0 + 0.2 * np.cos(3.0 * (x[:-1] + x[1:]))))
        
        # Multi-scale chaotic modulation with varying frequencies
        multi_scale = np.sum(np.sin(5.0 * x) * np.cos(4.0 * x) * 
                            np.exp(-0.2 * np.abs(x)) * 
                            (1.0 + 0.15 * np.sin(6.0 * x)))
        
        # Fractal-like gradient variation with hyperbolic tangent
        fractal_gradient = np.sum(np.tanh(2.0 * x) * np.exp(-0.3 * x**2) * 
                                 np.sin(3.0 * x) * np.cos(2.0 * x) * 
                                 (1.0 + 0.25 * np.sin(5.0 * x)))
        
        # Asymmetric coupling with exponential decay and sinusoidal modulation
        asymmetric_coupling = np.sum(np.exp(-0.4 * np.abs(x)) * 
                                    np.sin(3.5 * x) * np.cos(2.5 * x) * 
                                    (1.0 + 0.3 * np.sin(4.0 * x)) * 
                                    np.log(1.0 + np.abs(x)))
        
        # Combined function with optimized weights
        return 0.30 * chaotic_term + 0.25 * radial_asymmetry + 0.20 * cross_interference + \
               0.12 * multi_scale + 0.10 * fractal_gradient + 0.03 * asymmetric_coupling
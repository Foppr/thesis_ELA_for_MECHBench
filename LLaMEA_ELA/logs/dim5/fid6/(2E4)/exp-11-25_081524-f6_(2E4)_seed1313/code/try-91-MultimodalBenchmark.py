import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial landscape with adaptive curvature
        base = np.sum(0.1 * x**6 + 0.3 * x**4 + 0.5 * x**2)
        
        # Sinusoidal modulation with dynamic frequency and amplitude
        sin_mod = np.sum(np.sin(10.0 * x) * np.cos(7.0 * x) * 
                        (1.0 + 0.3 * np.sin(3.0 * x)) * np.exp(-0.1 * x**2))
        
        # Polynomial chaos expansion with mixed monomial terms
        chaos = np.sum(0.2 * x**3.5 + 0.15 * x**5.3 - 0.25 * x**2.7 + 
                      0.1 * x**4.1 + 0.05 * x**6.8)
        
        # Adaptive gradient field with directional bias
        grad_field = np.sum(np.abs(x[:-1] - x[1:]) * 
                           (1.0 + 0.2 * np.sin(5.0 * x[:-1]) * np.cos(3.0 * x[1:])))
        
        # Multi-scale fractal-like structure with recursive interactions
        fractal = 0.25 * np.sum(np.abs(x)**1.3 + np.abs(x)**2.1 + 
                               0.5 * np.abs(x)**1.7)
        
        # Non-smooth composite with step functions and random noise
        step_noise = np.sum(np.floor(3.0 * np.sin(x)) * np.cos(2.0 * x) + 
                           0.1 * np.random.randn(len(x)))
        
        # Cross-dimensional coupling with exponential interaction
        cross_coupling = 0.1 * np.sum(np.exp(-0.5 * (x[:-1]**2 + x[1:]**2)) * 
                                    (x[:-1] * x[1:]) * 
                                    np.sin(0.3 * x[:-1] + 0.4 * x[1:]))
        
        # Dynamic dimensional scaling with logarithmic perturbations
        dim_scaling = 1.0 + 0.2 * np.log(self.dim + 1) + 0.08 * np.sin(0.1 * self.dim)
        
        return (base + sin_mod + chaos + grad_field + fractal + step_noise + 
                cross_coupling) * dim_scaling
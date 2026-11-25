import numpy as np

class TrigonometricEllipticChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric polynomial components with varying frequencies
        trig_poly = np.sum(np.sin(1.5 * x) * np.cos(2.0 * x) * 
                          (1.0 + 0.3 * np.sin(3.0 * x)) * 
                          np.exp(-0.1 * np.abs(x))) / self.dim
        
        # Adaptive elliptic conditioning with dynamic scaling
        ellip_cond = np.sum((x**2) / (1.0 + 0.5 * np.abs(x)) * 
                           np.cos(0.5 * x) * 
                           np.exp(-0.05 * np.sum(x**2))) / self.dim
        
        # Chaotic gradient modulation with logistic map influence
        chaos_grad = np.sum(np.sin(x * (1.0 + 0.4 * np.sin(2.0 * np.sum(x**2)))) * 
                          np.cos(x * (1.0 + 0.3 * np.cos(1.5 * np.sum(x**2)))) * 
                          np.exp(-0.1 * r**2)) / self.dim
        
        # Cross-dimensional coupling with polynomial interaction
        cross_poly = np.sum((x[:-1]**2 + x[1:]**2) * 
                          np.sin(x[:-1] * x[1:] * (1.0 + 0.2 * np.cos(np.sum(x)))) * 
                          np.cos(x[:-1] + x[1:] + 0.3 * np.sin(2.0 * r))) / (self.dim - 1)
        
        # Multi-scale harmonic interference
        multi_harm = np.sum(np.sin(3.0 * x) * np.cos(4.0 * x) * 
                           np.exp(-0.08 * np.sum(x**2)) * 
                           (1.0 + 0.25 * np.sin(5.0 * r))) / self.dim
        
        # Asymmetric saddle points with exponential decay
        saddle = np.sum(x**3 * np.sin(2.0 * x) - x**4 * np.cos(1.5 * x) + 
                       0.2 * x**2 * np.exp(-0.03 * np.abs(x)) * 
                       np.sin(3.0 * r)) / (self.dim * 10.0)
        
        # Dynamic phase modulation with sine-cosine coupling
        phase_mod = np.sum(np.cos(x * np.sin(x)) * np.sin(x * np.cos(x)) * 
                          np.exp(-0.04 * r**2) * 
                          (1.0 + 0.3 * np.cos(4.0 * r))) / self.dim
        
        # Combined weighted sum of all components
        total = 0.22 * trig_poly + 0.18 * ellip_cond + 0.15 * chaos_grad + 0.13 * cross_poly + \
                0.12 * multi_harm + 0.10 * saddle + 0.07 * phase_mod
        
        return total
import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Base quadratic term for global attraction
        f1 = np.sum(x_scaled**2)
        
        # Enhanced chaotic exponential modulation with sinusoidal perturbations (higher decay rates)
        f2 = 0.6 * np.sum(np.exp(-7 * np.abs(x_scaled)) * 
                         (np.sin(25 * x_scaled)**3 + np.cos(22 * x_scaled)**3))
        
        # Asymmetric saddle point landscape with varying curvature and fractal-like behavior
        f3 = 0.5 * np.sum((x_scaled**4 - 0.4 * x_scaled**2)**2)
        
        # Multi-scale trigonometric interference creating rugged terrain (higher frequencies)
        f4 = 0.6 * np.sum(np.sin(40 * x_scaled) * np.cos(35 * x_scaled) * 
                         np.sin(30 * x_scaled) * np.cos(25 * x_scaled))
        
        # Logarithmic barrier terms to create narrow valleys and sharp gradients (enhanced)
        f5 = 0.6 * np.sum(np.log(1 + 0.3 * np.abs(x_scaled)) * 
                          np.sin(40 * x_scaled)**3)
        
        # Cross-dimensional interaction with asymmetric coupling (stronger coupling)
        f6 = 0.4 * np.sum(np.sin(20 * x_scaled) * 
                         np.cos(18 * x_scaled) * 
                         np.sin(16 * x_scaled) * 
                         np.cos(14 * x_scaled))
        
        # Power-law modulated oscillations with fractional exponents for scale-invariant ruggedness
        f7 = 0.35 * np.sum(np.abs(x_scaled)**2.1 * 
                          np.sin(50 * x_scaled)**3)
        
        # Gaussian mixture with varying variances and multiple peaks (more complex)
        f8 = 0.45 * np.sum(np.exp(-0.5 * (x_scaled - 0.4)**2) + 
                         np.exp(-0.5 * (x_scaled + 0.4)**2) +
                         np.exp(-0.5 * (x_scaled - 0.2)**2))
        
        # Fractional Brownian motion inspired term with long-range dependence and self-similarity
        f9 = 0.35 * np.sum(np.sin(40 * x_scaled) * 
                          np.cos(42 * x_scaled) * 
                          np.sin(44 * x_scaled) * 
                          np.cos(46 * x_scaled))
        
        # Additional high-frequency oscillation with chaotic phase modulation
        f10 = 0.25 * np.sum(np.sin(60 * x_scaled) * np.cos(55 * x_scaled) * 
                           np.sin(50 * x_scaled))
        
        # Fractal-like self-similarity term using recursive trigonometric composition
        f11 = 0.3 * np.sum(np.sin(20 * np.sin(15 * x_scaled))**2)
        
        # Cross-dimensional coupling with non-linear interaction terms
        f12 = 0.4 * np.sum((x_scaled**2 + 0.1 * x_scaled)**3)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12
import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Base quadratic term for global attraction
        f1 = np.sum(x_scaled**2)
        
        # Chaotic exponential modulation with sinusoidal perturbations
        f2 = 0.3 * np.sum(np.exp(-3 * np.abs(x_scaled)) * 
                         (np.sin(15 * x_scaled)**2 + np.cos(12 * x_scaled)**2))
        
        # Asymmetric saddle point landscape with varying curvature
        f3 = 0.25 * np.sum((x_scaled**3 - 0.5 * x_scaled)**2)
        
        # Multi-scale trigonometric interference creating rugged terrain
        f4 = 0.4 * np.sum(np.sin(20 * x_scaled) * np.cos(18 * x_scaled) * 
                         np.sin(16 * x_scaled) * np.cos(14 * x_scaled))
        
        # Logarithmic barrier terms to create narrow valleys and sharp gradients
        f5 = 0.35 * np.sum(np.log(1 + 0.1 * np.abs(x_scaled)) * 
                          np.sin(25 * x_scaled)**2)
        
        # Cross-dimensional interaction with asymmetric coupling
        f6 = 0.2 * np.sum(np.sin(10 * x_scaled) * 
                         np.cos(8 * x_scaled) * 
                         np.sin(6 * x_scaled) * 
                         np.cos(4 * x_scaled))
        
        # Power-law modulated oscillations to create scale-invariant ruggedness
        f7 = 0.15 * np.sum(np.abs(x_scaled)**1.5 * 
                          np.sin(30 * x_scaled)**2)
        
        # Gaussian mixture with varying variances to simulate multiple local optima
        f8 = 0.2 * np.sum(np.exp(-0.5 * (x_scaled - 0.3)**2) + 
                         np.exp(-0.5 * (x_scaled + 0.3)**2))
        
        # Fractional Brownian motion inspired term with long-range dependence
        f9 = 0.18 * np.sum(np.sin(22 * x_scaled) * 
                          np.cos(24 * x_scaled) * 
                          np.sin(26 * x_scaled))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
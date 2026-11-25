import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Base quadratic term for global attraction
        f1 = np.sum(x_scaled**2)
        
        # Chaotic exponential modulation with sinusoidal perturbations (enhanced decay)
        f2 = 0.4 * np.sum(np.exp(-5 * np.abs(x_scaled)) * 
                         (np.sin(20 * x_scaled)**2 + np.cos(18 * x_scaled)**2))
        
        # Asymmetric saddle point landscape with varying curvature (enhanced)
        f3 = 0.35 * np.sum((x_scaled**3 - 0.3 * x_scaled)**2)
        
        # Multi-scale trigonometric interference creating rugged terrain (adjusted frequencies)
        f4 = 0.4 * np.sum(np.sin(30 * x_scaled) * np.cos(25 * x_scaled) * 
                         np.sin(20 * x_scaled) * np.cos(15 * x_scaled))
        
        # Logarithmic barrier terms to create narrow valleys and sharp gradients
        f5 = 0.45 * np.sum(np.log(1 + 0.2 * np.abs(x_scaled)) * 
                          np.sin(35 * x_scaled)**2)
        
        # Cross-dimensional interaction with asymmetric coupling (enhanced)
        f6 = 0.3 * np.sum(np.sin(15 * x_scaled) * 
                         np.cos(13 * x_scaled) * 
                         np.sin(11 * x_scaled) * 
                         np.cos(9 * x_scaled))
        
        # Power-law modulated oscillations to create scale-invariant ruggedness
        f7 = 0.25 * np.sum(np.abs(x_scaled)**1.8 * 
                          np.sin(40 * x_scaled)**2)
        
        # Gaussian mixture with varying variances to simulate multiple local optima (enhanced)
        f8 = 0.3 * np.sum(np.exp(-0.5 * (x_scaled - 0.3)**2) + 
                         np.exp(-0.5 * (x_scaled + 0.3)**2))
        
        # Fractional Brownian motion inspired term with long-range dependence (enhanced)
        f9 = 0.25 * np.sum(np.sin(30 * x_scaled) * 
                          np.cos(32 * x_scaled) * 
                          np.sin(34 * x_scaled))
        
        # Additional high-frequency oscillation to increase ruggedness
        f10 = 0.15 * np.sum(np.sin(50 * x_scaled) * np.cos(45 * x_scaled))
        
        # Minor mutation: Adjusted frequency and amplitude for enhanced ruggedness
        f11 = 0.2 * np.sum(np.sin(60 * x_scaled) * np.cos(55 * x_scaled) * np.sin(50 * x_scaled))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11
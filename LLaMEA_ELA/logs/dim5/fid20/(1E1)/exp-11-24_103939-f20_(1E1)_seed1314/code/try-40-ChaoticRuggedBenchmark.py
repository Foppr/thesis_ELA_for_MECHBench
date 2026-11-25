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
        f2 = 0.5 * np.sum(np.exp(-6 * np.abs(x_scaled)) * 
                         (np.sin(25 * x_scaled)**2 + np.cos(22 * x_scaled)**2))
        
        # Asymmetric saddle point landscape with varying curvature (enhanced)
        f3 = 0.4 * np.sum((x_scaled**3 - 0.35 * x_scaled)**2)
        
        # Multi-scale trigonometric interference creating rugged terrain (adjusted frequencies)
        f4 = 0.5 * np.sum(np.sin(35 * x_scaled) * np.cos(30 * x_scaled) * 
                         np.sin(25 * x_scaled) * np.cos(20 * x_scaled))
        
        # Logarithmic barrier terms to create narrow valleys and sharp gradients
        f5 = 0.5 * np.sum(np.log(1 + 0.25 * np.abs(x_scaled)) * 
                          np.sin(40 * x_scaled)**2)
        
        # Cross-dimensional interaction with asymmetric coupling (enhanced)
        f6 = 0.35 * np.sum(np.sin(20 * x_scaled) * 
                         np.cos(18 * x_scaled) * 
                         np.sin(16 * x_scaled) * 
                         np.cos(14 * x_scaled))
        
        # Power-law modulated oscillations to create scale-invariant ruggedness
        f7 = 0.3 * np.sum(np.abs(x_scaled)**2.1 * 
                          np.sin(45 * x_scaled)**2)
        
        # Gaussian mixture with varying variances to simulate multiple local optima (enhanced)
        f8 = 0.35 * np.sum(np.exp(-0.5 * (x_scaled - 0.35)**2) + 
                         np.exp(-0.5 * (x_scaled + 0.35)**2))
        
        # Fractional Brownian motion inspired term with long-range dependence (enhanced)
        f9 = 0.3 * np.sum(np.sin(35 * x_scaled) * 
                          np.cos(37 * x_scaled) * 
                          np.sin(39 * x_scaled))
        
        # Additional high-frequency oscillation to increase ruggedness
        f10 = 0.2 * np.sum(np.sin(60 * x_scaled) * np.cos(55 * x_scaled))
        
        # Quantum interference pattern with phase modulation
        f11 = 0.25 * np.sum(np.sin(50 * x_scaled + np.pi/4) * 
                           np.cos(48 * x_scaled + np.pi/3) * 
                           np.sin(46 * x_scaled + np.pi/6))
        
        # Memory-dependent term with delayed feedback
        f12 = 0.15 * np.sum(np.sin(28 * x_scaled) * 
                           np.cos(26 * x_scaled) * 
                           np.sin(24 * x_scaled) * 
                           np.cos(22 * x_scaled))
        
        # Fractal-like self-similar ruggedness at multiple scales
        f13 = 0.2 * np.sum(np.abs(x_scaled)**1.5 * 
                          np.sin(65 * x_scaled)**2 + 
                          np.abs(x_scaled)**1.7 * 
                          np.cos(60 * x_scaled)**2)
        
        # Complex harmonic coupling with time-delayed interactions
        f14 = 0.18 * np.sum(np.sin(33 * x_scaled) * 
                           np.cos(31 * x_scaled) * 
                           np.sin(29 * x_scaled) * 
                           np.cos(27 * x_scaled))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14
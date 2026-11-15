import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters
        self.fractal_dims = np.linspace(0.5, 2.5, dim)
        self.scale_factors = np.logspace(-1, 1, dim)
        self.frequency_bases = np.logspace(0, 2, dim)
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Fractal-inspired polynomial with varying dimensions
        f2 = 0.5 * np.sum(np.abs(x_norm)**(1.5 + 0.5 * np.sin(np.arange(self.dim) * np.pi / 4)))
        
        # Multi-scale sinusoidal components with fractal frequencies
        f3 = 0.3 * np.sum(np.sin(self.frequency_bases * x_norm * np.cos(x_norm)))
        
        # Scale-invariant interaction using power-law
        f4 = 0.2 * np.sum(np.abs(x_norm)**self.fractal_dims)
        
        # Self-similar cross-dimensional terms
        f5 = 0.15 * np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * np.exp(-0.1 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Logarithmic fractal structure
        f6 = 0.25 * np.sum(np.log(1 + np.abs(x_norm)) * np.sin(self.frequency_bases * x_norm))
        
        # Multi-fractal Gaussian with adaptive variance
        f7 = 0.1 * np.sum(np.exp(-0.5 * (x_norm / (1 + np.abs(x_norm)))**2) * np.sin(self.fractal_dims * x_norm))
        
        # Chaotic feedback loop with delayed effect
        f8 = 0.18 * np.sum(np.sin(x_norm * np.sin(x_norm * 0.5)) * np.cos(x_norm * 0.3))
        
        # Fractional Brownian motion inspired term
        f9 = 0.12 * np.sum(np.abs(x_norm)**(1.2 + 0.3 * np.cos(np.arange(self.dim) * np.pi / 3)))
        
        # Multi-scale penalty with varying strength
        f10 = 0.2 * np.sum(np.exp(-self.scale_factors * np.abs(x_norm)) * np.sin(x_norm))
        
        # Complex interaction with delayed feedback
        f11 = 0.1 * np.sum(np.sin(x_norm * np.cos(x_norm * 0.7)) * np.exp(-0.2 * x_norm**2))
        
        # Adaptive fractal dimension interaction
        f12 = 0.15 * np.sum(np.abs(x_norm)**(1.8 + 0.2 * np.sin(np.arange(self.dim) * 0.5)))
        
        # Multi-scale oscillation with amplitude modulation
        f13 = 0.1 * np.sum(np.sin(10 * x_norm * np.log(1 + np.abs(x_norm))) * np.exp(-0.1 * x_norm**2))
        
        # Logarithmic polynomial with fractal scaling
        f14 = 0.08 * np.sum(np.log(1 + np.abs(x_norm)) * x_norm**2)
        
        # Cross-scale coupling with variable interaction strength
        f15 = 0.12 * np.sum(np.sin(x_norm[:-2] * x_norm[1:-1] * x_norm[2:]) * np.exp(-0.05 * np.abs(x_norm[:-2] + x_norm[1:-1] + x_norm[2:])))
        
        # Fractional derivative inspired term
        f16 = 0.05 * np.sum(np.abs(x_norm)**1.6 * np.sin(x_norm))
        
        # Multi-fractal sine with varying frequency
        f17 = 0.18 * np.sum(np.sin(15 * x_norm * np.sin(0.5 * x_norm)) * np.exp(-0.15 * x_norm**2))
        
        # Scale-adaptive penalty with exponential decay
        f18 = 0.1 * np.sum(np.exp(-0.3 * np.abs(x_norm)) * np.cos(x_norm * 2))
        
        # Complex interaction with time-delayed feedback
        f19 = 0.07 * np.sum(np.sin(x_norm * np.sin(x_norm * 0.3)) * np.cos(x_norm * 0.8))
        
        # Self-similar multi-modal structure
        f20 = 0.13 * np.sum(np.sin(5 * x_norm + np.sin(3 * x_norm)) * np.exp(-0.2 * np.abs(x_norm)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20
import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced logarithmic barrier with singularities and chaotic modulation
        f1 = np.sum(np.log(1 + np.abs(x_norm)) * np.sin(2 * np.pi * x_norm) * np.exp(-0.3 * x_norm**2))
        
        # Fractional polynomial interactions with non-integer exponents and multi-scale coupling
        f2 = np.sum(np.sign(x_norm) * np.abs(x_norm)**1.8 * np.cos(3 * x_norm) * np.sin(4 * x_norm))
        
        # Multi-scale harmonic oscillations with varying frequencies and chaotic modulation
        f3 = np.sum(np.sin(5 * x_norm + 0.4 * np.sin(12 * x_norm)) * np.cos(2 * x_norm + 0.2 * np.cos(8 * x_norm)) * np.exp(-0.15 * np.abs(x_norm)))
        
        # Self-similar fractal patterns using recursive-like interactions with exponential decay
        f4 = np.sum((x_norm[:-1]**2 + x_norm[1:]**2)**0.55 * (x_norm[:-1] - x_norm[1:])**2 * np.exp(-0.25 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Enhanced logarithmic coupling with exponential decay and multi-modal perturbations
        f5 = np.sum(np.exp(-np.abs(x_norm)) * np.log(1 + np.abs(x_norm)) * np.sin(4 * x_norm) * (1 + 0.15 * np.sin(9 * x_norm)))
        
        # Multi-scale chaotic perturbations with adaptive amplitudes and fractional modulation
        f6 = np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm) * np.exp(-0.4 * x_norm**2) * (1 + 0.12 * np.sin(4 * x_norm)) * np.log(1 + np.abs(x_norm)))
        
        # Fractional cross-dimensional interactions with non-local coupling and chaotic scaling
        f7 = np.sum(np.abs(x_norm[:-1] - x_norm[1:])**1.4 + 0.15 * np.abs(x_norm[:-1] + x_norm[1:])**1.2 * np.exp(-0.25 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Add dimensionality-dependent scaling factor for increased complexity
        dim_factor = np.log(self.dim + 2)
        
        # Combined fractal landscape with deterministic randomness and multi-scale chaos
        result = (0.25 * f1 + 0.55 * f2 + 0.35 * f3 + 0.65 * f4 + 0.35 * f5 + 0.75 * f6 + 0.25 * f7) * dim_factor
        
        # Add small perturbation for increased complexity
        noise = 0.001 * np.random.random()
        
        return result + noise
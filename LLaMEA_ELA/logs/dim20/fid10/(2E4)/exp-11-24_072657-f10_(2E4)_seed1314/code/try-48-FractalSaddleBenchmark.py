import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Logarithmic barrier terms with varying scales
        f1 = np.sum(np.log(1 + np.abs(x_norm)) * np.sin(2 * np.pi * x_norm))
        
        # Fractional polynomial interactions with non-integer exponents
        f2 = np.sum(np.sign(x_norm) * np.abs(x_norm)**1.7 * np.cos(3 * x_norm))
        
        # Multi-scale harmonic oscillations with varying frequencies
        f3 = np.sum(np.sin(5 * x_norm + 0.5 * np.sin(10 * x_norm)) * np.cos(2 * x_norm + 0.3 * np.cos(7 * x_norm)))
        
        # Self-similar fractal patterns using recursive-like interactions
        f4 = np.sum((x_norm[:-1]**2 + x_norm[1:]**2)**0.6 * (x_norm[:-1] - x_norm[1:])**2)
        
        # Logarithmic coupling with exponential decay
        f5 = np.sum(np.exp(-np.abs(x_norm)) * np.log(1 + np.abs(x_norm)) * np.sin(4 * x_norm))
        
        # Multi-scale chaotic perturbations with adaptive amplitudes
        f6 = np.sum(np.sin(9 * x_norm) * np.cos(6 * x_norm) * np.exp(-0.5 * x_norm**2) * (1 + 0.1 * np.sin(3 * x_norm)))
        
        # Fractional cross-dimensional interactions
        f7 = np.sum(np.abs(x_norm[:-1] - x_norm[1:])**1.3 + 0.2 * np.abs(x_norm[:-1] + x_norm[1:])**1.1)
        
        # Combined fractal landscape with deterministic randomness
        result = 0.3 * f1 + 0.5 * f2 + 0.4 * f3 + 0.6 * f4 + 0.4 * f5 + 0.7 * f6 + 0.3 * f7
        
        # Add small perturbation for increased complexity
        noise = 0.001 * np.random.random()
        
        return result + noise
import numpy as np

class FractalEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Self-similar fractal component with recursive cosine modulation
        fractal_term = np.sum(np.cos(2.0 * np.pi * np.sqrt(np.sum(x**2)) * (1.0 + 0.1 * np.sin(3.0 * np.sum(x)))) / (1.0 + 0.05 * np.sum(x**2))) / self.dim
        
        # Adaptive elliptic distortion with varying eccentricity
        ellip_term = np.sum((x**2 + 1.0) * np.exp(-0.1 * np.sum(x**2)) * np.cos(2.0 * np.pi * np.sqrt(np.sum(x**2)) * 0.5)) / self.dim
        
        # Dynamic noise injection with amplitude modulation
        noise_term = np.sum(np.sin(x * (1.0 + 0.2 * np.sin(0.5 * np.sum(x**2)))) * np.cos(x * (1.0 + 0.3 * np.cos(0.7 * np.sum(x**2))))) / self.dim
        
        # Cross-term interaction with fractal-like scaling
        cross_term = np.sum(np.sin(x[:-1] * x[1:]) * np.cos(x[:-1] + x[1:]) * (1.0 + 0.1 * np.abs(x[:-1] - x[1:]))) / (self.dim - 1)
        
        # Multiscale periodic component with varying frequencies
        multi_freq = np.sum(np.sin(5.0 * x) * np.cos(3.0 * x) * np.exp(-0.02 * np.sum(x**2))) / self.dim
        
        # Adaptive conditioning with dynamic scaling factor
        cond_factor = 1.0 + 0.5 * np.mean(np.abs(x))**1.8
        cond_term = np.sum((x**2) * cond_factor * np.sin(2.0 * x)) / self.dim
        
        # Saddle-point structure with mixed polynomial and trigonometric components
        saddle_term = np.sum(x**3 * np.cos(x) - x**5 * np.sin(x) + x**2 * np.tan(x/2.0)) / (self.dim * 10.0)
        
        # Combined weighted sum of all components
        total = 0.2 * fractal_term + 0.2 * ellip_term + 0.15 * noise_term + 0.1 * cross_term + 0.15 * multi_freq + 0.1 * cond_term + 0.05 * saddle_term
        
        return total
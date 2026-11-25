import numpy as np

class FractalEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal component with recursive sine modulation and scaling
        fractal_term = np.sum(np.sin(3.0 * np.pi * np.sqrt(np.sum(x**2)) * (1.0 + 0.15 * np.cos(2.0 * np.sum(x)))) / 
                             (1.0 + 0.08 * np.sum(x**2) + 0.02 * np.sum(np.abs(x)))) / self.dim
        
        # Improved elliptic distortion with variable eccentricity and exponential scaling
        ellip_term = np.sum((x**2 + 0.5) * np.exp(-0.15 * np.sum(x**2)) * 
                           np.cos(3.0 * np.pi * np.sqrt(np.sum(x**2)) * 0.6)) / self.dim
        
        # Enhanced dynamic noise with amplitude and frequency modulation
        noise_term = np.sum(np.sin(x * (1.0 + 0.25 * np.sin(0.7 * np.sum(x**2))) * 
                                  np.cos(x * (1.0 + 0.35 * np.cos(0.9 * np.sum(x**2))))) / 
                           (1.0 + 0.1 * np.abs(x))) / self.dim
        
        # Refined cross-term interaction with fractal-like scaling and directional coupling
        cross_term = np.sum(np.sin(x[:-1] * x[1:]) * np.cos(x[:-1] + x[1:]) * 
                           (1.0 + 0.2 * np.abs(x[:-1] - x[1:]) + 0.1 * np.sin(2.0 * np.sum(x)))) / (self.dim - 1)
        
        # Multi-scale periodic component with varying frequencies and adaptive weights
        multi_freq = np.sum(np.sin(6.0 * x) * np.cos(4.0 * x) * 
                           np.exp(-0.03 * np.sum(x**2)) * (1.0 + 0.1 * np.sin(0.5 * np.sum(x)))) / self.dim
        
        # Enhanced adaptive conditioning with dynamic scaling and polynomial modulation
        cond_factor = 1.0 + 0.6 * np.mean(np.abs(x))**2.0
        cond_term = np.sum((x**2) * cond_factor * np.sin(3.0 * x) * 
                          np.cos(0.5 * x)) / self.dim
        
        # Strengthened saddle-point structure with higher-order polynomial and trigonometric mixing
        saddle_term = np.sum(x**4 * np.cos(x) - x**6 * np.sin(x) + x**3 * np.tan(x/3.0)) / (self.dim * 12.0)
        
        # Combined weighted sum of all components with refined coefficients
        total = 0.25 * fractal_term + 0.2 * ellip_term + 0.18 * noise_term + 0.12 * cross_term + \
                0.15 * multi_freq + 0.08 * cond_term + 0.02 * saddle_term
        
        return total
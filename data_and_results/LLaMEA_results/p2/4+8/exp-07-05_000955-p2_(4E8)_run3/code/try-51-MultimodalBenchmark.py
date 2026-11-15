import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term for global convergence
        f1 = np.sum(x**2)
        
        # Enhanced chaotic sine-wave interactions with higher frequency modulation and amplitude scaling
        f2 = 0.6 * np.sum(np.sin(10.0 * x + np.sin(7.0 * x)) * np.cos(12.0 * x + np.sin(6.0 * x)))
        
        # Modified radial gradient with inverse exponential decay and multi-scale sinusoidal modulation
        f3 = 0.35 * np.sum(np.exp(-0.5 * np.sum(x**2)) * np.sin(7.0 * np.sum(x**2)) * np.cos(3.0 * np.sum(x**2)))
        
        # Cross-term interactions with higher-order polynomial modulation and trigonometric coupling
        f4 = 0.25 * np.sum((x**5) * np.sin(10.0 * x) * np.cos(5.0 * x) + (x**6) * np.sin(4.0 * x) * np.cos(8.0 * x))
        
        # Multi-scale sinusoidal modulation with adaptive amplitude scaling and phase shifts
        f5 = 0.3 * np.sum(np.sin(15.0 * x) * np.sin(20.0 * x) * np.cos(7.0 * x) * np.sin(9.0 * x))
        
        # Adaptive scaling with Gaussian-like decay, higher-order polynomial terms, and chaotic perturbations
        f6 = 0.15 * np.sum(np.exp(-0.2 * np.sum(x**2)) * x**7 * np.sin(6.0 * x))
        
        # Additional coupling term with exponential and trigonometric interactions to increase nonlinearity
        f7 = 0.1 * np.sum(np.sin(x) * np.cos(3.0 * x) * np.sin(5.0 * x) * np.exp(-0.1 * np.sum(x**2)))
        
        # Cross-dimensional coupling with polynomial and exponential interactions
        f8 = 0.2 * np.sum(np.exp(-0.1 * np.sum((x - np.roll(x, 1))**2)) * np.sin(8.0 * x) * np.cos(4.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
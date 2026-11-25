import numpy as np

class AdaptiveTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Periodic trigonometric components with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 2 * np.pi * (1.0 + 0.5 * np.sin(i * 0.7))
            amp = 1.0 + 0.3 * np.cos(i * 0.9)
            f2 += amp * np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Adaptive Gaussian peaks with position-dependent heights and widths
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            peak_height = 2.0 + 1.5 * np.sin(i * 0.6)
            peak_width = 0.5 + 0.3 * np.cos(i * 0.4)
            f3 -= peak_height * np.exp(-0.5 * ((xi - 2.0 * np.sin(i * 0.8)) / peak_width)**2)
        
        # Cross-dimensional interaction terms with asymmetric coupling
        f4 = 0.0
        for i in range(self.dim-1):
            xi, xj = x[i], x[i+1]
            coupling_strength = 0.5 + 0.3 * np.sin(i * 0.5)
            f4 += coupling_strength * np.sin(xi + 0.7 * xj) * np.cos(0.8 * xi - xj)
        
        # Fractional power nonlinearities with sinusoidal modulation
        f5 = 0.1 * np.sum((np.abs(x)**1.8 + 0.5 * np.sin(x)) * np.exp(-0.2 * np.abs(x)))
        
        # Saddle-point structure with multi-scale interference
        f6 = 0.15 * np.sum(np.sin(5.0 * x) * np.cos(3.0 * x) * np.exp(-0.1 * x**2))
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6
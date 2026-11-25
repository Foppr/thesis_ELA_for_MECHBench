import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial polynomial conditioning with adaptive exponents and coupling
        radial_poly = np.sum((x**2 + 0.4 * x**4 + 0.1 * x**6) * (1.0 + 0.3 * np.cos(self.dim * x)))
        
        # Composite sinusoidal waves with dynamic frequency modulation and phase shifts
        sin_wave = np.sum(np.sin(4.0 * x + 0.6 * np.sin(3.0 * x)) * 
                         np.cos(2.5 * x + 0.4 * np.cos(1.8 * x)) * 
                         np.exp(-0.15 * np.abs(x)))
        
        # Multi-scale Gaussian peaks with varying heights, widths, and positions
        gaussian_sum = 0.0
        for i in range(min(5, self.dim)):
            height = 2.0 + 0.3 * np.sin(i * 0.9)
            width = 1.0 + 0.3 * np.cos(i * 0.7)
            center = -4.5 + 9.0 * (i / max(1, self.dim - 1))
            gaussian_sum += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Chaotic exponential coupling with time-varying parameters and cross-terms
        exp_coupling = np.sum(np.exp(-0.25 * (x[:-1]**2 + x[1:]**2)) * 
                             np.sin(3.5 * (x[:-1] - x[1:])) * 
                             np.cos(3.0 * (x[:-1] + x[1:])))
        
        # Adaptive noise modulation with dynamic intensity and frequency
        noise = 0.15 * np.random.rand() * np.sum(np.sin(6.0 * x) * np.cos(2.5 * x))
        
        # Gradient-based curvature adjustment with non-uniform scaling
        grad_curvature = 0.4 * np.sum(np.gradient(x)**2 * (1.0 + 0.4 * np.abs(x)))
        
        # Combined function value with enhanced fitness landscape
        return radial_poly + sin_wave + gaussian_sum + exp_coupling + noise + grad_curvature
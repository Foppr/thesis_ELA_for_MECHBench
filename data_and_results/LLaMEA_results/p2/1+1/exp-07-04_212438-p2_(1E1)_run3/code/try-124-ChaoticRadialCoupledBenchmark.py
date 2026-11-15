import numpy as np

class ChaoticRadialCoupledBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with fractional exponents and chaotic modulation
        f1 = np.sum((x**3.7 + 0.5 * x**2.3 - 2.1 * x**1.9 + 0.8 * x**0.7) * 
                   np.sin(10.0 * np.sin(7.0 * x)) * np.cos(5.0 * np.cos(3.0 * x)))
        
        # Radial basis function with time-varying centers and dynamic widths
        centers = np.sin(np.linspace(0, 2*np.pi, self.dim)) * 4.0
        widths = 0.5 + 3.5 * np.sin(np.linspace(0, 3*np.pi, self.dim))**2
        f2 = np.sum(np.exp(-0.5 * (x - centers)**2 / widths) * 
                   np.sin(12.0 * x) * np.cos(8.0 * x) * np.tan(0.5 * x))
        
        # Temporal coupling with delayed feedback and dynamic phase shifts
        delay = 1
        if self.dim > 1:
            f3 = np.sum(np.sin(15.0 * x[:-delay]) * np.cos(15.0 * x[delay:]) * 
                       np.exp(-0.3 * np.abs(x[:-delay] - x[delay:])) * 
                       np.sin(2.0 * np.sum(x**2)))
        else:
            f3 = 0.0
        
        # Multi-scale fractal-like component with recursive structure
        f4 = np.sum(np.sin(25.0 * x) * np.cos(30.0 * x) * 
                   np.sin(35.0 * x) * np.cos(40.0 * x) * 
                   np.exp(-0.1 * x**4) * np.sin(1.5 * np.sum(x**4)))
        
        # Coupled oscillatory terms with variable coupling and frequency modulation
        f5 = np.sum(np.sin(20.0 * x[:-1] * x[1:]) * 
                   np.cos(20.0 * (x[:-1] + x[1:])) * 
                   np.exp(-0.5 * (x[:-1] - x[1:])**2) * 
                   np.sin(5.0 * np.sum(x**3)))
        
        # Fractional power interaction with chaotic amplification
        f6 = np.sum((x[:-1]**1.3 + x[1:]**1.7) * 
                   np.sin(18.0 * x[:-1]) * np.cos(18.0 * x[1:]) * 
                   np.exp(-0.4 * np.abs(x[:-1] - x[1:])) * 
                   np.sin(3.0 * np.sum(x**2)))
        
        # Combined function with dynamic weighting and normalization
        return 0.25 * f1 + 0.20 * f2 + 0.18 * f3 + 0.15 * f4 + 0.12 * f5 + 0.10 * f6
import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic component with exponential decay and multi-scale correlations
        chaos = np.sum(np.exp(-np.abs(x)) * np.sin(np.pi * x) * np.cos(2 * np.pi * x))
        
        # Gradient-based curvature with varying scale parameters
        grad_curv = np.sum((x**3 - 3*x)**2 * np.exp(-0.1 * np.abs(x)))
        
        # Multi-scale oscillatory component with exponentially decaying amplitudes
        scales = np.arange(1, self.dim + 1)
        oscill = np.sum(np.exp(-0.5 * scales) * np.sin(scales * x) * np.cos(scales * x))
        
        # Saddle-point dominant structure with asymmetric hessian
        saddle = np.sum((x[:-1]**2 - x[1:]**2)**2 * np.exp(-0.05 * np.abs(x[:-1] + x[1:])))
        
        # Exponentially decaying correlation structure
        corr = np.sum(np.exp(-0.2 * np.arange(1, self.dim + 1)) * np.sin(2 * np.pi * x) * np.cos(2 * np.pi * x))
        
        # Fractional power interaction with non-convexity
        frac = np.sum(np.abs(x)**1.7 * np.sin(3 * x) * np.cos(3 * x))
        
        # Asymmetric exponential decay with chaotic modulation
        asym = np.sum(np.exp(-np.abs(x)**1.5) * np.sin(5 * x) * np.cos(5 * x) * np.exp(-0.3 * x**2))
        
        # Combined function with chaotic amplification and multi-scale interactions
        return 0.4 * chaos + 0.3 * grad_curv + 0.2 * oscill + 0.15 * saddle + 0.1 * corr + 0.05 * frac + 0.03 * asym
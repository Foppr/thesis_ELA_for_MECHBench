import numpy as np

class ExponentialWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay term with oscillatory modulation
        f1 = np.sum(np.exp(-0.5 * np.abs(x)) * np.cos(2.0 * np.pi * x))
        
        # Multi-scale trigonometric interference pattern
        f2 = np.sum(np.sin(10.0 * x) * np.cos(5.0 * x) * np.exp(-0.1 * x**2))
        
        # Gradient-based attraction field with repulsion zones
        f3 = np.sum((x**2 + 1.0)**(-1.5) * np.sin(3.0 * x))
        
        # High-frequency wave component with varying amplitude
        f4 = 0.5 * np.sum(np.sin(20.0 * np.exp(-0.3 * np.abs(x))) * np.cos(15.0 * x))
        
        # Asymmetric basin structure with saddle points
        f5 = 0.3 * np.sum(np.log(1.0 + 0.1 * x**4) * np.tanh(x))
        
        # Combine all components with varying weights
        return 0.8 * f1 + 1.2 * f2 + 0.6 * f3 + 1.0 * f4 + 0.7 * f5
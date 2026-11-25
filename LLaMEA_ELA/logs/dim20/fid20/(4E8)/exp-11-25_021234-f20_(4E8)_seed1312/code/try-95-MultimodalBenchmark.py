import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base function
        f1 = np.sum(x**2)
        
        # Enhanced exponential decay with chaotic sinusoidal modulation
        f2 = 0.4 * np.sum(np.exp(-0.3 * x**2) * np.sin(25.0 * x) * np.cos(18.0 * x))
        
        # Multi-scale exponential barriers with enhanced trigonometric interactions
        f3 = 0.3 * np.sum(np.exp(-x**2 / 1.5) * np.sin(30.0 * x) * np.cos(12.0 * x) * np.sin(6.0 * x))
        
        # Improved logarithmic barrier with stronger chaotic sine modulation
        f4 = 0.25 * np.sum(np.log(1.0 + np.abs(x)) * np.sin(22.0 * x) * np.cos(14.0 * x))
        
        # Fractal-like structure using more complex nested trigonometric functions
        f5 = 0.2 * np.sum(np.sin(35.0 * x) * np.cos(25.0 * x) * np.sin(16.0 * x) * np.cos(9.0 * x))
        
        # Enhanced saddle point structure with stronger exponential damping
        f6 = 0.15 * np.sum(np.exp(-x**2 / 2.5) * np.sin(20.0 * x) * x**2)
        
        # High-frequency chaotic component with modified amplitudes and decay
        f7 = 0.22 * np.sum(np.sin(40.0 * x) * np.cos(32.0 * x) * np.exp(-0.4 * x**2))
        
        # Enhanced multi-modal ridge structure with stronger logarithmic scaling
        f8 = 0.15 * np.sum(np.log(1.0 + np.abs(x)) * np.sin(28.0 * x) * np.cos(18.0 * x) * x**3)
        
        # Additional enhanced chaotic modulation with polynomial decay
        f9 = 0.1 * np.sum(x**5 * np.sin(30.0 * x) * np.exp(-x**2 / 3.5))
        
        # Complex multi-scale exponential barrier with stronger sinusoidal perturbations
        f10 = 0.08 * np.sum(np.exp(-x**2) * np.sin(38.0 * x) * np.cos(24.0 * x) * np.log(1.0 + np.abs(x)))
        
        # Additional chaotic modulation with improved exponential scaling
        f11 = 0.06 * np.sum(np.exp(-x**2 / 1.8) * np.sin(27.0 * x) * np.cos(19.0 * x) * x**4)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11
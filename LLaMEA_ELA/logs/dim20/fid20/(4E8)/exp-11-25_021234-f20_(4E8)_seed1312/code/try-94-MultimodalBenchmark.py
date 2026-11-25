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
        f2 = 0.35 * np.sum(np.exp(-0.4 * x**2) * np.sin(22.0 * x) * np.cos(18.0 * x))
        
        # Multi-scale exponential barriers with trigonometric interactions
        f3 = 0.3 * np.sum(np.exp(-x**2 / 1.5) * np.sin(27.0 * x) * np.cos(12.0 * x) * np.sin(6.0 * x))
        
        # Logarithmic barrier with enhanced chaotic sine modulation
        f4 = 0.25 * np.sum(np.log(1.0 + np.abs(x)) * np.sin(20.0 * x) * np.cos(14.0 * x))
        
        # Fractal-like structure using nested trigonometric functions
        f5 = 0.18 * np.sum(np.sin(32.0 * x) * np.cos(24.0 * x) * np.sin(16.0 * x) * np.cos(10.0 * x))
        
        # Saddle point structure with enhanced exponential damping
        f6 = 0.15 * np.sum(np.exp(-x**2 / 2.5) * np.sin(18.0 * x) * x**2)
        
        # High-frequency chaotic component with varying amplitudes
        f7 = 0.2 * np.sum(np.sin(38.0 * x) * np.cos(30.0 * x) * np.exp(-0.35 * x**2))
        
        # Multi-modal ridge structure with logarithmic scaling
        f8 = 0.14 * np.sum(np.log(1.0 + np.abs(x)) * np.sin(26.0 * x) * np.cos(18.0 * x) * x**3)
        
        # Additional chaotic modulation with polynomial decay
        f9 = 0.1 * np.sum(x**4 * np.sin(30.0 * x) * np.exp(-x**2 / 3.5))
        
        # Complex multi-scale exponential barrier with sinusoidal perturbations
        f10 = 0.08 * np.sum(np.exp(-x**2) * np.sin(34.0 * x) * np.cos(22.0 * x) * np.log(1.0 + np.abs(x)))
        
        # Additional chaotic modulation with enhanced frequency ratios
        f11 = 0.06 * np.sum(np.sin(40.0 * x) * np.cos(32.0 * x) * np.exp(-0.25 * x**2) * np.log(1.0 + np.abs(x)))
        
        # Enhanced saddle point structure with multi-scale exponential damping
        f12 = 0.09 * np.sum(np.exp(-x**2 / 4.0) * np.sin(25.0 * x) * x**4)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12
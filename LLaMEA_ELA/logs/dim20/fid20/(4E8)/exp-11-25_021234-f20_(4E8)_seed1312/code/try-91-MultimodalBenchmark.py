import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base function
        f1 = np.sum(x**2)
        
        # Exponential decay with chaotic sinusoidal modulation
        f2 = 0.3 * np.sum(np.exp(-0.5 * x**2) * np.sin(20.0 * x) * np.cos(15.0 * x))
        
        # Multi-scale exponential barriers with trigonometric interactions
        f3 = 0.25 * np.sum(np.exp(-x**2 / 2.0) * np.sin(25.0 * x) * np.cos(10.0 * x) * np.sin(5.0 * x))
        
        # Logarithmic barrier with chaotic sine modulation
        f4 = 0.2 * np.sum(np.log(1.0 + np.abs(x)) * np.sin(18.0 * x) * np.cos(12.0 * x))
        
        # Fractal-like structure using nested trigonometric functions
        f5 = 0.15 * np.sum(np.sin(30.0 * x) * np.cos(22.0 * x) * np.sin(14.0 * x) * np.cos(8.0 * x))
        
        # Saddle point structure with exponential damping
        f6 = 0.1 * np.sum(np.exp(-x**2 / 3.0) * np.sin(16.0 * x) * x**2)
        
        # High-frequency chaotic component with varying amplitudes
        f7 = 0.18 * np.sum(np.sin(35.0 * x) * np.cos(28.0 * x) * np.exp(-0.3 * x**2))
        
        # Multi-modal ridge structure with logarithmic scaling
        f8 = 0.12 * np.sum(np.log(1.0 + np.abs(x)) * np.sin(24.0 * x) * np.cos(16.0 * x) * x**3)
        
        # Additional chaotic modulation with polynomial decay
        f9 = 0.08 * np.sum(x**4 * np.sin(27.0 * x) * np.exp(-x**2 / 4.0))
        
        # Complex multi-scale exponential barrier with sinusoidal perturbations
        f10 = 0.05 * np.sum(np.exp(-x**2) * np.sin(32.0 * x) * np.cos(20.0 * x) * np.log(1.0 + np.abs(x)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
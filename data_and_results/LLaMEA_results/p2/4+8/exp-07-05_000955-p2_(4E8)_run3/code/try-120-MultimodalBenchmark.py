import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave component with varying frequencies and amplitudes
        f1 = 0.3 * np.sum(np.sin(10.0 * np.sin(2.0 * x)) * np.cos(7.0 * np.cos(3.0 * x)))
        
        # Polynomial chaos expansion with cross-terms and varying degrees
        f2 = 0.25 * np.sum((x**2 + 0.5 * x**3 + 0.1 * x**4) * np.sin(5.0 * x))
        
        # Adaptive ridge-like structure with dynamic scaling
        f3 = 0.2 * np.sum(np.exp(-0.5 * x**2) * np.cos(8.0 * x) * (1.0 + 0.3 * np.sin(4.0 * x)))
        
        # Multi-scale fractal sine interaction with logarithmic scaling
        f4 = 0.15 * np.sum(np.sin(np.log(np.abs(x) + 2.0)) * np.cos(np.log(np.abs(x) + 2.0)) * np.sin(6.0 * x))
        
        # Saddle point distribution with hyperbolic tangent and polynomial coupling
        f5 = 0.18 * np.sum(np.tanh(x) * (x**3 - x) * np.cos(3.0 * x))
        
        # Cross-term coupling with exponential decay and chaotic modulation
        f6 = 0.12 * np.sum(np.exp(-0.3 * np.abs(x)) * np.sin(11.0 * x) * np.cos(9.0 * x) * np.sin(2.0 * np.sum(x)))
        
        # Additional chaotic noise component with dynamic frequency modulation
        f7 = 0.08 * np.sum(np.sin(0.2 * np.sum(x**2)) * np.cos(0.15 * np.sum(x)) * np.exp(-0.05 * np.sum(np.abs(x))))
        
        # Final fractal-like interaction with recursive trigonometric functions
        f8 = 0.07 * np.sum(np.sin(np.sin(4.0 * x)) * np.cos(np.cos(3.0 * x)) * np.sin(5.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
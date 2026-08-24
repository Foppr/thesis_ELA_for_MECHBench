import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term for global convergence
        f1 = np.sum(x**2)
        
        # Enhanced chaotic tangent-wave interactions with higher frequency components
        f2 = 0.4 * np.sum(np.tan(7.0 * x + np.tan(5.0 * x)) * np.cos(9.0 * x + np.tan(4.0 * x)))
        
        # Modified radial gradient with Gaussian-like decay and additional sinusoidal modulation
        f3 = 0.25 * np.sum(np.exp(-0.3 * np.sum(x**2)) * np.sin(5.0 * np.sum(x**2)) * np.cos(2.0 * np.sum(x**2)))
        
        # Cross-term interactions with cubic and quartic polynomial modulation
        f4 = 0.15 * np.sum((x**3 + 0.5 * x**4) * np.sin(8.0 * x) * np.cos(4.0 * x))
        
        # Multi-scale sinusoidal modulation with varying amplitudes and frequencies
        f5 = 0.2 * np.sum(np.sin(12.0 * x) * np.sin(18.0 * x) * np.cos(6.0 * x) * np.sin(3.0 * x))
        
        # Adaptive scaling with exponential and polynomial components
        f6 = 0.1 * np.sum(np.exp(-0.1 * np.sum(x**2)) * (x**4 + 0.3 * x**5))
        
        # Additional chaotic component with fractional powers for increased complexity
        f7 = 0.05 * np.sum(np.sin(np.sqrt(np.abs(x))) * np.cos(np.sqrt(np.abs(x))) * np.exp(-0.5 * np.sum(x**2)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7
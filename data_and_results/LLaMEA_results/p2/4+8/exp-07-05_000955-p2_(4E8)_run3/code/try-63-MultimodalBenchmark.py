import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term for global convergence
        f1 = np.sum(x**2)
        
        # Enhanced chaotic sine-wave interactions with higher frequency components
        f2 = 0.5 * np.sum(np.sin(8.0 * x + np.sin(6.0 * x)) * np.cos(10.0 * x + np.sin(5.0 * x)))
        
        # Modified radial gradient with Gaussian-like decay and additional sinusoidal modulation
        f3 = 0.3 * np.sum(np.exp(-0.4 * np.sum(x**2)) * np.sin(6.0 * np.sum(x**2)) * np.cos(3.0 * np.sum(x**2)))
        
        # Cross-term interactions with cubic and quartic polynomial modulation
        f4 = 0.2 * np.sum((x**3 + 0.6 * x**4) * np.sin(9.0 * x) * np.cos(5.0 * x))
        
        # Multi-scale sinusoidal modulation with varying amplitudes and frequencies
        f5 = 0.25 * np.sum(np.sin(15.0 * x) * np.sin(20.0 * x) * np.cos(7.0 * x) * np.sin(4.0 * x))
        
        # Adaptive scaling with exponential and polynomial components
        f6 = 0.15 * np.sum(np.exp(-0.15 * np.sum(x**2)) * (x**4 + 0.4 * x**5))
        
        # Additional chaotic component with fractional powers for increased complexity
        f7 = 0.08 * np.sum(np.sin(np.sqrt(np.abs(x))) * np.cos(np.sqrt(np.abs(x))) * np.exp(-0.6 * np.sum(x**2)))
        
        # Enhanced interaction terms with additional coupling and modulation
        f8 = 0.1 * np.sum(np.sin(12.0 * x) * np.cos(14.0 * x) * np.exp(-0.2 * np.sum(x**2)) * (x**2 + 0.5 * x**3))
        
        # Additional high-frequency chaotic modulation
        f9 = 0.05 * np.sum(np.sin(25.0 * x + np.sin(18.0 * x)) * np.cos(22.0 * x + np.sin(15.0 * x)))
        
        # Modified polynomial coupling with variable exponents
        f10 = 0.12 * np.sum((x**5 + 0.3 * x**6) * np.sin(7.0 * x) * np.cos(4.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
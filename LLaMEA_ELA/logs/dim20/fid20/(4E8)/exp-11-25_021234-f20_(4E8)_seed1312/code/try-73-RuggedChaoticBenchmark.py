import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with varying degrees
        f1 = np.sum(x**4 + 0.5 * x**3 + 0.2 * x**2)
        
        # Enhanced logarithmic barrier terms with sharper gradients
        f2 = np.sum(1.5 / (np.log(np.abs(x) + 1.05)) * np.sin(12.0 * x))
        
        # Multi-scale sinusoidal modulations with enhanced frequency mixing
        f3 = 0.6 * np.sum(np.sin(25.0 * x) * np.exp(-0.25 * np.abs(x)) + 
                          np.cos(35.0 * x) * np.exp(-0.15 * np.abs(x)) + 
                          np.sin(45.0 * x) * np.exp(-0.08 * np.abs(x)))
        
        # Enhanced chaotic component with modified trigonometric mixing
        f4 = 0.4 * np.sum((x**2 + 0.15 * x)**2 * np.cos(18.0 * x) * np.sin(10.0 * x))
        
        # Enhanced fractal-like structure with increased self-similarity
        f5 = 0.3 * np.sum(np.sin(45.0 * x) * np.cos(30.0 * x) * np.exp(-0.12 * x**2) + 
                          np.sin(65.0 * x) * np.cos(40.0 * x) * np.exp(-0.08 * x**2))
        
        # Enhanced non-smooth regions with modified fractional powers
        f6 = 0.2 * np.sum(np.abs(x)**1.8 + np.abs(x)**2.5)
        
        # Increased high-frequency oscillations with varying amplitudes
        f7 = 0.3 * np.sum(np.sin(110.0 * x) * np.cos(90.0 * x) * np.exp(-0.03 * x**2))
        
        # Enhanced mixed polynomial and exponential terms
        f8 = 0.15 * np.sum(x**5 * np.exp(-0.12 * np.abs(x)) + x**6 * np.sin(14.0 * x))
        
        # Additional chaotic modulation with sine-cosine product
        f9 = 0.25 * np.sum(np.sin(70.0 * x) * np.cos(50.0 * x) * np.exp(-0.06 * x**2))
        
        # Modified polynomial chaos with higher order terms
        f10 = 0.1 * np.sum(x**7 + x**8 * np.sin(16.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
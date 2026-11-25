import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2)
        
        # Polynomial chaos component with varying degrees
        f2 = 0.3 * np.sum((x**4 + 0.5*x**3 - 0.2*x**2 + 0.1*x) * np.sin(7.0 * x))
        
        # Logarithmic barrier to enhance non-smoothness near boundaries
        f3 = 0.25 * np.sum(np.log(1.0 + np.abs(x)) * np.cos(9.0 * x))
        
        # Multi-scale sinusoidal modulations with varying frequencies
        f4 = 0.4 * np.sum(np.sin(15.0 * x) * np.cos(11.0 * x) * np.sin(6.0 * x) * np.exp(-0.2 * x**2))
        
        # Rugged landscape through chaotic sine-cosine combinations
        f5 = 0.35 * np.sum(np.sin(22.0 * x) * np.cos(18.0 * x) * np.sin(14.0 * x) * np.cos(10.0 * x))
        
        # Fractal-like structure with overlapping peaks and valleys
        f6 = 0.2 * np.sum(np.sin(25.0 * x) * np.cos(20.0 * x) * np.sin(15.0 * x) * np.cos(10.0 * x) * np.exp(-0.1 * x**2))
        
        # Saddle point enhancement with cubic terms
        f7 = 0.15 * np.sum(x**3 * np.sin(8.0 * x) * np.cos(5.0 * x))
        
        # Additional chaotic modulation with exponential decay
        f8 = 0.2 * np.sum(np.sin(28.0 * x) * np.exp(-0.4 * x**2) * np.cos(23.0 * x) * np.sin(19.0 * x))
        
        # Multi-scale ruggedness through nested sinusoidal components
        f9 = 0.18 * np.sum(np.sin(30.0 * x) * np.cos(25.0 * x) * np.sin(20.0 * x) * np.cos(15.0 * x) * np.exp(-0.3 * x**2))
        
        # Combined logarithmic and polynomial barrier
        f10 = 0.1 * np.sum(np.log(1.0 + np.abs(x)**1.5) * np.sin(12.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
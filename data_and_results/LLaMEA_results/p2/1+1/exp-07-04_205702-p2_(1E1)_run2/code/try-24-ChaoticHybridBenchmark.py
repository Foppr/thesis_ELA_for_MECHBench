import numpy as np

class ChaoticHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial with chaotic modulation
        f1 = np.sum(x**8 * (1.0 + 0.6 * np.sin(12.0 * x) * np.cos(8.0 * x)))
        
        # Exponential with multi-scale sinusoidal modulation
        f2 = 0.0
        for i in range(self.dim):
            f2 -= np.exp(-0.04 * x[i]**2) * np.sin(7.0 * x[i]) * np.cos(5.0 * x[i]) * np.tan(0.5 * x[i])
        
        # Multi-modal Gaussian peaks with dynamic positioning and scaling
        f3 = 0.0
        for i in range(self.dim):
            sigma = 0.7 + 0.3 * np.sin(0.9 * i + 0.5 * np.cos(0.6 * i))
            mu = 2.0 * np.cos(0.6 * i) + 1.5 * np.sin(0.5 * i)
            f3 -= np.exp(-0.5 * ((x[i] - mu) / sigma)**5) * (1.0 + 0.5 * np.sin(10.0 * x[i]))
        
        # Cross-dimensional interaction with chaotic coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                f4 += np.sin(x[i] * x[j]) * np.exp(-0.2 * (x[i] - x[j])**2) * np.cos(3.0 * x[i] + x[j])
        
        # Asymmetric long-range coupling with chaotic phase
        f5 = 0.0
        for i in range(self.dim):
            f5 += np.sin(0.3 * x[i]) * np.exp(-0.15 * np.sum(x**2)) * np.cos(4.0 * x[i] + np.sin(0.3 * i))
        
        # Adaptive conditioning with chaotic weights
        weights = np.array([1.0 + 0.4 * np.sin(0.4 * i + np.cos(0.2 * i)) for i in range(self.dim)])
        f6 = np.sum(weights * np.abs(x)**4.0)
        
        # Chaotic sine-cosine interaction component
        f7 = 0.08 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)) * np.sin(0.5 * x) * np.cos(0.3 * x))
        
        # Add a global chaotic attractor term
        f8 = 0.02 * np.sum(np.sin(2.5 * x) * np.cos(3.0 * x) * np.exp(-0.015 * np.sum(x**2)))
        
        # Introduce a new component for better conditioning and fitness improvement
        f9 = 0.02 * np.sum(np.sin(0.2 * x) * np.cos(0.3 * x) * np.exp(-0.07 * np.sum(x**2)))
        
        # Add a novel hyper-chaotic component with higher dimensional coupling
        f10 = 0.03 * np.sum(np.sin(x) * np.cos(x**2) * np.tan(0.15 * x) * np.exp(-0.03 * np.sum(x**3)))
        
        # Add a novel fractional-order chaotic component
        f11 = 0.02 * np.sum(np.sin(x**0.7) * np.cos(x**1.5) * np.exp(-0.04 * np.sum(np.abs(x)**0.7)))
        
        # Add a novel component with ultra-high frequency oscillations
        f12 = 0.04 * np.sum(np.sin(30.0 * x) * np.cos(25.0 * x) * np.exp(-0.008 * np.sum(x**2)))
        
        # Add a novel component with hyper-chaotic cross-dimension coupling
        f13 = 0.025 * np.sum(np.sin(x**2) * np.cos(x**3) * np.tan(0.2 * x) * np.exp(-0.03 * np.sum(x**4)))
        
        # Add a novel component with fractal-like conditioning
        f14 = 0.018 * np.sum(np.sin(0.1 * x) * np.cos(0.15 * x) * np.exp(-0.02 * np.sum(np.abs(x)**0.8)))
        
        # Add a novel component with multi-scale chaotic modulation
        f15 = 0.032 * np.sum(np.sin(15.0 * x) * np.cos(10.0 * x) * np.exp(-0.01 * np.sum(x**2)) * np.sin(0.05 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15
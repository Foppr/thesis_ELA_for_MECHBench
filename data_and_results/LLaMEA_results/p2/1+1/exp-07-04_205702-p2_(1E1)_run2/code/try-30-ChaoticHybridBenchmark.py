import numpy as np

class ChaoticHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial with intensified chaotic modulation
        f1 = np.sum(x**8 * (1.0 + 0.7 * np.sin(15.0 * x) * np.cos(8.0 * x)))
        
        # Exponential with multi-scale sinusoidal modulation and enhanced decay
        f2 = 0.0
        for i in range(self.dim):
            f2 -= np.exp(-0.05 * x[i]**2) * np.sin(8.0 * x[i]) * np.cos(6.0 * x[i]) * np.tan(0.6 * x[i])
        
        # Multi-modal Gaussian peaks with dynamic positioning, scaling, and enhanced interaction
        f3 = 0.0
        for i in range(self.dim):
            sigma = 0.7 + 0.3 * np.sin(1.2 * i) * np.cos(0.6 * i)
            mu = 2.0 * np.cos(0.7 * i) + 1.5 * np.sin(0.6 * i)
            f3 -= np.exp(-0.5 * ((x[i] - mu) / sigma)**5) * (1.0 + 0.5 * np.sin(11.0 * x[i]) * np.cos(7.0 * x[i]))
        
        # Cross-dimensional interaction with stronger chaotic coupling and higher-order terms
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                f4 += np.sin(x[i] * x[j]) * np.exp(-0.2 * (x[i] - x[j])**2) * np.cos(3.0 * x[i] + 1.5 * x[j]) * np.sin(0.5 * x[i] * x[j])
        
        # Asymmetric long-range coupling with enhanced chaotic phase and multi-scale modulation
        f5 = 0.0
        for i in range(self.dim):
            f5 += np.sin(0.3 * x[i]) * np.exp(-0.15 * np.sum(x**2)) * np.cos(4.0 * x[i] + np.sin(0.3 * i)) * np.sin(0.2 * i)
        
        # Adaptive conditioning with stronger chaotic weights and fractional exponents
        weights = np.array([1.0 + 0.4 * np.sin(0.5 * i + np.cos(0.2 * i)) * np.tan(0.1 * i) for i in range(self.dim)])
        f6 = np.sum(weights * np.abs(x)**4.0)
        
        # Chaotic sine-cosine interaction component with enhanced frequency
        f7 = 0.08 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)) * np.sin(0.5 * x) * np.cos(0.3 * x) * np.tan(0.2 * x))
        
        # Add a global chaotic attractor term with enhanced coupling
        f8 = 0.02 * np.sum(np.sin(2.5 * x) * np.cos(3.0 * x) * np.exp(-0.015 * np.sum(x**2)) * np.sin(0.1 * x))
        
        # Introduce a new component for better conditioning and fitness improvement with ultra-high frequency
        f9 = 0.02 * np.sum(np.sin(0.2 * x) * np.cos(0.3 * x) * np.exp(-0.07 * np.sum(x**2)) * np.tan(3.0 * x))
        
        # Add a novel hyper-chaotic component with higher dimensional coupling and complex interaction
        f10 = 0.03 * np.sum(np.sin(x) * np.cos(x**2) * np.tan(0.15 * x) * np.exp(-0.03 * np.sum(x**3)) * np.sin(0.2 * x**2))
        
        # Add a novel fractional-order chaotic component with enhanced nonlinearity
        f11 = 0.02 * np.sum(np.sin(x**0.7) * np.cos(x**1.6) * np.exp(-0.04 * np.sum(np.abs(x)**0.7)) * np.cos(0.1 * x))
        
        # Add a novel component with ultra-high frequency oscillations and complex modulation
        f12 = 0.04 * np.sum(np.sin(30.0 * x) * np.cos(25.0 * x) * np.exp(-0.008 * np.sum(x**2)) * np.sin(0.1 * x) * np.cos(0.05 * x))
        
        # Add a novel multi-scale chaotic component with enhanced ruggedness
        f13 = 0.015 * np.sum(np.sin(0.1 * x) * np.cos(0.15 * x) * np.tan(0.05 * x) * np.exp(-0.05 * np.sum(x**4)) * np.sin(2.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13
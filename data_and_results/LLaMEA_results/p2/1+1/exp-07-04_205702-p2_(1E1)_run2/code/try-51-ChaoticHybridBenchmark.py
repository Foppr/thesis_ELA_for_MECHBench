import numpy as np

class ChaoticHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial with chaotic modulation
        f1 = np.sum(x**8 * (1.0 + 0.7 * np.sin(15.0 * x) * np.cos(8.0 * x)))
        
        # Multi-scale exponential with ultra-high frequency sinusoidal modulation
        f2 = 0.0
        for i in range(self.dim):
            f2 -= np.exp(-0.05 * x[i]**2) * np.sin(12.0 * x[i]) * np.cos(8.0 * x[i]) * np.tan(0.6 * x[i]) * np.sin(20.0 * x[i])
        
        # Complex multi-modal Gaussian peaks with dynamic positioning, scaling, and chaotic phase shifts
        f3 = 0.0
        for i in range(self.dim):
            sigma = 0.8 + 0.3 * np.sin(1.2 * i + np.cos(0.7 * i))
            mu = 2.0 * np.cos(0.7 * i) + 1.8 * np.sin(0.6 * i) + 0.5 * np.sin(3.0 * i)
            f3 -= np.exp(-0.5 * ((x[i] - mu) / sigma)**6) * (1.0 + 0.6 * np.sin(12.0 * x[i]) * np.cos(9.0 * x[i]))
        
        # Enhanced cross-dimensional interaction with hyper-chaotic coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                f4 += np.sin(x[i] * x[j]) * np.exp(-0.2 * (x[i] - x[j])**2) * np.cos(3.0 * x[i] + 1.5 * x[j]) * np.sin(0.5 * x[i] * x[j])
        
        # Asymmetric long-range coupling with ultra-chaotic phase
        f5 = 0.0
        for i in range(self.dim):
            f5 += np.sin(0.3 * x[i]) * np.exp(-0.15 * np.sum(x**2)) * np.cos(4.0 * x[i] + np.sin(0.3 * i) * np.cos(0.2 * i))
        
        # Adaptive conditioning with hyper-chaotic weights
        weights = np.array([1.0 + 0.5 * np.sin(0.5 * i + np.cos(0.2 * i) * np.sin(0.1 * i)) for i in range(self.dim)])
        f6 = np.sum(weights * np.abs(x)**4.0)
        
        # Ultra-high frequency chaotic sine-cosine interaction component
        f7 = 0.08 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)) * np.sin(0.6 * x) * np.cos(0.3 * x) * np.sin(30.0 * x))
        
        # Enhanced global chaotic attractor term
        f8 = 0.02 * np.sum(np.sin(2.5 * x) * np.cos(3.0 * x) * np.exp(-0.015 * np.sum(x**2)) * np.sin(5.0 * x))
        
        # Novel hyper-chaotic component with higher dimensional coupling and fractional exponents
        f9 = 0.03 * np.sum(np.sin(x**0.7) * np.cos(x**1.7) * np.tan(0.15 * x) * np.exp(-0.03 * np.sum(x**2.5)))
        
        # Additional fractional-order chaotic component with ultra-high frequency
        f10 = 0.025 * np.sum(np.sin(x**0.5) * np.cos(x**1.5) * np.exp(-0.04 * np.sum(np.abs(x)**0.5)))
        
        # Ultra-high frequency oscillation component with multi-scale chaotic interaction
        f11 = 0.04 * np.sum(np.sin(30.0 * x) * np.cos(25.0 * x) * np.exp(-0.005 * np.sum(x**2)))
        
        # Enhanced multi-scale chaotic interaction with modified weights and phase shifts
        f12 = 0.015 * np.sum(np.sin(0.8 * x) * np.cos(0.6 * x) * np.tan(0.15 * x) * np.exp(-0.025 * np.sum(x**3)))
        
        # Additional high-frequency chaotic component with enhanced conditioning
        f13 = 0.025 * np.sum(np.sin(20.0 * x) * np.cos(18.0 * x) * np.tan(0.4 * x) * np.exp(-0.01 * np.sum(x**2)))
        
        # Multi-scale chaotic interaction with complex phase modulation
        f14 = 0.012 * np.sum(np.sin(0.4 * x) * np.cos(0.2 * x) * np.exp(-0.04 * np.sum(x**4)) * np.sin(10.0 * x))
        
        # Enhanced chaotic modulation for superior conditioning
        f15 = 0.015 * np.sum(np.sin(0.9 * x) * np.cos(1.1 * x) * np.exp(-0.015 * np.sum(np.abs(x)**3.0)))
        
        # Ultra-high frequency chaotic component with complex coupling
        f16 = 0.03 * np.sum(np.sin(25.0 * x) * np.cos(22.0 * x) * np.tan(0.35 * x) * np.exp(-0.007 * np.sum(x**2)))
        
        # Multi-scale chaotic interaction with modified weights and ultra-high frequency
        f17 = 0.008 * np.sum(np.sin(0.3 * x) * np.cos(0.15 * x) * np.exp(-0.035 * np.sum(x**4)) * np.sin(35.0 * x))
        
        # Additional complex chaotic component with fractional exponents and high frequency
        f18 = 0.02 * np.sum(np.sin(x**0.8) * np.cos(x**1.8) * np.exp(-0.03 * np.sum(np.abs(x)**0.8)) * np.sin(28.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18
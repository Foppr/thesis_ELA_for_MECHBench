import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with dynamic exponents
        f1 = np.sum((x**3.2 + 0.8 * x**2.5 + 0.3 * x**1.7) / self.dim)
        
        # Trigonometric modulation with chaotic frequency scaling
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 25.0 * (1.0 + 0.6 * np.sin(i * 0.8)) * (1.0 + 0.4 * np.cos(i * 0.5))
            f2 += np.sin(freq * xi) * np.cos(freq * xi**1.5) * np.exp(-0.15 * xi**2)
        
        # Exponential decay with sinusoidal perturbations
        f3 = 0.15 * np.sum(np.exp(-0.2 * np.abs(x)) * np.sin(8.0 * x) * np.cos(5.0 * x))
        
        # Fractional power interactions with dynamic coupling
        f4 = 0.1 * np.sum((np.abs(x)**2.3 + 0.6 * np.abs(x)**1.9 + 0.2 * np.abs(x)**1.3) / self.dim)
        
        # Cross-dimensional coupling with asymmetric interaction terms
        f5 = 0.08 * np.sum(np.sin(0.7 * x[:-1] + 1.2 * x[1:]) * np.cos(1.1 * x[:-1] - 0.9 * x[1:]))
        
        # Saddle point structure with multi-scale interference
        f6 = 0.2 * np.sum(np.sin(30.0 * np.sin(5.0 * x)) * np.cos(20.0 * np.cos(4.0 * x)))
        
        # Asymmetric polynomial corruption with varying coefficients
        f7 = 0.05 * np.sum((x**4.5 + 0.9 * x**3.8 + 0.6 * x**2.9 + 0.3 * x**1.8) / self.dim)
        
        # Gaussian-like noise with dynamic variance
        f8 = 0.12 * np.sum(np.exp(-0.5 * (x - 1.5)**2) * np.sin(15.0 * x))
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Sinusoidal waves with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 10.0 * (1.0 + 0.5 * np.sin(i * 0.7))
            amp = 1.5 * (1.0 + 0.3 * np.cos(i * 0.9))
            f2 += amp * np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Polynomial potential with mixed exponents
        f3 = 0.05 * np.sum((x**6.2 + 0.7 * x**5.8 + 0.4 * x**3.1 + 0.2 * x**2.3) / self.dim)
        
        # Gaussian noise component with spatial correlation
        f4 = 0.1 * np.sum(np.exp(-0.5 * (x - np.mean(x))**2) * np.sin(15.0 * x))
        
        # Saddle point structure with exponential scaling
        f5 = 0.2 * np.sum(np.exp(-0.2 * np.abs(x)) * np.sin(8.0 * x) * np.cos(5.0 * x))
        
        # Chaotic modulation using tent map-like behavior
        f6 = 0.15 * np.sum(np.sin(30.0 * np.abs(x) - 0.5 * np.sin(20.0 * x)) * np.cos(25.0 * x**2))
        
        # Asymmetric interactions between variables
        f7 = 0.08 * np.sum((x[:-1]**2.5 + 0.8 * x[1:]**3.2) * np.sin(x[:-1] + x[1:]))
        
        # Fractional Brownian motion-like roughness
        f8 = 0.12 * np.sum(np.abs(x)**1.7 * np.cos(18.0 * x))
        
        # Combine all components with adjusted weights for enhanced complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
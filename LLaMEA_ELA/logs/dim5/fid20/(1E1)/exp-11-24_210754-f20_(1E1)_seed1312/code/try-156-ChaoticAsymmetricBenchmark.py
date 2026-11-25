import numpy as np

class ChaoticAsymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay base with dimension scaling
        f1 = np.sum(np.exp(-0.5 * np.abs(x)) * (x**2) / self.dim)
        
        # Trigonometric interference with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 10.0 + 5.0 * np.sin(i * 0.7)
            amp = 1.5 + 0.5 * np.cos(i * 0.9)
            f2 += amp * np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Asymmetric polynomial potentials with mixed powers
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            if xi >= 0:
                f3 += 0.8 * xi**3.2 + 0.3 * xi**1.7
            else:
                f3 += 0.5 * xi**4.1 + 0.6 * xi**2.3
        
        # Cross-dimensional interaction terms with exponential coupling
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += np.exp(-0.1 * (x[i]**2 + x[i+1]**2)) * np.sin(5.0 * (x[i] - x[i+1]))
        
        # Saddle point structure with chaotic modulation
        f5 = 0.0
        for i in range(self.dim):
            xi = x[i]
            mod = np.sin(20.0 * xi) * np.cos(15.0 * xi)
            f5 += mod * np.exp(-0.3 * np.abs(xi))
        
        # Fractional power noise with chaotic scaling
        f6 = 0.05 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # Combined fitness with weighted components
        return f1 + 0.7 * f2 + 0.6 * f3 + 0.4 * f4 + 0.5 * f5 + f6
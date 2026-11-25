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
            amp = 1.0 + 0.3 * np.cos(i * 0.9)
            f2 += amp * np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Asymmetric polynomial potentials with mixed degrees
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            if xi >= 0:
                f3 += 0.5 * xi**4.2 + 0.3 * xi**2.7
            else:
                f3 += 0.8 * xi**3.9 + 0.4 * xi**1.8
        
        # Cross-dimensional interaction terms with exponential coupling
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += np.exp(-0.1 * (x[i]**2 + x[i+1]**2)) * np.sin(15.0 * (x[i] + x[i+1]))
        
        # Fractal-like recursive structure with diminishing amplitude
        f5 = 0.0
        for i in range(self.dim):
            xi = x[i]
            scale = 0.8**(i % 3)
            f5 += scale * np.sin(20.0 * xi) * np.cos(12.0 * xi**2.3)
        
        # Sharp gradient regions with asymmetric saddle points
        f6 = 0.0
        for i in range(self.dim):
            xi = x[i]
            f6 += (xi**5.1 + 0.7 * xi**3.4 - 0.3 * xi**1.9) * np.exp(-0.2 * np.abs(xi))
        
        # Combine all components with carefully tuned weights
        return f1 + 0.3 * f2 + 0.2 * f3 + 0.15 * f4 + 0.25 * f5 + 0.35 * f6
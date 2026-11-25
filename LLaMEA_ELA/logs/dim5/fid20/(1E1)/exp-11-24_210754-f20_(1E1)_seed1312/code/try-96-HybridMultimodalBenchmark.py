import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with varying degrees
        f1 = np.sum(0.1 * x**6 + 0.3 * x**4 + 0.5 * x**2) / self.dim
        
        # Trigonometric oscillations with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 10.0 + 5.0 * np.sin(i * 0.7)
            amp = 1.5 + 0.5 * np.cos(i * 0.9)
            f2 += amp * np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Exponential decay with sinusoidal modulation
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            f3 += np.exp(-0.5 * xi**2) * np.sin(8.0 * xi) * np.cos(4.0 * xi)
        
        # Asymmetric saddle points with different curvature
        f4 = 0.0
        for i in range(self.dim):
            xi = x[i]
            f4 += (xi**3 - 0.5 * xi**2 + 0.1 * xi) * np.exp(-0.1 * np.abs(xi))
        
        # Cross-dimensional interaction terms with non-uniform scaling
        f5 = 0.0
        for i in range(self.dim-1):
            f5 += (x[i]**2 + x[i+1]**2) * np.sin(3.0 * x[i] * x[i+1])
        
        # Fractional power components with varying exponents
        f6 = 0.0
        for i in range(self.dim):
            xi = x[i]
            exp = 1.3 + 0.4 * np.sin(i * 0.5)
            f6 += np.abs(xi)**exp
        
        # Combine all components with adaptive weights
        return 0.8 * f1 + 0.6 * f2 + 0.4 * f3 + 0.5 * f4 + 0.3 * f5 + 0.7 * f6
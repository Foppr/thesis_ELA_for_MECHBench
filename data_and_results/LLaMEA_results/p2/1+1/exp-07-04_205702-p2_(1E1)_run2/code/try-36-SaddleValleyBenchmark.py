import numpy as np

class SaddleValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with asymmetric conditioning
        f1 = np.sum(0.5 * x**4 + 0.3 * x**3 - 0.2 * x**2 + 0.1 * x)
        
        # Trigonometric saddle points with varying frequencies
        f2 = 0.0
        for i in range(self.dim):
            f2 -= np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Asymmetric valleys with dynamic scaling
        f3 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(0.5 * i)
            f3 += scale * (np.abs(x[i]) - 2.0)**2 * np.exp(-0.05 * (x[i] - 1.0)**2)
        
        # Exponential interaction terms with cross-dimensional coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f4 += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(0.5 * x[i] * x[j])
        
        # Dynamic conditioning with position-dependent weights
        f5 = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.3 * np.cos(0.2 * i + x[i])
            f5 += weight * np.sin(0.8 * x[i]) * np.cos(0.6 * x[i])
        
        # Embedded saddle point with hyperbolic tangent modulation
        f6 = 0.0
        for i in range(self.dim):
            f6 += np.tanh(x[i]) * np.exp(-0.02 * x[i]**2) * np.sin(1.5 * x[i])
        
        # Fractional power chaotic modulation
        f7 = 0.0
        for i in range(self.dim):
            f7 += np.abs(x[i])**1.7 * np.cos(0.3 * x[i]) * np.exp(-0.03 * np.abs(x[i]))
        
        # Cross-dimensional exponential coupling with sinusoidal modulation
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f8 += np.exp(-0.05 * (x[i]**2 + x[j]**2)) * np.sin(0.4 * x[i] + 0.6 * x[j])
        
        # Asymmetric Gaussian peaks with dynamic positioning
        f9 = 0.0
        for i in range(self.dim):
            mu = 2.0 * np.sin(0.3 * i)
            sigma = 0.8 + 0.2 * np.cos(0.2 * i)
            f9 -= np.exp(-0.5 * ((x[i] - mu) / sigma)**2) * np.cos(2.0 * x[i])
        
        # Global conditioning term with polynomial decay
        f10 = 0.01 * np.sum(x**2 * np.exp(-0.01 * np.sum(x**2)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
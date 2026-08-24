import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for fractal structure
        self.fractal_base = np.array([1.0 + 0.3 * np.sin(0.5 * i) for i in range(dim)])
        self.saddle_weights = np.array([0.5 + 0.5 * np.cos(0.7 * i) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with fractal scaling
        f1 = 0.5 * np.sum((x * self.fractal_base)**2)
        
        # Multi-modal component with asymmetric peaks
        f2 = 0.0
        for i in range(self.dim):
            # Asymmetric Gaussian peaks
            mu = 2.0 * np.sin(0.3 * i) + 1.5 * np.cos(0.4 * i)
            sigma = 0.8 + 0.3 * np.sin(0.6 * i)
            f2 -= np.exp(-0.5 * ((x[i] - mu) / sigma)**2) * (1.0 + 0.3 * np.sin(5.0 * x[i]))
        
        # Saddle point structure with directional correlation
        f3 = 0.0
        for i in range(self.dim):
            # Saddle point in each dimension
            f3 += self.saddle_weights[i] * x[i] * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
        
        # Fractal-like interaction terms
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Fractal coupling with varying strength
                strength = 0.3 * np.sin(0.2 * (i + j)) + 0.4
                f4 += strength * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # High-frequency oscillation component
        f5 = 0.0
        for i in range(self.dim):
            f5 -= 0.2 * np.sin(10.0 * x[i]) * np.cos(8.0 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Asymmetric conditioning with exponential weights
        f6 = 0.0
        for i in range(self.dim):
            weight = np.exp(0.1 * np.sin(0.4 * i) * x[i]**2)
            f6 += weight * np.abs(x[i])**1.7
        
        # Cross-dimensional fractal coupling with non-linear interaction
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                f7 += np.sin(x[i] * np.cos(x[j])) * np.exp(-0.08 * (x[i] - x[j])**2)
        
        # Add a global multi-scale fractal term
        f8 = 0.05 * np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) * np.exp(-0.02 * np.sum(x**2)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
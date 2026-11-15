import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quadratic base with adaptive scaling
        f1 = 0.5 * np.sum(x_norm**2)
        
        # Radial basis function components with varying widths
        centers = np.linspace(-1, 1, min(5, self.dim))
        widths = np.logspace(-1, 1, min(5, self.dim))
        rbf = 0.0
        for i in range(min(5, self.dim)):
            rbf += np.exp(-np.sum((x_norm - centers[i])**2) / (2 * widths[i]**2))
        f2 = 2.0 * rbf
        
        # Multi-modal trigonometric components
        f3 = 0.0
        for i in range(self.dim):
            f3 += np.sin(10 * x_norm[i]) * np.cos(7 * x_norm[i])
        f3 *= 0.3
        
        # Adaptive dimensionality coupling
        f4 = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                f4 += (x_norm[i] - x_norm[i+1])**2 * np.sin(x_norm[i] * x_norm[i+1])
        f4 *= 0.2
        
        # Asymmetric penalty terms
        f5 = 0.0
        for i in range(self.dim):
            if x_norm[i] > 0:
                f5 += x_norm[i]**3 * np.exp(-x_norm[i]**2)
            else:
                f5 += x_norm[i]**4 * np.exp(-x_norm[i]**2)
        f5 *= 0.15
        
        # High-frequency oscillation with amplitude modulation
        f6 = 0.0
        for i in range(self.dim):
            f6 += np.sin(20 * x_norm[i]) * np.cos(15 * x_norm[i]) * np.exp(-0.1 * np.abs(x_norm[i]))
        f6 *= 0.25
        
        # Cross-dimensional polynomial interactions
        f7 = 0.0
        if self.dim > 2:
            for i in range(self.dim - 2):
                f7 += x_norm[i] * x_norm[i+1] * x_norm[i+2] * np.sin(x_norm[i] + x_norm[i+1])
        f7 *= 0.1
        
        # Fractional dimensionality effect
        f8 = 0.0
        for i in range(self.dim):
            f8 += np.abs(x_norm[i])**(1.5 + 0.5 * np.sin(i * 0.5))
        f8 *= 0.2
        
        # Combined result
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
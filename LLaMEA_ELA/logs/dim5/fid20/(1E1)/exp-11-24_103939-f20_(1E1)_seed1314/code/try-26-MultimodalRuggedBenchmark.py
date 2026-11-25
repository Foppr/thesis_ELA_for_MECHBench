import numpy as np

class MultimodalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with multiple local minima
        f1 = np.sum((x_scaled**4 - 2 * x_scaled**2 + 0.5)**2)
        
        # Trigonometric interference creating complex ridges and valleys
        f2 = 0.5 * np.sum(np.sin(10 * x_scaled) * np.cos(8 * x_scaled) * 
                         np.sin(6 * x_scaled) * np.cos(4 * x_scaled))
        
        # Radial basis function mixture with varying centers and widths
        centers = np.linspace(-0.8, 0.8, 5)
        widths = np.logspace(-2, 1, 5)
        f3 = 0.0
        for i in range(5):
            f3 += np.exp(-widths[i] * np.sum((x_scaled - centers[i])**2))
        
        # Cross-dimensional coupling creating interaction between variables
        f4 = 0.3 * np.sum(np.sin(x_scaled[:-1] + x_scaled[1:]) * 
                         np.cos(x_scaled[:-1] - x_scaled[1:]))
        
        # Asymmetric saddle points with varying curvature
        f5 = 0.25 * np.sum((x_scaled**3 - 0.3 * x_scaled)**2)
        
        # Logarithmic barrier to prevent boundary escape
        f6 = 0.4 * np.sum(np.log(1 + 0.2 * np.abs(x_scaled)))
        
        # Fractional power modulation creating scale-invariant features
        f7 = 0.3 * np.sum(np.abs(x_scaled)**1.5 * np.sin(20 * x_scaled)**2)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7
import numpy as np

class FractalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similarity using iterative polynomial transformations
        f1 = np.sum(np.sin(2.0 * x) * np.cos(0.5 * x) * np.exp(-0.1 * x**2))
        
        # Gaussian radial basis functions with variable widths and centers
        centers = np.linspace(-5, 5, self.dim // 2 + 1)
        widths = np.logspace(-1, 1, len(centers))
        f2 = 0.0
        for i in range(len(centers)):
            f2 += np.sum(widths[i] * np.exp(-0.5 * ((x - centers[i]) / (widths[i] * 2))**2))
        
        # Quaternion-inspired coupling terms for increased non-separability
        f3 = 0.0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                f3 += (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
        
        # Nested multimodal structure with varying scales and orientations
        f4 = 0.5 * np.sum(np.sin(10.0 * x) + np.cos(5.0 * x) + np.tan(0.5 * x))
        
        # Complex fitness landscape with multiple interacting peaks and valleys
        f5 = 0.3 * np.sum((x**4 - 2.0 * x**2 + 1) * np.exp(-0.1 * x**2))
        
        # Cross-term interactions that create complex, irregular gradients
        f6 = 0.2 * np.sum(np.sin(x[:-1] * x[1:]) * np.cos(0.5 * (x[:-1]**2 + x[1:]**2)))
        
        return f1 + f2 + f3 + f4 + f5 + f6
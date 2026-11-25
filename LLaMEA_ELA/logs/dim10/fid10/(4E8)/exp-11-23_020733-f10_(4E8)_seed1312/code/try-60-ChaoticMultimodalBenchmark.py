import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with modified weight
        result = 1.5 * np.sum(x**2)
        
        # Enhanced chaotic logistic map components with higher sensitivity
        for i in range(self.dim):
            r = 3.95 + 0.3 * np.sin(i * 1.7)
            x_log = 0.5
            for _ in range(15):
                x_log = r * x_log * (1 - x_log)
            result += 0.4 * x_log * np.sin(x[i])**3
        
        # Increased radial basis function terms with overlapping centers and varying widths
        centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i in range(min(7, self.dim)):
            dist = np.sum((x - centers[i])**2)
            result += 0.3 * np.exp(-dist / (2 * 0.4**2)) * np.cos(4 * dist) * np.sin(2 * dist)
        
        # More complex asymmetric saddle points with higher-order polynomial terms
        for i in range(self.dim):
            result += 0.18 * x[i]**3 + 0.09 * x[i]**5 + 0.04 * np.sin(9 * x[i]) * np.cos(5 * x[i]) + 0.02 * x[i]**7
        
        # Stronger cross-dimensional interaction with trigonometric coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.abs(x[i] - x[j]) * np.exp(-0.3 * (x[i] + x[j])**2)
                result += 0.2 * interaction * np.sin(3 * x[i] * x[j]) * np.cos(x[i] * x[j])
        
        # Enhanced irregular noise with multiple frequency components and fractal characteristics
        noise = 0.08 * np.sum(np.sin(17 * x) + np.cos(11 * x) + np.tan(7 * x) + np.sin(13 * x**2))
        result += noise
        
        # Additional global scaling factor with non-linear transformation
        result *= 1.3
        
        return result
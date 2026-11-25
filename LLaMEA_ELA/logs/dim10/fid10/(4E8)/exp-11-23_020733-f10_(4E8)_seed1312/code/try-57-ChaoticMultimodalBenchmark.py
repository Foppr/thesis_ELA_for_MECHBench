import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced chaotic logistic map components with stronger nonlinearity
        for i in range(self.dim):
            r = 3.9 + 0.3 * np.sin(i * 1.7) + 0.1 * np.cos(i * 2.3)
            x_log = 0.5
            for _ in range(15):
                x_log = r * x_log * (1 - x_log)
            result += 0.3 * x_log * np.sin(x[i])**3 + 0.15 * np.cos(x[i])**2
        
        # Enhanced radial basis function terms with adaptive centers and widths
        centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i in range(min(7, self.dim)):
            dist = np.sum((x - centers[i])**2)
            result += 0.3 * np.exp(-dist / (2 * 0.4**2)) * np.cos(4 * dist) + 0.1 * np.sin(2 * dist)
        
        # Modified asymmetric saddle points with higher-order polynomial terms
        for i in range(self.dim):
            result += 0.15 * x[i]**3 + 0.08 * x[i]**5 + 0.04 * x[i]**7 + 0.02 * np.sin(9 * x[i]) * np.cos(5 * x[i])
        
        # Increased cross-dimensional interaction with higher-order coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i] - x[j])**2 * np.exp(-0.3 * (x[i] + x[j])**2)
                result += 0.15 * interaction * np.sin(3 * x[i] * x[j]) + 0.05 * np.cos(2 * x[i]**2 + x[j]**2)
        
        # Additional fractal noise with multiple frequency components
        noise = 0.06 * np.sum(np.sin(17 * x) + np.cos(11 * x) + np.tan(7 * x) + np.sin(13 * x**2))
        result += noise
        
        # Global scaling factor with dynamic adjustment based on dimensionality
        result *= (1.2 + 0.05 * np.log(self.dim))
        
        return result
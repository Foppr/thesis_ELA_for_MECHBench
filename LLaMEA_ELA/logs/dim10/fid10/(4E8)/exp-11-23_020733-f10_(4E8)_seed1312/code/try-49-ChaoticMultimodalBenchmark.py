import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add chaotic logistic map components with modified r values
        for i in range(self.dim):
            # Logistic map with varying r values
            r = 3.8 + 0.2 * np.sin(i)
            x_log = 0.5
            for _ in range(10):
                x_log = r * x_log * (1 - x_log)
            result += 0.25 * x_log * np.sin(x[i])**2
        
        # Radial basis function terms with varying centers and widths
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(min(5, self.dim)):
            dist = np.sum((x - centers[i])**2)
            result += 0.2 * np.exp(-dist / (2 * 0.6**2)) * np.cos(3 * dist)
        
        # Asymmetric saddle points with varying steepness
        for i in range(self.dim):
            result += 0.12 * x[i]**3 + 0.06 * x[i]**5 + 0.03 * np.sin(7 * x[i]) * np.cos(4 * x[i])
        
        # Cross-dimensional interaction with non-linear coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.abs(x[i] - x[j]) * np.exp(-0.5 * (x[i] + x[j])**2)
                result += 0.1 * interaction * np.sin(2 * x[i] * x[j])
        
        # Add irregular noise with fractal-like characteristics
        noise = 0.04 * np.sum(np.sin(13 * x) + np.cos(9 * x) + np.tan(5 * x))
        result += noise
        
        # Introduce a global scaling factor to control difficulty
        result *= 1.15
        
        return result
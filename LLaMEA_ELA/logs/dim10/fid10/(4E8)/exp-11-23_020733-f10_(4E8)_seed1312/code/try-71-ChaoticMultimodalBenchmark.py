import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add chaotic logistic map components with modified r values and enhanced sensitivity
        for i in range(self.dim):
            # Logistic map with varying r values and increased chaos
            r = 3.8 + 0.2 * np.sin(i * 1.5)
            x_log = 0.5
            for _ in range(20):  # More iterations for higher chaos
                x_log = r * x_log * (1 - x_log)
            result += 0.35 * x_log * np.sin(x[i])**4  # Quartic sine for sharper minima
        
        # Radial basis function terms with varying centers, widths, and enhanced interaction
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        for i in range(min(5, self.dim)):
            dist = np.sum((x - centers[i])**2)
            result += 0.3 * np.exp(-dist / (2 * 0.6**2)) * np.cos(3 * dist) * np.sin(0.4 * dist)
        
        # Asymmetric saddle points with modified steepness and added trigonometric modulation
        for i in range(self.dim):
            result += 0.18 * x[i]**3 + 0.1 * x[i]**5 + 0.05 * np.sin(9 * x[i]) * np.cos(4 * x[i])
        
        # Cross-dimensional interaction with non-linear coupling and enhanced complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.abs(x[i] - x[j]) * np.exp(-0.25 * (x[i] + x[j])**2)
                result += 0.2 * interaction * np.sin(4 * x[i] * x[j]) * np.cos(3 * x[i] + x[j])
        
        # Add irregular noise with fractal-like characteristics and increased frequency
        noise = 0.08 * np.sum(np.sin(19 * x) + np.cos(13 * x) + np.tan(6 * x))
        result += noise
        
        # Introduce a global scaling factor to control difficulty
        result *= 1.15
        
        return result
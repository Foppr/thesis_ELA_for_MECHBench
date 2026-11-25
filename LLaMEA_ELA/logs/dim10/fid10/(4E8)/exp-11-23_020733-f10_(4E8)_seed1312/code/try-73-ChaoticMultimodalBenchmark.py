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
            r = 3.9 + 0.1 * np.sin(i * 1.3)
            x_log = 0.5
            for _ in range(15):
                x_log = r * x_log * (1 - x_log)
            result += 0.4 * x_log * np.sin(x[i])**2
        
        # Radial basis function terms with varying centers and widths
        centers = np.linspace(-4, 4, min(7, self.dim))
        for i in range(min(7, self.dim)):
            dist = np.sum((x - centers[i])**2)
            result += 0.3 * np.exp(-dist / (2 * 0.3**2)) * np.cos(4.0 * dist)
        
        # Asymmetric saddle points with varying steepness
        for i in range(self.dim):
            result += 0.2 * x[i]**3 + 0.12 * x[i]**5 + 0.06 * np.sin(8 * x[i]) * np.cos(5 * x[i])
        
        # Cross-dimensional interaction with non-linear coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.abs(x[i] - x[j]) * np.exp(-0.3 * (x[i] + x[j])**2)
                result += 0.15 * interaction * np.sin(3.0 * x[i] * x[j])
        
        # Add irregular noise with fractal-like characteristics
        noise = 0.08 * np.sum(np.sin(16 * x) + np.cos(12 * x) + np.tan(8 * x))
        result += noise
        
        # Introduce a global scaling factor to control difficulty
        result *= 1.3
        
        # Add boundary penalty mechanism
        penalty = 0.0
        for i in range(self.dim):
            if x[i] < -4.5 or x[i] > 4.5:
                penalty += 2.0 * (np.abs(x[i]) - 4.5)**2
        result += penalty
        
        return result
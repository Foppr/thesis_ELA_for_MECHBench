import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced chaotic logistic map components with time-varying parameters
        for i in range(self.dim):
            # Logistic map with dynamic r values based on position
            r = 3.8 + 0.3 * np.sin(x[i] * 0.5)
            x_log = 0.5
            for _ in range(15):
                x_log = r * x_log * (1 - x_log)
            result += 0.25 * x_log * np.sin(x[i])**3
        
        # Modified radial basis function terms with adaptive centers and widths
        centers = np.linspace(-4.5, 4.5, min(6, self.dim))
        for i in range(min(6, self.dim)):
            dist = np.sum((x - centers[i])**2)
            result += 0.2 * np.exp(-dist / (2 * 0.3**2)) * np.cos(4 * dist) * np.sin(0.5 * dist)
        
        # Enhanced asymmetric saddle points with higher-order polynomial terms
        for i in range(self.dim):
            result += 0.12 * x[i]**3 + 0.08 * x[i]**5 + 0.03 * np.sin(8 * x[i]) * np.cos(5 * x[i])
        
        # Improved cross-dimensional interaction with nonlinear coupling and phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.abs(x[i] - x[j]) * np.exp(-0.3 * (x[i]**2 + x[j]**2))
                result += 0.1 * interaction * np.sin(3 * x[i] * x[j] + 0.5 * (i - j))
        
        # Enhanced irregular noise with fractal characteristics and multi-scale components
        noise = 0.04 * np.sum(np.sin(15 * x) + np.cos(11 * x) + np.tan(7 * x) + 0.5 * np.sin(23 * x))
        result += noise
        
        # Add a global scaling factor with adaptive difficulty
        result *= 1.2
        
        return result
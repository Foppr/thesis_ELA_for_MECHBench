import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with varying coefficients
        result = 0.5 * np.sum(x**2)
        
        # Add chaotic gradient components with exponential growth
        for i in range(self.dim):
            result += 0.3 * np.sin(2 ** (i+1) * x[i]) * np.cos(3 ** (i+1) * x[i])
            
        # Introduce saddle points via hyperbolic tangent interactions
        for i in range(self.dim):
            result += 0.1 * np.tanh(5 * x[i]) * np.sin(7 * x[i])
            
        # Add non-separable polynomial terms with varying degrees
        poly_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_sum += (x[i] - x[j])**4 + 0.5 * (x[i] + x[j])**3
        result += 0.05 * poly_sum
        
        # Include varying curvature via sinusoidal modulation of quadratic terms
        for i in range(self.dim):
            result += 0.2 * np.sin(10 * x[i]) * x[i]**2
            
        # Add chaotic cross-dimensional interactions with sigmoidal scaling
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) / (1 + np.exp(-x[i] - x[j]))
        result += 0.1 * cross_term
        
        # Introduce a complex landscape with multiple local minima using a sum of Gaussians
        gaussian_sum = 0
        centers = np.linspace(-4, 4, 7)
        for c in centers:
            gaussian_sum += np.exp(-0.5 * np.sum((x - c)**2))
        result += 0.15 * gaussian_sum
        
        return result
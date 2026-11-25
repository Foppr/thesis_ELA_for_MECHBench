import numpy as np

class HybridMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.weights = np.random.normal(0, 1, 15)
        
    def f(self, x):
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(15):
            dist_sq = np.sum((x - self.centers[i]) ** 2)
            rbf_sum += self.weights[i] * np.exp(-dist_sq / (2 * 0.5**2))
        
        # Polynomial chaos expansion component with mixed terms
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += x[i]**4 - 6*x[i]**2 + 12
        
        # Cross-dimensional polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_sum += 0.3 * x[i]**2 * x[j]**3
        
        # Add a global conditioning term that varies with dimensionality
        condition_term = np.sum(x**2) * (1 + 0.1 * self.dim)
        
        # Introduce implicit constraints via trigonometric penalties
        constraint_penalty = 0.0
        for i in range(self.dim):
            constraint_penalty += np.sin(3 * x[i]) * np.cos(5 * x[i])
        
        # Combine all components with dynamic scaling
        result = rbf_sum + 0.5 * poly_sum + 0.1 * condition_term + 0.2 * constraint_penalty
        
        return result
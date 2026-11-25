import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic central basin
        quadratic_term = np.sum(x_normalized**2)
        
        # Highly oscillatory component with exponential growth
        oscillatory_term = 0.0
        for i in range(self.dim):
            oscillatory_term += np.sin(10 * np.pi * x_normalized[i] ** 3) ** 2 * np.exp(2 * abs(x_normalized[i]))
        
        # Polynomial penalty with varying exponents
        polynomial_penalty = 0.0
        for i in range(self.dim):
            polynomial_penalty += (x_normalized[i] ** 4 + 0.5 * x_normalized[i] ** 3 + 0.1) ** 2
        
        # Cross-dimensional interaction term
        cross_term = np.prod(np.abs(x_normalized) + 0.1)
        
        # Combine all terms with adaptive weights based on dimensionality
        weight1 = 1.0 + 0.1 * self.dim
        weight2 = 2.0 + 0.05 * self.dim
        weight3 = 0.5 + 0.02 * self.dim
        
        return weight1 * quadratic_term + weight2 * oscillatory_term + weight3 * polynomial_penalty + cross_term
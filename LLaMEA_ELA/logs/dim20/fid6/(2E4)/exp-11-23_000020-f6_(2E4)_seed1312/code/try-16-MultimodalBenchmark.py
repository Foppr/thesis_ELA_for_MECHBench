import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base polynomial chaos term with varying exponents
        result = np.sum(x_norm**4) + 0.5 * np.sum(x_norm**6)
        
        # Radial basis function components with multiple centers
        rbfs = []
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(min(5, self.dim)):
            center = np.full(self.dim, centers[i])
            rbf = np.exp(-5 * np.sum((x_norm - center)**2))
            rbfs.append(rbf)
        
        result += 0.3 * np.sum(rbfs)
        
        # Skew-symmetric interaction terms creating asymmetric landscape
        skew_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                skew_interaction += (x_norm[i]**3) * (x_norm[j]**2) * np.sin(x_norm[i] + x_norm[j])
        
        result += 0.25 * skew_interaction
        
        # High-dimensional coupling through nested trigonometric products
        product_term = 1.0
        for i in range(self.dim):
            product_term *= np.cos(3 * x_norm[i]) + 0.5 * np.sin(7 * x_norm[i])
        
        result += 0.4 * (product_term - 1.0)
        
        # Add a complex penalty term with exponential decay
        penalty = 0
        for i in range(self.dim):
            penalty += np.exp(-2 * np.abs(x_norm[i])) * np.sin(5 * x_norm[i])**2
        
        result += 0.15 * penalty
        
        # Add cubic polynomial interactions for enhanced multimodality
        cubic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_interaction += x_norm[i]**3 * x_norm[j]**3 * np.cos(x_norm[i] - x_norm[j])
        
        result += 0.2 * cubic_interaction
        
        return result
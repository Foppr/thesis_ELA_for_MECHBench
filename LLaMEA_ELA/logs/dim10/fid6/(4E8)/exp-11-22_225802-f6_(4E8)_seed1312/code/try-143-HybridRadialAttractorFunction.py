import numpy as np

class HybridRadialAttractorFunction:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis centers in [-5, 5]^dim
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (15, dim))
        
    def f(self, x):
        # Radial basis component with multiple local minima
        rb_result = 0.0
        for i in range(self.centers.shape[0]):
            center = self.centers[i]
            distance = np.sum((x - center)**2)
            # Use different widths for each RBF
            width = 0.5 + 0.5 * np.random.rand()
            rb_result += np.exp(-distance / (2 * width**2))
        
        # Gradient attraction fields creating valleys and ridges
        grad_result = 0.0
        for i in range(self.dim):
            # Create periodic gradient components
            grad_result += 0.3 * np.sin(2 * x[i]) * np.cos(3 * x[i])
            grad_result += 0.2 * np.sin(5 * x[i]) * np.cos(7 * x[i])
            
        # Add cross-dimensional coupling with polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling to avoid overcomplexity
                coupling += 0.1 * (x[i]**2 + x[j]**2) * np.sin(3 * (x[i] - x[j]))
        
        # Add a global shaping term with cubic and quartic components
        shape_term = 0.05 * np.sum(x**3) + 0.03 * np.sum(x**4)
        
        # Combine all components with appropriate weights
        result = 2.0 * rb_result + 1.5 * grad_result + 0.8 * coupling + 0.6 * shape_term
        
        # Add small noise to break symmetry and increase challenge
        noise = 0.001 * np.random.rand()
        
        return result + noise
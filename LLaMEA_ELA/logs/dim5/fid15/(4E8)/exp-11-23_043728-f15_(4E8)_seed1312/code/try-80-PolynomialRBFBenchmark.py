import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for polynomial chaos and RBF components
        self.poly_degree = 4
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        self.weights = np.random.normal(0, 1, 10)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Polynomial chaos component with mixed monomials
        poly_term = 0.0
        for i in range(1, self.poly_degree + 1):
            for j in range(self.dim):
                poly_term += (x_norm[j] ** i) * np.sin(i * np.pi * x_norm[j])
        
        # Radial basis function component with multiple centers
        rbf_sum = 0.0
        for i in range(len(self.rbf_centers)):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            weight = self.weights[i]
            distance = np.sum((x_norm - center) ** 2)
            rbf_sum += weight * np.exp(-distance / (2 * width ** 2))
        
        # Add coupling terms between dimensions
        coupling_term = 0.0
        for i in range(self.dim - 1):
            coupling_term += 0.3 * (x_norm[i] ** 2) * (x_norm[i + 1] ** 3) * np.cos(2 * np.pi * x_norm[i])
        
        # Create multi-scale structure with sinusoidal modulation
        scale_modulation = 0.0
        for i in range(self.dim):
            scale_modulation += np.sin(5 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
        
        # Combine all components with adaptive weighting based on dimensionality
        adaptive_weight = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Add noise and ensure bounded fitness values
        noise = 0.01 * np.random.randn()
        
        # Final fitness value with penalty for large values
        result = adaptive_weight * (poly_term + rbf_sum + coupling_term + scale_modulation) + noise
        
        # Apply boundedness constraint to prevent extreme values
        result = np.clip(result, -100, 100)
        
        return result
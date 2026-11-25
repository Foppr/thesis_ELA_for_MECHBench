import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random weights and centers for RBF components
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-1, 1, (10, dim))
        self.rbf_weights = np.random.uniform(-2, 2, 10)
        self.poly_coeffs = np.random.uniform(-0.5, 0.5, dim * 3)
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial chaos expansion component (sparse grid approximation)
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(3):
                poly_term += self.poly_coeffs[i * 3 + j] * (x_scaled[i] ** (j + 1))
        
        # Radial Basis Function network component
        rbf_term = 0.0
        for i in range(10):
            center = self.rbf_centers[i]
            distance = np.sum((x_scaled - center) ** 2)
            # Gaussian RBF with varying width
            width = 0.5 + 0.3 * np.sin(i)
            rbf_term += self.rbf_weights[i] * np.exp(-distance / (2 * width ** 2))
        
        # Add coupling terms between dimensions for interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling += 0.3 * np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * (i + j)
        
        # Create multimodal structure with sinusoidal modulation
        modal_term = 0.0
        for i in range(self.dim):
            modal_term += np.sin(2 * np.pi * x_scaled[i]) * np.cos(3 * np.pi * x_scaled[i])
            
        # Combine all components with adaptive weights
        return 1.5 * poly_term + 2.0 * rbf_term + 0.8 * coupling + 1.2 * modal_term
import numpy as np

class ExponentialRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random global minima positions
        np.random.seed(42)  # For reproducibility
        self.global_minima = np.random.uniform(-5.0, 5.0, (9, dim))  # 9 global minima
        # Precompute radial basis function weights
        self.weights = np.random.exponential(1.0, 9)
    
    def f(self, x):
        # Ensure x is a numpy array
        if not isinstance(x, np.ndarray):
            x = np.array(x)
        
        # Calculate distances to all global minima
        distances = np.linalg.norm(self.global_minima - x, axis=1)
        
        # Compute exponential radial basis function values
        rbf_values = self.weights * np.exp(-distances**2 / (2 * 0.5**2))
        
        # Sum the RBF values to get the function value
        func_value = np.sum(rbf_values)
        
        # Add a quadratic penalty term that increases near the boundary
        boundary_penalty = 0.1 * np.sum(np.maximum(0, np.abs(x) - 4.5)**2)
        
        return func_value + boundary_penalty
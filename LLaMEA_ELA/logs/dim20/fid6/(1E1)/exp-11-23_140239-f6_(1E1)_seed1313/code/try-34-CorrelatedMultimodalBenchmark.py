import numpy as np

class CorrelatedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute correlation matrix
        self.correlation_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                self.correlation_matrix[i, j] = np.exp(-0.5 * (i - j)**2 / (0.1 * dim))
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Transform using correlation matrix
        transformed_x = self.correlation_matrix @ x
        
        # Base multimodal function with correlated dimensions
        result = 0.0
        
        # Add multiple Gaussian peaks with varying positions and scales
        peak_positions = np.linspace(-4, 4, min(5, self.dim))
        for i, pos in enumerate(peak_positions):
            if i < len(x):
                # Multimodal term with exponential decay
                result += np.exp(-0.5 * (x[i] - pos)**2 / (0.5 * (i + 1))) * np.cos(2 * np.pi * x[i] / (i + 1))
        
        # Add interaction terms based on correlation matrix
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i < len(x) and j < len(x):
                    corr = self.correlation_matrix[i, j]
                    result += 0.3 * corr * (x[i] - x[j])**2
        
        # Add higher-order polynomial for increased complexity
        result += 0.1 * np.sum(transformed_x**4)
        
        # Add noise component
        noise = 0.05 * np.sum(np.sin(5 * x) * np.cos(3 * x))
        
        return result + noise
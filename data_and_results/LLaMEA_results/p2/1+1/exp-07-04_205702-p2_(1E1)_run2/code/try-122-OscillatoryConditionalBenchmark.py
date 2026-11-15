import numpy as np

class OscillatoryConditionalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random correlation matrix and eigenvalues for conditioning
        np.random.seed(42)
        self.correlation_matrix = np.random.rand(dim, dim)
        self.correlation_matrix = np.dot(self.correlation_matrix, self.correlation_matrix.T)
        np.fill_diagonal(self.correlation_matrix, 1.0)
        self.eigenvals = np.random.rand(dim) * 10 + 1.0
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply linear transformation based on correlation and conditioning
        x_transformed = np.linalg.cholesky(self.correlation_matrix).T @ x
        
        # Base quadratic term with dynamic conditioning
        f1 = 0.5 * np.sum(x_transformed**2 * self.eigenvals)
        
        # Add periodic oscillations with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            f2 += np.sin(2.0 * np.pi * x[i] / 3.0) * np.cos(1.5 * np.pi * x[i] / 2.0)
        
        # Introduce multi-modal structure with Gaussian peaks and periodic modulation
        f3 = 0.0
        for i in range(4):
            mu = np.array([2.0 * np.sin(0.5 * i), 3.0 * np.cos(0.3 * i)] + [0.0] * (self.dim - 2))[:self.dim]
            sigma = 0.5 + 0.3 * np.sin(0.7 * i)
            height = 1.0 + 1.5 * np.cos(0.4 * i)
            gaussian = height * np.exp(-0.5 * np.sum(((x - mu) / sigma)**2))
            periodic = np.sin(2.0 * np.pi * np.sum(x - mu)) * np.cos(1.5 * np.pi * np.sum(x - mu))
            f3 += gaussian * periodic
        
        # Add cross-term interactions with dynamic weights
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = 0.5 + 0.5 * np.sin(0.3 * (i + j))
                f4 += weight * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Introduce asymmetric basin with exponential and trigonometric components
        f5 = 0.0
        for i in range(self.dim):
            f5 -= np.exp(-0.2 * (x[i] - 2.0)**2) * np.sin(1.2 * x[i])
        
        # Add noise to increase robustness
        noise = 0.02 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + noise
import numpy as np

class MultimodalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with multiple centers
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        if self.dim > 1:
            centers = np.random.uniform(-4.0, 4.0, (self.dim, 5))
        else:
            centers = np.array([[-4.0], [-2.0], [0.0], [2.0], [4.0]])
            
        rbf_term = 0.0
        for i in range(5):
            center = centers[:, i] if self.dim > 1 else np.array([centers[i]])
            rbf_term += np.exp(-np.sum((x - center)**2) / (2.0 * (0.5 + 0.5 * np.sin(i + self.dim * 0.3))))
        
        # Sinusoidal oscillation component with varying frequencies
        sin_term = np.sum(np.sin(2.0 * np.pi * x * (1.0 + 0.2 * np.sin(self.dim))) * 
                         np.cos(3.0 * np.pi * x * (1.0 + 0.1 * np.cos(self.dim))) * 
                         np.sin(5.0 * x * (1.0 + 0.15 * np.sin(self.dim)))) / self.dim
        
        # Adaptive conditioning component
        conditioning = np.array([1.0 + 0.5 * np.sin(i + self.dim * 0.4) for i in range(self.dim)])
        cond_term = np.sum(conditioning * x**2 + 0.3 * np.sin(conditioning * x)) / self.dim
        
        # Cross-dimensional interaction term
        cross_term = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                cross_term += (x[i]**2 + x[i+1]**2) * np.sin(np.pi * (x[i] - x[i+1])**2)
        cross_term /= (self.dim - 1)
        
        # Add noise component
        noise = 0.01 * np.random.rand()
        
        # Combine terms with dynamic weights
        weights = [0.4 + 0.1 * np.sin(self.dim), 
                  0.3 + 0.05 * np.cos(self.dim), 
                  0.2 + 0.08 * np.sin(self.dim * 0.5), 
                  0.1 + 0.03 * np.cos(self.dim * 0.7)]
        
        result = weights[0] * rbf_term + weights[1] * sin_term + weights[2] * cond_term + weights[3] * cross_term
        
        return result + noise
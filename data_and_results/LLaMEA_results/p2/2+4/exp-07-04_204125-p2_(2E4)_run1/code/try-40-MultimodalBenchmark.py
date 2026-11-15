import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for radial basis functions
        self.centers = np.random.uniform(-4.0, 4.0, (10, dim))
        self.weights = np.random.uniform(0.5, 2.0, 10)
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic global component
        quadratic = 0.1 * np.sum(x**2)
        
        # Trigonometric modulations
        trig = np.sum(np.sin(0.5 * x) + 0.5 * np.cos(1.5 * x))
        
        # Radial basis function components
        rbf = 0.0
        for i in range(10):
            dist = np.sum((x - self.centers[i])**2)
            rbf += self.weights[i] * np.exp(-0.1 * dist)
        
        # Add interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.05 * np.sin(2.0 * (x[i] + x[j])) * np.cos(0.5 * (x[i] - x[j]))
        
        # Add a tunable complexity factor based on dimensionality
        complexity = 1.0 + 0.05 * self.dim
        
        return complexity * (quadratic + trig + rbf + interaction)
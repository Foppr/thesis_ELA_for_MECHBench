import numpy as np

class ChaoticRadialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for logistic map
        self.logistic_r = np.random.uniform(3.57, 4.0, size=dim)
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, size=(10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, size=10)
        # Saddle point interaction parameters
        self.saddle_strength = np.random.uniform(0.5, 2.0, size=dim)
        self.saddle_frequency = np.random.uniform(1.0, 5.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic map component
        chaotic = 0.0
        for i in range(self.dim):
            # Use logistic map with dimension-specific r values
            logistic_val = x[i]
            for _ in range(10):  # Iterate chaos several times
                logistic_val = self.logistic_r[i] * logistic_val * (1 - logistic_val)
            chaotic += logistic_val * np.sin(self.saddle_frequency[i] * x[i])
            
        # Radial basis function component with multiple centers
        rbf = 0.0
        for i in range(10):
            center = self.rbf_centers[i]
            diff = x - center
            rbf += np.exp(-np.sum(diff**2) / (2 * self.rbf_widths[i]**2))
            
        # Saddle point interaction terms
        saddle = 0.0
        for i in range(self.dim):
            # Create saddle point landscape with sinusoidal modulation
            saddle += self.saddle_strength[i] * x[i]**2 * np.cos(self.saddle_frequency[i] * x[i])
            
        # Cross-dimensional interaction terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Combined landscape with dynamic weighting
        return (2.0 * chaotic + 
                1.5 * rbf + 
                1.8 * saddle + 
                1.2 * cross_interaction)
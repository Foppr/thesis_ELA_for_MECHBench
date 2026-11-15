import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute exponential decay centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (12, dim))
        self.weights = np.random.uniform(0.5, 3.0, 12)
        self.amplitudes = np.random.uniform(0.1, 1.5, 12)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay radial basis function component
        exp_sum = 0.0
        for i in range(12):
            center = self.centers[i]
            weight = self.weights[i]
            amplitude = self.amplitudes[i]
            distance = np.sum((x - center) ** 2)
            exp_sum += weight * amplitude * np.exp(-distance / (2 * 0.4 ** 2))
        
        # Trigonometric modulation component with multiple frequencies
        trig_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            trig_sum += (np.sin(5 * xi) * np.cos(3 * xi) * np.tan(2 * xi) + 
                        0.6 * np.sin(8 * xi) * np.cos(4 * xi) * np.tan(3 * xi) + 
                        0.4 * np.sin(6 * xi) * np.cos(5 * xi) * np.tan(4 * xi) + 
                        0.2 * np.sin(9 * xi) * np.cos(2 * xi) * np.tan(5 * xi))
        
        # Saddle-point conditioning term with cross-dimensional interaction
        saddle_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            saddle_conditioning += xi ** 2 - xi ** 4 + 0.1 * np.sin(10 * xi)
        
        # Additional cross-dimensional interaction terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-interaction
                cross_interaction += (x[i] ** 2) * (x[j] ** 3) * np.cos(x[i] * x[j])
        
        # Quadratic basin component with variable conditioning
        quadratic_term = np.sum(x**2) / self.dim
        
        # Combine all components with different weights
        result = 0.35 * exp_sum + 0.25 * trig_sum + 0.2 * saddle_conditioning + 0.15 * cross_interaction + 0.05 * quadratic_term
        
        return result
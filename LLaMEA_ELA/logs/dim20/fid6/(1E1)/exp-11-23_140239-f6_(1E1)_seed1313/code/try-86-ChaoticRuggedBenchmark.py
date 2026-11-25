import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for radial basis functions
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        self.rbf_weights = np.random.uniform(-1.0, 1.0, 10)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 2.0 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) + 0.5 * np.sin(7.0 * x[i])
        
        # Add radial basis functions for ruggedness
        for i in range(10):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            weight = self.rbf_weights[i]
            dist = np.sum((x - center)**2)
            result += weight * np.exp(-dist / (2 * width**2))
        
        # Add gradient-based attractor fields with chaotic perturbations
        attractor_force = 0.0
        for i in range(5):
            a_x = np.random.uniform(-5.0, 5.0)
            a_y = np.random.uniform(-5.0, 5.0)
            force = 1.0 / (1.0 + np.sqrt((x[0] - a_x)**2 + (x[1] - a_y)**2))
            attractor_force += force * np.sin(i * x[0] + i * x[1])
        
        result += 0.3 * attractor_force
        
        # Add higher-order polynomial terms
        for i in range(self.dim):
            result += 0.5 * x[i]**6 - 1.2 * x[i]**4 + 0.8 * x[i]**2
        
        # Add noise component with chaotic modulation
        noise = 0.1 * np.sum(np.sin(10 * x) * np.cos(5 * x) * np.sin(x[0] * 3))
        
        return result + noise
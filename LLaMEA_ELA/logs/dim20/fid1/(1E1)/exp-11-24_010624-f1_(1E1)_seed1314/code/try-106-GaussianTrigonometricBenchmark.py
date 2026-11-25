import numpy as np

class GaussianTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute parameters for Gaussian components
        self.gaussian_centers = np.random.uniform(-3.0, 3.0, (10, dim))
        self.gaussian_weights = np.random.dirichlet(np.ones(10))
        self.frequency_params = np.random.uniform(1.0, 5.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian mixture component
        gaussian_result = 0.0
        for i in range(10):
            diff = x - self.gaussian_centers[i]
            distance_sq = np.sum(diff**2)
            gaussian_result += self.gaussian_weights[i] * np.exp(-0.5 * distance_sq)
        
        # Trigonometric oscillation component
        trig_result = 0.0
        for i in range(self.dim):
            trig_result += np.sin(self.frequency_params[i] * x[i]) * np.cos(self.frequency_params[i] * x[i])
            
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.1 * (self.dim - 1) * np.sin(np.sum(x**2) / (self.dim * 10))
        
        # Cross-dimensional coupling with varying strength
        coupling_result = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 * (1 + np.sin(0.5 * (x[i] + x[j])))
                coupling_result += coupling_strength * np.sin(x[i] * x[j])
                
        # Combine all components with scaling
        result = condition_factor * (gaussian_result + 0.5 * trig_result + 0.1 * coupling_result)
        
        # Add a global shift to increase difficulty
        global_shift = np.sum(np.sin(0.3 * x))
        result += 0.05 * global_shift
        
        return result
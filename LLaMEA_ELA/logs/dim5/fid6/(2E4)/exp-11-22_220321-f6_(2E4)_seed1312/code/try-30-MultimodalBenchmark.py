import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Sum of quadratic terms with different scales
        for i in range(self.dim):
            result += (x[i] ** 2) * (i + 1)
            
        # Add multiple local minima using sine waves with exponentially increasing frequencies
        for i in range(self.dim):
            freq = 5 ** (i % 5)  # Increased base frequency for more complexity
            result += 0.5 * np.sin(freq * x[i]) * np.cos(freq * x[(i + 1) % self.dim])
            
        # Add a complex penalty term with multiple local optima
        penalty = 0.0
        for i in range(self.dim):
            # Increased polynomial order and changed coefficients for higher complexity
            penalty += (x[i] ** 11 + x[i] ** 7 + x[i] ** 5 + x[i] ** 3) * (i + 1)
            
        # Add enhanced cross-dimensional interactions with additional nonlinear components
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Increased interaction strength and added new nonlinear component
                cross_term += np.sin(x[i]) * np.cos(x[j]) * (i + j) * np.exp(-0.2 * abs(x[i] - x[j])) * np.log(1 + abs(x[i] * x[j])) * np.tan(0.5 * x[i] + 0.3 * x[j])
                
        # Add a novel hyper-complex interaction term with trigonometric and exponential components
        hyper_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    hyper_term += np.sin(x[i] * x[j]) * np.cos(x[k]) * (i + j + k) * np.exp(-0.1 * (x[i]**2 + x[j]**2 + x[k]**2)) * np.log(1 + abs(x[i] * x[j] * x[k]))
        
        return result + 0.15 * penalty + 0.25 * cross_term + 0.1 * hyper_term
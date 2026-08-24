import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic terms with varying scales and enhanced curvature
        result = 0.0
        for i in range(self.dim):
            result += (x[i] - 1.2)**2 + (x[i] + 1.2)**2 + 0.03 * x[i]**4
        
        # Intensified interaction terms with exponential scaling and higher-order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_strength = np.exp(1.5 * (i + j)) * (1.0 + 0.5 * np.sin(i * j) + 0.2 * np.cos(i * j))
                result += interaction_strength * (x[i] - x[j])**2 + 0.1 * (x[i] * x[j])**2
        
        # Add multiple saddle point structures with enhanced sinusoidal modulations
        for i in range(self.dim):
            result += 0.8 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) + 0.3 * np.sin(5.0 * x[i]) + 0.1 * np.sin(7.0 * x[i])
        
        # Add complex global minimum with high curvature and additional polynomial terms
        result += 0.002 * np.sum(x**2) + 0.0005 * np.sum(x**6) + 0.0001 * np.sum(x**8) + 0.00005 * np.sum(x**10)
        
        # Add a highly periodic component with multiple frequencies to increase landscape complexity
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) + 0.5 * np.sin(6.0 * x[i]) * np.cos(4.0 * x[i]) + 0.3 * np.sin(8.0 * x[i])
        result += 0.15 * periodic_term
        
        # Shift global minimum to encourage better convergence with additional offset
        result += 0.7 * np.sum((x - 0.3)**2) + 0.2 * np.sum(np.sin(x)**2) + 0.1 * np.sum(np.cos(x)**2)
        
        # Add a new layer of complexity with fractional powers and logarithmic terms
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.05 * np.sin(1.0 / x[i]) * np.cos(1.0 / x[i]) + 0.02 * np.log(np.abs(x[i]) + 1)
        
        # Add a chaotic component using a logistic map-like structure
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(10.0 * np.sin(x[i])) + 0.5 * np.sin(15.0 * np.cos(x[i]))
        result += 0.1 * chaotic_term
        
        return result
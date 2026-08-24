import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic terms with varying scales and additional polynomial components
        result = 0.0
        for i in range(self.dim):
            result += (x[i] - 1.5)**2 + (x[i] + 1.5)**2 + 0.02 * x[i]**4 + 0.005 * x[i]**6
        
        # Exponentially increasing interaction terms with stronger scaling and additional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use stronger exponential scaling for interaction strength
                interaction_strength = np.exp(1.5 * (i + j))
                result += interaction_strength * (x[i] - x[j])**2
        
        # Add saddle point structure with enhanced sinusoidal modulation
        for i in range(self.dim):
            result += 0.8 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) + 0.3 * np.sin(5.0 * x[i])
        
        # Add a complex global minimum with high curvature and additional polynomial terms
        result += 0.002 * np.sum(x**2) + 0.0005 * np.sum(x**6) + 0.0001 * np.sum(x**8)
        
        # Add a highly periodic component to increase landscape complexity
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) + 0.5 * np.sin(6.0 * x[i])
        result += 0.15 * periodic_term
        
        # Shift global minimum to encourage better convergence with additional offset
        result += 0.7 * np.sum((x - 0.3)**2) + 0.05 * np.sum((x - 0.3)**4)
        
        # Add a noise-like component to increase ruggedness
        noise = 0.0
        for i in range(self.dim):
            noise += 0.02 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i])
        result += noise
        
        # Add fractal-like self-similarity with recursive scaling
        fractal = 0.0
        for i in range(self.dim):
            fractal += 0.01 * np.sin(15.0 * x[i]) * np.cos(12.0 * x[i]) + 0.005 * np.sin(20.0 * x[i])
        result += fractal
        
        # Add adaptive difficulty scaling based on dimensionality
        adaptive_scale = 1.0 + 0.1 * np.log(self.dim + 1)
        result *= adaptive_scale
        
        return result
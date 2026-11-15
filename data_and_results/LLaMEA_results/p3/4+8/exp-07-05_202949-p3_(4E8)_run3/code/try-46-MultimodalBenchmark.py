import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic terms with varying scales
        result = 0.0
        for i in range(self.dim):
            result += (x[i] - 1.0)**2 + (x[i] + 1.0)**2 + 0.01 * x[i]**4
        
        # Exponentially increasing interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use exponential scaling for interaction strength
                interaction_strength = np.exp(0.5 * (i + j))
                result += interaction_strength * (x[i] - x[j])**2
        
        # Add saddle point structure with sinusoidal modulation
        for i in range(self.dim):
            result += 0.5 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
        
        # Add a complex global minimum with high curvature
        result += 0.001 * np.sum(x**2) + 0.0001 * np.sum(x**6)
        
        # Add a periodic component to increase landscape complexity
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        result += 0.1 * periodic_term
        
        # Add higher-order polynomial terms for increased complexity
        result += 0.00001 * np.sum(x**8)
        
        # Introduce additional sinusoidal modulations with varying frequencies
        for i in range(self.dim):
            result += 0.3 * np.sin(5.0 * x[i]) + 0.2 * np.cos(4.0 * x[i]) + 0.1 * np.sin(7.0 * x[i])
        
        # Add a perturbed global minimum to increase challenge
        global_min_shift = 0.5
        result += 0.05 * np.sum((x - global_min_shift)**2)
        
        # Add a noise-like component with exponential decay
        noise = 0.0
        for i in range(self.dim):
            noise += np.exp(-0.1 * x[i]**2) * np.sin(10.0 * x[i])
        result += 0.02 * noise
        
        return result
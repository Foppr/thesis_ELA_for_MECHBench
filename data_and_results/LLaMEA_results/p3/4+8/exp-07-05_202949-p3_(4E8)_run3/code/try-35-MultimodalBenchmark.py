import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with polynomial scaling
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * r**2 + 0.1 * r**4 + 0.01 * r**6
        
        # Sinusoidal perturbations in radial direction
        sin_radial = np.sin(3.0 * r) * np.cos(2.0 * r)
        
        # Angular components with chaotic interaction
        angular_sum = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x[i], x[(i+1) % self.dim]) if self.dim > 1 else 0.0
            angular_sum += np.sin(5.0 * angle) * np.cos(4.0 * angle)
        
        # Adaptive conditioning based on dimensionality
        conditioning = 1.0 + 0.1 * self.dim
        
        # Cross-terms with chaotic modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
        
        # Asymmetric basin with exponential decay
        basin = 0.0
        for i in range(self.dim):
            basin += np.exp(-0.5 * (x[i] - 1.5)**2) + np.exp(-0.5 * (x[i] + 1.5)**2)
        
        # Final function value
        result = conditioning * (radial_term + sin_radial + angular_sum) + 0.5 * cross_term + 0.3 * basin
        
        # Add high-frequency noise to increase complexity
        noise = np.sum(np.sin(20.0 * x) * np.cos(15.0 * x))
        result += 0.05 * noise
        
        return result
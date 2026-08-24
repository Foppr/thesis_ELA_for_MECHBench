import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.a = 3.9
        self.b = 0.5
        self.c = 2.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with global minimum at origin
        result = 0.5 * np.sum(x**2)
        
        # Add polynomial interaction terms with varying degrees
        for i in range(self.dim):
            result += 0.1 * x[i]**4 + 0.05 * x[i]**6
        
        # Introduce chaotic behavior through logistic map-like interactions
        chaotic_term = 0.0
        for i in range(self.dim):
            # Simulate chaotic dynamics with logistic map
            chaotic_val = self.a * x[i] * (1 - x[i])
            chaotic_term += self.b * np.sin(chaotic_val * self.c) * x[i]**2
        
        result += chaotic_term
        
        # Add highly periodic sinusoidal components with varying frequencies
        periodic_term = 0.0
        for i in range(self.dim):
            # Multiple frequencies to increase complexity
            periodic_term += (0.8 * np.sin(2.0 * x[i]) + 
                             0.5 * np.sin(5.0 * x[i]) + 
                             0.3 * np.sin(8.0 * x[i]) + 
                             0.2 * np.sin(12.0 * x[i]))
        
        result += 0.2 * periodic_term
        
        # Add multipeak structure using Gaussian-like peaks
        peak_term = 0.0
        peak_centers = np.linspace(-4.0, 4.0, 9)
        for i in range(self.dim):
            for center in peak_centers:
                peak_term += 0.3 * np.exp(-0.5 * ((x[i] - center) / 0.8)**2)
        
        result += peak_term
        
        # Add a complex interaction term between all variables
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += (0.1 * np.sin(3.0 * (x[i] + x[j])) * 
                                   np.cos(2.0 * (x[i] - x[j])) + 
                                   0.05 * np.sin(4.0 * (x[i] * x[j])))
        
        result += interaction_term
        
        # Add a small noise-like component for additional ruggedness
        noise = 0.0
        for i in range(self.dim):
            noise += 0.01 * np.sin(15.0 * x[i]) * np.cos(10.0 * x[i])
        
        result += noise
        
        # Shift global minimum to encourage convergence to a specific point
        result += 0.1 * np.sum((x - 0.5)**2)
        
        return result
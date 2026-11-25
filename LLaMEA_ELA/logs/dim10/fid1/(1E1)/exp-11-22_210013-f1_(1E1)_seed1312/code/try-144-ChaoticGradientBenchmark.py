import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin with chaotic perturbations
        base = np.sum(x**2)
        
        # Add chaotic behavior via logistic map-inspired terms
        chaos = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Logistic-like chaotic component
            chaos += 0.5 * (4 * xi * (1 - xi))**2
            
        # Introduce varying curvature and saddle points
        curvature = 0.0
        for i in range(self.dim):
            curvature += 0.3 * np.sin(3 * x[i])**2 + 0.2 * np.cos(2 * x[i])**2
            curvature += 0.1 * x[i]**4
        
        # Implicit constraint term (penalty for violating bounds or specific regions)
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.5:
                penalty += 10 * (abs(x[i]) - 4.5)**2
            if x[i] * x[(i+1) % self.dim] < 0:
                penalty += 0.5 * abs(x[i] * x[(i+1) % self.dim])
        
        # Add multi-scale oscillatory behavior
        oscillation = 0.0
        for i in range(self.dim):
            oscillation += 0.4 * np.sin(10 * x[i]) * np.cos(7 * x[(i+1) % self.dim])
            oscillation += 0.2 * np.sin(5 * x[i] + 1) * np.exp(-0.5 * x[i]**2)
        
        # Combine all components with different weights
        return 1.0 * base + 0.7 * chaos + 0.8 * curvature + 0.5 * penalty + 0.6 * oscillation
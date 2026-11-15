import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_value = np.sum(x**2)
        
        # Add chaotic sine modulation with varying frequencies
        for i in range(self.dim):
            f_value += 2.0 * np.sin(10 * x[i]) * np.sin(15 * x[i]) * np.sin(20 * x[i])
            
        # Introduce saddle points via cross-variable terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.5 * np.sin(5 * x[i]) * np.cos(8 * x[j]) * (x[i]**2 - x[j]**2)
                
        # Add non-smooth components with absolute value and step functions
        for i in range(self.dim):
            f_value += 0.3 * np.abs(x[i])**1.5
            
        # Incorporate chaotic logistic map-like behavior
        for i in range(self.dim):
            f_value += 0.4 * np.sin(25 * x[i]) * np.cos(30 * x[i]) * np.sin(35 * x[i])
            
        # Add varying curvature via polynomial terms with random exponents
        for i in range(self.dim):
            exp = 3 + 2 * np.sin(i)
            f_value += 0.2 * np.abs(x[i])**exp
            
        # Cross-variable interaction with hyperbolic tangent
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.3 * np.tanh(2 * x[i]) * np.sin(7 * x[j]) * np.cos(9 * x[i] + x[j])
                
        # Add a multi-modal component with irregular bumps
        for i in range(self.dim):
            f_value += 0.6 * np.sin(40 * x[i]) * np.cos(25 * x[i]) * np.sin(30 * x[i])
            
        # Introduce noise to increase irregularity
        noise = np.random.normal(0, 0.05, self.dim)
        f_value += 0.1 * np.sum(noise * x)
        
        # Add a component with varying amplitude and frequency
        for i in range(self.dim):
            f_value += 0.25 * np.sin(50 * x[i]) * np.cos(45 * x[i]) * np.sin(40 * x[i])
            
        # Add a component with piecewise smoothness
        for i in range(self.dim):
            f_value += 0.3 * (np.abs(x[i])**(1.2 + 0.1 * np.sin(i))) * np.cos(10 * x[i])
            
        return f_value
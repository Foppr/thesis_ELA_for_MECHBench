import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] for controlled trigonometric behavior
        scaled_x = x * (np.pi / 5.0)
        
        # Base exponential decay component with chaotic gradient
        result = 0.0
        for i in range(self.dim):
            result += np.exp(-0.5 * x[i]**2) * np.sin(scaled_x[i])**3
            
        # Add polynomial coupling terms with varying exponents
        for i in range(self.dim):
            result += 0.2 * (x[i]**4 - 2*x[i]**2 + 1)
            
        # Introduce dynamic saddle-point interactions
        saddle_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                saddle_term += np.sin(2 * scaled_x[i]) * np.cos(3 * scaled_x[j])
        result += 0.3 * saddle_term
        
        # Add multi-scale oscillatory components
        oscillation = 0.0
        for i in range(self.dim):
            oscillation += np.sin(7 * scaled_x[i]) * np.cos(11 * scaled_x[i])
        result += 0.25 * oscillation
        
        # Include cross-dimensional coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(5 * (x[i] + x[j]))
        result += 0.15 * coupling
        
        # Add a global minimum with dynamic penalty
        result += 0.1 * np.sum(x**2) + 0.05 * np.sum(np.abs(x))**1.5
        
        # Introduce chaotic damping factor based on dimensionality
        damping = np.exp(-0.02 * self.dim)
        result *= damping
        
        return result
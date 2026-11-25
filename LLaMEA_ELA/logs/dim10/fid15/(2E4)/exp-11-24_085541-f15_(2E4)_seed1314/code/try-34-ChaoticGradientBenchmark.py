import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.alpha = 3.8
        self.beta = 0.1
        self.gamma = 0.05
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with conditioning
        result = 0.5 * np.sum(x**2)
        
        # Chaotic component using logistic map-like dynamics
        chaotic_sum = 0.0
        for i in range(self.dim):
            # Apply chaotic transformation to each dimension
            chaotic_val = np.sin(x[i]) * np.cos(2 * x[i])
            chaotic_sum += chaotic_val**3
            
        result += 2.0 * chaotic_sum
        
        # Add saddle point structure with hyperbolic tangent components
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += np.tanh(x[i])**2 - 0.5 * x[i]**2
            
        result += 1.5 * saddle_term
        
        # Introduce variable conditioning based on dimension
        condition_factor = 1.0 + 0.3 * np.log(1.0 + self.dim)
        result *= condition_factor
        
        # Add gradient-dependent oscillation
        grad_osc = 0.0
        for i in range(self.dim):
            # Use finite differences to approximate gradient influence
            if i < self.dim - 1:
                diff = x[i+1] - x[i]
                grad_osc += np.sin(3.0 * diff) * np.cos(2.0 * diff)
                
        result += 0.8 * grad_osc
        
        # Add path-dependent term that encourages specific search trajectories
        path_term = 0.0
        for i in range(self.dim - 1):
            path_term += (x[i] + x[i+1])**2 * np.sin(0.5 * x[i])
            
        result += 0.6 * path_term
        
        # Add a global minimum attractor with radial basis function
        center = np.ones(self.dim) * 1.0
        rbf = np.sum(np.exp(-0.5 * ((x - center)**2) / 0.5))
        result -= 0.4 * rbf
        
        return result
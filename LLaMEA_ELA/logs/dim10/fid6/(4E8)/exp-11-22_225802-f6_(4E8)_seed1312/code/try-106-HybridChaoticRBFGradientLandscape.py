import numpy as np

class HybridChaoticRBFGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stable polynomial evaluation
        normalized_x = x / 5.0
        
        # Polynomial chaos component with mixed exponents
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (normalized_x[i]**3 + 0.5 * normalized_x[i]**4 + 0.3 * normalized_x[i]**5)
            
        # Radial basis function component with multiple centers
        rbf_term = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0.0
            rbf_term += np.exp(-5.0 * (normalized_x[i] - center)**2)
            
        # Gradient-based saddle point component with alternating signs
        grad_saddle = 0.0
        for i in range(self.dim):
            grad_saddle += (-1)**i * normalized_x[i]**2 * np.sin(3 * normalized_x[i])
            
        # Multi-scale oscillation component
        oscillation = 0.0
        for i in range(self.dim):
            oscillation += 2.0 * np.sin(7 * normalized_x[i]) * np.cos(11 * normalized_x[i])
            
        # Cross-dimensional coupling with varying strength
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.2 * (normalized_x[i]**2 + normalized_x[j]**2) * np.sin(5 * (normalized_x[i] - normalized_x[j]))
                
        # Global scaling and offset
        result = poly_term + rbf_term + grad_saddle + oscillation + coupling
        
        # Add a small penalty for distance from origin to encourage convergence
        result += 0.1 * np.sum(normalized_x**2)
        
        return result
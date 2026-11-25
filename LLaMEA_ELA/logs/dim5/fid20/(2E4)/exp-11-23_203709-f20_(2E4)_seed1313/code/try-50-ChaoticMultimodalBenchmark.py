import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced trigonometric chaotic component with exponentially increasing frequencies
        chaotic = 0
        for i in range(self.dim):
            chaotic += (3.2 * np.sin(6.1 * x[i]) * np.cos(4.9 * x[i]) + 
                       2.1 * np.sin(8.7 * x[i]) * np.cos(5.3 * x[i]) + 
                       1.4 * np.sin(10.2 * x[i]) * np.cos(3.6 * x[i]) +
                       0.7 * np.sin(12.5 * x[i]) * np.cos(2.8 * x[i]))
        
        # Multi-scale radial basis function with dynamic centers and varying widths
        rbf = 0
        centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            rbf += 4.1 * np.exp(-0.5 * ((x[i] - center) / 1.5)**2) + \
                   3.3 * np.exp(-0.3 * ((x[i] - center) / 2.1)**2) + \
                   2.7 * np.exp(-0.1 * ((x[i] - center) / 1.0)**2)
        
        # Extended cross-dimensional interaction terms with multi-scale coupling
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Wider interaction scope
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross_interaction += 2.3 * np.sin(8.1 * dist) * np.cos(6.4 * dist) / (dist**1.8 + 0.03)
        
        # Higher-order polynomial modulation with chaotic coefficient scaling
        poly_mod = 0
        for i in range(self.dim):
            poly_mod += 1.1 * x[i]**7 - 1.5 * x[i]**6 + 1.2 * x[i]**5 - 0.8 * x[i]**4 + 0.4 * x[i]**3
        
        # Additional chaotic scaling factor that increases with dimensionality
        dim_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Combine all components with enhanced scaling and additive constants
        return 1.5 * chaotic + 3.2 * rbf + 0.35 * cross_interaction + 0.7 * poly_mod + 40.0 * self.dim * dim_factor
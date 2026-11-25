import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for additional complexity
        self.chaotic_sequence = np.array([np.sin(2**i * np.pi * 0.1) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map component for chaotic behavior
        logistic = 0.0
        r = 3.99  # Chaos parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = 0.5
            else:
                x_prev = x[i-1]
            logistic += (r * x_prev * (1 - x_prev)) * np.sin(x[i])
        
        # Radial basis function with varying widths and centers
        rbf = 0.0
        centers = np.linspace(-4, 4, min(5, self.dim))
        widths = np.logspace(-1, 1, min(5, self.dim))
        
        for i in range(min(5, self.dim)):
            center = centers[i]
            width = widths[i]
            rbf += np.exp(-0.5 * ((x - center) / width)**2)
        
        # Multi-scale sinusoidal modulation
        scale_mod = 0.0
        for i in range(self.dim):
            scale_mod += np.sin(10 * x[i]) * np.cos(3 * x[(i + 1) % self.dim])
            scale_mod += 0.5 * np.sin(20 * x[i]) * np.cos(7 * x[(i + 2) % self.dim])
        
        # Cross-dimensional coupling with chaotic sequence
        coupling = 0.0
        for i in range(self.dim):
            coupling += self.chaotic_sequence[i] * x[i] * np.sin(x[(i + 1) % self.dim])
        
        # Polynomial curvature term with variable exponents
        poly_curvature = 0.0
        for i in range(self.dim):
            poly_curvature += (x[i]**3 - 3*x[i]**2 + 2*x[i]) * np.cos(2 * x[(i + 1) % self.dim])
        
        # Final combined landscape with adaptive weights
        return 0.6 * logistic + 1.2 * rbf + 0.8 * scale_mod + 0.9 * coupling + 0.5 * poly_curvature
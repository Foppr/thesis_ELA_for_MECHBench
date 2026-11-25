import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Logistic map component for chaotic behavior
        logistic_term = 0.0
        r = 3.95  # Chaotic regime parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = x_norm[-1]  # Wrap around
            else:
                x_prev = x_norm[i-1]
            logistic_term += r * x_prev * (1 - x_prev)
        
        # Radial basis function with varying widths and centers
        rbf_term = 0.0
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        widths = np.logspace(-2, 1, min(5, self.dim))
        for i in range(min(5, self.dim)):
            center = centers[i]
            width = widths[i]
            rbf_term += np.exp(-width * np.sum((x_norm - center)**2))
        
        # Asymmetric coupling terms between dimensions
        coupling_term = 0.0
        for i in range(self.dim-1):
            coupling_term += (x_norm[i]**3 + x_norm[i+1]**2) * np.exp(-0.5 * (x_norm[i] - x_norm[i+1])**2)
        
        # High-frequency oscillatory component
        oscillation_term = 0.0
        for i in range(self.dim):
            oscillation_term += np.sin(20 * x_norm[i]) * np.cos(15 * x_norm[i]) * (1 + 0.1 * np.sin(7 * x_norm[i]))
        
        # Mixed polynomial and exponential terms
        poly_exp_term = 0.0
        for i in range(self.dim):
            if i % 2 == 0:
                poly_exp_term += x_norm[i]**7 * np.exp(-0.3 * x_norm[i]**2)
            else:
                poly_exp_term += x_norm[i]**4 * np.exp(-0.2 * x_norm[i]**2)
        
        # Combine all terms with different weights
        return (0.5 * np.sum(x_norm**2) + 
                0.3 * logistic_term + 
                0.2 * rbf_term + 
                0.15 * coupling_term + 
                0.1 * oscillation_term + 
                0.05 * poly_exp_term)
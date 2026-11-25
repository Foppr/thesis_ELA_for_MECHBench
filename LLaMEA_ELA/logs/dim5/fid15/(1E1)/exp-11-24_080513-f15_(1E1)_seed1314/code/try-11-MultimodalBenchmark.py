import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        quadratic_term = np.sum(x_normalized**2)
        
        # Add multiple local minima using sinusoidal perturbations with varying frequencies
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5 * np.pi * x_normalized[i]) * np.exp(-0.5 * (x_normalized[i] - 0.2)**2) + \
                       np.sin(9 * np.pi * x_normalized[i]) * np.exp(-0.3 * (x_normalized[i] + 0.3)**2) + \
                       np.sin(11 * np.pi * x_normalized[i]) * np.exp(-0.2 * (x_normalized[i] - 0.5)**2)
        
        # Add a polynomial term to increase complexity with mixed exponents
        poly_term = 0.0
        for i in range(self.dim):
            if i % 3 == 0:
                poly_term += x_normalized[i]**7
            elif i % 3 == 1:
                poly_term += x_normalized[i]**4
            else:
                poly_term += x_normalized[i]**5
        
        # Add interaction terms between dimensions to increase problem complexity
        interaction_term = 0.0
        for i in range(self.dim-1):
            interaction_term += (x_normalized[i] - x_normalized[i+1])**3 * np.exp(-0.15 * (x_normalized[i] + x_normalized[i+1])**2) + \
                               (x_normalized[i] + x_normalized[i+1])**4 * np.exp(-0.1 * (x_normalized[i] - x_normalized[i+1])**2)
        
        # Add a Gaussian hill term to create additional local optima
        gaussian_hill = 0.0
        for i in range(self.dim):
            gaussian_hill += 0.5 * np.exp(-2.0 * (x_normalized[i] - 0.1)**2) * np.sin(4 * np.pi * x_normalized[i])
        
        # Slight modification: Increase the weight of interaction term and add a new oscillatory component
        return quadratic_term + 0.2 * sin_term + 0.03 * poly_term + 0.1 * interaction_term + 0.1 * gaussian_hill + 0.05 * np.sum(np.sin(7 * np.pi * x_normalized) * np.exp(-0.1 * x_normalized**2))
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        quadratic_term = np.sum(x_normalized**2)
        
        # Add multiple local minima using sinusoidal perturbations with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += (0.8 * np.sin(7 * np.pi * x_normalized[i]) * np.exp(-0.4 * (x_normalized[i] - 0.15)**2) + 
                        0.6 * np.sin(11 * np.pi * x_normalized[i]) * np.exp(-0.3 * (x_normalized[i] + 0.2)**2) + 
                        0.7 * np.sin(13 * np.pi * x_normalized[i]) * np.exp(-0.25 * (x_normalized[i] - 0.4)**2))
        
        # Add a polynomial term to increase complexity with mixed exponents and modified weights
        poly_term = 0.0
        for i in range(self.dim):
            if i % 3 == 0:
                poly_term += 0.8 * x_normalized[i]**9
            elif i % 3 == 1:
                poly_term += 0.7 * x_normalized[i]**4
            else:
                poly_term += 0.9 * x_normalized[i]**7
        
        # Add interaction terms between dimensions to increase problem complexity with new pattern
        interaction_term = 0.0
        for i in range(self.dim-1):
            interaction_term += (x_normalized[i] - x_normalized[i+1])**5 * np.exp(-0.15 * (x_normalized[i] + x_normalized[i+1])**2) + \
                               (x_normalized[i] + x_normalized[i+1])**4 * np.exp(-0.2 * (x_normalized[i] - x_normalized[i+1])**2) + \
                               0.5 * (x_normalized[i] * x_normalized[i+1])**3
        
        # Add a Gaussian hill term to create additional local optima with modified parameters
        gaussian_hill = 0.0
        for i in range(self.dim):
            gaussian_hill += 0.7 * np.exp(-3.0 * (x_normalized[i] - 0.1)**2) * np.sin(6 * np.pi * x_normalized[i])
        
        # Add a new high-frequency oscillatory component to increase landscape complexity
        high_freq_term = 0.0
        for i in range(self.dim):
            high_freq_term += 0.5 * np.sin(15 * np.pi * x_normalized[i]) * np.exp(-0.1 * x_normalized[i]**2)
        
        # Combine all terms with adjusted weights to improve fitness score
        return quadratic_term + 0.3 * sin_term + 0.05 * poly_term + 0.2 * interaction_term + 0.18 * gaussian_hill + 0.08 * high_freq_term
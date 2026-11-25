import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Enhanced global quadratic basin with variable coefficients
        quadratic_term = 0.3 * np.sum(x_normalized**2)
        
        # Complex nested sinusoidal oscillations with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += (np.sin(11 * np.pi * x_normalized[i]) + 
                        0.5 * np.sin(17 * np.pi * x_normalized[i]) + 
                        0.2 * np.sin(23 * np.pi * x_normalized[i])) * \
                       np.exp(-0.3 * (x_normalized[i] - 0.2)**2) + \
                       0.15 * x_normalized[i]**4
        
        # Advanced multivariate interaction terms with cubic and quartic cross-terms
        multivariate_sin = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                multivariate_sin += (np.sin(5 * np.pi * x_normalized[i]) * 
                                   np.sin(3 * np.pi * x_normalized[j]) * 
                                   (1 + 0.2 * (x_normalized[i]**3 + x_normalized[j]**3)) + 
                                   0.1 * x_normalized[i]**2 * x_normalized[j]**2)
        
        # Dynamically shifted global minimum with higher-order polynomial
        shift_term = 0.0
        for i in range(self.dim):
            shift_term += 0.6 * (x_normalized[i] - 0.4)**5 + 0.3 * (x_normalized[i] - 0.4)**6
        
        # Additional chaotic component with exponential modulation
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.exp(-2.0 * np.sum(x_normalized[:i+1]**2)) * np.sin(9 * np.pi * x_normalized[i])
        
        return quadratic_term + sin_term + multivariate_sin + shift_term + chaotic_term
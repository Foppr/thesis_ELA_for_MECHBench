import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic_term = 0.1 * np.sum(x_normalized**2)
        
        # Chaotic sinusoidal components with exponential modulation
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(20 * np.pi * x_normalized[i]) * np.exp(-5 * np.abs(x_normalized[i])) + \
                           0.3 * np.cos(12 * np.pi * x_normalized[i]) * np.exp(-3 * (x_normalized[i]**2))
        
        # Multivariate coupling with saddle-point characteristics
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for complexity control
                coupling_term += (x_normalized[i] * x_normalized[j]) * \
                                np.sin(8 * np.pi * (x_normalized[i] + x_normalized[j])) * \
                                np.exp(-0.5 * (x_normalized[i]**2 + x_normalized[j]**2))
        
        # Add noise-like perturbations for increased ruggedness
        noise_term = 0.0
        for i in range(self.dim):
            noise_term += 0.1 * np.sin(30 * x_normalized[i]) * np.cos(25 * x_normalized[i])
        
        # Shifted global minimum with higher-order polynomial terms
        shift_term = 0.5 * np.sum((x_normalized + 0.2)**6)
        
        return quadratic_term + chaotic_term + coupling_term + noise_term + shift_term
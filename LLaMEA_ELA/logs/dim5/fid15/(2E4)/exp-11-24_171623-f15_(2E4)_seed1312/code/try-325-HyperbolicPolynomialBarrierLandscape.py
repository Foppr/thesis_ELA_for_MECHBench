import numpy as np

class HyperbolicPolynomialBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Hyperbolic tangent barrier parameters with varying steepness
        self.barrier_steepness = 0.5 + 3.0 * np.random.rand(dim)
        self.barrier_heights = 1.0 + 4.0 * np.random.rand(dim)
        # Polynomial coupling coefficients with mixed degrees
        self.coupling_degrees = 2 + 3 * np.random.randint(1, 4, (dim, dim))
        self.coupling_coefficients = -1.0 + 2.0 * np.random.rand(dim, dim)
        # Dynamic noise parameters with time-varying scaling
        self.noise_amplitudes = 0.5 + 3.0 * np.random.rand(dim)
        self.noise_frequencies = 0.5 + 4.0 * np.random.rand(dim)
        # Condition factors for variable conditioning
        self.conditioning_factors = 0.1 + 2.5 * np.random.rand(dim)
        # Additional polynomial terms for increased complexity
        self.poly_exponents = 2 + 3 * np.random.randint(1, 4, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Hyperbolic tangent barrier component
        barrier_sum = 0.0
        for i in range(self.dim):
            barrier_sum += self.barrier_heights[i] * (1.0 - np.tanh(self.barrier_steepness[i] * x_norm[i])**2)
        
        # Polynomial coupling between dimensions
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += (self.coupling_coefficients[i, j] * 
                                   (x_norm[i]**self.coupling_degrees[i, j]) * 
                                   (x_norm[j]**self.coupling_degrees[i, j]))
        
        # Dynamic noise component
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_amplitudes[i] * np.sin(self.noise_frequencies[i] * x_norm[i]) * np.cos(self.noise_frequencies[i] * x_norm[i])
        
        # Polynomial terms for added complexity
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += (x_norm[i]**self.poly_exponents[i])
        
        # Combine components with varying weights
        result = 0.35 * barrier_sum + 0.35 * coupling_sum + 0.2 * noise_sum + 0.1 * poly_sum
        
        # Apply adaptive conditioning
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + self.conditioning_factors[i] * np.abs(x_norm[i])**2)
        
        # Add global penalty term
        penalty = 0.3 * np.sum(np.abs(x_norm)**4)
        
        return result * condition_factor + penalty
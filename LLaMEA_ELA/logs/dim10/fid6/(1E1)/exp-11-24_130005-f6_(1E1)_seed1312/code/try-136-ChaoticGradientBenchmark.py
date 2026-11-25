import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with varying curvature
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sinusoidal modulation with logistic map influence
        chaotic_mod = 0.0
        for i in range(self.dim):
            x_logistic = 0.5
            for _ in range(15):
                x_logistic = 3.8 * x_logistic * (1 - x_logistic)
            chaotic_mod += np.sin(20.0 * x_scaled[i] * x_logistic) * np.cos(15.0 * x_scaled[i] * x_logistic)
        
        # Multi-scale oscillatory component with fractal-like frequency variations
        oscillatory = 0.0
        for i in range(self.dim):
            freqs = [2.0, 5.0, 10.0, 15.0]
            for f in freqs:
                oscillatory += np.sin(f * x_scaled[i]) * np.cos(0.5 * f * x_scaled[i])
        
        # Implicit constraint-like term that creates narrow valleys and sharp gradients
        constraint_term = 0.0
        for i in range(self.dim):
            constraint_term += (np.sin(10.0 * x_scaled[i]) + 0.5 * np.sin(20.0 * x_scaled[i]))**2
        
        # Cross-dimensional interaction with varying strength and phase shifts
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                cross_interaction += np.sin(x_scaled[i] + x_scaled[j]) * \
                                   np.cos(2.0 * x_scaled[i] - 1.5 * x_scaled[j]) * \
                                   (1.0 + 0.3 * np.sin(5.0 * x_scaled[i] * x_scaled[j]))
        
        # Fractal-like curvature with recursive scaling
        fractal_curvature = 0.0
        for i in range(self.dim):
            fractal_curvature += (np.sin(8.0 * x_scaled[i]) + 
                                0.7 * np.sin(16.0 * x_scaled[i]) + 
                                0.3 * np.sin(24.0 * x_scaled[i]))
        
        # Variable difficulty based on dimensionality with exponential scaling
        dim_factor = np.exp(0.1 * self.dim)
        
        # Combine all components with dimensionality-dependent weights
        return (quadratic + 0.5 * chaotic_mod + 0.8 * oscillatory + 
                1.2 * constraint_term + 0.6 * cross_interaction + 
                0.4 * fractal_curvature) * dim_factor
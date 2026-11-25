import numpy as np

class ChaoticRadialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters
        self.chebyshev_roots = np.cos(np.pi * np.arange(1, dim + 1) / (dim + 1))
        self.chaotic_params = np.random.uniform(0.1, 0.9, dim)
        self.gradient_weights = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with chaotic modulation
        rb_value = 0.0
        for i in range(self.dim):
            distance = np.sum((x - self.chebyshev_roots[i])**2)
            rb_value += np.exp(-distance / (2 * (0.5 + 0.5 * np.sin(i * 0.3))) ) * \
                       (1.0 + 0.3 * np.sin(self.chaotic_params[i] * distance))
        
        # Chaotic dynamical system component
        chaotic_value = 0.0
        for i in range(self.dim):
            # Logistic map inspired term
            logistic_term = self.chaotic_params[i] * x[i] * (1 - x[i])
            chaotic_value += np.sin(logistic_term * 5) * np.cos(logistic_term * 3)
        
        # Asymmetric gradient flow terms
        gradient_flow = 0.0
        for i in range(self.dim):
            if i > 0:
                diff = x[i] - x[i-1]
                gradient_flow += self.gradient_weights[i] * (diff**3 + 0.5 * diff**2)
        
        # Multi-scale sinusoidal modulation
        modulation = 0.0
        for i in range(self.dim):
            modulation += np.sin(x[i] * (1 + 0.1 * np.sin(i * 0.7))) * \
                         np.cos(x[i] * (0.5 + 0.2 * np.cos(i * 0.4)))
        
        # Cross-dimensional interaction with hyperbolic tangent
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                cross_interaction += np.tanh(x[i] * x[j]) * (i + j) * 0.1
        
        # Polynomial coupling with variable exponents
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+2, self.dim)):
                exp_factor = 1.5 + 0.5 * np.sin(i * 0.5)
                poly_coupling += (x[i]**exp_factor) * (x[j]**(exp_factor + 0.3))
        
        # Final combined function value
        f_val = rb_value + chaotic_value + gradient_flow + modulation + cross_interaction + poly_coupling
        
        return f_val
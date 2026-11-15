import numpy as np

class PolynomialChaoticBasisBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component with Hermite polynomials
        chaos_poly = 0.0
        for i in range(self.dim):
            # Third-order Hermite polynomial terms
            h3 = 2 * x_norm[i]**3 - 3 * x_norm[i]
            chaos_poly += h3 * np.sin(2 * x_norm[i] * np.pi) * np.cos(x_norm[i] * np.pi)
        
        # Radial basis function with chaotic modulation
        r = np.sqrt(np.sum(x_norm**2))
        rbf = 0.0
        for i in range(self.dim):
            # Chaotic modulation using logistic map
            logistic_mod = 3.8 * (x_norm[i] + 0.2) % 1.0
            rbf += np.exp(-0.5 * (x_norm[i] - np.sin(logistic_mod * 2 * np.pi))**2) * np.cos(3 * x_norm[i] * np.pi)
        
        # Sinusoidal coupling with polynomial weighting
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Polynomial weight based on dimension
                weight = (i + 1) * (j + 1)
                coupling += weight * np.sin(x_norm[i] * x_norm[j] * 4 * np.pi) * np.cos(2 * x_norm[i] * x_norm[j] * np.pi)
        
        # Cross-dimensional exponential interaction with chaotic scaling
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic scaling factor
                scale = 1 + 0.3 * np.sin(5 * r * np.pi)
                exp_interaction += np.exp(-scale * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(3 * x_norm[i] * x_norm[j])
        
        # Multi-modal component with polynomial interactions and sinusoidal modulation
        multimodal = 0.0
        for i in range(self.dim):
            # Higher-order polynomial with sinusoidal modulation
            multimodal += (x_norm[i]**6 + x_norm[i]**4) * np.sin(5 * x_norm[i] * np.pi) * np.cos(2 * x_norm[i] * np.pi)
        
        # Additional chaotic gradient component
        chaotic_grad = 0.0
        for i in range(self.dim):
            # Logistic map based chaotic modulation
            chaotic_input = 3.7 * (x_norm[i] + 0.1) % 1.0
            chaotic_grad += np.tanh(2 * x_norm[i]) * np.sin(4 * chaotic_input * np.pi) * np.cos(x_norm[i] * 3 * np.pi)
        
        # Combined fitness function with adaptive weights
        return 0.3 * chaos_poly + 0.25 * rbf + 0.2 * coupling + 0.15 * exp_interaction + 0.1 * multimodal + 0.05 * chaotic_grad
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic oscillation component using logistic map-like behavior with higher-order terms
        chaotic_component = 0
        for i in range(self.dim):
            # Logistic map-inspired chaotic sequence with cubic nonlinearity
            chaotic_param = 3.8 * np.sin(i * np.pi / (self.dim + 3)) + 0.2
            term1 = np.sin(chaotic_param * x[i] * np.cos(x[i]))
            term2 = np.cos(chaotic_param * x[i] * np.sin(x[i]))
            chaotic_component += term1 * term2 + 0.15 * np.sin(3 * chaotic_param * x[i]) * np.cos(2 * chaotic_param * x[i])
        
        # Radial basis function with dynamic centers, adaptive widths, and polynomial interactions
        rbf_component = 0
        for i in range(self.dim):
            center = 4.5 * np.sin(i * np.pi / (self.dim + 1)) * np.cos(i * np.pi / (self.dim + 2))
            width = 0.15 + 0.7 * np.cos(i * np.pi / (self.dim + 3))
            # Add polynomial interaction terms
            poly_term = x[i]**4 - 3*x[i]**3 + 2*x[i]**2 - x[i]
            rbf_component += np.exp(-0.5 * ((x[i] - center) / width)**2) * (1 + 0.5 * np.sin(i * np.pi / 5) + 0.3 * poly_term)
        
        # Hybrid penalty term combining elliptic, hyperbolic, and polynomial components
        hybrid_penalty = 0
        for i in range(self.dim):
            scale = 1.0 + 0.25 * np.sin(i * np.pi / self.dim) + 0.15 * np.cos(i * np.pi / (self.dim + 2))
            elliptic_term = (x[i]**2) / (scale + 0.15)
            hyperbolic_term = np.tanh(x[i])**3
            polynomial_term = x[i]**5 - 3*x[i]**3 + 2*x[i]**2
            hybrid_penalty += elliptic_term + 0.4 * hyperbolic_term + 0.15 * polynomial_term
        
        # Dynamic scaling with chaotic modulation and noise injection
        dim_scale = 1.0 + 0.25 * np.sin(self.dim * np.pi / 8) * np.cos(self.dim * np.pi / 6)
        
        # Add adaptive noise to increase complexity
        noise = 0.03 * np.random.normal(0, 1)
        
        # Combine components with dynamic weights
        weight1 = 0.35 + 0.25 * np.cos(self.dim * np.pi / 10) + 0.04 * np.sin(self.dim * np.pi / 13)
        weight2 = 0.35 + 0.18 * np.sin(self.dim * np.pi / 7) + 0.02 * np.cos(self.dim * np.pi / 9)
        weight3 = 0.3 + 0.12 * np.cos(self.dim * np.pi / 11) + 0.03 * np.sin(self.dim * np.pi / 14)
        
        return weight1 * chaotic_component + weight2 * rbf_component + weight3 * hybrid_penalty * dim_scale + self.dim * 0.4 + noise
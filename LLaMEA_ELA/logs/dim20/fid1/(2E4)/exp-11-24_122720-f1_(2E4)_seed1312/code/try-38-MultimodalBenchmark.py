import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic oscillation component using logistic map-like behavior
        chaotic_component = 0
        for i in range(self.dim):
            # Logistic map-inspired chaotic sequence
            chaotic_param = 3.8 * np.sin(i * np.pi / (self.dim + 2)) + 0.1
            chaotic_component += np.sin(chaotic_param * x[i] * np.cos(x[i])) * np.cos(chaotic_param * x[i] * np.sin(x[i]))
        
        # Radial basis function with dynamic centers and adaptive widths
        rbf_component = 0
        for i in range(self.dim):
            center = 4 * np.sin(i * np.pi / (self.dim + 1)) * np.cos(i * np.pi / (self.dim + 3))
            width = 0.3 + 0.7 * np.cos(i * np.pi / (self.dim + 2))
            rbf_component += np.exp(-0.5 * ((x[i] - center) / width)**2) * (1 + 0.3 * np.sin(i * np.pi / 4))
        
        # Hybrid penalty term combining elliptic and hyperbolic components
        hybrid_penalty = 0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(i * np.pi / self.dim) + 0.2 * np.cos(i * np.pi / (self.dim + 1))
            elliptic_term = (x[i]**2) / (scale + 0.1)
            hyperbolic_term = np.tanh(x[i])**2
            hybrid_penalty += elliptic_term + 0.5 * hyperbolic_term
        
        # Dynamic scaling with chaotic modulation
        dim_scale = 1.0 + 0.2 * np.sin(self.dim * np.pi / 7) * np.cos(self.dim * np.pi / 5)
        
        # Combine components with dynamic weights
        weight1 = 0.4 + 0.3 * np.cos(self.dim * np.pi / 9)
        weight2 = 0.3 + 0.2 * np.sin(self.dim * np.pi / 6)
        weight3 = 0.3 + 0.1 * np.cos(self.dim * np.pi / 10)
        
        return weight1 * chaotic_component + weight2 * rbf_component + weight3 * hybrid_penalty * dim_scale + self.dim * 0.5
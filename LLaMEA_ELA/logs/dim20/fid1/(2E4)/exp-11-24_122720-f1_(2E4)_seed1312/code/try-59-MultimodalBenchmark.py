import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillation component with modified frequency scaling and higher-order interactions
        chaotic_component = 0
        for i in range(self.dim):
            # Modified logistic-like chaotic behavior with additional nonlinearities
            freq_scale = 4.0 * np.sin(i * np.pi / (self.dim + 3)) + 1.5
            term1 = np.sin(freq_scale * x[i] * np.cos(x[i]**2))
            term2 = np.cos(freq_scale * x[i]**2 * np.sin(x[i]))
            chaotic_component += term1 * term2 + 0.25 * np.sin(6 * freq_scale * x[i]) * np.cos(3 * freq_scale * x[i]**2)
        
        # Enhanced radial basis function with dynamic centers, adaptive widths, and cross-terms
        rbf_component = 0
        for i in range(self.dim):
            center = 3.5 * np.sin(i * np.pi / (self.dim + 2)) * np.cos(i * np.pi / (self.dim + 4))
            width = 0.15 + 0.7 * np.cos(i * np.pi / (self.dim + 3))
            # Add cross-terms between dimensions
            cross_term = sum(x[j] * np.sin(i * x[j]) for j in range(self.dim) if j != i)
            rbf_component += np.exp(-0.5 * ((x[i] - center) / width)**2) * (1 + 0.35 * np.sin(i * np.pi / 5) + 0.15 * cross_term)
        
        # Enhanced hybrid penalty term with additional conditioning components
        hybrid_penalty = 0
        for i in range(self.dim):
            scale = 1.2 + 0.6 * np.sin(i * np.pi / self.dim) + 0.1 * np.cos(i * np.pi / (self.dim + 2))
            elliptic_term = (x[i]**2) / (scale + 0.05)
            hyperbolic_term = np.tanh(x[i])**3
            polynomial_term = x[i]**6 - 3*x[i]**4 + 3*x[i]**2 - 1
            hybrid_penalty += elliptic_term + 0.4 * hyperbolic_term + 0.15 * polynomial_term
        
        # Dynamic scaling with enhanced modulation and noise injection
        dim_scale = 1.0 + 0.6 * np.sin(self.dim * np.pi / 8) * np.cos(self.dim * np.pi / 6)
        
        # Add adaptive noise to increase complexity
        noise = 0.03 * np.random.normal(0, 1)
        
        # Combine components with optimized weights
        weight1 = 0.35 + 0.25 * np.cos(self.dim * np.pi / 10) + 0.04 * np.sin(self.dim * np.pi / 13)
        weight2 = 0.45 + 0.2 * np.sin(self.dim * np.pi / 7) + 0.02 * np.cos(self.dim * np.pi / 9)
        weight3 = 0.4 + 0.15 * np.cos(self.dim * np.pi / 11) + 0.03 * np.sin(self.dim * np.pi / 14)
        
        return weight1 * chaotic_component + weight2 * rbf_component + weight3 * hybrid_penalty * dim_scale + self.dim * 0.4 + noise
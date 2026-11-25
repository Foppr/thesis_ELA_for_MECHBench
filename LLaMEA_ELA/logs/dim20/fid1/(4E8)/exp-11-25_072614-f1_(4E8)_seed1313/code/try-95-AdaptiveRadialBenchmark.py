import numpy as np

class AdaptiveRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic radial basis functions with higher frequency sinusoidal modulation and cross-terms
        rbfs = []
        centers = np.linspace(-4.8, 4.8, min(20, self.dim))
        widths = np.logspace(-1.5, 2.0, min(20, self.dim))
        phases = np.linspace(0, 5*np.pi, min(20, self.dim))
        
        for i, (center, width, phase) in enumerate(zip(centers, widths, phases)):
            if i < self.dim:
                # Hyperchaotic modulation with cubic, exponential, and trigonometric components
                rbf = np.exp(-np.sum((x - center)**2) / (2 * width**2)) * np.sin(phase * np.sum(x - center)**3) * np.cos(np.sum(x**2) * 0.1)
                rbfs.append(rbf)
        
        # Modified asymmetric gradient field with polynomial, hyperbolic, and cross-term components
        grad_field = np.sum((x - 1.5)**5 * np.tanh(x) + (x + 1.5)**5 * np.cosh(x)) / self.dim
        
        # Dynamic noise injection with chaotic scaling based on input magnitude, position, and interaction terms
        noise_level = 0.3 * (1 + np.mean(np.abs(x)) / 5.0) * (1 + 0.8 * np.cos(np.sum(x**2))) * (1 + 0.2 * np.sin(np.prod(x)))
        noise = np.random.normal(0, noise_level, self.dim)
        
        # Novel cross-term interaction components with enhanced nonlinearity
        cross_terms = np.sum((x[:-1] - x[1:])**6) / (self.dim - 1) if self.dim > 1 else 0
        
        # Combine components with adjusted weighting based on input characteristics and cross-terms
        rbf_sum = np.sum(rbfs) if rbfs else 0
        total = 0.35 * rbf_sum + 0.3 * grad_field + 0.25 * np.sum(noise**2) / self.dim + 0.1 * cross_terms
        
        return total
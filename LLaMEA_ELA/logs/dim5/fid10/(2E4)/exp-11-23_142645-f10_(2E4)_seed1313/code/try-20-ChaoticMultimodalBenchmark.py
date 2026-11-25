import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic component
        chaos = 0.0
        r = 3.99
        for i in range(10):
            x_ = np.roll(x, i % self.dim)
            chaos += np.sum(r * x_ * (1 - x_))
        
        # Multiquadratic terms with varying exponents
        quad_terms = np.sum((x**2 + 0.1 * x**4 + 0.01 * x**6))
        
        # Asymmetric sine-wave perturbations
        asym_sine = np.sum(np.sin(5.0 * x) * np.cos(7.0 * x) * np.abs(x))
        
        # Cross-term interactions with exponential decay
        cross_terms = np.sum(np.exp(-0.1 * np.abs(x)) * (x**3 + 0.5 * x**5))
        
        # Add noise-like component from shifted sine waves
        noise = np.sum(np.sin(2.0 * x + 1.0) + np.cos(3.0 * x - 1.0))
        
        return quad_terms + asym_sine + cross_terms + noise + 0.01 * chaos
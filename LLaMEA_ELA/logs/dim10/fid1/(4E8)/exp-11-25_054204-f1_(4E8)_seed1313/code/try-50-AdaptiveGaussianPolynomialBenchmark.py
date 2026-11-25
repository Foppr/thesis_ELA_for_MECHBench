import numpy as np

class AdaptiveGaussianPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for reuse
        self.centers = np.random.uniform(-4.0, 4.0, (10, dim))
        self.weights = np.random.exponential(1.0, 10)
        self.weights /= np.sum(self.weights)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian mixture component
        gaussian_sum = 0.0
        for i in range(10):
            diff = x - self.centers[i]
            distance_sq = np.sum(diff**2)
            gaussian_sum += self.weights[i] * np.exp(-0.5 * distance_sq / (0.5**2))
        
        # Adaptive polynomial terms with dimensionality-dependent exponents
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (i + 1) * x[i]**(3 + i % 3)
            
        # Directional cosine interaction term
        cos_interaction = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                cos_interaction += np.cos(x[i] * x[i+1]) * (i + 1)
                
        # Gradient-adaptive modulation
        grad_mod = 1.0
        if self.dim > 1:
            grad_magnitude = np.sqrt(np.sum(np.gradient(x)**2))
            grad_mod = 1.0 + 0.5 * np.sin(grad_magnitude)
            
        # Cross-dimension coupling with varying strength
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += 0.1 * (i + 1) * (j + 1) * x[i] * x[j]
                
        # Nonlinear correlation with exponential decay
        exp_corr = np.sum(np.exp(-x**2) * x)
        
        return gaussian_sum + poly_term * grad_mod + cross_coupling + exp_corr
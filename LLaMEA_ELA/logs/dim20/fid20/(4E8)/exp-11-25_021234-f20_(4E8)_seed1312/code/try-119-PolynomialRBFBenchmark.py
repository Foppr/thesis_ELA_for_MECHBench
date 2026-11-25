import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random centers for RBFs
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        # Generate random weights for polynomial terms
        self.poly_weights = np.random.uniform(-1.0, 1.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion term (sparse grid approximation)
        f1 = 0.0
        for i in range(self.dim):
            f1 += self.poly_weights[i] * (x[i] ** 3) + 0.5 * (x[i] ** 2) + 0.1 * x[i]
        
        # Radial Basis Function component with varying widths
        f2 = 0.0
        for i in range(10):  # 10 RBF centers
            center = self.rbf_centers[i]
            sigma = 0.5 + 0.5 * np.sin(i)  # Adaptive width
            rbf_value = np.exp(-np.sum((x - center)**2) / (2 * sigma**2))
            f2 += rbf_value * (1.0 + 0.3 * np.cos(2.0 * i))
        
        # Adaptive conditioning based on distance from origin
        dist_from_origin = np.sqrt(np.sum(x**2))
        condition_factor = 1.0 + 0.8 * np.sin(dist_from_origin)
        
        # Cross-terms with varying coupling strengths
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.5 * np.cos(0.2 * (i + j))
                f3 += coupling * np.sin(x[i]) * np.cos(x[j])
        
        # Multi-scale oscillatory component
        f4 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.1 * i)
            amp = 1.0 + 0.5 * np.cos(0.3 * i)
            f4 += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Asymmetric penalty terms
        f5 = 0.0
        for i in range(self.dim):
            if x[i] > 0:
                penalty = 2.0 * x[i]**2
            else:
                penalty = 1.5 * x[i]**2
            f5 += penalty * (1.0 + 0.2 * np.sin(3.0 * x[i]))
        
        # Saddle point interactions with non-uniform coupling
        f6 = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                strength = 0.3 + 0.4 * np.sin(0.5 * i)
                f6 += strength * np.sin(x[i]) * np.sin(x[i+1])
        
        return condition_factor * (f1 + f2 + f3 + f4 + f5 + f6)
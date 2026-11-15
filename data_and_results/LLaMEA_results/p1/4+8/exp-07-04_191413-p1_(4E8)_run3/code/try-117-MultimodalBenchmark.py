import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for radial basis functions
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.weights = np.random.uniform(0.5, 2.0, 10)
        self.sigmas = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Polynomial chaos expansion component
        poly_term = np.sum(x**4 - 6*x**2 + 8*x)
        
        # Radial basis function component with multiple centers
        rbf_sum = 0.0
        for i in range(10):
            dist = np.sum((x - self.centers[i])**2)
            rbf_sum += self.weights[i] * np.exp(-dist / (2 * self.sigmas[i]**2))
        
        # Cross-dimensional coupling with trigonometric modulation
        coupling = 0.0
        for i in range(self.dim-1):
            coupling += np.sin(x[i]) * np.cos(x[i+1]) * (i+1) / self.dim
        
        # Fractional power and exponential scaling for conditioning
        frac_term = np.sum(np.abs(x)**1.5) * np.exp(-0.1 * np.sum(x**2))
        
        # Hyperbolic tangent modulation to create sharp fitness transitions
        tanh_mod = np.sum(np.tanh(x)**3)
        
        # Add a chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10 * np.pi * x[i]) * np.cos(7 * np.pi * x[i]) * np.sin(5 * np.pi * x[i])
        
        # Combine all terms with varying weights
        return poly_term + 0.5 * rbf_sum + 0.3 * coupling + 0.2 * frac_term + 0.1 * tanh_mod + 0.15 * chaotic
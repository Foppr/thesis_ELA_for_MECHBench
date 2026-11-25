import numpy as np

class RadialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive centers for radial basis functions
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        # Initialize varying bandwidths
        self.bandwidths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(10):
            center = self.centers[i]
            bandwidth = self.bandwidths[i]
            rbf_sum += np.exp(-np.sum(((x - center) ** 2) / (2 * bandwidth ** 2)))
        
        # Chaotic perturbation using a gradient-based logistic map
        chaotic_perturbation = 0.0
        r = 3.8
        for i in range(self.dim):
            if i == 0:
                prev_x = x[i]
            else:
                prev_x = x[i-1]
            # Gradient-based chaotic component
            grad = np.cos(prev_x) * np.sin(x[i]) if i < self.dim - 1 else 0.0
            chaotic_perturbation += r * prev_x * (1 - prev_x) + grad
        
        # Polynomial interaction terms
        poly_interaction = np.sum(x ** 3 + 0.5 * x ** 2 - 0.3 * x + 0.1)
        
        # Cross-term interaction with sinusoidal modulation
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            cross_interaction += (x[i] * x[i+1]) * np.sin(x[i] + x[i+1])
        
        # Combine all terms
        return 0.4 * rbf_sum + 0.3 * chaotic_perturbation + 0.2 * poly_interaction + 0.1 * cross_interaction
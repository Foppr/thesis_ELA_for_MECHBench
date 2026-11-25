import numpy as np

class ChaoticArnoldCatBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random weights for radial basis functions
        self.rbf_weights = np.random.uniform(-2.0, 2.0, dim)
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_bandwidths = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Arnold cat map chaotic component
        cat_map = 0.0
        for i in range(self.dim):
            if i == 0:
                cat_map += x[i] + x[(i+1) % self.dim]
            else:
                cat_map += x[i-1] + x[(i+1) % self.dim]
            cat_map = cat_map % 1.0
        
        # Exponential radial basis function with adaptive bandwidths
        rbf = 0.0
        for i in range(self.dim):
            diff = x - self.rbf_centers[i]
            rbf += self.rbf_weights[i] * np.exp(-0.5 * np.sum(diff**2) / (self.rbf_bandwidths[i]**2))
        
        # Gradient-enhanced polynomial terms with mixed degrees
        poly = 0.0
        for i in range(self.dim):
            if i % 4 == 0:
                poly += x[i]**6 * np.sin(x[i])
            elif i % 4 == 1:
                poly += x[i]**5 * np.cos(x[i])
            elif i % 4 == 2:
                poly += x[i]**4 * np.tan(x[i])
            else:
                poly += x[i]**3 * np.exp(-x[i]**2)
        
        # Cross-dimensional coupling with trigonometric interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.sin(x[i] * x[j]) * (i + j + 1)
        
        # Adaptive noise modulation with dynamic variance
        noise_mod = np.random.normal(0, 0.1 * np.mean(np.abs(x)), 1)[0]
        
        return cat_map + rbf + poly + cross_coupling + noise_mod
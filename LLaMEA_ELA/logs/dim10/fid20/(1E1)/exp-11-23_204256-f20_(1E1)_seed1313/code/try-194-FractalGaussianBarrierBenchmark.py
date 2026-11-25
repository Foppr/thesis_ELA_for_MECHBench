import numpy as np

class FractalGaussianBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian mixture centers and covariances for different scales
        self.scales = [1.0, 0.5, 0.25, 0.125]
        self.gaussians = []
        for scale in self.scales:
            center = np.random.uniform(-scale, scale, dim)
            cov = np.diag([scale**2] * dim)
            self.gaussians.append((center, cov))
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal Gaussian mixture with varying scales
        fitness = 0.0
        for center, cov in self.gaussians:
            diff = x_norm - center
            exponent = -0.5 * np.dot(diff, np.linalg.solve(cov, diff))
            fitness += np.exp(exponent)
        
        # Add logarithmic barrier terms that become very large near boundaries
        barrier = 0.0
        for i in range(self.dim):
            barrier += np.log(1.0 + np.exp(5.0 * (1.0 - abs(x_norm[i]))))
        
        # Introduce fractal self-similarity through recursive scaling
        scale_factor = 1.0
        for _ in range(3):  # Triple recursive scaling
            scale_factor *= 0.5
            for i in range(self.dim):
                xi = x_norm[i] * scale_factor
                fitness += scale_factor * np.sin(xi * np.pi) * np.cos(xi * np.pi / 2.0)
        
        # Combine all components with adaptive weighting
        return fitness + barrier + 0.1 * np.sum(x_norm**4)
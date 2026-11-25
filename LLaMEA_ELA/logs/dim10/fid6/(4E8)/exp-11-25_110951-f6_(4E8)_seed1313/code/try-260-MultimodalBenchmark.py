import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for performance
        self.mu = np.random.uniform(-2, 2, (10, dim))
        self.sigma = np.random.uniform(0.5, 2.0, (10, dim))
        self.weights = np.random.dirichlet(np.ones(10))
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Gaussian mixture component
        gaussian = 0.0
        for i in range(10):
            diff = x_norm - self.mu[i]
            exponent = -0.5 * np.sum((diff / self.sigma[i])**2)
            gaussian += self.weights[i] * np.exp(exponent)
        
        # Trigonometric chaos component
        trig_chaos = 0.0
        for i in range(self.dim):
            trig_chaos += np.sin(10 * x_norm[i]) * np.cos(7 * x_norm[i]) * \
                         (1.0 + 0.3 * np.sin(15 * x_norm[i]))
        
        # Adaptive conditioning based on distance from origin
        dist_from_origin = np.sqrt(np.sum(x_norm**2))
        condition_factor = 1.0 + 2.0 * np.exp(-dist_from_origin)
        
        # Cross-dimensional interaction with dynamic coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(5 * (x_norm[i] + x_norm[j])) * \
                          np.cos(3 * (x_norm[i] - x_norm[j]))
                cross_interaction += coupling * (1.0 + 0.2 * np.sin(8 * x_norm[i]))
        
        # Asymmetric saddle-like structure
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x_norm[i]**4) - 2 * (x_norm[i]**2) + 0.5 * np.sin(12 * x_norm[i])
        
        # Final hybrid landscape
        return condition_factor * (gaussian + 0.3 * trig_chaos + 0.2 * cross_interaction + 0.4 * saddle)
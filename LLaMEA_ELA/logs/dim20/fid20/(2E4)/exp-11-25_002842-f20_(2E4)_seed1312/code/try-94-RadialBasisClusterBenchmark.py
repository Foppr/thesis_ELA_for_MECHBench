import numpy as np

class RadialBasisClusterBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize cluster centers in [-5, 5]^dim
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        # Initialize adaptive weights for each dimension
        self.weights = np.random.uniform(0.5, 2.0, dim)
        # Dynamic penalty parameters
        self.penalty_strength = np.random.uniform(1.0, 5.0)
        self.cluster_scale = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Radial basis function components
        rbf_sum = 0.0
        for i in range(10):
            dist = np.linalg.norm(x - self.centers[i])
            rbf_sum += self.cluster_scale[i] * np.exp(-dist**2 / (2 * 1.0**2))
        
        # Adaptive weighted distance from origin
        weighted_dist = np.sum(self.weights * np.abs(x))
        
        # Dynamic penalty based on distance from cluster centers
        min_dist = np.min([np.linalg.norm(x - center) for center in self.centers])
        penalty = self.penalty_strength * (1.0 / (min_dist + 0.1)) ** 2
        
        # Multi-scale harmonic modulation
        harmonic_mod = 0.0
        scales = [1.0, 2.0, 3.0]
        for scale in scales:
            harmonic_mod += np.sum(np.sin(scale * x) * np.cos(scale * x))
        
        # Dimensionality-dependent conditioning
        condition_factor = 1.0 + 0.5 * np.std(x)
        
        # Combine all components with dynamic scaling
        return (0.3 * rbf_sum + 
                0.4 * weighted_dist + 
                0.2 * penalty + 
                0.1 * harmonic_mod * condition_factor)
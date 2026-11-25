import numpy as np

class GaussianSinusoidalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Global optimum at origin
        global_optimum = np.zeros(self.dim)
        
        # Gaussian mixture components with different centers and variances
        centers = [
            np.zeros(self.dim),
            np.ones(self.dim) * 0.5,
            np.ones(self.dim) * -0.5,
            np.ones(self.dim) * 0.3,
            np.ones(self.dim) * -0.3,
            np.ones(self.dim) * 0.7,
            np.ones(self.dim) * -0.7
        ]
        
        # Compute Gaussian components
        gaussians = []
        for center in centers:
            # Different variances for each component
            variance = 0.1 + 0.3 * np.random.rand()
            gaussian = np.exp(-0.5 * np.sum(((x_scaled - center) / variance) ** 2))
            gaussians.append(gaussian)
        
        # Combine Gaussian components with weights
        weights = [0.15, 0.12, 0.12, 0.1, 0.1, 0.13, 0.18]
        gaussian_sum = np.sum([w * g for w, g in zip(weights, gaussians)])
        
        # Add sinusoidal modulations with varying frequencies
        sin_modulation = np.sum(np.sin(10 * x_scaled) * np.cos(8 * x_scaled)) + \
                        0.5 * np.sum(np.sin(15 * x_scaled) * np.cos(12 * x_scaled)) + \
                        0.3 * np.sum(np.sin(20 * x_scaled) * np.cos(18 * x_scaled))
        
        # Radial symmetry component with polynomial and trigonometric terms
        r = np.sqrt(np.sum(x_scaled**2))
        radial_component = 0.5 * r**2 + 0.3 * np.sin(5 * r) + 0.2 * np.cos(3 * r)
        
        # Cross-dimensional coupling with interaction terms
        cross_coupling = 0.1 * np.sum((x_scaled[:-1] * x_scaled[1:]) ** 2) + \
                        0.05 * np.sum(np.abs(x_scaled[:-1] - x_scaled[1:]))
        
        # Add noise component for increased complexity
        noise = 0.05 * np.random.rand()
        
        # Combine all components with optimized weights
        return 0.4 * gaussian_sum + 0.3 * sin_modulation + 0.2 * radial_component + 0.05 * cross_coupling + noise
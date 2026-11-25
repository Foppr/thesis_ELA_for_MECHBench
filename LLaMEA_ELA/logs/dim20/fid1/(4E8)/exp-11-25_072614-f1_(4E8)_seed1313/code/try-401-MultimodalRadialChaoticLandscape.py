import numpy as np

class MultimodalRadialChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.omega = np.array([0.5 + 0.3 * np.sin(0.7 * np.pi * i) for i in range(dim)])
        self.gamma = np.array([0.8 + 0.2 * np.cos(0.6 * np.pi * i) for i in range(dim)])
        self.alpha = np.array([1.0 + 0.5 * np.sin(0.9 * np.pi * i) for i in range(dim)])
        # Radial basis function centers and widths
        self.centers = np.random.uniform(-4.0, 4.0, dim)
        self.widths = np.array([0.5 + 0.3 * np.sin(0.8 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric oscillation component
        trig_component = 0.0
        for i in range(self.dim):
            trig_component += self.alpha[i] * np.sin(self.omega[i] * x[i] + self.gamma[i] * np.sum(x)) * np.exp(-0.1 * x[i]**2)
        trig_component /= self.dim
        
        # Radial basis function component
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_component += np.exp(-0.5 * ((x[i] - self.centers[i]) / self.widths[i])**2)
        rbf_component /= self.dim
        
        # Adaptive conditioning with chaotic modulation
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.3 * np.sin(0.6 * np.pi * i + 0.4 * np.sum(x))
            conditioning += cond_factor * x[i]**2 * np.exp(-0.05 * x[i]**2)
        conditioning /= self.dim
        
        # Cross-dimensional interaction with chaotic coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.3 * np.sin(0.4 * np.pi * (i - j) + 0.2 * np.sum(x))
                cross_interaction += coupling * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        cross_interaction /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-scale chaotic modulation
        chaotic_modulation = 0.0
        for i in range(self.dim):
            mod_factor = 1.0 + 0.4 * np.sin(0.8 * np.pi * i + 0.3 * np.sum(x) + 0.2 * np.sin(0.5 * np.sum(x)))
            chaotic_modulation += mod_factor * np.cos(x[i] + 0.1 * np.sum(x)) * np.exp(-0.15 * x[i]**2)
        chaotic_modulation /= self.dim
        
        # Combine all components with adaptive weighting
        result = 0.3 * trig_component + 0.25 * rbf_component + 0.2 * conditioning + 0.15 * cross_interaction + 0.1 * chaotic_modulation
        
        return result
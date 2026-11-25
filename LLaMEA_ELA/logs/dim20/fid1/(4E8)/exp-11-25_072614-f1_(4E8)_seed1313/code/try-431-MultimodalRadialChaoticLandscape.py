import numpy as np

class MultimodalRadialChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with enhanced diversity and complexity
        self.omega = np.array([0.8 + 0.3 * np.sin(1.2 * np.pi * i) for i in range(dim)])
        self.gamma = np.array([0.95 + 0.15 * np.cos(0.7 * np.pi * i) for i in range(dim)])
        self.alpha = np.array([1.3 + 0.4 * np.sin(1.1 * np.pi * i) for i in range(dim)])
        # Radial basis function centers and widths with increased variability
        self.centers = np.random.uniform(-4.8, 4.8, dim)
        self.widths = np.array([0.7 + 0.3 * np.sin(1.0 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced trigonometric oscillation component with increased complexity
        trig_component = 0.0
        for i in range(self.dim):
            trig_component += self.alpha[i] * np.sin(self.omega[i] * x[i] + self.gamma[i] * np.sum(x)) * np.exp(-0.15 * x[i]**2)
        trig_component /= self.dim
        
        # Improved radial basis function component with stronger interaction
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_component += np.exp(-0.3 * ((x[i] - self.centers[i]) / self.widths[i])**2)
        rbf_component /= self.dim
        
        # Enhanced adaptive conditioning with stronger chaotic modulation
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.5 * np.sin(0.8 * np.pi * i + 0.6 * np.sum(x))
            conditioning += cond_factor * x[i]**2 * np.exp(-0.08 * x[i]**2)
        conditioning /= self.dim
        
        # Stronger cross-dimensional interaction with novel coupling mechanism
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.7 + 0.3 * np.sin(0.6 * np.pi * (i - j) + 0.4 * np.sum(x))
                cross_interaction += coupling * np.sin(x[i] * x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2))
        cross_interaction /= (self.dim * (self.dim - 1) / 2.0)
        
        # Advanced chaotic modulation with multiple phase shifts
        chaotic_modulation = 0.0
        for i in range(self.dim):
            mod_factor = 1.0 + 0.6 * np.sin(1.0 * np.pi * i + 0.5 * np.sum(x) + 0.4 * np.sin(0.7 * np.sum(x)))
            chaotic_modulation += mod_factor * np.cos(x[i] + 0.2 * np.sum(x)) * np.exp(-0.2 * x[i]**2)
        chaotic_modulation /= self.dim
        
        # Combine all components with refined weighting for better discrimination
        result = 0.4 * trig_component + 0.15 * rbf_component + 0.25 * conditioning + 0.15 * cross_interaction + 0.05 * chaotic_modulation
        
        return result
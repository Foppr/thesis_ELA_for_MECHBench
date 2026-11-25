import numpy as np

class MultimodalRadialChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters with stronger modulation and dynamic phase shifts
        self.omega = np.array([1.0 + 0.5 * np.sin(1.2 * np.pi * i) for i in range(dim)])
        self.gamma = np.array([1.1 + 0.2 * np.cos(0.8 * np.pi * i) for i in range(dim)])
        self.alpha = np.array([1.5 + 0.4 * np.sin(1.3 * np.pi * i) for i in range(dim)])
        # Radial basis function centers and widths with increased variability
        self.centers = np.random.uniform(-4.8, 4.8, dim)
        self.widths = np.array([0.8 + 0.3 * np.sin(1.1 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced trigonometric oscillation component with stronger coupling
        trig_component = 0.0
        for i in range(self.dim):
            trig_component += self.alpha[i] * np.sin(self.omega[i] * x[i] + self.gamma[i] * np.sum(x)) * np.exp(-0.15 * x[i]**2)
        trig_component /= self.dim
        
        # Enhanced radial basis function component with multi-scale interactions
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_component += np.exp(-0.3 * ((x[i] - self.centers[i]) / self.widths[i])**2) + 0.5 * np.sin(2.0 * x[i])
        rbf_component /= self.dim
        
        # Stronger adaptive conditioning with exponential modulation
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.6 * np.sin(0.8 * np.pi * i + 0.6 * np.sum(x)) + 0.3 * np.cos(1.5 * x[i])
            conditioning += cond_factor * x[i]**2 * np.exp(-0.08 * x[i]**2) + 0.2 * np.sin(3.0 * x[i])
        conditioning /= self.dim
        
        # Cross-dimensional interaction with chaotic coupling and multi-scale interactions
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.8 + 0.3 * np.sin(0.7 * np.pi * (i - j) + 0.4 * np.sum(x)) + 0.2 * np.cos(1.2 * x[i] * x[j])
                cross_interaction += coupling * np.sin(x[i] * x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2))
        cross_interaction /= (self.dim * (self.dim - 1) / 2.0)
        
        # Novel chaotic modulation with multi-frequency interactions
        chaotic_modulation = 0.0
        for i in range(self.dim):
            mod_factor = 1.0 + 0.7 * np.sin(1.1 * np.pi * i + 0.5 * np.sum(x) + 0.4 * np.sin(0.8 * np.sum(x)) + 0.3 * np.cos(1.3 * x[i]))
            chaotic_modulation += mod_factor * np.cos(x[i] + 0.2 * np.sum(x)) * np.exp(-0.2 * x[i]**2) + 0.4 * np.sin(2.5 * x[i])
        chaotic_modulation /= self.dim
        
        # Combine all components with updated weighting
        result = 0.3 * trig_component + 0.25 * rbf_component + 0.2 * conditioning + 0.15 * cross_interaction + 0.1 * chaotic_modulation
        
        return result
import numpy as np

class MultimodalRadialChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters with dynamic phase shifts
        self.omega = np.array([0.7 + 0.4 * np.sin(0.9 * np.pi * i) for i in range(dim)])
        self.gamma = np.array([1.0 + 0.3 * np.cos(0.7 * np.pi * i) for i in range(dim)])
        self.alpha = np.array([1.2 + 0.6 * np.sin(1.1 * np.pi * i) for i in range(dim)])
        # Dynamic radial basis function centers and widths
        self.centers = np.random.uniform(-4.5, 4.5, dim)
        self.widths = np.array([0.7 + 0.4 * np.sin(0.9 * np.pi * i) for i in range(dim)])
        # Additional chaotic modulation parameters
        self.phi = np.array([0.2 + 0.3 * np.cos(0.5 * np.pi * i) for i in range(dim)])
        self.psi = np.array([0.1 + 0.2 * np.sin(0.8 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced trigonometric oscillation component
        trig_component = 0.0
        for i in range(self.dim):
            phase_shift = self.phi[i] * np.sin(0.3 * np.sum(x))
            trig_component += self.alpha[i] * np.sin(self.omega[i] * x[i] + self.gamma[i] * np.sum(x) + phase_shift) * np.exp(-0.12 * x[i]**2)
        trig_component /= self.dim
        
        # Enhanced radial basis function component
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_component += np.exp(-0.5 * ((x[i] - self.centers[i]) / self.widths[i])**2) * (1.0 + 0.2 * np.sin(0.6 * np.pi * i + 0.3 * np.sum(x)))
        rbf_component /= self.dim
        
        # Enhanced adaptive conditioning with chaotic modulation
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.4 * np.sin(0.7 * np.pi * i + 0.5 * np.sum(x) + self.psi[i] * np.cos(0.4 * np.sum(x)))
            conditioning += cond_factor * x[i]**2 * np.exp(-0.06 * x[i]**2)
        conditioning /= self.dim
        
        # Enhanced cross-dimensional interaction with dynamic coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.6 + 0.4 * np.sin(0.5 * np.pi * (i - j) + 0.3 * np.sum(x) + 0.2 * np.cos(0.7 * np.sum(x)))
                cross_interaction += coupling * np.sin(x[i] * x[j]) * np.exp(-0.12 * (x[i]**2 + x[j]**2))
        cross_interaction /= (self.dim * (self.dim - 1) / 2.0)
        
        # Enhanced multi-scale chaotic modulation
        chaotic_modulation = 0.0
        for i in range(self.dim):
            mod_factor = 1.0 + 0.5 * np.sin(0.9 * np.pi * i + 0.4 * np.sum(x) + 0.3 * np.cos(0.6 * np.sum(x)) + 0.2 * np.sin(0.8 * np.sum(x)))
            chaotic_modulation += mod_factor * np.cos(x[i] + 0.15 * np.sum(x)) * np.exp(-0.2 * x[i]**2)
        chaotic_modulation /= self.dim
        
        # Novel hybrid interaction term
        hybrid_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                hybrid_factor = 0.3 + 0.2 * np.sin(0.4 * np.pi * (i + j) + 0.5 * np.sum(x))
                hybrid_interaction += hybrid_factor * (np.sin(x[i]) * np.cos(x[j]) + np.cos(x[i]) * np.sin(x[j])) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
        hybrid_interaction /= (self.dim * (self.dim - 1) / 2.0)
        
        # Combine all components with enhanced weighting
        result = 0.25 * trig_component + 0.3 * rbf_component + 0.2 * conditioning + 0.15 * cross_interaction + 0.08 * chaotic_modulation + 0.02 * hybrid_interaction
        
        return result
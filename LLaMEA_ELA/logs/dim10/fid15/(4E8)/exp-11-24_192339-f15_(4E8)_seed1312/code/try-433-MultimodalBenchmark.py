import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation angles for chaotic rotation
        self.angles = np.array([np.pi * (i ** 1.3) / dim for i in range(dim)])
        # Multi-scale periodicity parameters
        self.periods = np.array([2.0 + 1.5 * np.sin(i * 0.5) for i in range(dim)])
        # Bifurcation control parameters
        self.bifurcations = np.array([0.5 + 0.3 * np.cos(i * 0.4) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic rotation component
        rotated = np.zeros_like(x)
        for i in range(self.dim):
            rot_sum = 0
            for j in range(self.dim):
                rot_sum += x[j] * np.cos(self.angles[i] + j * 0.1)
            rotated[i] = rot_sum
        
        # Multi-scale periodic potentials with bifurcation modulation
        potential = 0
        for i in range(self.dim):
            period = self.periods[i % len(self.periods)]
            bifur = self.bifurcations[i % len(self.bifurcations)]
            # Saddle-node bifurcation pattern
            node = np.abs(x[i]) - bifur
            # Periodic modulation
            periodic = np.sin(period * x[i]) * np.cos(period * x[i]**2)
            # Combined potential
            potential += (node**2 * np.exp(-0.1 * node**2) + 
                         0.5 * periodic * np.exp(-0.05 * x[i]**2))
        
        # Dynamic conditioning with exponential modulation
        conditioning = 0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.5 * np.sin(0.3 * x[i]) * np.cos(0.7 * x[i])
            conditioning += (x[i]**2) * cond_factor
        
        # Embedded chaotic attractor with multi-scale coupling
        attractor = 0
        for i in range(self.dim):
            # Logistic map-like dynamics
            logistic = 4.0 * np.abs(x[i] - 0.5) * (1 - np.abs(x[i] - 0.5))
            attractor += logistic * np.exp(-0.2 * x[i]**2)
        
        # Cross-term coupling with rotation-invariance breaking
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j]) * np.sin(0.5 * (x[i] + x[j]))
        
        # Combine all components with dynamic weighting
        weights = [0.35, 0.25, 0.20, 0.15 + 0.05 * np.sin(sum(x))]
        return (weights[0] * potential + 
                weights[1] * conditioning + 
                weights[2] * attractor + 
                weights[3] * cross_term)
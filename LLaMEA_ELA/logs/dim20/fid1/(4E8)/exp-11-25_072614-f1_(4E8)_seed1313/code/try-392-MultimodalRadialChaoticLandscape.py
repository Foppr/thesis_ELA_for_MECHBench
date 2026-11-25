import numpy as np

class MultimodalRadialChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive conditioning parameters with enhanced chaos
        self.conditioning = np.array([1.0 + 0.7 * np.sin(0.4 * np.pi * i) for i in range(dim)])
        self.frequency = np.array([2.5 + 2.0 * np.cos(0.5 * np.pi * i) for i in range(dim)])
        self.amplitude = np.array([1.2 + 0.4 * np.sin(0.6 * np.pi * i) for i in range(dim)])
        # Radial basis function centers and widths with increased diversity
        self.centers = np.random.uniform(-4.5, 4.5, (dim, dim))
        self.widths = np.array([0.6 + 0.4 * np.cos(0.3 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal oscillation component with higher frequency modulation
        sin_component = 0.0
        for i in range(self.dim):
            sin_component += self.amplitude[i] * np.sin(self.frequency[i] * x[i]) * np.exp(-0.12 * x[i]**2)
        sin_component /= self.dim
        
        # Improved radial basis function component with multi-scale widths
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_term = 0.0
            for j in range(self.dim):
                diff = x[j] - self.centers[i, j]
                rbf_term += np.exp(-0.5 * (diff**2) / (self.widths[i]**2))
            rbf_component += rbf_term
        rbf_component /= self.dim
        
        # Enhanced chaotic conditioning with stronger coupling
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += self.conditioning[i] * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.08 * x[i]**2)
        chaotic_component /= self.dim
        
        # Stronger cross-dimensional interaction with multi-scale coupling
        cross_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.7 * (x[i] + x.j)) * np.cos(0.4 * (x[i] - x[j]))
                cross_component += coupling * np.exp(-0.15 * (x[i]**2 + x[j]**2))
        cross_component /= (self.dim * (self.dim - 1) / 2.0)
        
        # Enhanced adaptive fitness landscape with multiple local minima and saddle points
        adaptive_component = 0.0
        for i in range(self.dim):
            adaptive_component += (x[i]**8 - 4.0 * x[i]**6 + 6.0 * x[i]**4 - 4.0 * x[i]**2) * np.exp(-0.2 * x[i]**2)
        adaptive_component /= self.dim
        
        # Dynamic weighting with improved balance
        total = 0.25 * sin_component + 0.35 * rbf_component + 0.2 * chaotic_component + 0.1 * cross_component + 0.1 * adaptive_component
        
        return total
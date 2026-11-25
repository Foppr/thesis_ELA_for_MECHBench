import numpy as np

class ExponentialWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with dimension-dependent base
        exp_component = 0
        for i in range(self.dim):
            base = 1.5 + 0.5 * np.sin(i * np.pi / (self.dim + 2))
            exp_component += np.exp(-base * abs(x[i])) * np.cos(i * np.pi / (self.dim + 1) * x[i])
        
        # Sinusoidal wave interference component with varying frequencies
        wave_component = 0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(i * np.pi / (self.dim + 3))
            wave_component += np.sin(freq * x[i]) * np.cos(i * np.pi / (self.dim + 4) * x[i])
        
        # Adaptive elliptic shaping with dynamic eccentricity
        ellipse_component = 0
        for i in range(self.dim):
            eccentricity = 0.5 + 0.3 * np.sin(i * np.pi / (self.dim + 5))
            ellipse_component += (x[i]**2) / (1.0 + eccentricity * np.cos(i * np.pi / (self.dim + 6))**2)
        
        # Cross-term interaction with exponential coupling
        cross_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.5 * (x[i]**2 + x[j]**2))
                cross_component += coupling * np.sin(x[i] * x[j])
        
        # Global scaling factor based on dimensionality
        scale_factor = 1.0 + 0.2 * np.sin(self.dim * np.pi / 8)
        
        # Combine components with dynamic weights
        weight1 = 0.3 + 0.1 * np.sin(self.dim * np.pi / 7)
        weight2 = 0.25 + 0.15 * np.cos(self.dim * np.pi / 6)
        weight3 = 0.2 + 0.1 * np.sin(self.dim * np.pi / 5)
        weight4 = 0.25 + 0.1 * np.cos(self.dim * np.pi / 4)
        
        return scale_factor * (weight1 * exp_component + weight2 * wave_component + 
                              weight3 * ellipse_component + weight4 * cross_component)
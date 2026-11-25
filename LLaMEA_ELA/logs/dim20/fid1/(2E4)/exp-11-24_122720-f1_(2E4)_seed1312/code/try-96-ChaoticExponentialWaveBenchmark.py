import numpy as np

class ChaoticExponentialWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic exponential decay component with fractional Brownian motion effects
        exp_component = 0
        for i in range(self.dim):
            base = 1.5 + 0.5 * np.sin(i * np.pi / (self.dim + 2) + np.cos(i * np.pi / (self.dim + 3)))
            exp_component += np.exp(-base * abs(x[i])) * np.cos(i * np.pi / (self.dim + 1) * x[i] + 
                                                              np.sin(x[i] * np.pi / (self.dim + 4)))
        
        # Quantum-inspired wave interference with adaptive frequencies
        wave_component = 0
        for i in range(self.dim):
            freq = 2.0 + 2.5 * np.sin(i * np.pi / (self.dim + 3) + np.cos(i * np.pi / (self.dim + 5)))
            wave_component += np.sin(freq * x[i]) * np.cos(i * np.pi / (self.dim + 4) * x[i] + 
                                                          np.sin(x[i] * np.pi / (self.dim + 6)))
        
        # Dynamic elliptic shaping with memory-dependent eccentricity
        ellipse_component = 0
        for i in range(self.dim):
            eccentricity = 0.2 + 0.8 * np.sin(i * np.pi / (self.dim + 5) + np.cos(i * np.pi / (self.dim + 7)))
            ellipse_component += (x[i]**2) / (1.0 + eccentricity * np.cos(i * np.pi / (self.dim + 6))**2 + 
                                            0.1 * np.sin(x[i] * np.pi / (self.dim + 8)))
        
        # Cross-term interaction with chaotic coupling
        cross_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.5 * (x[i]**2 + x[j]**2)) * (1.0 + 0.3 * np.sin(x[i] * x[j]))
                cross_component += coupling * np.sin(x[i] * x[j] + np.cos(x[i] + x[j]))
        
        # Fractal-like scaling factor with chaotic modulation
        scale_factor = 1.2 + 0.8 * np.sin(self.dim * np.pi / 8 + np.cos(self.dim * np.pi / 9))
        
        # Combine components with chaotic weights
        weight1 = 0.3 + 0.1 * np.sin(self.dim * np.pi / 7 + np.cos(self.dim * np.pi / 10))
        weight2 = 0.25 + 0.15 * np.cos(self.dim * np.pi / 6 + np.sin(self.dim * np.pi / 11))
        weight3 = 0.2 + 0.1 * np.sin(self.dim * np.pi / 5 + np.cos(self.dim * np.pi / 12))
        weight4 = 0.25 + 0.15 * np.cos(self.dim * np.pi / 4 + np.sin(self.dim * np.pi / 13))
        
        # Add a global minimum modifier to improve fitness
        global_min_modifier = 0.1 * np.sum(np.abs(x))
        
        return scale_factor * (weight1 * exp_component + weight2 * wave_component + 
                              weight3 * ellipse_component + weight4 * cross_component) + global_min_modifier
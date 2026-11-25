import numpy as np

class ChaoticSineWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave component with dynamic frequency modulation
        sine_component = 0
        for i in range(self.dim):
            freq_mod = 2.0 + 1.5 * np.sin(i * np.pi / (self.dim + 1) + np.cos(i * np.pi / (self.dim + 3)))
            sine_component += np.sin(freq_mod * x[i] + np.sin(x[i])) * np.cos(i * np.pi / (self.dim + 2) * x[i])
        
        # Adaptive elliptic shaping with fractal-like eccentricity
        ellipse_component = 0
        for i in range(self.dim):
            eccentricity = 0.3 + 0.4 * np.sin(i * np.pi / (self.dim + 4) + np.cos(i * np.pi / (self.dim + 6)))
            ellipse_component += (x[i]**2) / (1.0 + eccentricity * np.sin(i * np.pi / (self.dim + 5))**2)
        
        # Cross-term interaction with chaotic coupling
        cross_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.5 * (x[i]**2 + x[j]**2)) * np.cos(x[i] * x[j])
                cross_component += coupling * np.exp(-0.1 * abs(x[i] - x[j]))
        
        # Fractal-like exponential decay with chaotic base
        exp_component = 0
        for i in range(self.dim):
            base = 1.2 + 0.8 * np.sin(i * np.pi / (self.dim + 7) + np.cos(i * np.pi / (self.dim + 9)))
            exp_component += np.exp(-base * abs(x[i])) * np.sin(i * np.pi / (self.dim + 8) * x[i])
        
        # Global scaling factor with chaotic modulation
        scale_factor = 1.5 + 0.5 * np.sin(self.dim * np.pi / 9 + np.cos(self.dim * np.pi / 11))
        
        # Dynamic weights with chaotic variation
        weight1 = 0.25 + 0.1 * np.sin(self.dim * np.pi / 8 + np.cos(self.dim * np.pi / 10))
        weight2 = 0.3 + 0.15 * np.sin(self.dim * np.pi / 7 + np.cos(self.dim * np.pi / 9))
        weight3 = 0.2 + 0.1 * np.sin(self.dim * np.pi / 6 + np.cos(self.dim * np.pi / 8))
        weight4 = 0.25 + 0.15 * np.sin(self.dim * np.pi / 5 + np.cos(self.dim * np.pi / 7))
        
        return scale_factor * (weight1 * sine_component + weight2 * ellipse_component + 
                              weight3 * cross_component + weight4 * exp_component)
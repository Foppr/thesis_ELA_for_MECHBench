import numpy as np

class FractalMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Adaptive peak density scaling factors
        self.peak_densities = np.array([1.0 + 0.5 * np.sin(0.8 * np.pi * i + 0.3 * np.sum(np.arange(dim))) for i in range(dim)])
        # Dynamic correlation structure with time-varying coupling
        self.correlation_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i == j:
                    self.correlation_matrix[i, j] = 1.0
                else:
                    self.correlation_matrix[i, j] = 0.3 * np.cos(0.6 * np.pi * (i - j) + 0.4 * np.sum(np.arange(dim)))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Multi-modal term with adaptive peak density
        multimodal_term = 0.0
        for i in range(self.dim):
            density = self.peak_densities[i]
            multimodal_term += (x[i]**2 + density * np.sin(4.0 * x[i] + 0.2 * np.sum(x))) * np.exp(-0.2 * x[i]**2)
        multimodal_term /= self.dim
        
        # Self-similar basin structure with fractal dimension scaling
        basin_term = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.4 * np.sin(0.7 * np.pi * i + 0.3 * np.sum(x))
            basin_term += (scale_factor * x[i]**3 - 2.0 * x[i] + 0.1 * np.cos(np.sum(x))) * np.exp(-0.15 * x[i]**2)
        basin_term /= self.dim
        
        # Cross-dimensional correlation with dynamic coupling
        correlation_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr = self.correlation_matrix[i, j]
                correlation_term += corr * np.sin(x[i] + x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        correlation_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Adaptive peak positioning with chaotic modulation
        peak_positioning = 0.0
        for i in range(self.dim):
            position_mod = 0.5 * np.sin(0.9 * np.pi * i + 0.4 * np.sum(x) + 0.2 * np.sin(np.sum(x)))
            peak_positioning += (x[i]**4 + position_mod * x[i]**2 + 0.1 * np.sin(3.0 * x[i])) * np.exp(-0.1 * x[i]**2)
        peak_positioning /= self.dim
        
        # Multi-scale oscillation with varying frequency
        multiscale_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.8 * np.sin(0.6 * np.pi * i + 0.3 * np.sum(x))
            multiscale_term += (np.sin(freq * x[i]) + 0.3 * np.cos(freq * x[i])) * np.exp(-0.15 * x[i]**2)
        multiscale_term /= self.dim
        
        # Dynamic basin ruggedness with varying curvature
        ruggedness_term = 0.0
        for i in range(self.dim):
            curvature = 1.5 + 0.6 * np.sin(0.8 * np.pi * i + 0.4 * np.sum(x))
            ruggedness_term += (curvature * x[i]**5 - 3.0 * x[i]**3 + 2.0 * x[i] + 0.1 * np.cos(np.sum(x))) * np.exp(-0.2 * x[i]**2)
        ruggedness_term /= self.dim
        
        # Self-similar correlation structure with multi-scale coupling
        self_correlation = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = 0.8 + 0.3 * np.sin(0.7 * (i - j) + 0.5 * np.sum(x))
                self_correlation += scale_factor * np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(0.3 * x[i] * x[j])
        self_correlation /= (self.dim * (self.dim - 1) / 2.0)
        
        # Chaotic basin complexity with dynamic scaling
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_factor = 1.2 + 0.5 * np.sin(0.9 * np.pi * i + 0.3 * np.sum(x))
            chaos_term += (chaos_factor * x[i]**6 - 4.0 * x[i]**4 + 3.0 * x[i]**2 + 0.1 * np.sin(np.sum(x))) * np.exp(-0.1 * x[i]**2)
        chaos_term /= self.dim
        
        # Weighted combination with adaptive scaling
        weights = np.array([0.2, 0.15, 0.25, 0.1, 0.15, 0.1, 0.05])
        
        total = (weights[0] * multimodal_term + 
                 weights[1] * basin_term + 
                 weights[2] * correlation_term + 
                 weights[3] * peak_positioning + 
                 weights[4] * multiscale_term + 
                 weights[5] * ruggedness_term + 
                 weights[6] * self_correlation + 
                 0.1 * chaos_term)
        
        return total
import numpy as np

class AdaptiveTrigonometricBasinFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Periodic trigonometric base with adaptive frequencies and amplitudes
        result = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i * 0.7)
            amp = 1.5 + 0.3 * np.cos(i * 1.2)
            result += amp * np.sin(freq * x[i])**2 + amp * np.cos(freq * x[i])**2
            
        # Adaptive radial basins with varying center positions and widths
        for i in range(self.dim):
            center = 2.0 * np.sin(i * 0.8)
            width = 1.0 + 0.4 * np.cos(i * 1.5)
            basin_term = np.exp(-np.sum((x - center)**2) / (2.0 * width**2))
            result += 0.5 * basin_term * (1.0 + 0.3 * np.sin(i * 2.0))
            
        # Cross-dimensional quadratic interactions with adaptive coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 * (i + 1) * (j + 1) * np.exp(-0.1 * (x[i] - x[j])**2)
                result += coupling * (x[i]**2 + x[j]**2)
                
        # Multi-scale oscillatory components with varying periods and amplitudes
        for i in range(self.dim):
            period = 4.0 + 2.0 * np.sin(i * 0.5)
            amplitude = 1.0 + 0.5 * np.cos(i * 1.3)
            result += amplitude * np.sin(x[i] / period) * np.cos(x[i] / (period * 0.7))
            
        # Asymmetric penalty terms with directional sensitivity
        for i in range(self.dim):
            if x[i] > 0:
                penalty = 0.8 * x[i]**3 * np.exp(-x[i] / 2.0)
            else:
                penalty = 0.6 * x[i]**4 * np.exp(x[i] / 3.0)
            result += penalty
            
        # Central attraction with adaptive strength and spatial variation
        dist_to_center = np.sqrt(np.sum(x**2))
        attraction = 1.5 * np.exp(-dist_to_center**2 / 8.0) * (1.0 + 0.4 * np.sin(dist_to_center * 0.5))
        result += attraction
        
        # Boundary repulsion with variable intensity and spatial dependence
        boundary_penalty = 0.0
        for i in range(self.dim):
            if x[i] < -4.0:
                boundary_penalty += 2.0 * (x[i] + 4.0)**2
            elif x[i] > 4.0:
                boundary_penalty += 2.0 * (x[i] - 4.0)**2
        result += boundary_penalty
        
        # Higher-order interaction terms with cubic and quartic components
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_interaction = 0.1 * x[i]**3 * x[j] + 0.1 * x[i] * x[j]**3
                result += cubic_interaction * np.exp(-0.2 * (x[i]**2 + x[j]**2))
                
        return result
import numpy as np

class ExponentialTrigonometricFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Exponential radial basis functions with varying centers and widths
        result = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(i * 0.5) - 1.0
            width = 0.5 + 0.3 * np.cos(i * 0.8)
            radial_term = np.exp(-np.sum((x - center)**2) / (2.0 * width**2))
            result += 1.5 * radial_term * (1.0 + 0.2 * np.sin(i * 1.3))
            
        # Trigonometric coupling terms with frequency modulation
        for i in range(self.dim):
            freq1 = 2.0 + 0.5 * np.sin(i * 0.7)
            freq2 = 1.5 + 0.4 * np.cos(i * 1.1)
            coupling = np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
            result += 0.8 * coupling * (1.0 + 0.3 * np.sin(x[i] * 2.0))
            
        # Dynamic penalty landscape with exponential decay
        dist = np.sqrt(np.sum(x**2))
        penalty = 2.5 * dist * np.exp(-dist / 5.0) * (1.0 + 0.1 * np.cos(dist * 1.5))
        result += penalty
        
        # Cross-dimensional interaction with trigonometric coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                result += 0.5 * coupling * (1.0 + 0.2 * np.sin(i + j))
                
        # Asymmetric basin terms with exponential decay
        for i in range(self.dim):
            asym_term = (x[i] - 1.0)**3 + 0.5 * (x[i] + 1.0)**2
            result += 0.3 * asym_term * np.exp(-abs(x[i]) * 0.4)
            
        # Multi-scale oscillatory terms with varying amplitudes
        for i in range(self.dim):
            amp = 0.8 + 0.2 * np.sin(i * 0.6)
            freq = 3.0 + 1.0 * np.cos(i * 0.9)
            result += amp * np.sin(freq * x[i])**2 * np.cos(freq * x[i])
            
        # Central repulsion with trigonometric modulation
        center_dist = np.sqrt(np.sum((x - 0.5)**2))
        result += 1.0 * np.exp(-center_dist**2 / 4.0) * np.sin(center_dist * 2.0)
        
        # Nested structure with exponential scaling
        for i in range(self.dim):
            nested_term = (x[i] - 1.5)**4 + 0.4 * (x[i] + 1.5)**3
            result += 0.25 * nested_term * np.exp(-abs(x[i]) * 0.3)
            
        # Chaotic modulation with sine-cosine coupling
        chaos_mod = 0.2 * np.sum(np.sin(x * 2.0) * np.cos(x * 1.5))
        result += chaos_mod
        
        # Balanced curvature term with trigonometric components
        curvature_term = 0.1 * np.sum((x**2) * np.cos(x))
        result += curvature_term
        
        return result
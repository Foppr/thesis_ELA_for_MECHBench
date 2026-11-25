import numpy as np

class ChaoticRadialFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Nested radial basis functions with hierarchical scaling
        result = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.35 * np.sin(i * 2.0)
            center = np.sin(i * 1.5) * 2.0
            width = 0.85 + 0.35 * np.cos(i * 0.7)
            result += scale_factor * np.exp(-np.sum((x - center)**2) / (2.0 * width**2))
            
        # Enhanced chaotic sine couplings with multiple modulation frequencies
        for i in range(self.dim):
            freq1 = 3.2 + 0.4 * np.sin(i)
            freq2 = 2.2 + 0.25 * np.cos(i)
            chaotic_factor = np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
            result += 0.65 * np.sin(2.0 * x[i] + chaotic_factor) * np.cos(2.0 * x[i] - chaotic_factor)
            
        # Dynamic penalty landscape with multi-scale oscillations
        dist = np.sqrt(np.sum(x**2))
        penalty = 3.2 * dist * np.exp(-dist / 4.2) * (1.0 + 0.25 * np.sin(dist * 2.2))
        result += penalty
        
        # Cross-dimensional interaction with non-linear coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                log_factor = 1.0 + 0.55 * np.sin(x[i] * x[j] * 0.5)
                result += 0.42 * coupling * log_factor * (1.0 / (1.0 + abs(x[i] - x[j])**1.6))
                
        # Multi-scale oscillatory terms with frequency modulation
        for i in range(self.dim):
            freq = 3.2 * (i + 1) * np.cos(i * 0.85)
            result += 0.32 * np.sin(freq * x[i])**4 * np.cos(freq * x[i])**2
            
        # Asymmetric basin terms with varying exponents
        for i in range(self.dim):
            asym_term = (x[i] - 1.6)**5 + 0.75 * (x[i] + 1.6)**4
            result += 0.16 * asym_term * np.exp(-abs(x[i]) * 0.52)
            
        # Central repulsion with time-varying strength
        center_dist = np.sqrt(np.sum((x - 0.75)**2))
        result += 1.25 * np.exp(-center_dist**2 / 3.2) * np.sin(center_dist * 1.6)
        
        # Nested basin structure with varying depths
        for i in range(self.dim):
            nested_term = (x[i] - 2.1)**6 + 0.32 * (x[i] + 2.1)**5
            result += 0.21 * nested_term * np.exp(-abs(x[i]) * 0.32)
            
        return result
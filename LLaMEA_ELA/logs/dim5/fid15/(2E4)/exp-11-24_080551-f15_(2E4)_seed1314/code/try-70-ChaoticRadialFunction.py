import numpy as np

class ChaoticRadialFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Nested radial basis functions with hierarchical scaling
        result = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.4 * np.sin(i * 1.8)
            center = np.sin(i * 1.3) * 2.5
            width = 0.7 + 0.3 * np.cos(i * 0.9)
            result += scale_factor * np.exp(-np.sum((x - center)**2) / (2.0 * width**2))
            
        # Enhanced chaotic sine couplings with multiple modulation frequencies
        for i in range(self.dim):
            freq1 = 2.5 + 0.6 * np.sin(i * 0.7)
            freq2 = 1.8 + 0.4 * np.cos(i * 1.2)
            chaotic_factor = np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
            result += 0.7 * np.sin(2.5 * x[i] + chaotic_factor) * np.cos(2.5 * x[i] - chaotic_factor)
            
        # Dynamic penalty landscape with multi-scale oscillations
        dist = np.sqrt(np.sum(x**2))
        penalty = 2.5 * dist * np.exp(-dist / 3.5) * (1.0 + 0.3 * np.sin(dist * 1.8))
        result += penalty
        
        # Cross-dimensional interaction with non-linear coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                log_factor = 1.0 + 0.6 * np.sin(x[i] * x[j] * 0.6)
                result += 0.5 * coupling * log_factor * (1.0 / (1.0 + abs(x[i] - x[j])**1.8))
                
        # Multi-scale oscillatory terms with frequency modulation
        for i in range(self.dim):
            freq = 4.0 * (i + 1) * np.cos(i * 0.9)
            result += 0.4 * np.sin(freq * x[i])**3 * np.cos(freq * x[i])**3
            
        # Asymmetric basin terms with varying exponents
        for i in range(self.dim):
            asym_term = (x[i] - 1.2)**4 + 0.8 * (x[i] + 1.2)**3
            result += 0.2 * asym_term * np.exp(-abs(x[i]) * 0.6)
            
        # Central repulsion with time-varying strength
        center_dist = np.sqrt(np.sum((x - 0.5)**2))
        result += 1.0 * np.exp(-center_dist**2 / 2.5) * np.sin(center_dist * 1.8)
        
        # Nested basin structure with varying depths
        for i in range(self.dim):
            nested_term = (x[i] - 1.8)**5 + 0.4 * (x[i] + 1.8)**4
            result += 0.25 * nested_term * np.exp(-abs(x[i]) * 0.4)
            
        # Additional mutation: introducing a new type of interaction term with higher frequency oscillations
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited interaction range
                high_freq_interaction = np.sin(6.0 * x[i] * x[j]) * np.cos(8.0 * (x[i] + x[j]))
                result += 0.3 * high_freq_interaction * (1.0 / (1.0 + abs(x[i] - x[j])**2.5))
                
        # Additional complexity through polynomial coupling
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
        result += 0.35 * poly_coupling
        
        return result
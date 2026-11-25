import numpy as np

class ChaoticRadialFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Polynomial chaos expansion with randomized coefficients
        result = 0.0
        for i in range(self.dim):
            poly_term = (x[i]**5 + 0.7 * x[i]**4 + 0.3 * x[i]**3 + 0.1 * x[i]**2 + 0.05 * x[i])
            chaos_coeff = 1.0 + 0.2 * np.sin(i * 1.3) * np.cos(i * 0.7)
            result += chaos_coeff * poly_term
            
        # Radial basis functions with varying centers and widths
        for i in range(self.dim):
            center = np.sin(i * 1.7) * 3.0
            width = 0.5 + 0.3 * np.cos(i * 0.9)
            result += 2.0 * np.exp(-np.sum((x - center)**2) / (2.0 * width**2))
            
        # Sine-cosine coupling terms with chaotic modulation
        for i in range(self.dim):
            freq_mod = 2.0 + 0.5 * np.sin(i * 1.1)
            result += 1.5 * np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] * 0.8) * np.exp(-0.1 * x[i]**2)
            
        # Cross-dimensional interaction with polynomial coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling = (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
                result += 0.8 * poly_coupling * np.exp(-0.2 * (x[i] - x[j])**2)
                
        # Asymmetric curvature with exponential decay
        for i in range(self.dim):
            asym_term = (x[i] - 1.0)**6 + 0.5 * (x[i] + 1.0)**5
            result += 0.3 * asym_term * np.exp(-0.3 * abs(x[i]))
            
        # Multi-scale oscillatory component with frequency control
        for i in range(self.dim):
            freq = 4.0 * (i + 1) * np.sin(i * 0.6)
            result += 0.5 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.exp(-0.05 * x[i]**2)
            
        # Central attraction with radial penalty
        center_dist = np.sqrt(np.sum(x**2))
        result += 1.0 * np.exp(-center_dist**2 / 4.0) * (1.0 + 0.3 * np.sin(center_dist * 1.5))
        
        # Additional chaotic interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_coupling = np.sin(x[i] * x[j] * 1.5) * np.cos(x[i] + x[j] * 2.0)
                strength = 0.4 * (1.0 + 0.3 * np.sin(i + j * 0.8))
                result += strength * chaotic_coupling * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Novel basin structure with cubic terms
        for i in range(self.dim):
            basin_term = (x[i] - 2.5)**3 + 0.4 * (x[i] + 2.5)**3
            result += 0.25 * basin_term * np.exp(-0.2 * abs(x[i]))
            
        # High-frequency chaotic modulation
        high_freq = 0.0
        for i in range(self.dim):
            freq = 8.0 + 1.5 * np.sin(i * 0.4)
            high_freq += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.6) * (0.02 + 0.03 * abs(x[i]))
        result += 0.4 * high_freq
        
        # Multi-modal structure with varying amplitudes
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.sin(x[i] * 6.0) * np.cos(x[i] * 2.0) * (1.0 + 0.2 * np.sin(i * 1.2))
        result += 0.2 * multimodal
        
        # Enhanced penalty term to improve conditioning
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.1 * (x[i]**2 - 25.0)**2 * np.exp(-0.1 * abs(x[i]))
        result += penalty
        
        # Additional structured interaction to reduce correlations
        structured_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                structured_interaction += (x[i] - x[j])**4 * np.sin(x[i] + x[j])
        result += 0.15 * structured_interaction
        
        return result
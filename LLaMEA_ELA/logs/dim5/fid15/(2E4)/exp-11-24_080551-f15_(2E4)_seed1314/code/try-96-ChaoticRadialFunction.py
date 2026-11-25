import numpy as np

class ChaoticRadialFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Nested radial basis functions with hierarchical scaling
        result = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(i * 2.0)
            center = np.sin(i * 1.5) * 2.0
            width = 0.8 + 0.4 * np.cos(i * 0.7)
            result += scale_factor * np.exp(-np.sum((x - center)**2) / (2.0 * width**2))
            
        # Enhanced chaotic sine couplings with multiple modulation frequencies
        for i in range(self.dim):
            freq1 = 3.0 + 0.5 * np.sin(i)
            freq2 = 2.0 + 0.3 * np.cos(i)
            chaotic_factor = np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
            result += 0.6 * np.sin(2.0 * x[i] + chaotic_factor) * np.cos(2.0 * x[i] - chaotic_factor)
            
        # Dynamic penalty landscape with multi-scale oscillations
        dist = np.sqrt(np.sum(x**2))
        penalty = 3.0 * dist * np.exp(-dist / 4.0) * (1.0 + 0.2 * np.sin(dist * 2.0))
        result += penalty
        
        # Cross-dimensional interaction with non-linear coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                log_factor = 1.0 + 0.5 * np.sin(x[i] * x[j] * 0.5)
                result += 0.4 * coupling * log_factor * (1.0 / (1.0 + abs(x[i] - x[j])**1.5))
                
        # Multi-scale oscillatory terms with frequency modulation
        for i in range(self.dim):
            freq = 3.0 * (i + 1) * np.cos(i * 0.8)
            result += 0.3 * np.sin(freq * x[i])**4 * np.cos(freq * x[i])**2
            
        # Asymmetric basin terms with varying exponents
        for i in range(self.dim):
            asym_term = (x[i] - 1.5)**5 + 0.7 * (x[i] + 1.5)**4
            result += 0.15 * asym_term * np.exp(-abs(x[i]) * 0.5)
            
        # Central repulsion with time-varying strength
        center_dist = np.sqrt(np.sum((x - 0.7)**2))
        result += 1.2 * np.exp(-center_dist**2 / 3.0) * np.sin(center_dist * 1.5)
        
        # Nested basin structure with varying depths
        for i in range(self.dim):
            nested_term = (x[i] - 2.0)**6 + 0.3 * (x[i] + 2.0)**5
            result += 0.2 * nested_term * np.exp(-abs(x[i]) * 0.3)
            
        # New mutation: introducing a new type of interaction term with higher frequency oscillations
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                high_freq_interaction = np.sin(5.0 * x[i] * x[j]) * np.cos(7.0 * (x[i] + x[j]))
                result += 0.25 * high_freq_interaction * (1.0 / (1.0 + abs(x[i] - x[j])**2))
                
        # New mutation: adding a new term with cubic polynomial interactions and modified coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_coupling = (x[i]**3) * np.sin(x[j]) + (x[j]**3) * np.cos(x[i])
                result += 0.18 * cubic_coupling * np.exp(-0.5 * (x[i] - x[j])**2)
                
        # Major mutation: Introducing quartic polynomial interactions with sinusoidal modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                quartic_interaction = (x[i]**4) * np.cos(x[j]) + (x[j]**4) * np.sin(x[i])
                modulator = 0.8 + 0.2 * np.sin(3.0 * (x[i] + x[j]))
                result += 0.22 * quartic_interaction * modulator * np.exp(-0.3 * (x[i] - x[j])**2)
                
        # Major mutation: Adding a new high-frequency chaotic term with exponential decay
        for i in range(self.dim):
            freq = 10.0 + 2.0 * np.sin(i * 0.5)
            chaos_term = np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.exp(-x[i]**2 / 5.0)
            result += 0.35 * chaos_term
            
        # Major mutation: Introducing a new hyperbolic tangent interaction term with modified coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                tanh_interaction = np.tanh(x[i]) * np.tanh(x[j]) * (x[i] + x[j])**2
                result += 0.15 * tanh_interaction * np.exp(-0.4 * abs(x[i] - x[j]))
                
        # Major mutation: Adding a new multi-modal sinusoidal landscape with variable amplitude
        for i in range(self.dim):
            amp = 1.5 + 0.5 * np.sin(i * 1.2)
            freq = 4.0 + 1.0 * np.cos(i * 0.9)
            result += amp * np.sin(freq * x[i])**3 * np.cos(freq * x[i])**3
            
        # Minor mutation: Slight modification to the exponential decay factor in central repulsion
        center_dist = np.sqrt(np.sum((x - 0.7)**2))
        result -= 0.1 * np.exp(-center_dist**2 / 4.0) * np.sin(center_dist * 1.5)
        
        # Additional mutation: Modifying radial basis function with sinusoidal amplitude modulation
        for i in range(self.dim):
            amp_mod = 1.0 + 0.3 * np.cos(i * 1.1)
            result += 0.2 * amp_mod * np.exp(-np.sum((x - np.sin(i * 1.3))**2) / (2.0 * 0.9**2))
            
        return result
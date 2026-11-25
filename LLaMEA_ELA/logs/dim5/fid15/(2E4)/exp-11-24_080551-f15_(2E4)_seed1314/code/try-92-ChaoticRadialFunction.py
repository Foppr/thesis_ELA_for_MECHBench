import numpy as np

class ChaoticRadialFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Nested radial basis functions with hierarchical scaling and modified centers
        result = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.2 * np.sin(i * 1.3)
            center = np.sin(i * 1.7) * 1.8
            width = 0.9 + 0.3 * np.cos(i * 0.5)
            result += scale_factor * np.exp(-np.sum((x - center)**2) / (2.0 * width**2))
            
        # Enhanced chaotic sine couplings with reduced frequency modulation
        for i in range(self.dim):
            freq1 = 2.5 + 0.4 * np.sin(i * 0.7)
            freq2 = 1.8 + 0.2 * np.cos(i * 1.2)
            chaotic_factor = np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
            result += 0.5 * np.sin(1.5 * x[i] + chaotic_factor) * np.cos(1.5 * x[i] - chaotic_factor)
            
        # Dynamic penalty landscape with smoother oscillations
        dist = np.sqrt(np.sum(x**2))
        penalty = 2.5 * dist * np.exp(-dist / 3.5) * (1.0 + 0.15 * np.sin(dist * 1.8))
        result += penalty
        
        # Cross-dimensional interaction with controlled coupling strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                log_factor = 1.0 + 0.4 * np.sin(x[i] * x[j] * 0.3)
                result += 0.35 * coupling * log_factor * (1.0 / (1.0 + abs(x[i] - x[j])**1.2))
                
        # Multi-scale oscillatory terms with reduced frequency
        for i in range(self.dim):
            freq = 2.5 * (i + 1) * np.cos(i * 0.6)
            result += 0.25 * np.sin(freq * x[i])**3 * np.cos(freq * x[i])**2
            
        # Asymmetric basin terms with adjusted exponents
        for i in range(self.dim):
            asym_term = (x[i] - 1.2)**4 + 0.6 * (x[i] + 1.2)**3
            result += 0.12 * asym_term * np.exp(-abs(x[i]) * 0.4)
            
        # Central repulsion with modified strength
        center_dist = np.sqrt(np.sum((x - 0.6)**2))
        result += 1.0 * np.exp(-center_dist**2 / 2.5) * np.sin(center_dist * 1.3)
        
        # Nested basin structure with adjusted depths
        for i in range(self.dim):
            nested_term = (x[i] - 1.8)**5 + 0.25 * (x[i] + 1.8)**4
            result += 0.18 * nested_term * np.exp(-abs(x[i]) * 0.25)
            
        # New interaction term with cubic polynomial and controlled coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_coupling = (x[i]**3) * np.sin(x[j]) + (x[j]**3) * np.cos(x[i])
                result += 0.15 * cubic_coupling * np.exp(-0.4 * (x[i] - x[j])**2)
                
        # Chaotic interaction with modified coupling and strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod_coupling = np.sin(x[i] * x[j] * 1.8) * np.cos(x[i] + x[j] * 1.3)
                strength = 0.25 * (1.0 + 0.15 * np.sin(i + j))
                result += strength * mod_coupling * np.exp(-0.2 * (x[i]**2 + x[j]**2))
                
        # Quartic interaction term with symmetric curvature
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                quartic_term = (x[i]**4) * np.sin(x[j]) + (x[j]**4) * np.cos(x[i])
                result += 0.18 * quartic_term * np.exp(-0.25 * abs(x[i] - x[j]))
                
        # New radial term with variable center and width
        for i in range(self.dim):
            center_var = np.sin(i * 1.1) * 1.3
            width_var = 0.7 + 0.25 * np.cos(i * 0.8)
            radial_term = np.exp(-np.sum((x - center_var)**2) / (2.0 * width_var**2))
            result += 0.2 * radial_term * (1.0 + 0.3 * np.sin(i * 2.5))
            
        # Penalty term with adjusted scaling
        for i in range(self.dim):
            scaled_penalty = 1.8 * abs(x[i]) * np.exp(-abs(x[i]) / 2.5) * (1.0 + 0.25 * np.cos(i * 1.5))
            result += scaled_penalty
            
        return result
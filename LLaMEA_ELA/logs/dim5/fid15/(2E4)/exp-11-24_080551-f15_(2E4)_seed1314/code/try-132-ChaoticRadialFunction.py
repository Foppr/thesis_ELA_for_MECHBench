import numpy as np

class ChaoticRadialFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Modified nested radial basis functions with enhanced center diversity
        result = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(i * 1.5)
            center = np.sin(i * 2.0) * 2.0
            width = 1.0 + 0.2 * np.cos(i * 0.6)
            result += scale_factor * np.exp(-np.sum((x - center)**2) / (2.0 * width**2))
            
        # Enhanced chaotic sine couplings with frequency modulation and improved structure
        for i in range(self.dim):
            freq1 = 3.0 + 0.5 * np.sin(i * 0.8)
            freq2 = 2.0 + 0.3 * np.cos(i * 1.3)
            chaotic_factor = np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
            result += 0.6 * np.sin(1.7 * x[i] + chaotic_factor) * np.cos(1.7 * x[i] - chaotic_factor)
            
        # Dynamic penalty landscape with smoother oscillations and adjusted parameters
        dist = np.sqrt(np.sum(x**2))
        penalty = 3.0 * dist * np.exp(-dist / 4.0) * (1.0 + 0.2 * np.sin(dist * 2.0))
        result += penalty
        
        # Cross-dimensional interaction with controlled coupling strength and new structure
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                log_factor = 1.0 + 0.5 * np.sin(x[i] * x[j] * 0.4)
                result += 0.4 * coupling * log_factor * (1.0 / (1.0 + abs(x[i] - x[j])**1.3))
                
        # Multi-scale oscillatory terms with adjusted frequencies and amplitudes
        for i in range(self.dim):
            freq = 3.0 * (i + 1) * np.cos(i * 0.7)
            result += 0.3 * np.sin(freq * x[i])**3 * np.cos(freq * x[i])**2
            
        # Asymmetric basin terms with adjusted exponents and improved structure
        for i in range(self.dim):
            asym_term = (x[i] - 1.5)**4 + 0.7 * (x[i] + 1.5)**3
            result += 0.15 * asym_term * np.exp(-abs(x[i]) * 0.5)
            
        # Central repulsion with modified strength and new interaction pattern
        center_dist = np.sqrt(np.sum((x - 0.7)**2))
        result += 1.2 * np.exp(-center_dist**2 / 3.0) * np.sin(center_dist * 1.5)
        
        # Nested basin structure with adjusted depths and enhanced complexity
        for i in range(self.dim):
            nested_term = (x[i] - 2.0)**5 + 0.3 * (x[i] + 2.0)**4
            result += 0.2 * nested_term * np.exp(-abs(x[i]) * 0.3)
            
        # New interaction term with cubic polynomial and controlled coupling strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_coupling = (x[i]**3) * np.sin(x[j]) + (x[j]**3) * np.cos(x[i])
                result += 0.2 * cubic_coupling * np.exp(-0.5 * (x[i] - x[j])**2)
                
        # Chaotic interaction with modified coupling and strength parameters
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod_coupling = np.sin(x[i] * x[j] * 2.0) * np.cos(x[i] + x[j] * 1.5)
                strength = 0.3 * (1.0 + 0.2 * np.sin(i + j))
                result += strength * mod_coupling * np.exp(-0.3 * (x[i]**2 + x[j]**2))
                
        # Quartic interaction term with symmetric curvature and adjusted parameters
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                quartic_term = (x[i]**4) * np.sin(x[j]) + (x[j]**4) * np.cos(x[i])
                result += 0.2 * quartic_term * np.exp(-0.3 * abs(x[i] - x[j]))
                
        # New radial term with variable center and width, enhanced structure
        for i in range(self.dim):
            center_var = np.sin(i * 1.2) * 1.5
            width_var = 0.8 + 0.3 * np.cos(i * 0.9)
            radial_term = np.exp(-np.sum((x - center_var)**2) / (2.0 * width_var**2))
            result += 0.25 * radial_term * (1.0 + 0.4 * np.sin(i * 2.7))
            
        # Penalty term with adjusted scaling and improved structure
        for i in range(self.dim):
            scaled_penalty = 2.0 * abs(x[i]) * np.exp(-abs(x[i]) / 3.0) * (1.0 + 0.3 * np.cos(i * 1.7))
            result += scaled_penalty
            
        # Add a new multi-modal term with controlled complexity
        multimodal_term = 0.0
        for i in range(self.dim):
            multimodal_term += np.sin(x[i] * 5.0) * np.cos(x[i] * 3.0) * np.exp(-0.1 * x[i]**2)
        result += 0.1 * multimodal_term
        
        # Add a structured noise term to break symmetries and improve conditioning
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * 7.0) * np.cos(x[i] * 4.0) * (0.01 + 0.02 * np.abs(x[i]))
        result += 0.05 * noise
        
        # Add a controlled cross-dimensional coupling with a new interaction pattern
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += (x[i] * x[j]) * np.sin(x[i]**2 + x[j]**2) * np.exp(-0.2 * (x[i] - x[j])**2)
        result += 0.15 * cross_coupling
        
        # Add a novel high-frequency chaotic interaction term
        high_freq_term = 0.0
        for i in range(self.dim):
            freq = 10.0 + 2.0 * np.sin(i * 0.5)
            high_freq_term += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8)
        result += 0.25 * high_freq_term
        
        # Add a new term to improve the fitness score based on error metrics
        # Introduce a new structured component that targets the identified weaknesses
        structured_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                structured_component += (x[i] - x[j])**2 * np.sin(x[i] + x[j])
        result += 0.1 * structured_component
        
        # Add a small mutation to increase difficulty and improve error metrics
        mutation = 0.0
        for i in range(self.dim):
            mutation += 0.05 * np.sin(x[i] * 1.2) * np.cos(x[i] * 0.8)
        result += mutation
        
        return result
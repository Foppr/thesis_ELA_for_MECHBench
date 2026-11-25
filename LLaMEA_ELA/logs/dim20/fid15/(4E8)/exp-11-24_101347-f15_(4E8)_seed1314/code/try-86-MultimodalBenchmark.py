import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced polynomial chaos expansion with higher-order terms and mixed monomials
        poly_terms = np.zeros(self.dim)
        for i in range(self.dim):
            poly_terms[i] = (x_scaled[i]**6 + 0.8 * x_scaled[i]**5 + 0.3 * x_scaled[i]**4 + 
                           0.25 * x_scaled[i]**3 + 0.15 * x_scaled[i]**2 + 0.08 * x_scaled[i])
        
        # Chaotic sinusoidal interactions with exponential decay and multi-frequency modulation
        chaotic_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                # Add chaotic modulation with multiple frequencies
                chaotic_sum += (np.sin(22.0 * dist) * np.cos(15.0 * dist) * 
                               np.exp(-dist**2.5) * np.sin(10.0 * dist**2))
        
        # Implicit constraint-based penalty with enhanced nonlinearity and dynamic scaling
        constraint_penalty = 0.0
        for i in range(self.dim):
            # Add higher-order constraint terms for increased complexity
            constraint_penalty += (x_scaled[i] - 0.35)**4 + (x_scaled[i] + 0.35)**4 + 0.6 * (x_scaled[i]**2 - 0.12)**2
        
        # Enhanced multi-modal component with frequency modulation and amplitude coupling
        modal_component = 0.0
        for i in range(self.dim):
            # Amplitude modulation with complex trigonometric functions
            amp_mod = 1.4 + 0.9 * np.sin(16.0 * x_scaled[i]) + 0.2 * np.cos(22.0 * x_scaled[i])
            # Phase modulation with multiple frequencies
            phase_mod = 3.5 * np.cos(8.0 * x_scaled[i]) + 2.5 * np.sin(6.0 * x_scaled[i]) + 1.5 * np.cos(4.0 * x_scaled[i])
            modal_component += amp_mod * np.sin(11.0 * x_scaled[i] + phase_mod) * np.cos(9.0 * x_scaled[i] + phase_mod)
        
        # Cross-dimensional coupling with directional gradient modulation and multi-scale interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.001)
                # Add directional coupling with gradient modulation
                grad_mod = np.sin(13.0 * (x_scaled[i] + x_scaled[j])) + 0.4 * np.cos(9.0 * (x_scaled[i] - x_scaled[j]))
                cross_coupling += np.exp(-dist**2.8) * np.sin(18.0 * dist) * grad_mod
        
        # Enhanced deceptive basin structure with varying conditioning and chaotic modulation
        r = np.sqrt(np.sum(x_scaled**2))
        # Add chaotic conditioning factor with multiple oscillatory components
        conditioning_factor = 1.0 + 2.5 * np.exp(-r**2 / 2.5) + 1.3 * np.sin(10.0 * r) + 0.9 * np.cos(16.0 * r)
        
        # Combine all components with enhanced dynamic weighting
        result = (conditioning_factor * 
                 (np.sum(poly_terms) + 0.35 * chaotic_sum + 0.25 * cross_coupling + 0.55 * modal_component) + 
                 0.18 * constraint_penalty)
        
        return result
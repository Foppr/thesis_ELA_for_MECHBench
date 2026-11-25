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
            poly_terms[i] = (x_scaled[i]**7 + 0.8 * x_scaled[i]**6 + 0.5 * x_scaled[i]**5 + 
                           0.3 * x_scaled[i]**4 + 0.15 * x_scaled[i]**3 + 0.08 * x_scaled[i]**2 + 0.03 * x_scaled[i])
        
        # Intensified chaotic sinusoidal interactions with exponential decay and multi-frequency modulation
        chaotic_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                # Add intensified chaotic modulation with multiple frequencies
                chaotic_sum += (np.sin(30.0 * dist) * np.cos(25.0 * dist) * 
                               np.exp(-dist**4) * np.sin(15.0 * dist**2) * 
                               np.cos(8.0 * dist**3))
        
        # Enhanced implicit constraint-based penalty with increased nonlinearity and dynamic scaling
        constraint_penalty = 0.0
        for i in range(self.dim):
            # Add higher-order constraint terms for increased complexity
            constraint_penalty += (x_scaled[i] - 0.4)**5 + (x_scaled[i] + 0.4)**5 + 0.6 * (x_scaled[i]**2 - 0.15)**2
        
        # Enhanced multi-modal component with frequency modulation and amplitude coupling
        modal_component = 0.0
        for i in range(self.dim):
            # Amplitude modulation with complex trigonometric functions
            amp_mod = 2.0 + 1.2 * np.sin(20.0 * x_scaled[i]) + 0.5 * np.cos(25.0 * x_scaled[i]) + 0.2 * np.sin(30.0 * x_scaled[i])
            # Phase modulation with multiple frequencies
            phase_mod = 5.0 * np.cos(12.0 * x_scaled[i]) + 4.0 * np.sin(10.0 * x_scaled[i]) + 3.0 * np.cos(8.0 * x_scaled[i]) + 2.0 * np.sin(6.0 * x_scaled[i])
            modal_component += amp_mod * np.sin(15.0 * x_scaled[i] + phase_mod) * np.cos(15.0 * x_scaled[i] + phase_mod)
        
        # Cross-dimensional coupling with directional gradient modulation and multi-scale interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.001)
                # Add directional coupling with gradient modulation
                grad_mod = np.sin(20.0 * (x_scaled[i] + x_scaled[j])) + 0.7 * np.cos(15.0 * (x_scaled[i] - x_scaled[j])) + 0.3 * np.sin(10.0 * (x_scaled[i] + x_scaled[j]))
                cross_coupling += np.exp(-dist**4) * np.sin(25.0 * dist) * grad_mod
        
        # Enhanced deceptive basin structure with varying conditioning and chaotic modulation
        r = np.sqrt(np.sum(x_scaled**2))
        # Add intensified conditioning factor with multiple oscillatory components
        conditioning_factor = 1.0 + 4.0 * np.exp(-r**2 / 2.5) + 2.0 * np.sin(15.0 * r) + 1.2 * np.cos(20.0 * r) + 0.6 * np.sin(25.0 * r**2)
        
        # Combine all components with enhanced dynamic weighting
        result = (conditioning_factor * 
                 (np.sum(poly_terms) + 0.5 * chaotic_sum + 0.4 * cross_coupling + 0.7 * modal_component) + 
                 0.2 * constraint_penalty)
        
        return result
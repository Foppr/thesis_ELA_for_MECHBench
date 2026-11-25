import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced polynomial chaos expansion with higher-order terms and modified weights
        poly_terms = np.zeros(self.dim)
        for i in range(self.dim):
            poly_terms[i] = (1.2 * x_scaled[i]**6 + 0.9 * x_scaled[i]**5 + 0.7 * x_scaled[i]**4 + 
                           0.5 * x_scaled[i]**3 + 0.3 * x_scaled[i]**2 + 0.1 * x_scaled[i])
        
        # Multi-scale harmonic interactions with increased frequency complexity and modified coupling
        harmonic_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                harmonic_sum += (np.sin(35.0 * dist) * np.cos(25.0 * dist) + 
                               0.5 * np.sin(45.0 * dist) * np.cos(35.0 * dist)) * np.exp(-dist**2.5)
        
        # Implicit constraint-based penalty with enhanced nonlinearity and modified scaling
        constraint_penalty = 0.0
        for i in range(self.dim):
            constraint_penalty += (x_scaled[i] - 0.3)**2 * (x_scaled[i] + 0.3)**2 * (x_scaled[i]**2 + 0.1)
        
        # Enhanced multi-modal component with increased amplitude modulation and phase complexity
        modal_component = 0.0
        for i in range(self.dim):
            amp_mod = 1.5 + 1.2 * np.sin(18.0 * x_scaled[i]) + 0.8 * np.cos(15.0 * x_scaled[i])
            phase_mod = 5.0 * np.cos(12.0 * x_scaled[i]) + 3.5 * np.sin(10.0 * x_scaled[i]) + 2.0 * np.cos(8.0 * x_scaled[i])
            modal_component += amp_mod * np.sin(14.0 * x_scaled[i] + phase_mod) * np.cos(11.0 * x_scaled[i] + phase_mod)
        
        # Advanced cross-dimensional coupling with exponential decay, sinusoidal modulation, and additional harmonic terms
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.02)
                cross_coupling += (np.exp(-dist**3.0) * np.sin(20.0 * dist) * np.cos(15.0 * dist) + 
                                 0.3 * np.exp(-dist**2.0) * np.sin(25.0 * dist))
        
        # Deceptive basin structure with enhanced conditioning and additional chaotic components
        r = np.sqrt(np.sum(x_scaled**2))
        conditioning_factor = 1.0 + 4.0 * np.exp(-r**2 / 2.0) + 1.5 * np.sin(15.0 * r) + 0.8 * np.cos(20.0 * r)
        
        # Combine all components with adjusted weighting and enhanced nonlinearity
        result = (conditioning_factor * 
                 (np.sum(poly_terms) + 0.6 * harmonic_sum + 0.4 * cross_coupling + 0.8 * modal_component) + 
                 0.2 * constraint_penalty)
        
        return result
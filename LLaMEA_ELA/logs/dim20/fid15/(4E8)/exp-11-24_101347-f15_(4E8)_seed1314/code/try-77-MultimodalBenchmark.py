import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial chaos expansion with modified terms
        poly_terms = np.zeros(self.dim)
        for i in range(self.dim):
            poly_terms[i] = (0.8 * x_scaled[i]**4 + 0.6 * x_scaled[i]**3 + 0.3 * x_scaled[i]**2 + 0.15 * x_scaled[i])
        
        # Multi-scale harmonic interactions with altered frequencies
        harmonic_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                harmonic_sum += np.sin(25.0 * dist) * np.cos(18.0 * dist) * np.exp(-dist**2)
        
        # Implicit constraint-based penalty with modified scaling
        constraint_penalty = 0.0
        for i in range(self.dim):
            constraint_penalty += (x_scaled[i] - 0.25)**2 * (x_scaled[i] + 0.25)**2
        
        # Multi-modal component with altered amplitude and phase modulation
        modal_component = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + 0.6 * np.sin(12.0 * x_scaled[i])
            phase_mod = 3.5 * np.cos(8.0 * x_scaled[i]) + 2.5 * np.sin(6.0 * x_scaled[i])
            modal_component += amp_mod * np.sin(9.0 * x_scaled[i] + phase_mod) * np.cos(7.0 * x_scaled[i] + phase_mod)
        
        # Cross-dimensional coupling with modified exponential decay and sinusoidal modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.01)
                cross_coupling += np.exp(-dist**2.5) * np.sin(15.0 * dist) * np.cos(10.0 * dist)
        
        # Deceptive basin structure with modified conditioning
        r = np.sqrt(np.sum(x_scaled**2))
        conditioning_factor = 1.0 + 2.5 * np.exp(-r**2 / 1.5) + 0.9 * np.sin(10.0 * r)
        
        # Combine all components with adjusted weighting
        result = (conditioning_factor * 
                 (np.sum(poly_terms) + 0.4 * harmonic_sum + 0.3 * cross_coupling + 0.6 * modal_component) + 
                 0.15 * constraint_penalty)
        
        return result
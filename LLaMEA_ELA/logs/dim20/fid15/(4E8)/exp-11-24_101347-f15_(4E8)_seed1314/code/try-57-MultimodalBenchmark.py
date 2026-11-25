import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial chaos expansion with mixed terms
        poly_terms = np.zeros(self.dim)
        for i in range(self.dim):
            poly_terms[i] = (x_scaled[i]**4 + 0.5 * x_scaled[i]**3 + 0.2 * x_scaled[i]**2 + 0.1 * x_scaled[i])
        
        # Multi-scale harmonic interactions with varying frequencies
        harmonic_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                harmonic_sum += np.sin(20.0 * dist) * np.cos(15.0 * dist) * np.exp(-dist**2)
        
        # Implicit constraint-based penalty with dynamic scaling
        constraint_penalty = 0.0
        for i in range(self.dim):
            constraint_penalty += (x_scaled[i] - 0.3)**2 * (x_scaled[i] + 0.3)**2
        
        # Multi-modal component with varying amplitude and phase modulation
        modal_component = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + 0.5 * np.sin(10.0 * x_scaled[i])
            phase_mod = 3.0 * np.cos(7.0 * x_scaled[i]) + 2.0 * np.sin(5.0 * x_scaled[i])
            modal_component += amp_mod * np.sin(8.0 * x_scaled[i] + phase_mod) * np.cos(6.0 * x_scaled[i] + phase_mod)
        
        # Cross-dimensional coupling with exponential decay and sinusoidal modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.01)
                cross_coupling += np.exp(-dist**2) * np.sin(12.0 * dist) * np.cos(9.0 * dist)
        
        # Deceptive basin structure with varying conditioning
        r = np.sqrt(np.sum(x_scaled**2))
        conditioning_factor = 1.0 + 2.0 * np.exp(-r**2 / 2.0) + 0.8 * np.sin(8.0 * r)
        
        # Combine all components with dynamic weighting
        result = (conditioning_factor * 
                 (np.sum(poly_terms) + 0.3 * harmonic_sum + 0.4 * cross_coupling + 0.5 * modal_component) + 
                 0.1 * constraint_penalty)
        
        return result
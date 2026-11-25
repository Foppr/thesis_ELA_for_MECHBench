import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic component with modified logistic map and multi-scale interference
        chaotic_term = 0.0
        r = 3.8  # Slightly reduced chaos for better control
        for i in range(self.dim):
            x_prev = x_norm[i] if i == 0 else x_norm[i-1]
            x_next = x_norm[(i+1) % self.dim] if i < self.dim - 1 else x_norm[0]
            chaotic_term += np.sin(r * x_prev * (1 - x_prev)) * np.cos(3 * np.pi * x_prev) * np.sin(np.pi * x_next)
        
        # Modified exponential decay with enhanced coupling and phase modulation
        exp_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                exp_decay += np.exp(-1.5 * dist) * np.sin(3 * np.pi * dist) * np.cos(3 * np.pi * dist) * (1 + 0.3 * np.sin(np.pi * (i+j)))
        
        # Dynamic conditioning with increased sensitivity and multi-scale modulation
        r = np.sqrt(np.sum(x_norm**2))
        condition_factor = 1.0 + 5.0 * np.sin(3 * np.pi * r)**3
        
        # Multi-modal sinusoidal terms with frequency modulation, amplitude scaling, and phase coupling
        modal_terms = 0.0
        for i in range(self.dim):
            freq = (i % 6) + 3  # Reduced base frequency for smoother landscape
            amp = 1.0 / (1.0 + 0.1 * i)
            phase = np.pi * i / (self.dim * 0.7)  # Adjusted phase shift
            modal_terms += amp * np.sin(freq * np.pi * x_norm[i] + phase) * np.cos(freq * np.pi * x_norm[i]) * np.sin(3 * np.pi * x_norm[i])
        
        # Enhanced quadratic basin with modified cross-terms and increased conditioning
        quadratic_basin = 0.25 * np.sum(x_norm**2) + 0.1 * np.sum(x_norm[:-1] * x_norm[1:]) + 0.08 * np.sum(x_norm * x_norm[::-1])
        
        # Add higher-order polynomial terms with reduced weights for better balance
        cubic_term = 0.08 * np.sum(x_norm**3)
        quartic_term = 0.03 * np.sum(x_norm**4)
        quintic_term = 0.01 * np.sum(x_norm**5)
        
        # Combine all terms with adjusted weighting for better discrimination and reduced bias
        result = condition_factor * (0.6 * r**2 + 0.3 * chaotic_term + 0.2 * exp_decay + 0.3 * modal_terms + 
                                   quadratic_basin + cubic_term + quartic_term + quintic_term)
        
        # Final adjustment with modified conditioning for better algorithm discrimination
        condition_factor = 1.0 + 7.0 * np.sin(2.5 * np.pi * r)**4
        
        # Re-compute with updated conditioning
        result = condition_factor * (0.6 * r**2 + 0.3 * chaotic_term + 0.2 * exp_decay + 0.3 * modal_terms + 
                                   quadratic_basin + cubic_term + quartic_term + quintic_term)
        
        return result
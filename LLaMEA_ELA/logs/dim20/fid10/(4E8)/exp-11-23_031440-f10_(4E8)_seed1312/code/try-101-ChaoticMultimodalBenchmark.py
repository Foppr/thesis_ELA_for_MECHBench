import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic logistic map component with feedback loops and multiple iterations
        chaotic_term = 0.0
        r = 3.9  # Increased chaos parameter
        for i in range(self.dim):
            x_prev = x_norm[i] if i == 0 else x_norm[i-1]
            x_next = x_norm[(i+1) % self.dim] if i < self.dim - 1 else x_norm[0]
            chaotic_term += np.sin(r * x_prev * (1 - x_prev)) * np.cos(2 * np.pi * x_prev) * np.sin(np.pi * x_next)
        
        # Exponential decay interactions with modified decay rates and additional coupling terms
        exp_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                exp_decay += np.exp(-2.5 * dist) * np.sin(4 * np.pi * dist) * np.cos(2 * np.pi * dist) * (1 + 0.3 * np.sin(np.pi * (i+j)))
        
        # Dynamic conditioning with increased complexity and multiple scaling factors
        r = np.sqrt(np.sum(x_norm**2))
        condition_factor = 1.0 + 5.0 * np.sin(4 * np.pi * r)**4
        
        # Multi-modal sinusoidal terms with varying frequencies, amplitudes, phase shifts, and coupling
        modal_terms = 0.0
        for i in range(self.dim):
            freq = (i % 7) + 3  # Slightly reduced base frequency
            amp = 1.0 / (1.0 + 0.3 * i)
            phase = np.pi * i / (self.dim * 0.6)  # Adjusted phase shift
            modal_terms += amp * np.sin(freq * np.pi * x_norm[i] + phase) * np.cos(freq * np.pi * x_norm[i]) * np.sin(2 * np.pi * x_norm[i])
        
        # Enhanced quadratic basin with cross-terms for increased conditioning and interaction
        quadratic_basin = 0.4 * np.sum(x_norm**2) + 0.2 * np.sum(x_norm[:-1] * x_norm[1:]) + 0.15 * np.sum(x_norm * x_norm[::-1])
        
        # Add cubic, quartic, and quintic terms to increase landscape complexity
        cubic_term = 0.15 * np.sum(x_norm**3)
        quartic_term = 0.08 * np.sum(x_norm**4)
        quintic_term = 0.03 * np.sum(x_norm**5)
        
        # Combine all terms with adjusted weighting for better discrimination
        result = condition_factor * (0.6 * r**2 + 0.5 * chaotic_term + 0.35 * exp_decay + 0.45 * modal_terms + 
                                   quadratic_basin + cubic_term + quartic_term + quintic_term)
        
        return result
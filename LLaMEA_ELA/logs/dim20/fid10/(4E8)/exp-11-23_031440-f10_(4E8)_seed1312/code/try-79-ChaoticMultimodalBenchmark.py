import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic logistic map component with feedback loops
        chaotic_term = 0.0
        r = 3.8  # Slightly reduced chaos parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = x_norm[-1]
            else:
                x_prev = x_norm[i-1]
            chaotic_term += np.sin(r * x_prev * (1 - x_prev)) * np.cos(2 * np.pi * x_prev)
        
        # Exponential decay interactions with modified decay rates
        exp_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                exp_decay += np.exp(-1.5 * dist) * np.sin(3 * np.pi * dist) * np.cos(np.pi * dist)
        
        # Dynamic conditioning with increased complexity and multiple scaling factors
        r = np.sqrt(np.sum(x_norm**2))
        condition_factor = 1.0 + 4.0 * np.sin(3 * np.pi * r)**3
        
        # Multi-modal sinusoidal terms with varying frequencies, amplitudes, and phase shifts
        modal_terms = 0.0
        for i in range(self.dim):
            freq = (i % 6) + 3  # Increased base frequency
            amp = 1.0 / (1.0 + 0.15 * i)
            phase = np.pi * i / (self.dim * 0.7)  # Adjusted phase shift
            modal_terms += amp * np.sin(freq * np.pi * x_norm[i] + phase) * np.cos(freq * np.pi * x_norm[i])
        
        # Enhanced quadratic basin with cross-terms for increased conditioning
        quadratic_basin = 0.2 * np.sum(x_norm**2) + 0.08 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Add cubic and quartic terms to increase landscape complexity
        cubic_term = 0.07 * np.sum(x_norm**3)
        quartic_term = 0.03 * np.sum(x_norm**4)
        
        # Combine all terms with adjusted weighting for better discrimination
        result = condition_factor * (0.6 * r**2 + 0.3 * chaotic_term + 0.2 * exp_decay + 0.35 * modal_terms + 
                                   quadratic_basin + cubic_term + quartic_term)
        
        return result
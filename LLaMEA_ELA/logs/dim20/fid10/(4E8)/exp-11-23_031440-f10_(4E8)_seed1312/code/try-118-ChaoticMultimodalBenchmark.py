import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic logistic map with multiple feedback loops and higher chaos parameter
        chaotic_term = 0.0
        r = 4.0  # Increased chaos parameter
        for i in range(self.dim):
            x_prev = x_norm[i] if i == 0 else x_norm[i-1]
            x_next = x_norm[(i+1) % self.dim] if i < self.dim - 1 else x_norm[0]
            chaotic_term += np.sin(r * x_prev * (1 - x_prev)) * np.cos(2 * np.pi * x_prev) * np.sin(np.pi * x_next) * np.tanh(3.0 * x_prev)
        
        # Multi-scale exponential decay with varying rates and coupling terms
        exp_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                exp_decay += np.exp(-3.0 * dist) * np.sin(6 * np.pi * dist) * np.cos(3 * np.pi * dist) * (1 + 0.7 * np.sin(np.pi * (i+j)) + 0.3 * np.cos(2 * np.pi * i))
        
        # Dynamic conditioning with polynomial and trigonometric components
        r = np.sqrt(np.sum(x_norm**2))
        condition_factor = 1.0 + 8.0 * np.sin(5 * np.pi * r)**6 + 3.0 * np.cos(4 * np.pi * r)**2
        
        # Multi-modal sinusoidal terms with adaptive frequencies, amplitudes, phase shifts, and coupling
        modal_terms = 0.0
        for i in range(self.dim):
            freq = (i % 10) + 5  # Increased base frequency
            amp = 1.0 / (1.0 + 0.3 * i)
            phase = np.pi * i / (self.dim * 0.7)  # Adjusted phase shift
            modal_terms += amp * np.sin(freq * np.pi * x_norm[i] + phase) * np.cos(freq * np.pi * x_norm[i]) * np.sin(3 * np.pi * x_norm[i]) * np.tanh(2.0 * x_norm[i])
        
        # Enhanced quadratic basin with cross-terms and higher-order interactions
        quadratic_basin = 0.4 * np.sum(x_norm**2) + 0.2 * np.sum(x_norm[:-1] * x_norm[1:]) + 0.15 * np.sum(x_norm * x_norm[::-1]) + 0.05 * np.sum(x_norm**3)
        
        # Add higher-order polynomial terms to increase landscape complexity
        cubic_term = 0.15 * np.sum(x_norm**3)
        quartic_term = 0.08 * np.sum(x_norm**4)
        quintic_term = 0.04 * np.sum(x_norm**5)
        sextic_term = 0.02 * np.sum(x_norm**6)
        
        # Combine all terms with adjusted weighting for better discrimination
        result = condition_factor * (0.8 * r**2 + 0.5 * chaotic_term + 0.4 * exp_decay + 0.5 * modal_terms + 
                                   quadratic_basin + cubic_term + quartic_term + quintic_term + sextic_term)
        
        # Major mutation: Introduce a novel hyperbolic secant component to increase gradient complexity and non-linearity
        sech_component = 0.1 * np.sum(np.power(np.cosh(2.0 * x_norm), -2))
        
        # Add the new component to the result
        result += sech_component
        
        # Additional mutation: Introduce a fractional Brownian motion-like term with fractal characteristics
        fbm_term = 0.0
        for i in range(self.dim):
            fbm_term += np.sin(2**i * x_norm[i]) * (1.0 / (1.0 + 0.1 * i)) * np.cos(np.pi * x_norm[i]**2)
        
        result += 0.2 * fbm_term
        
        # Final adjustment: Add a global scaling factor that depends on dimensionality
        global_scale = 1.0 + 0.1 * self.dim
        result *= global_scale
        
        return result
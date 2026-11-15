import numpy as np

class MultimodalChaoticAttractor:
    def __init__(self, dim):
        self.dim = dim
        # Initialize dynamic scaling factors
        self.scaling_factors = np.array([np.exp(-0.1 * i) * np.sin(i * 0.5) for i in range(dim)])
        # Precompute periodic coefficients for attractor terms
        self.attractor_coeffs = np.array([np.cos(i * 0.3) + 1.5 for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base with dynamic scaling
        result = np.sum(self.scaling_factors * x**2)
        
        # Add periodic attractor terms with asymmetric coupling
        for i in range(self.dim):
            # Asymmetric sinusoidal attractors
            result += self.attractor_coeffs[i] * np.sin(x[i] * (1.0 + 0.3 * np.cos(x[i] * 0.5))) * np.exp(-0.1 * x[i]**2)
            
        # Cross-dimensional asymmetric correlations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric interaction term
                asym_factor = 1.0 + 0.2 * np.sin(i * 0.3) * np.cos(j * 0.4)
                result += asym_factor * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Multi-scale periodic modulations
        for i in range(self.dim):
            # High-frequency modulation
            result += 0.5 * np.sin(10.0 * x[i]) * np.cos(5.0 * x[i]) * np.exp(-0.02 * np.abs(x[i]))
            # Medium-frequency modulation
            result += 0.3 * np.sin(3.0 * x[i]) * np.cos(1.5 * x[i]) * np.exp(-0.03 * x[i]**2)
            
        # Dynamic basin boundaries with exponential decay
        for i in range(self.dim):
            result += 0.2 * np.exp(-0.01 * np.abs(x[i])) * np.sin(2.0 * x[i]) * np.cos(2.0 * x[i])
            
        # Add global minimum attractor with non-linear scaling
        global_min_term = 0.0
        for i in range(self.dim):
            global_min_term += np.sin(0.5 * x[i]) * np.exp(-0.05 * x[i]**2)
        result += 0.1 * global_min_term**2
        
        # Introduce chaotic phase shifts with memory effect
        phase_shift = np.sum(np.sin(x * 0.7) * np.cos(x * 0.3))
        result += 0.15 * np.sin(phase_shift) * np.cos(phase_shift * 0.8)
        
        # Add multi-modal structure with varying depths
        modal_depth = 0.0
        for i in range(self.dim):
            modal_depth += 0.4 * np.sin(4.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.03 * np.abs(x[i]))
        result += modal_depth
        
        # Final dynamic scaling with global influence
        global_scale = 1.0 + 0.1 * np.sin(np.sum(x) * 0.2)
        result *= global_scale
        
        return result
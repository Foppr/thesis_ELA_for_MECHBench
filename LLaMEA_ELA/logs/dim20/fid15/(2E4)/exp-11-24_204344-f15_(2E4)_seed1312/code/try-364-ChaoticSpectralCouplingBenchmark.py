import numpy as np

class ChaoticSpectralCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Chaotic oscillator component with time-delayed feedback
        chaotic_term = 0.0
        for i in range(self.dim):
            # Use a logistic map for chaotic dynamics
            chaotic_val = 0.0
            a = 3.9 + 0.1 * np.sin(i * 0.5)
            x_prev = x[i] if i > 0 else x[-1]
            chaotic_val = a * x_prev * (1 - x_prev)
            chaotic_term += np.sin(chaotic_val * 10.0) * np.cos(chaotic_val * 7.0)
        
        # Spectral filtering with frequency-dependent attenuation
        spectral_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.4 + self.dim * 0.3)
            amp = 1.0 + 0.5 * np.cos(i * 0.6 + self.dim * 0.2)
            spectral_term += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive coupling with dimension interaction
        coupling_term = 0.0
        for i in range(self.dim):
            # Create a coupling strength that varies with position and dimension
            coupling_strength = 0.5 + 0.5 * np.sin(x[i] * 0.3 + i * 0.7)
            if i > 0:
                coupling_term += coupling_strength * (x[i] - x[i-1])**2
        
        # Emergent symmetry breaking with mirror reflections
        symmetry_term = 0.0
        for i in range(self.dim):
            # Apply asymmetric modulation based on dimension index
            asym_factor = 1.0 + 0.3 * np.sin(i * 0.8)
            symmetry_term += asym_factor * np.sin(x[i] * 2.0) * np.cos(x[i] * 1.5)
        
        # Scale-invariant features with multi-resolution structure
        scale_term = 0.0
        for i in range(self.dim):
            # Add components at multiple scales
            for k in range(1, 4):
                scale_factor = 1.0 / (k ** 1.5)
                scale_term += scale_factor * np.sin(k * x[i] * 0.5) * np.cos(k * x[i] * 0.3)
        
        # Dynamic conditioning with nonlinear transformations
        condition_term = 0.0
        for i in range(self.dim):
            # Apply a dynamic transformation that depends on the entire vector
            trans_val = x[i] + 0.1 * np.sum(x) * np.sin(i * 0.2)
            condition_term += np.tanh(trans_val) ** 2
        
        # Combine all terms with chaotic weights
        total = (0.25 * chaotic_term + 
                0.20 * spectral_term + 
                0.15 * coupling_term + 
                0.20 * symmetry_term + 
                0.10 * scale_term + 
                0.10 * condition_term)
        
        # Apply a global chaotic modulation factor
        global_mod = 1.0 + 0.3 * np.sin(np.sum(x) * 0.5 + self.dim * 0.4)
        
        return total * global_mod
import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dimensionality
        self.chaotic_seq = np.array([np.sin(2**i * np.pi * 0.12345) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic radial basis components
        for i in range(self.dim):
            # Use logistic map-like behavior for radial basis centers
            center = 4 * self.chaotic_seq[i] * (1 - self.chaotic_seq[i])
            f_val += 0.5 * np.exp(-0.5 * (x[i] - center)**2) * np.sin(10 * x[i])
            
        # Add asymmetric coupling terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric interaction based on chaotic sequence
                asym_factor = 1 + 0.3 * self.chaotic_seq[i] * np.sin(x[j])
                f_val += asym_factor * np.sin(3 * x[i]) * np.cos(2 * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Add polynomial chaos terms with dynamic exponents
        for i in range(self.dim):
            # Exponent varies based on chaotic sequence
            exp_val = 2 + 3 * self.chaotic_seq[i]
            f_val += 0.1 * (x[i]**exp_val) * np.cos(5 * x[i])
            
        # Add cross-dimensional coupling with sine-cosine products
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.2 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (1 + 0.1 * np.sin(7 * x[i]))
                
        # Add a complex multi-modal component using chaotic modulation
        modulator = np.sum(np.sin(self.chaotic_seq * x))
        f_val += 0.3 * np.sin(modulator) * np.cos(4 * np.sum(x)) + 0.1 * np.sin(8 * np.sum(x))
        
        # Add a perturbation term based on chaotic sequence
        perturbation = np.sum(self.chaotic_seq * np.sin(x))
        f_val += 0.05 * np.tan(perturbation)
        
        # Add a final non-monotonic transformation
        f_val += 0.02 * np.sum(np.abs(x) * np.sin(10 * x))
        
        return f_val
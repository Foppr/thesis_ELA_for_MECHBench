import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for initialization
        self.chaotic_seq = self._generate_chaotic_sequence()
    
    def _generate_chaotic_sequence(self):
        # Generate a chaotic sequence using logistic map
        seq = np.zeros(self.dim)
        x = 0.5
        for i in range(self.dim):
            x = 4 * x * (1 - x)
            seq[i] = x
        return seq
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic radial basis function component
        f2 = 0.0
        for i in range(self.dim):
            # Use chaotic sequence to modulate RBF centers
            center = self.chaotic_seq[i] * 2 - 1  # Map to [-1, 1]
            f2 += np.exp(-5.0 * (x_norm[i] - center)**2)
        
        # Add multi-modal sinusoidal interference
        f3 = 0.3 * np.sum(np.sin(10 * x_norm) * np.cos(5 * x_norm))
        
        # Introduce cross-dimensional interactions with chaotic coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling between dimensions
                coupling = self.chaotic_seq[i] * self.chaotic_seq[j]
                f4 += coupling * (x_norm[i] - x_norm[j])**2
        
        # Add a quartic term with chaotic modulation
        f5 = 0.05 * np.sum((x_norm**2 + 0.1 * self.chaotic_seq)**2)
        
        return f1 + f2 + f3 + f4 + f5
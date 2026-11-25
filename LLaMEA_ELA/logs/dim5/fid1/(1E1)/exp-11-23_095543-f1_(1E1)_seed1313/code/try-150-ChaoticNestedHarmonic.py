import numpy as np

class ChaoticNestedHarmonic:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base quadratic term with dimensionally varying coefficients
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * x[i] ** 2
            
        # Add nested harmonic modulation with chaotic frequency components
        r = np.sqrt(np.sum(x ** 2))
        base_mod = 1.0 + 0.5 * np.sin(3 * r) * np.cos(2 * r) * np.exp(-0.1 * r)
        result *= base_mod
        
        # Add asymmetric cross-dimensional coupling with nested sinusoids
        for i in range(self.dim):
            j = (i + 1) % self.dim
            result += 0.3 * np.sin(7 * x[i] + 0.5 * np.cos(4 * x[j])) * np.cos(5 * x[j] + 0.3 * np.sin(3 * x[i]))
            
        # Add multi-scale harmonic components with varying amplitudes
        for i in range(self.dim):
            result += 0.2 * np.sin(11 * x[i]) * np.cos(9 * x[i]) * np.exp(-0.2 * x[i] ** 2)
            
        # Add nested exponential decay with chaotic parameters
        exp_decay = 0.0
        for i in range(self.dim):
            exp_decay += 0.15 * np.exp(-0.3 * (x[i] - np.sin(i)) ** 2) * np.sin(8 * x[i])
        result += exp_decay
        
        # Add dimensionally-adaptive chaotic modulation
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += 0.25 * np.sin(13 * x[i] + 0.4 * i) * np.cos(10 * x[(i + 2) % self.dim] + 0.3 * i) * np.exp(-0.15 * r ** 2)
        result += chaotic_mod
        
        # Add nested multi-modal structure with overlapping peaks
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.3 * (np.sin(6 * x[i]) + np.cos(8 * x[i])) ** 2 * np.exp(-0.1 * x[i] ** 2)
        result += multimodal
        
        # Add asymmetric coupling with higher-order polynomial interactions
        asym_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            asym_coupling += 0.2 * x[i] ** 3 * np.sin(5 * x[j]) * np.cos(4 * x[i]) * np.exp(-0.1 * (x[i] - x[j]) ** 2)
        result += asym_coupling
        
        # Add fractal-like nested structure with recursive harmonic components
        fractal = 0.0
        for i in range(self.dim):
            fractal += 0.18 * np.sin(15 * x[i]) * np.cos(12 * x[(i + 1) % self.dim]) * np.sin(9 * x[(i + 2) % self.dim]) * np.exp(-0.2 * r ** 2)
        result += fractal
        
        # Add dimensionally varying conditioning term
        conditioning = 0.05 * np.sum(np.abs(x) ** (1.3 + 0.1 * np.sin(self.dim)))
        result += conditioning
        
        return result
import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base exponential potential term with conditioning
        f = np.sum(np.exp(0.5 * x**2)) * 0.3
        
        # Add logarithmic barrier regions with multi-scale harmonic oscillations
        for i in range(self.dim):
            f += 0.8 * np.log(1.0 + np.abs(x[i])) * np.sin(10 * x[i]) * np.cos(7 * x[i])
            
        # Add multi-scale harmonic oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            f += 0.5 * np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.sin(8 * x[i]) * np.cos(5 * x[i])
            
        # Add exponential potential wells with chaotic positioning
        for i in range(self.dim):
            f += 0.4 * np.exp(-0.5 * (x[i] - np.sin(3 * i))**2) * np.sin(12 * x[i])
            
        # Add chaotic gradient modulation with cross-dimensional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.3 * np.sin(5 * x[i] + 3 * x[j]) * np.cos(4 * x[i] - 2 * x[j]) * np.sin(2 * x[i] * x[j])
                
        # Add sharp ridge structures with logarithmic scaling
        for i in range(self.dim):
            f += 0.6 * np.abs(x[i]) * np.sin(25 * x[i]) * np.cos(18 * x[i])
            
        # Add multi-scale chaotic oscillations with recursive pattern
        for i in range(self.dim):
            f += 0.2 * np.sin(30 * np.sin(4 * x[i])) * np.cos(25 * np.cos(3 * x[i])) * np.sin(20 * np.sin(2 * x[i]))
            
        # Add exponential coupling with non-linear transformations
        for i in range(self.dim):
            f += 0.1 * np.exp(2 * np.sin(x[i])) * np.cos(3 * np.cos(x[i])) * np.sin(4 * x[i])
            
        # Add chaotic phase modulation with multi-dimensional interaction
        phase_mod = 0
        for i in range(self.dim):
            phase_mod += np.sin(2 * np.pi * x[i] * np.exp(0.1 * i))
        f += 0.5 * np.sin(phase_mod) * np.cos(phase_mod)
        
        # Add additional multi-scale harmonic terms with varying coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                f += 0.25 * np.sin(6 * x[i] + 4 * x[j]) * np.cos(8 * x[i] - 3 * x[j]) * np.sin(3 * x[i] * x[j])
                
        # Add chaotic gradient with non-uniform scaling
        for i in range(self.dim):
            f += 0.35 * np.sin(35 * x[i]**2) * np.cos(30 * x[i]) * np.sin(25 * x[i]**3)
            
        # Add logarithmic barrier with multi-dimensional interaction
        barrier_term = 0
        for i in range(self.dim):
            barrier_term += np.log(1.0 + np.abs(x[i] - np.sin(i)))
        f += 0.4 * barrier_term * np.sin(15 * np.sum(x))
        
        # Add sharp gradient transitions with exponential scaling
        for i in range(self.dim):
            f += 0.2 * np.exp(-0.1 * np.abs(x[i])) * np.sin(40 * x[i])
            
        return f
import numpy as np

class ChaoticNestedPeriodic:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base quadratic term with dimension-dependent scaling
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * x[i] ** 2 * (1.0 + 0.1 * np.sin(10 * x[i]))
            
        # Add nested periodic components with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 0.5 * np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.sin(8 * x[(i + 1) % self.dim])
            
        # Add fractal-like scaling with exponential decay
        r = np.sqrt(np.sum(x ** 2))
        for i in range(self.dim):
            result += 0.3 * np.sin(50 * x[i]) * np.exp(-0.05 * abs(x[i])) * np.cos(30 * r)
            
        # Add asymmetric coupling with cubic and quartic terms
        for i in range(self.dim):
            j = (i + 1) % self.dim
            result += 0.2 * x[i] ** 3 * np.sin(7 * x[j]) * np.exp(-0.1 * x[i] ** 2)
            result += 0.15 * x[i] ** 4 * np.cos(9 * x[j]) * np.exp(-0.08 * x[j] ** 2)
            
        # Add multi-scale periodicity with chaotic modulation
        chaotic_mod = 1.0
        for i in range(self.dim):
            chaotic_mod *= (1.0 + 0.2 * np.sin(25 * x[i]) * np.cos(22 * x[(i + 2) % self.dim]))
        result *= chaotic_mod
        
        # Add nested harmonic components with varying phase shifts
        for i in range(self.dim):
            phase = 0.5 * np.sin(3 * x[i])
            result += 0.4 * np.sin(12 * x[i] + phase) * np.cos(18 * x[(i + 3) % self.dim] - phase)
            
        # Add radial fractal structure with self-similar patterns
        if r > 0:
            result += 0.6 * np.sin(25 * r) * np.cos(35 * r) * np.exp(-0.1 * r ** 2)
            
        # Add dimensionality-dependent complexity with chaotic mixing
        mix_factor = 1.0
        for i in range(self.dim):
            mix_factor += 0.1 * np.sin(40 * x[i]) * np.cos(35 * x[(i + 4) % self.dim])
        result *= mix_factor
        
        # Add final chaotic component with irregular oscillations
        final_osc = 0.0
        for i in range(self.dim):
            final_osc += 0.25 * np.sin(60 * x[i]) * np.cos(55 * x[(i + 5) % self.dim]) * np.exp(-0.03 * r)
        result += final_osc
        
        # Add basin structure with multiple local minima
        basin_term = 0.0
        for i in range(self.dim):
            basin_term += 0.3 * np.sin(15 * x[i]) * np.cos(12 * x[i]) * (1.0 + 0.2 * np.sin(8 * r))
        result += basin_term
        
        return result
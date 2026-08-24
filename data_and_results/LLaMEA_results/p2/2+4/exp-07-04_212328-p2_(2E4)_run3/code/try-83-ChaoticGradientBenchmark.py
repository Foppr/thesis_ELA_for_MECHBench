import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term with varying conditioning
        f = 0.5 * np.sum(x**2)
        
        # Add chaotic exponential decay interactions
        for i in range(self.dim):
            f += 0.3 * np.exp(-0.5 * x[i]**2) * np.sin(10 * x[i])
            
        # Add asymmetric harmonic modulations with directional bias
        for i in range(self.dim):
            f += 0.2 * np.sin(5 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Add multi-scale gradient variations with varying frequencies
        for i in range(self.dim):
            f += 0.15 * np.sin(15 * x[i]) * np.cos(7 * x[i]) * np.sin(3 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Add saddle point structure with exponential coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                f += 0.1 * np.exp(-0.2 * (x[i]**2 + x[j]**2)) * np.sin(4 * x[i] + 3 * x[j]) * np.cos(2 * x[i] - x[j])
                
        # Add chaotic gradient modulation with recursive structure
        for i in range(self.dim):
            f += 0.08 * np.sin(20 * np.sin(5 * x[i])) * np.cos(15 * np.cos(4 * x[i])) * np.exp(-0.1 * x[i]**2)
            
        # Add asymmetric harmonic landscape with varying amplitudes
        for i in range(self.dim):
            f += 0.25 * np.sin(8 * x[i]) * np.cos(6 * x[i]) * np.exp(-0.08 * np.abs(x[i]))
            
        # Add multi-modal structure with varying scales and positions
        for i in range(self.dim):
            f += 0.1 * np.exp(-0.3 * (x[i] - 2.0)**2) * np.sin(12 * x[i]) + 0.1 * np.exp(-0.3 * (x[i] + 2.0)**2) * np.cos(10 * x[i])
            
        # Add directional bias with exponential scaling
        for i in range(self.dim):
            f += 0.05 * x[i] * np.exp(-0.1 * np.abs(x[i])) * np.sin(5 * x[i])
            
        # Add higher-order gradient interactions with non-linear coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.07 * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(3 * x[i] * x[j]) * np.cos(2 * x[i] + x[j])
                
        # Add complex harmonic coupling with variable phase shifts
        for i in range(self.dim):
            f += 0.12 * np.sin(18 * x[i] + 0.5 * np.sin(3 * x[i])) * np.cos(12 * x[i] + 0.3 * np.cos(2 * x[i]))
            
        # Add chaotic modulation with exponential decay and harmonic components
        for i in range(self.dim):
            f += 0.06 * np.exp(-0.2 * x[i]**2) * np.sin(25 * x[i]) * np.cos(15 * x[i]) * np.exp(-0.03 * np.abs(x[i]))
            
        # Add multi-scale exponential interactions
        for i in range(self.dim):
            f += 0.09 * np.exp(-0.15 * x[i]**2) * np.sin(30 * x[i]) * np.cos(20 * x[i]) * np.sin(10 * x[i])
            
        # Add asymmetric saddle points with varying depths
        for i in range(self.dim):
            f += 0.15 * np.exp(-0.2 * (x[i] - 1.5)**2) * np.sin(6 * x[i]) * np.cos(4 * x[i]) * np.exp(-0.05 * np.abs(x[i]))
            
        # Add gradient-based directional bias with exponential weighting
        for i in range(self.dim):
            f += 0.04 * x[i]**3 * np.exp(-0.1 * np.abs(x[i])) * np.sin(8 * x[i])
            
        # Add ultra-high frequency chaotic components
        for i in range(self.dim):
            f += 0.03 * np.sin(50 * x[i]) * np.cos(40 * x[i]) * np.sin(30 * x[i]) * np.exp(-0.02 * x[i]**2)
            
        # Add complex harmonic coupling with variable coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.05 * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(5 * x[i] * x[j]) * np.cos(3 * x[i] + 2 * x[j]) * np.sin(2 * x[i] - x[j])
                
        # Add multi-scale harmonic modulations with varying amplitudes
        for i in range(self.dim):
            f += 0.11 * np.sin(25 * x[i]) * np.cos(18 * x[i]) * np.sin(12 * x[i]) * np.exp(-0.06 * np.abs(x[i]))
            
        return f
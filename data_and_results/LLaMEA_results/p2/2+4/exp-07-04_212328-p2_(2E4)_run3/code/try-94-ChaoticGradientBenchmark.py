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
        
        # Add chaotic gradient components with varying frequencies
        for i in range(self.dim):
            f += 0.3 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.sin(5 * x[i])
            
        # Add multi-scale harmonic interactions with exponential coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                f += 0.2 * np.sin(3 * x[i] + 2 * x[j]) * np.cos(4 * x[i] - x[j]) * np.sin(2 * x[i] * x[j])
                
        # Add saddle point structure with hyperbolic tangent components
        for i in range(self.dim):
            f += 0.15 * np.tanh(3 * x[i]) * np.sin(5 * x[i]) * np.cos(2 * x[i])
            
        # Add variable-dimensional coupling with phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = np.sin(0.5 * (i + j))
                f += 0.1 * np.sin(2 * x[i] + x[j] + phase_shift) * np.cos(x[i] - 2 * x[j] + phase_shift)
                
        # Add chaotic modulation with recursive structure
        for i in range(self.dim):
            f += 0.12 * np.sin(15 * np.sin(4 * x[i])) * np.cos(12 * np.cos(3 * x[i])) * np.sin(8 * np.sin(2 * x[i]))
            
        # Add curvature-inducing polynomial terms
        for i in range(self.dim):
            f += 0.08 * x[i]**4 + 0.05 * x[i]**3 + 0.03 * x[i]**2
            
        # Add asymmetric harmonic components for gradient complexity
        for i in range(self.dim):
            f += 0.25 * np.sin(8 * x[i]) * np.cos(6 * x[i]) * np.sin(4 * x[i]) * np.cos(2 * x[i])
            
        # Add cross-dimensional coupling with varying strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.1 * (i + 1) / (j + 1)
                f += strength * np.sin(3 * x[i] * x[j]) * np.cos(2 * x[i] + x[j]) * np.sin(x[i] - x[j])
                
        # Add chaotic gradient modulation with exponential scaling
        gradient_mod = 0
        for i in range(self.dim):
            gradient_mod += np.sin(2 * np.pi * x[i] * np.exp(0.2 * i))
        f += 0.2 * np.sin(gradient_mod)
        
        # Add multi-modal structure with varying scales
        for i in range(self.dim):
            f += 0.18 * np.sin(12 * x[i]) * np.cos(9 * x[i]) * np.sin(6 * x[i]) * np.cos(3 * x[i])
            
        # Add complex curvature with higher-order terms
        for i in range(self.dim):
            f += 0.06 * x[i]**5 + 0.04 * x[i]**4 + 0.02 * x[i]**3
            
        # Add non-uniform scaling with chaotic components
        for i in range(self.dim):
            f += 0.1 * np.sin(20 * x[i]**2) * np.cos(15 * x[i]**2) * np.sin(10 * x[i]**2)
            
        # Add variable-dimensional coupling with non-linear interaction
        if self.dim > 2:
            for i in range(0, self.dim - 2, 3):
                f += 0.08 * np.sin(2 * x[i] * x[i+1] + x[i+2]) * np.cos(x[i] + x[i+1] * x[i+2]) * np.sin(x[i] * x[i+1] - x[i+2])
                
        # Add chaotic phase modulation with complex interaction
        phase_sum = 0
        for i in range(self.dim):
            phase_sum += np.sin(3 * np.pi * x[i] * (i + 1) * 0.1)
        f += 0.15 * np.sin(phase_sum) * np.cos(phase_sum * 0.5) * np.sin(phase_sum * 0.25)
        
        # Add additional saddle point components
        for i in range(self.dim):
            f += 0.09 * np.tanh(5 * x[i]) * np.sin(3 * x[i]) * np.cos(4 * x[i])
            
        return f
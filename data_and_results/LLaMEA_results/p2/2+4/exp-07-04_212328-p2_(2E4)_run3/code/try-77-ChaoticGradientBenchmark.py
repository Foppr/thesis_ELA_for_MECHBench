import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base polynomial with varying degrees and dynamic scaling
        f = 0.0
        for i in range(self.dim):
            # Dynamic scaling factor based on position
            scale = 1.0 + 0.5 * np.sin(x[i] * 0.5)
            f += scale * (x[i]**4 + 0.5 * x[i]**3 + 0.2 * x[i]**2 + 0.1 * x[i])
            
        # Add chaotic interaction terms with dynamic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on distance
                dist = np.abs(x[i] - x[j])
                coupling = 0.3 * np.exp(-dist * 0.5) * np.sin(x[i] * x[j])
                f += coupling
                
        # Add implicit constraint surface with penalty
        constraint_sum = 0.0
        for i in range(self.dim):
            constraint_sum += np.sin(x[i] * 2.0) * np.cos(x[i] * 1.5)
        penalty = 10.0 * np.maximum(0.0, constraint_sum)**2
        f += penalty
        
        # Add multi-scale oscillatory components with varying frequencies
        for i in range(self.dim):
            f += 2.0 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.sin(3 * x[i])
            
        # Add directional bias with gradient modulation
        gradient_bias = 0.0
        for i in range(self.dim):
            gradient_bias += (i + 1) * np.sin(x[i] * (i + 1) * 0.8)
        f += 0.5 * gradient_bias**2
        
        # Add chaotic modulation with recursive structure
        for i in range(self.dim):
            f += 0.4 * np.sin(15 * np.sin(3 * x[i])) * np.cos(12 * np.cos(2 * x[i]))
            
        # Add dynamic curvature with position-dependent Hessian effects
        for i in range(self.dim):
            f += 0.3 * np.sin(x[i]**2) * np.cos(x[i] * 0.5) * np.sin(x[i] * 0.3)
            
        # Add multi-modal structure with varying amplitudes
        for i in range(self.dim):
            f += 0.2 * np.sin(5 * x[i] + 2) * np.cos(3 * x[i] - 1) * np.sin(2 * x[i] + 1)
            
        # Add noise component with spatial correlation
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * 7.0) * np.cos(x[i] * 4.0) * np.sin(x[i] * 2.0)
        f += 0.1 * noise
        
        return f
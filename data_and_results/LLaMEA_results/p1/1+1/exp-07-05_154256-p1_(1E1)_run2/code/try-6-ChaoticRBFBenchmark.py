import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for nonlinearity
        self.chaos_seq = np.array([np.sin(2**i * np.pi * 0.1) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial Basis Function component with chaotic scaling
        rbf = 0
        for i in range(self.dim):
            rbf += np.exp(-0.5 * np.sum((x - self.chaos_seq[i]) ** 2)) * np.sin(2 * np.pi * x[i])
        
        # Logistic map chaotic dynamics component
        chaos = 0
        r = 3.99  # Chaos parameter
        for i in range(self.dim):
            chaos += (r * x[i] * (1 - x[i])) * np.cos(0.5 * x[i])
        
        # Asymmetric coupling terms
        asym = 0
        for i in range(self.dim-1):
            asym += (x[i] ** 3) * np.exp(-0.1 * x[i+1]**2) + (x[i+1] ** 2) * np.sin(0.2 * x[i])
        
        # Fractional polynomial interaction
        frac_poly = 0
        for i in range(self.dim):
            frac_poly += x[i] ** 1.5 * np.cos(0.3 * x[i]) + x[i] ** 0.7
        
        # Cross-term with sine modulation
        cross = 0
        for i in range(self.dim):
            cross += np.sin(0.1 * x[i]) * np.exp(-0.05 * x[i]**2) * np.cos(0.2 * x[i])
        
        # Combine all components with varying weights
        return 0.3 * rbf + 1.2 * chaos + 0.8 * asym + 0.4 * frac_poly + 0.2 * cross
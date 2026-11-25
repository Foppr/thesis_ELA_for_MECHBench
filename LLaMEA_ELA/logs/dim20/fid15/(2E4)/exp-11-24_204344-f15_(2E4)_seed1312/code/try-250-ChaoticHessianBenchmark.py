import numpy as np

class ChaoticHessianBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Chaotic gradient component with dynamic scaling
        grad_term = 0.0
        for i in range(self.dim):
            # Dynamic gradient magnitude with chaotic modulation
            scale = 1.0 + 0.3 * np.sin(3.0 * x[i] + i) + 0.2 * np.cos(7.0 * x[i] - i)
            grad_term += scale * x[i]**2
        
        # Saddle-point embedded structure with dynamic positioning
        saddle_term = 0.0
        for i in range(self.dim):
            # Create saddle points at dynamic locations
            pos = 2.0 * np.sin(0.5 * i) + 0.5 * np.cos(1.3 * i)
            saddle_term += (x[i] - pos)**2 * (x[i] + pos)**2
        
        # Hessian conditioning with dynamic eigenvalues
        hess_term = 0.0
        for i in range(self.dim):
            # Dynamic eigenvalue scaling based on position and dimension
            lambda1 = 1.0 + 0.5 * np.sin(x[i] + i)
            lambda2 = 1.0 + 0.3 * np.cos(x[i] - i)
            hess_term += lambda1 * x[i]**4 + lambda2 * x[i]**2
        
        # Cross-dimensional coupling with chaotic interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling strength
                coupling = np.sin(2.0 * x[i]) * np.cos(3.0 * x[j]) + 0.1 * np.sin(5.0 * (x[i] + x[j]))
                cross_term += coupling
        
        # Multi-scale periodic structure with recursive modulation
        periodic_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i)
            amp = 1.0 + 0.3 * np.cos(i)
            periodic_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Asymmetric basin structure with dynamic depth
        basin_term = 0.0
        for i in range(self.dim):
            # Dynamic basin depth based on position and dimension
            depth = 1.0 + 0.4 * np.sin(x[i] + i) + 0.2 * np.cos(2.0 * x[i])
            basin_term += depth * (x[i]**2 - 1.0)**2
        
        # Final composition with adaptive weights
        total = 0.3 * grad_term + 0.25 * saddle_term + 0.2 * hess_term + 0.15 * cross_term + 0.08 * periodic_term + 0.02 * basin_term
        
        # Global scaling factor with chaotic modulation
        scaling = 1.0 + 0.1 * np.sin(self.dim) + 0.05 * np.cos(self.dim * 0.7)
        
        return total * scaling
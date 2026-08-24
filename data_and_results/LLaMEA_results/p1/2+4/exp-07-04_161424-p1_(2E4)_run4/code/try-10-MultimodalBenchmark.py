import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic logistic map
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            # Logistic map with chaotic behavior
            logistic = 4.0 * x_norm[i] * (1.0 - x_norm[i])
            # Radial basis function with chaotic modulation
            rbfs[i] = np.exp(-10 * (x_norm[i] - logistic)**2) + 0.1 * np.sin(20 * x_norm[i])
        
        # Sum of radial basis functions
        radial_term = np.sum(rbfs)
        
        # Chaotic sine wave component
        chaotic_sine = np.sum(np.sin(100 * np.abs(x_norm) + np.sin(50 * x_norm))**2)
        
        # Polynomial cross-terms with gradient-based saddle points
        cross_poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_poly += (x_norm[i]**3 + x_norm[j]**3) * np.cos(5 * x_norm[i] * x_norm[j])
        
        # Gradient-based saddle point component
        saddle_term = np.sum((x_norm**2 - 1.0)**2 * np.cos(10 * x_norm))
        
        # Add global minimum perturbation
        perturbation = 0.05 * np.sum(np.sin(25 * x_norm)**4)
        
        # Combine all terms
        return 0.5 * radial_term + 0.3 * chaotic_sine + 0.2 * cross_poly + 0.1 * saddle_term + perturbation
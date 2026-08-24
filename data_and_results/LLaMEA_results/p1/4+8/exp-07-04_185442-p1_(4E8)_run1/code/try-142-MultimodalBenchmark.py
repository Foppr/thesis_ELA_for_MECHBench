import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.r_constants = np.linspace(3.5, 4.0, dim)
        self.sigma = 0.1
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map components
        logistic_terms = np.zeros(self.dim)
        for i in range(self.dim):
            r = self.r_constants[i]
            x_i = x_norm[i]
            logistic_terms[i] = r * x_i * (1 - x_i)
        
        # Multiquadratic radial basis functions
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            center = np.sin(i * np.pi / self.dim)
            rbfs[i] = (x_norm[i] - center)**2 + self.sigma
        
        # Adaptive gradient modulation
        grad_mod = np.zeros(self.dim)
        for i in range(self.dim):
            grad_mod[i] = np.exp(-0.5 * (x_norm[i] / (i + 1.0))**2)
        
        # Combine all terms with non-separability
        term1 = np.sum(logistic_terms**2)
        term2 = np.sum(1.0 / rbfs)
        term3 = np.sum(grad_mod * np.sin(5 * x_norm))
        term4 = np.sum(np.cos(3 * x_norm) * np.exp(-0.1 * x_norm**2))
        term5 = 0.5 * np.sum((x_norm[0] * x_norm[1])**4)
        
        # Add dynamic coupling between dimensions with modified interaction
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i] - x_norm[i+1])**2 * np.sin(x_norm[i] * x_norm[i+1] * 2)
        
        # Add modified polynomial cross-terms
        poly_cross = 0.0
        for i in range(self.dim - 2):
            poly_cross += (x_norm[i] * x_norm[i+1] * x_norm[i+2])**3
        
        # Add sinusoidal coupling with altered frequency
        sin_coupling = np.sum(np.sin(7 * x_norm) * np.cos(2 * x_norm))
        
        # Add noise for increased complexity
        noise = 0.01 * np.random.random()
        
        return term1 + term2 + term3 + term4 + term5 + coupling + poly_cross + sin_coupling + noise
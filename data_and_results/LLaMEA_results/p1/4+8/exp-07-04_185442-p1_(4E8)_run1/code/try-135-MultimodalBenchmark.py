import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.r_constants = np.linspace(3.8, 4.0, dim)
        self.sigma = 0.05
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine map components
        sine_terms = np.zeros(self.dim)
        for i in range(self.dim):
            r = self.r_constants[i]
            x_i = x_norm[i]
            sine_terms[i] = r * np.sin(np.pi * x_i)
        
        # Multiquadratic radial basis functions
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            center = np.cos(i * np.pi / self.dim)
            rbfs[i] = (x_norm[i] - center)**2 + self.sigma
        
        # Adaptive gradient modulation
        grad_mod = np.zeros(self.dim)
        for i in range(self.dim):
            grad_mod[i] = np.exp(-0.5 * (x_norm[i] / (i + 1.0))**2)
        
        # Combine all terms with non-separability
        term1 = np.sum(sine_terms**2)
        term2 = np.sum(1.0 / rbfs)
        term3 = np.sum(grad_mod * np.cos(3 * x_norm))
        term4 = np.sum(np.sin(2 * x_norm) * np.exp(-0.05 * x_norm**2))
        term5 = 0.3 * np.sum((x_norm[0] * x_norm[1])**3)
        
        # Add dynamic coupling between dimensions
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i] - x_norm[i+1])**2 * np.cos(x_norm[i] * x_norm[i+1])
        
        # Add noise for increased complexity
        noise = 0.005 * np.random.random()
        
        return term1 + term2 + term3 + term4 + term5 + coupling + noise
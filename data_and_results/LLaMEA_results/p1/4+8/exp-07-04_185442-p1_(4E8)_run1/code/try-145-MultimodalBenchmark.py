import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.r_constants = np.linspace(3.8, 4.0, dim)
        self.sigma = 0.05
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Enhanced chaotic logistic map with sine modulation
        logistic_terms = np.zeros(self.dim)
        for i in range(self.dim):
            r = self.r_constants[i]
            x_i = x_norm[i]
            logistic_terms[i] = r * x_i * (1 - x_i) * np.sin(2 * np.pi * x_i)
        
        # Modified multiquadratic RBF with adaptive centers
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            center = np.sin(i * np.pi / (self.dim + 1))
            rbfs[i] = (x_norm[i] - center)**2 + self.sigma * (i + 1)
        
        # Adaptive gradient modulation with cosine component
        grad_mod = np.zeros(self.dim)
        for i in range(self.dim):
            grad_mod[i] = np.exp(-0.3 * (x_norm[i] / (i + 1.0))**2) * np.cos(3 * x_norm[i])
        
        # Additional nonlinear cross-terms for increased complexity
        cross_terms = np.zeros(self.dim)
        for i in range(self.dim):
            cross_terms[i] = (x_norm[i]**3) * np.sin(4 * x_norm[(i + 1) % self.dim])
        
        # Combine all terms with improved separability and coupling
        term1 = np.sum(logistic_terms**2)
        term2 = np.sum(1.0 / rbfs)
        term3 = np.sum(grad_mod * np.sin(7 * x_norm))
        term4 = np.sum(np.cos(5 * x_norm) * np.exp(-0.15 * x_norm**2))
        term5 = 0.3 * np.sum((x_norm[0] * x_norm[1])**3)
        
        # Enhanced dynamic coupling between dimensions
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i] - x_norm[i+1])**3 * np.cos(x_norm[i] * x_norm[i+1])
        
        # Add higher-order polynomial noise
        noise = 0.005 * np.random.random() * np.sum(x_norm**4)
        
        # Introduce improved fitness scaling and bias reduction
        fitness = term1 + term2 + term3 + term4 + term5 + coupling + noise
        
        # Apply adaptive scaling to reduce bias and improve convergence
        adaptive_scale = 1.0 + 0.1 * np.sum(np.abs(x_norm))
        return fitness / adaptive_scale
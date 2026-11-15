import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.r_constants = np.linspace(3.8, 4.0, dim)
        self.sigma = 0.05
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Enhanced chaotic logistic maps with varying parameters
        logistic_terms = np.zeros(self.dim)
        for i in range(self.dim):
            r = self.r_constants[i]
            x_i = x_norm[i]
            logistic_terms[i] = r * x_i * (1 - x_i) * np.sin(x_i * np.pi)
        
        # Coupled radial basis functions with dynamic centers
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            center = np.sin(i * np.pi / (self.dim + 1)) * np.cos(i * np.pi / (self.dim + 2))
            rbfs[i] = (x_norm[i] - center)**2 + self.sigma * (i + 1)
        
        # Adaptive sine-cosine modulation with frequency coupling
        sc_mod = np.zeros(self.dim)
        for i in range(self.dim):
            sc_mod[i] = np.sin(2 * np.pi * x_norm[i] * (i + 1)) * np.cos(3 * np.pi * x_norm[i] * (i + 1))
        
        # Polynomial cross-terms with mixed conditioning
        poly_terms = np.zeros(self.dim)
        for i in range(self.dim):
            poly_terms[i] = (x_norm[i]**3) + (x_norm[i]**4) * np.sin(x_norm[i])
        
        # Dynamic coupling between adjacent dimensions
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i] - x_norm[i+1])**4 * np.cos(x_norm[i] * x_norm[i+1])
        
        # Add interaction terms between all dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(x_norm[i] * x_norm[j]) * (i + j + 1)
        
        # Combine all components
        term1 = np.sum(logistic_terms**2)
        term2 = np.sum(1.0 / rbfs)
        term3 = np.sum(sc_mod)
        term4 = np.sum(poly_terms)
        term5 = 0.3 * np.sum(x_norm**6)
        
        # Add noise and scaling for improved fitness
        noise = 0.005 * np.random.random()
        scaling = 1.0 + 0.1 * np.sum(x_norm**2)
        
        return (term1 + term2 + term3 + term4 + term5 + coupling + interaction) * scaling + noise
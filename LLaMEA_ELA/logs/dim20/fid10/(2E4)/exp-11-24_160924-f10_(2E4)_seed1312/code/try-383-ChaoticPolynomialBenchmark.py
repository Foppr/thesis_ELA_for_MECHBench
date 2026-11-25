import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize chaotic system parameters
        self.chaotic_a = np.random.uniform(3.5, 4.0, dim)
        self.chaotic_b = np.random.uniform(0.1, 0.3, dim)
        # Polynomial hierarchy coefficients
        self.poly_hier = np.random.uniform(-0.5, 0.5, (dim, dim, dim))
        # Noise injection parameters
        self.noise_amp = np.random.uniform(0.05, 0.2, dim)
        self.noise_freq = np.random.uniform(1.0, 3.0, dim)
        # Hierarchical interaction terms
        self.hier_weights = np.random.uniform(0.3, 1.5, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Chaotic dynamical system components
        for i in range(self.dim):
            # Logistic map with adaptive parameter
            chaotic_val = self.chaotic_a[i] * x[i] * (1.0 - x[i])
            # Add chaotic modulation
            chaotic_val += self.chaotic_b[i] * np.sin(2 * np.pi * x[i])
            result += 0.5 * chaotic_val**2
            
        # Hierarchical polynomial interactions
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(self.dim):
                for k in range(self.dim):
                    coeff = self.poly_hier[i][j][k]
                    poly_sum += coeff * x[j] * x[k]
            # Apply hierarchical scaling
            result += 0.3 * (poly_sum**3 + 0.1 * poly_sum**2)
            
        # Adaptive noise injection with chaotic modulation
        for i in range(self.dim):
            noise = self.noise_amp[i] * np.sin(self.noise_freq[i] * x[i])
            # Add chaotic modulation to noise
            noise += 0.05 * np.sin(3 * x[i]) * np.cos(2 * x[i])
            result += noise
            
        # Cross-dimensional hierarchical coupling
        for i in range(self.dim):
            hier_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = self.hier_weights[i][j]
                    # Apply nonlinear coupling with chaotic modulation
                    coupling = weight * np.sin(x[i] - x[j]) * (1.0 + 0.2 * np.sin(0.5 * x[i]))
                    hier_sum += coupling**2
            result += 0.2 * hier_sum
            
        # Global polynomial scaling with chaotic behavior
        global_poly = np.sum(x**4) + 0.2 * np.sum(x**6)
        result += 0.15 * global_poly
        
        return result
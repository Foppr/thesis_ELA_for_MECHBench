import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.tent_constants = np.linspace(1.5, 3.5, dim)
        self.elliptic_exponent = 2.0 + np.random.random(dim) * 3.0
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Chaotic tent map with adaptive parameter modulation
        tent_terms = np.zeros(self.dim)
        for i in range(self.dim):
            a = self.tent_constants[i]
            x_i = x_norm[i]
            if x_i < 0.5:
                tent_terms[i] = a * x_i
            else:
                tent_terms[i] = a * (1 - x_i)
        
        # Adaptive elliptic components with dynamic exponents
        elliptic_terms = np.zeros(self.dim)
        for i in range(self.dim):
            exponent = self.elliptic_exponent[i]
            elliptic_terms[i] = (x_norm[i]**exponent) * np.exp(-0.5 * (x_norm[i]**2))
        
        # Dynamic sine-cosine coupling between dimensions
        coupling_terms = np.zeros(self.dim)
        for i in range(self.dim):
            j = (i + 1) % self.dim
            coupling_terms[i] = np.sin(x_norm[i]) * np.cos(x_norm[j]) * np.exp(-0.1 * (x_norm[i] - x_norm[j])**2)
        
        # Additional nonlinear cross-terms with varying frequency
        cross_terms = np.zeros(self.dim)
        for i in range(self.dim):
            freq = 2.0 + i * 0.5
            cross_terms[i] = np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[(i + 2) % self.dim])
        
        # Combined objective function with enhanced multimodality
        term1 = np.sum(tent_terms**2)
        term2 = np.sum(elliptic_terms)
        term3 = np.sum(coupling_terms**2)
        term4 = np.sum(cross_terms**2)
        
        # Add dynamic coupling between all dimensions
        dynamic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_coupling += (x_norm[i] - x_norm[j])**4 * np.sin(x_norm[i] + x_norm[j])
        
        # Add noise term for increased complexity
        noise = 0.01 * np.random.random() * np.sum(np.abs(x_norm))
        
        return term1 + term2 + term3 + term4 + dynamic_coupling + noise
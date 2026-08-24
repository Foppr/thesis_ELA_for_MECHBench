import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters
        self.a_constants = np.linspace(1.5, 3.5, dim)
        self.b_constants = np.linspace(0.1, 0.9, dim)
        self.sigma = 0.05
        self.time = 0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic tent map components
        tent_terms = np.zeros(self.dim)
        for i in range(self.dim):
            a = self.a_constants[i]
            b = self.b_constants[i]
            x_i = x_norm[i]
            if x_i < b:
                tent_terms[i] = a * x_i / b
            else:
                tent_terms[i] = a * (1 - x_i) / (1 - b)
        
        # Hybrid radial basis functions with dynamic centers
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            center = np.sin(i * np.pi / self.dim + self.time * 0.1)
            rbfs[i] = (x_norm[i] - center)**2 + self.sigma + 0.01 * np.sin(self.time + i)
        
        # Spectral frequency modulations
        spectral_terms = np.zeros(self.dim)
        for i in range(self.dim):
            freq = (i + 1) * 2 * np.pi
            spectral_terms[i] = np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Adaptive gradient modulation with dynamic weights
        grad_mod = np.zeros(self.dim)
        for i in range(self.dim):
            weight = np.exp(-0.5 * (x_norm[i] / (i + 1.0))**2) * np.cos(self.time * 0.05 + i)
            grad_mod[i] = weight * np.sin(3 * x_norm[i])
        
        # Combine all terms with non-separability
        term1 = np.sum(tent_terms**2)
        term2 = np.sum(1.0 / rbfs)
        term3 = np.sum(grad_mod * spectral_terms)
        term4 = np.sum(np.cos(2 * x_norm) * np.exp(-0.05 * x_norm**2))
        term5 = 0.3 * np.sum((x_norm[0] * x_norm[1])**6)
        
        # Add dynamic coupling between dimensions with time-varying weights
        coupling = 0.0
        for i in range(self.dim - 1):
            weight = np.cos(self.time * 0.02 + i) * 0.5 + 0.5
            coupling += weight * (x_norm[i] - x_norm[i+1])**2 * np.sin(x_norm[i] * x_norm[i+1])
        
        # Add temporal noise and dynamic scaling
        noise = 0.02 * np.random.random() * np.sin(self.time * 0.1)
        scale_factor = 1.0 + 0.1 * np.sin(self.time * 0.05)
        
        # Update time for next evaluation
        self.time += 1
        
        return scale_factor * (term1 + term2 + term3 + term4 + term5 + coupling) + noise
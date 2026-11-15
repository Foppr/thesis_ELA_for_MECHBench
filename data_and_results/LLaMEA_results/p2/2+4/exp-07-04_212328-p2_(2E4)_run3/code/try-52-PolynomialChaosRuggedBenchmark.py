import numpy as np

class PolynomialChaosRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        # Precompute chaos coefficients for different dimensions
        self.chaos_coeffs = np.random.uniform(0.5, 2.0, size=(dim, 5))
        self.noise_scale = 0.1 + 0.2 * np.log10(dim + 1)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base polynomial landscape with varying degrees
        f = 0.0
        for i in range(self.dim):
            f += (x[i]**2 + 0.5 * x[i]**4 + 0.1 * x[i]**6) * self.chaos_coeffs[i, 0]
            
        # Add adaptive noise modulation based on input values
        noise = 0.0
        for i in range(self.dim):
            noise += self.noise_scale * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.sin(3 * x[i])
        f += noise
        
        # Introduce controlled ruggedness via multi-scale harmonic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling strength based on dimension
                coupling = 0.3 * (1 + 0.1 * (i + j)) / (1 + 0.05 * (i + j))
                f += coupling * np.sin(5 * x[i] + 3 * x[j]) * np.cos(4 * x[i] - 2 * x[j])
                
        # Add polynomial chaos terms with increasing complexity
        for i in range(self.dim):
            f += 0.2 * (x[i]**3 + x[i]**5) * self.chaos_coeffs[i, 1]
            
        # Add cross-dimensional coupling with varying frequency
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                freq = 2 + 0.5 * (i + j)
                f += 0.15 * np.sin(freq * x[i]) * np.cos(freq * x[j]) * np.sin(freq * (x[i] + x[j]))
                
        # Introduce a global minimum with adaptive scaling
        global_min = np.ones(self.dim) * 1.0
        diff = x - global_min
        f += 0.5 * np.sum(diff**2) * (1 + 0.1 * np.sin(2 * np.pi * self.dim))
        
        # Add higher-order chaos interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, min(j+2, self.dim)):
                    f += 0.05 * np.sin(2 * x[i] + x[j] - x[k]) * np.cos(x[i] * x[j] * x[k])
                    
        # Add dimension-dependent scaling factor
        f *= (1 + 0.05 * np.log10(self.dim + 1))
        
        # Add final chaotic modulation
        phase = np.sum(np.sin(2 * x))
        f += 0.1 * np.sin(phase) * np.cos(phase)
        
        return f
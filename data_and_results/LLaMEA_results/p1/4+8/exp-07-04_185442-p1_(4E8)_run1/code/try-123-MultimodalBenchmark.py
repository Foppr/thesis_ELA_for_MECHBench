import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.a_constants = np.linspace(0.5, 2.0, dim)
        self.b_constants = np.linspace(1.0, 3.0, dim)
        self.c_constants = np.linspace(0.1, 1.5, dim)
        self seasonal_freq = np.linspace(0.5, 2.5, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Tent map components with parameter variation
        tent_terms = np.zeros(self.dim)
        for i in range(self.dim):
            a = self.a_constants[i]
            if x_norm[i] < 0.5:
                tent_terms[i] = a * x_norm[i]
            else:
                tent_terms[i] = a * (1 - x_norm[i])
        
        # Higher-order polynomial interactions
        poly_terms = np.zeros(self.dim)
        for i in range(self.dim):
            poly_terms[i] = (x_norm[i]**3 + x_norm[i]**5 + x_norm[i]**7) * self.b_constants[i]
        
        # Seasonal forcing with dynamic frequency modulation
        seasonal_terms = np.zeros(self.dim)
        for i in range(self.dim):
            freq = self.seasonal_freq[i]
            seasonal_terms[i] = np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]**2)
        
        # Cross-dimensional coupling with exponential weighting
        coupling_terms = np.zeros(self.dim)
        for i in range(self.dim):
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling += np.exp(-abs(i - j) / self.dim) * (x_norm[i] - x_norm[j])**3
            coupling_terms[i] = coupling
        
        # Dynamic conditioning with sigmoid modulation
        cond_terms = np.zeros(self.dim)
        for i in range(self.dim):
            cond_terms[i] = (1.0 / (1.0 + np.exp(-self.c_constants[i] * x_norm[i]))) * x_norm[i]**2
        
        # Combine all terms with non-separable structure
        term1 = np.sum(tent_terms**2)
        term2 = np.sum(poly_terms**2)
        term3 = np.sum(seasonal_terms**2)
        term4 = np.sum(coupling_terms**2)
        term5 = np.sum(cond_terms**2)
        
        # Add exponential coupling between all dimensions
        exp_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_coupling += np.exp(-((x_norm[i] - x_norm[j])**2) / (2.0 * (i + j + 1.0))) * (i + j + 1.0)
        
        # Add chaotic noise with dynamic amplitude
        noise_amp = 0.05 * np.mean(np.abs(x_norm))
        noise = noise_amp * np.random.random()
        
        # Add periodic modulation with increasing frequency
        periodic_mod = 0.0
        for i in range(self.dim):
            periodic_mod += np.sin(2 * np.pi * (i + 1) * x_norm[i]) * np.cos(3 * np.pi * (i + 1) * x_norm[i])
        
        return term1 + term2 + term3 + term4 + term5 + exp_coupling + noise + 0.1 * periodic_mod
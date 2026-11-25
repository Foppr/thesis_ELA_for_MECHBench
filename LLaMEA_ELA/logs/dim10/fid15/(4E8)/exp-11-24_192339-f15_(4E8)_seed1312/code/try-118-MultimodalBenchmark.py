import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map based radial components
        tent_basis = 0
        for i in range(self.dim):
            u = 0.5 * (1 + np.sin(i * np.pi / self.dim))
            tent_val = 1.0 - 2.0 * np.abs(x[i] - u)
            tent_basis += np.exp(-0.5 * (tent_val / (0.5 + 0.1 * np.abs(x[i])))**2)
        
        # Spectral sine-wave coupling with frequency modulation
        spectral_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_mod_i = 1.0 + 0.3 * np.sin(i * np.pi / (self.dim + 1))
                freq_mod_j = 1.0 + 0.3 * np.cos(j * np.pi / (self.dim + 1))
                spectral_coupling += np.sin(freq_mod_i * x[i] + freq_mod_j * x[j]) * np.cos(freq_mod_i * x[i] - freq_mod_j * x[j])
        
        # Probabilistic radial basis with dynamic variance
        prob_radial = 0
        for i in range(self.dim):
            var = 0.5 + 0.5 * np.sin(i * np.pi / self.dim)
            prob_radial += np.exp(-0.5 * ((x[i] - np.cos(i * np.pi / self.dim)) / var)**2)
        
        # Cross-dimensional hyperbolic tangent interactions
        tanh_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                tanh_interaction += np.tanh(x[i] * x[j]) * np.sin((i + j) * np.pi / self.dim)
        
        # Global scaling and shifting
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        shift = 0.2 * np.sum(np.abs(x))
        
        # Combine all components
        return scale_factor * (0.4 * tent_basis + 0.3 * spectral_coupling + 0.2 * prob_radial + 0.1 * tanh_interaction) + shift
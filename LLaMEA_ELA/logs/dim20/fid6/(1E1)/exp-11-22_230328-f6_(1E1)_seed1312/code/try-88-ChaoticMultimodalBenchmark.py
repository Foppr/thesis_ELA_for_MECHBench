import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential energy wells with chaotic positioning
        energy_well = 0.0
        for i in range(self.dim):
            base_freq = 2 ** (i % 4)
            energy_well += np.exp(-0.5 * (x_norm[i] - np.sin(base_freq * np.pi * x_norm[i]))**2) * \
                          np.cos(base_freq * np.pi * x_norm[i])
        
        # Cross-dimensional coupling with dynamic interaction weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.sin((i + j) * np.pi / self.dim)
                coupling_term += weight * np.exp(-0.25 * (x_norm[i] - x_norm[j])**2) * \
                                np.sin(2 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Time-varying harmonic components with chaotic modulation
        time_harmonic = 0.0
        for i in range(self.dim):
            freq_mod = 1 + 0.5 * np.sin(i * np.pi / self.dim)
            time_harmonic += np.sin(freq_mod * x_norm[i] + np.cos(i * np.pi / 4)) * \
                            np.cos(freq_mod * x_norm[i] + np.sin(i * np.pi / 3))
        
        # Multi-scale fractal-like structure with chaotic amplitude modulation
        fractal_like = 0.0
        for scale in [1, 2, 3, 4]:
            fractal_like += np.sum(np.sin(scale * x_norm + np.random.rand()) * 
                                 np.cos(scale * x_norm + np.random.rand()) * 
                                 np.exp(-0.1 * scale * np.abs(x_norm)))
        
        # Combined fitness with dynamic global scaling and chaotic noise
        combined = energy_well + coupling_term + time_harmonic + fractal_like
        
        # Add chaotic dimensionality bias and non-stationary noise
        dim_bias = 0.2 * self.dim * np.sum(np.sin(x_norm * np.pi))
        noise = 0.02 * np.random.rand() * (1 + np.sin(self.dim * np.pi / 4))
        
        return combined + dim_bias + noise
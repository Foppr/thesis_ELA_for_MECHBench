import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.r = 3.99
        self.epsilon = 0.2
        self.alpha = 0.85
        self.beta = 1.2
        
    def f(self, x):
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Generate fractional-order chaotic sequence
        chaotic_seq = np.zeros(self.dim)
        chaotic_seq[0] = x_norm[0]
        
        for i in range(1, self.dim):
            # Fractional logistic map with memory effect
            chaotic_seq[i] = self.r * chaotic_seq[i-1] * (1 - chaotic_seq[i-1]**4) + \
                            self.epsilon * (x_norm[i] - chaotic_seq[i-1]) + \
                            0.02 * np.sin(self.alpha * chaotic_seq[i-1]) * np.cos(self.beta * x_norm[i])
        
        # Apply spectral coupling between dimensions
        spectral_coupling = np.zeros(self.dim)
        for i in range(self.dim):
            spectral_coupling[i] = np.sum(chaotic_seq * np.sin(np.pi * i * np.arange(self.dim) / self.dim))
        
        # Add adaptive scaling based on dimension
        adaptive_scale = np.array([1.0 + 0.1 * np.sin(0.5 * i) for i in range(self.dim)])
        chaotic_seq_scaled = chaotic_seq * adaptive_scale
        
        # Create hybrid periodic-multimodal structure
        period_pattern = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        multimodal_pattern = np.sum(np.sin(3 * np.pi * x_norm)**2 + np.cos(2 * np.pi * x_norm)**2)
        
        # Combine all components with dynamic weights
        total_energy = (np.sum(chaotic_seq_scaled**2) + 
                       0.4 * period_pattern**2 + 
                       0.3 * multimodal_pattern**2 +
                       0.1 * np.sum((spectral_coupling[1:] - spectral_coupling[:-1])**2) +
                       0.05 * np.sum(np.abs(chaotic_seq_scaled[:-1] - chaotic_seq_scaled[1:])**3))
        
        # Add high-frequency noise and fractal-like perturbations
        noise = 0.02 * np.random.rand()
        fractal_perturbation = 0.01 * np.sum(np.sin(10 * x_norm) * np.cos(8 * x_norm))
        
        return total_energy + noise + fractal_perturbation
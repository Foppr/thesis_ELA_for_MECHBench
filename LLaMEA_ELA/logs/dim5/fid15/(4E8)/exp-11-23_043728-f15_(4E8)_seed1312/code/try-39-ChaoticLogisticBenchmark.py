import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced hyperchaotic parameters with fractional dynamics
        self.r1 = 3.99
        self.r2 = 3.85
        self.epsilon = 0.2
        self.fractional_order = 0.7
        self.ridge_strength = 2.5
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Initialize hyperchaotic sequence with fractional integration
        chaotic_seq = np.zeros(self.dim)
        chaotic_seq[0] = x_norm[0]
        
        # Generate coupled hyperchaotic sequence using modified logistic maps
        for i in range(1, self.dim):
            # Fractional-order chaotic dynamics with cross-dimensional coupling
            chaotic_seq[i] = self.r1 * chaotic_seq[i-1] * (1 - chaotic_seq[i-1]**2) + \
                            self.epsilon * (x_norm[i] - chaotic_seq[i-1]) + \
                            0.03 * np.sin(7 * chaotic_seq[i-1]) + \
                            0.02 * chaotic_seq[i-1]**4 + \
                            0.01 * np.cos(5 * x_norm[i-1])
        
        # Introduce fractional Brownian motion coupling
        fbm_coupling = np.zeros(self.dim)
        for i in range(1, self.dim):
            fbm_coupling[i] = 0.3 * (chaotic_seq[i-1] - chaotic_seq[i]) + \
                             0.1 * np.random.randn() * (i ** self.fractional_order)
        
        # Add adaptive ridge structures for enhanced multimodality
        ridge_terms = np.zeros(self.dim)
        for i in range(self.dim):
            ridge_terms[i] = self.ridge_strength * np.sin(2 * np.pi * x_norm[i]) * \
                           np.exp(-0.1 * (i - self.dim/2)**2)
        
        # Combine all components with enhanced nonlinearity
        total_energy = np.sum(chaotic_seq**2) + \
                      0.5 * np.sum(fbm_coupling**2) + \
                      0.3 * np.sum(ridge_terms**2) + \
                      0.1 * np.sum((chaotic_seq[1:] - chaotic_seq[:-1])**2) + \
                      0.05 * np.sum(np.sin(10 * chaotic_seq)**2)
        
        # Add complex periodic attractor with multiple frequencies
        period_pattern = np.sum(np.sin(8 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) * 
                               np.sin(3 * np.pi * x_norm))
        
        # Combine all terms and add adaptive noise
        final_energy = total_energy + 0.2 * period_pattern**2 + \
                      0.02 * np.random.rand() * (1 + np.abs(np.mean(x_norm)))
        
        return final_energy
import numpy as np

class ChaoticSpectralCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.chaos_params = np.random.uniform(0.1, 0.9, (dim, 3))
        self.quaternion_weights = np.random.uniform(-1.0, 1.0, (dim, 4))
        self.spectral_filters = np.random.uniform(0.5, 2.0, (dim, 5))
        self.fractal_depths = np.random.randint(2, 6, dim)
        self.coupling_strengths = np.random.uniform(0.1, 1.5, (dim, 3))
        self.modulation_freqs = np.random.uniform(0.5, 3.0, dim)
        self.oscillation_mixing = np.random.uniform(-2.0, 2.0, (dim, 4))
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic dynamical system component
        chaotic_term = 0.0
        for i in range(self.dim):
            a, b, c = self.chaos_params[i]
            chaotic_term += a * np.sin(b * x[i]) + c * np.cos(a * x[i])
            # Add recursive fractal-like structure
            for depth in range(self.fractal_depths[i]):
                chaotic_term += np.sin(x[i] * (depth + 1) * self.modulation_freqs[i]) * \
                               np.cos(x[i] * (depth + 1) * self.modulation_freqs[i] * 0.7)
        
        # Quaternion-based spectral filtering
        spectral_term = 0.0
        for i in range(self.dim):
            q_weights = self.quaternion_weights[i]
            for j in range(5):
                freq = self.spectral_filters[i, j]
                spectral_term += q_weights[0] * np.sin(x[i] * freq) + \
                                q_weights[1] * np.cos(x[i] * freq * 0.8) + \
                                q_weights[2] * np.sin(x[i] * freq * 1.2) * \
                                np.exp(-0.1 * x[i]**2) + \
                                q_weights[3] * np.cos(x[i] * freq * 0.6)
        
        # Adaptive coupling between dimensions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(min(3, self.dim)):
                if i != j:
                    strength = self.coupling_strengths[i, j % 3]
                    coupling_term += strength * np.sin(x[i] - x[j]) * \
                                   np.cos(x[i] + x[j])
        
        # Fractal-like recursive oscillation
        fractal_term = 0.0
        for i in range(self.dim):
            base_freq = self.modulation_freqs[i]
            for depth in range(1, self.fractal_depths[i]):
                fractal_term += np.sin(x[i] * base_freq * (depth**1.5)) * \
                               np.cos(x[i] * base_freq * (depth**0.8)) * \
                               np.exp(-0.05 * x[i]**2)
        
        # Mixed oscillatory components with adaptive weights
        mixed_term = 0.0
        for i in range(self.dim):
            mix_weights = self.oscillation_mixing[i]
            mixed_term += mix_weights[0] * np.sin(x[i] * mix_weights[1]) + \
                         mix_weights[2] * np.cos(x[i] * mix_weights[3]) * \
                         np.exp(-0.03 * x[i]**2)
        
        # Combine all components with dynamic scaling
        total = 0.35 * chaotic_term + 0.25 * spectral_term + 0.20 * coupling_term + \
                0.15 * fractal_term + 0.05 * mixed_term
        
        # Add global multi-scale modulation
        global_mod = np.prod(1.0 + 0.3 * np.sin(x * 0.4) * np.cos(x * 0.2) * 
                            np.sin(x * 0.6) * np.cos(x * 0.8))
        
        return total * global_mod + 0.1 * np.sum(x**2)
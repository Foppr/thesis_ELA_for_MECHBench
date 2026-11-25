import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic gradient components with time-delayed feedback
        chaotic_term = 0.0
        for i in range(self.dim):
            # Time-delayed feedback with chaotic dynamics
            delayed_idx = (i - 1) % self.dim
            chaotic_term += np.sin(x_norm[i] + 0.5 * np.sin(x_norm[delayed_idx])) * \
                           np.cos(2 * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2)
        
        # Dynamic frequency modulation with stochastic perturbations
        freq_mod_term = 0.0
        for i in range(self.dim):
            # Dynamic frequency that depends on other dimensions
            freq = 3 + 2 * np.sin(x_norm[(i+1) % self.dim])
            freq_mod_term += np.sin(freq * x_norm[i]) * \
                           np.cos(freq * x_norm[i] / 3) * \
                           (1 + 0.1 * np.random.randn())
        
        # Asymmetric harmonic potentials with polynomial coupling
        poly_harmonic_term = 0.0
        for i in range(self.dim):
            j = (i + 2) % self.dim
            poly_harmonic_term += (x_norm[i]**3 + x_norm[j]**4) * \
                                np.sin(5 * x_norm[i]) * np.cos(3 * x_norm[j])
        
        # Stochastic perturbation with multi-scale noise
        noise_term = 0.0
        scales = [0.1, 0.5, 1.0]
        for i in range(self.dim):
            for scale in scales:
                noise_term += np.sin(10 * x_norm[i] / scale) * \
                             np.cos(5 * x_norm[i] / scale) * \
                             np.random.normal(0, scale)
        
        # Cross-dimensional coupling with asymmetric weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    weight = 1.0 + 0.5 * np.sin(x_norm[i] * x_norm[j])
                    cross_term += weight * (x_norm[i]**2) * (x_norm[j]**3)
        
        # Saddle point enhancement with hyperbolic tangent
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += np.tanh(x_norm[i]) * np.exp(-0.5 * x_norm[i]**2) + \
                          0.3 * np.sinh(2 * x_norm[i])
        
        # Final combined function with dynamic weighting
        return 0.25 * chaotic_term + 0.2 * freq_mod_term + 0.15 * poly_harmonic_term + \
               0.2 * noise_term + 0.1 * cross_term + 0.1 * saddle_term
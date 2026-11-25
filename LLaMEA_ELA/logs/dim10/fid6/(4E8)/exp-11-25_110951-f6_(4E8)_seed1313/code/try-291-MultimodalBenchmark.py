import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic gradient flow with higher dimensional coupling
        chaos_flow = 0.0
        for i in range(self.dim):
            # Use a more complex chaotic map with multiple feedback loops
            coupling = np.sin(x_norm[i]) * np.cos(2 * x_norm[i]) + \
                      0.5 * np.sin(3 * x_norm[i]) * np.cos(4 * x_norm[i]) + \
                      0.2 * np.sin(5 * x_norm[i])**2
            chaos_flow += coupling * np.exp(-0.3 * x_norm[i]**2) * \
                         (1 + 0.4 * np.sin(15 * x_norm[i]) + 0.3 * np.cos(12 * x_norm[i]))
        
        # Modified logarithmic barrier potentials with asymmetric minima
        barrier_pot = 0.0
        for i in range(self.dim):
            # Create multiple local minima using modified logarithmic scaling
            barrier_pot += np.log(1 + 0.6 * (x_norm[i] - 1)**2) + \
                          0.8 * np.log(1 + 0.4 * (x_norm[i] + 1)**2) + \
                          0.5 * np.log(1 + 0.3 * x_norm[i]**2) + \
                          0.2 * np.log(1 + 0.1 * (x_norm[i] - 0.5)**2)
        
        # Enhanced spectral harmonic interference with multi-frequency modulation
        spectral_term = 0.0
        for i in range(self.dim):
            freq_mod = 1 + 0.6 * np.sin(x_norm[i]) + 0.3 * np.cos(2 * x_norm[i])
            spectral_term += (np.sin(freq_mod * 20 * x_norm[i]) * np.cos(freq_mod * 15 * x_norm[i]) +
                             0.4 * np.sin(freq_mod * 25 * x_norm[i])**2 * np.cos(freq_mod * 22 * x_norm[i]) + 
                             0.2 * np.sin(freq_mod * 18 * x_norm[i]) * np.cos(freq_mod * 16 * x_norm[i]))
        
        # Multi-scale sinusoidal modulations with asymmetric elliptic coupling
        multi_scale = 0.0
        scales = [2, 3, 5, 7, 11, 13, 17]
        for i in range(self.dim):
            for s in scales:
                multi_scale += np.sin(s * x_norm[i]) * np.cos(s * x_norm[i] / (s + 1)) * \
                              np.exp(-0.15 * (x_norm[i] - np.sin(x_norm[i]))**2) + \
                              0.3 * np.sin(2 * s * x_norm[i])**2 * np.cos(3 * s * x_norm[i])
        
        # Enhanced cross-dimensional interaction with exponential coupling
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            cross_term += np.exp(-0.4 * (x_norm[i] - x_norm[j])**2) * \
                         (np.sin(4 * x_norm[i]) * np.cos(4 * x_norm[j]) + 
                          0.6 * np.sin(7 * x_norm[i]) * np.cos(7 * x_norm[j]) + 
                          0.3 * np.sin(5 * x_norm[i]) * np.cos(5 * x_norm[j]))
        
        # Asymmetric gradient modulation with dynamic weighting
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += (np.tan(x_norm[i]) * np.exp(-x_norm[i]**2) + 
                        0.4 * np.sin(8 * x_norm[i]) * np.cos(10 * x_norm[i]) + 
                        0.2 * np.cos(9 * x_norm[i]) * np.sin(11 * x_norm[i]))
        
        # Enhanced fractal-like structure with self-similar modulation
        fractal_like = 0.0
        for i in range(self.dim):
            fractal_like += (np.sin(30 * x_norm[i]) * np.cos(25 * x_norm[i]) + 
                           0.7 * np.sin(20 * x_norm[i])**3 * np.cos(18 * x_norm[i]) + 
                           0.4 * np.sin(28 * x_norm[i]) * np.cos(26 * x_norm[i]))
        
        # Additional cross-dimensional interaction with higher-order terms
        high_order_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            high_order_term += np.exp(-0.2 * (x_norm[i] - x_norm[j])**2) * \
                              np.sin(3 * x_norm[k]) * np.cos(4 * x_norm[i]) + \
                              0.5 * np.exp(-0.1 * (x_norm[i] - x_norm[k])**2) * \
                              np.cos(5 * x_norm[j]) * np.sin(6 * x_norm[i])
        
        # Dynamic weighting scheme with chaotic perturbation
        return (0.35 * chaos_flow + 0.3 * barrier_pot + 0.25 * spectral_term + 
                0.15 * multi_scale + 0.1 * cross_term + 0.08 * grad_mod + 0.07 * fractal_like + 0.05 * high_order_term)
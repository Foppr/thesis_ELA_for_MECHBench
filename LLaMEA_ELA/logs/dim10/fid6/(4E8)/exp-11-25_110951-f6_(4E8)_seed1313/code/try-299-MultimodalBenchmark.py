import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic gradient flow components with enhanced coupling strengths
        chaos_flow = 0.0
        for i in range(self.dim):
            # Enhanced chaotic map with modified coupling
            coupling = np.sin(x_norm[i]) * np.cos(2 * x_norm[i]) + 0.7 * np.sin(3 * x_norm[i])
            chaos_flow += coupling * np.exp(-0.3 * x_norm[i]**2) * (1 + 0.4 * np.sin(12 * x_norm[i]))
        
        # Logarithmic barrier potentials with shifted attraction points
        barrier_pot = 0.0
        for i in range(self.dim):
            # Shifted local minima using logarithmic scaling
            barrier_pot += np.log(1 + 0.6 * (x_norm[i] - 1.2)**2) + \
                          0.8 * np.log(1 + 0.4 * (x_norm[i] + 1.3)**2) + \
                          0.5 * np.log(1 + 0.3 * x_norm[i]**2)
        
        # Spectral harmonic interference with frequency modulation
        spectral_term = 0.0
        for i in range(self.dim):
            freq_mod = 1 + 0.6 * np.sin(x_norm[i])
            spectral_term += (np.sin(freq_mod * 17 * x_norm[i]) * np.cos(freq_mod * 14 * x_norm[i]) +
                             0.4 * np.sin(freq_mod * 22 * x_norm[i])**2 * np.cos(freq_mod * 20 * x_norm[i]))
        
        # Multi-scale sinusoidal modulations with asymmetric elliptic coupling
        multi_scale = 0.0
        scales = [2, 3, 5, 7, 11]
        for i in range(self.dim):
            for s in scales:
                multi_scale += np.sin(s * x_norm[i]) * np.cos(s * x_norm[i] / (s + 1)) * \
                              np.exp(-0.15 * (x_norm[i] - np.sin(x_norm[i]))**2)
        
        # Cross-dimensional interaction with exponential coupling
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            cross_term += np.exp(-0.4 * (x_norm[i] - x_norm[j])**2) * \
                         (np.sin(3.5 * x_norm[i]) * np.cos(3.5 * x_norm[j]) + 
                          0.6 * np.sin(5.5 * x_norm[i]) * np.cos(5.5 * x_norm[j]))
        
        # Asymmetric gradient modulation with dynamic weighting
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += (np.tan(x_norm[i]) * np.exp(-0.8 * x_norm[i]**2) + 
                        0.4 * np.sin(7.5 * x_norm[i]) * np.cos(9.5 * x_norm[i]))
        
        # Fractal-like structure with self-similar modulation
        fractal_like = 0.0
        for i in range(self.dim):
            fractal_like += (np.sin(27 * x_norm[i]) * np.cos(24 * x_norm[i]) + 
                           0.7 * np.sin(20 * x_norm[i])**3 * np.cos(17 * x_norm[i]))
        
        # Dynamic weighting scheme with chaotic perturbation
        return (0.35 * chaos_flow + 0.28 * barrier_pot + 0.18 * spectral_term + 
                0.12 * multi_scale + 0.09 * cross_term + 0.06 * grad_mod + 0.02 * fractal_like)
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic gradient flow components with varying coupling strengths
        chaos_flow = 0.0
        for i in range(self.dim):
            # Use a chaotic map for dynamic coupling
            coupling = np.sin(x_norm[i]) * np.cos(2 * x_norm[i]) + 0.5 * np.sin(3 * x_norm[i])
            chaos_flow += coupling * np.exp(-0.5 * x_norm[i]**2) * (1 + 0.3 * np.sin(10 * x_norm[i]))
        
        # Logarithmic barrier potentials with multiple attraction points
        barrier_pot = 0.0
        for i in range(self.dim):
            # Create multiple local minima using logarithmic scaling
            barrier_pot += np.log(1 + 0.5 * (x_norm[i] - 1)**2) + \
                          0.7 * np.log(1 + 0.3 * (x_norm[i] + 1)**2) + \
                          0.4 * np.log(1 + 0.2 * x_norm[i]**2)
        
        # Spectral harmonic interference with frequency modulation
        spectral_term = 0.0
        for i in range(self.dim):
            freq_mod = 1 + 0.5 * np.sin(x_norm[i])
            spectral_term += (np.sin(freq_mod * 15 * x_norm[i]) * np.cos(freq_mod * 12 * x_norm[i]) +
                             0.3 * np.sin(freq_mod * 20 * x_norm[i])**2 * np.cos(freq_mod * 18 * x_norm[i]))
        
        # Multi-scale sinusoidal modulations with asymmetric elliptic coupling
        multi_scale = 0.0
        scales = [2, 3, 5, 7, 11]
        for i in range(self.dim):
            for s in scales:
                multi_scale += np.sin(s * x_norm[i]) * np.cos(s * x_norm[i] / (s + 1)) * \
                              np.exp(-0.1 * (x_norm[i] - np.sin(x_norm[i]))**2)
        
        # Cross-dimensional interaction with exponential coupling
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            cross_term += np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * \
                         (np.sin(3 * x_norm[i]) * np.cos(3 * x_norm[j]) + 
                          0.5 * np.sin(5 * x_norm[i]) * np.cos(5 * x_norm[j]))
        
        # Asymmetric gradient modulation with dynamic weighting
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += (np.tan(x_norm[i]) * np.exp(-x_norm[i]**2) + 
                        0.3 * np.sin(7 * x_norm[i]) * np.cos(9 * x_norm[i]))
        
        # Fractal-like structure with self-similar modulation
        fractal_like = 0.0
        for i in range(self.dim):
            fractal_like += (np.sin(25 * x_norm[i]) * np.cos(22 * x_norm[i]) + 
                           0.6 * np.sin(18 * x_norm[i])**3 * np.cos(15 * x_norm[i]))
        
        # Dynamic weighting scheme with chaotic perturbation
        return (0.3 * chaos_flow + 0.25 * barrier_pot + 0.2 * spectral_term + 
                0.1 * multi_scale + 0.08 * cross_term + 0.07 * grad_mod + 0.05 * fractal_like)
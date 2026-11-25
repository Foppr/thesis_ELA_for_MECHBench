import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos interactions with gradient-based saddle points
        poly_term = 0
        for i in range(self.dim):
            poly_term += (x_norm[i]**6 - 2 * x_norm[i]**4 + x_norm[i]**2) * (1 + 0.3 * np.sin(10 * x_norm[i]))
        
        # Multi-scale harmonic modulations with chaotic phase couplings
        harm_term = 0
        scales = [1.0, 2.5, 4.0, 6.5]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            harm_term += np.sin(x_norm[i] * scale * np.pi) * np.cos(x_norm[i] * scale * np.pi / 2.0) * \
                        (1 + 0.2 * np.tanh(x_norm[i] * 3.0))
        
        # Chaotic gradient interactions with cross-dimensional coupling
        grad_term = 0
        for i in range(self.dim):
            grad_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    coupling = np.sin(x_norm[i] * x_norm[j] * 5.0) + 1.0
                    grad_sum += coupling * np.exp(-distance * 2.0) * (x_norm[i] - x_norm[j])
            grad_term += grad_sum * np.tanh(x_norm[i]) ** 2
        
        # Saddle-point attraction with hyperbolic tangent conditioning
        saddle_term = 0
        for i in range(self.dim):
            saddle_term += (np.tanh(x_norm[i]) ** 3) * (x_norm[i]**4 - 2 * x_norm[i]**2 + 1)
        
        # Multi-scale fractal-like self-similarity with dynamic weights
        fractal_term = 0
        weights = [0.5, 0.8, 0.3, 0.9]
        for i in range(self.dim):
            weight_idx = i % len(weights)
            weight = weights[weight_idx]
            fractal_term += weight * np.sin(x_norm[i] * 12.0) * np.cos(x_norm[i] * 8.0) * \
                           (1 + 0.4 * np.sin(x_norm[i] * 15.0))
        
        # Global chaotic modulation with adaptive scaling
        chaos_mod = 1 + 0.3 * np.sin(np.sum(x_norm**2) * 3.0)
        
        # Combine all terms with dynamic weighting
        result = 0.25 * poly_term + 0.20 * harm_term + 0.25 * grad_term + \
                 0.15 * saddle_term + 0.15 * fractal_term
        
        return result * chaos_mod * (1 + 0.1 * np.sum(np.abs(x_norm)))
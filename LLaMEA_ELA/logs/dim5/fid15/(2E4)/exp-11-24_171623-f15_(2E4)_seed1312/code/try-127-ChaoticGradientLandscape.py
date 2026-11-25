import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Modified polynomial chaos interactions with altered exponents and enhanced sine modulation
        poly_term = 0
        for i in range(self.dim):
            poly_term += (x_norm[i]**7 - 1.8 * x_norm[i]**5 + 0.8 * x_norm[i]**3) * (1 + 0.4 * np.sin(12 * x_norm[i]))
        
        # Adjusted multi-scale harmonic modulations with different frequencies and coupling
        harm_term = 0
        scales = [1.2, 2.8, 4.2, 6.8]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            harm_term += np.sin(x_norm[i] * scale * np.pi) * np.cos(x_norm[i] * scale * np.pi / 2.5) * \
                        (1 + 0.25 * np.tanh(x_norm[i] * 3.5))
        
        # Enhanced chaotic gradient interactions with stronger cross-dimensional coupling
        grad_term = 0
        for i in range(self.dim):
            grad_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    coupling = np.sin(x_norm[i] * x_norm[j] * 6.0) + 1.2
                    grad_sum += coupling * np.exp(-distance * 2.5) * (x_norm[i] - x_norm[j])
            grad_term += grad_sum * np.tanh(x_norm[i]) ** 2
        
        # Saddle-point attraction with modified hyperbolic tangent conditioning
        saddle_term = 0
        for i in range(self.dim):
            saddle_term += (np.tanh(x_norm[i]) ** 4) * (x_norm[i]**5 - 2.2 * x_norm[i]**3 + 1.1 * x_norm[i])
        
        # Modified fractal-like self-similarity with adjusted weights
        fractal_term = 0
        weights = [0.6, 0.7, 0.4, 0.8]
        for i in range(self.dim):
            weight_idx = i % len(weights)
            weight = weights[weight_idx]
            fractal_term += weight * np.sin(x_norm[i] * 13.0) * np.cos(x_norm[i] * 9.0) * \
                           (1 + 0.35 * np.sin(x_norm[i] * 16.0))
        
        # Global chaotic modulation with modified scaling
        chaos_mod = 1 + 0.25 * np.sin(np.sum(x_norm**2) * 4.0)
        
        # Combine all terms with adjusted dynamic weighting
        result = 0.30 * poly_term + 0.18 * harm_term + 0.28 * grad_term + \
                 0.12 * saddle_term + 0.12 * fractal_term
        
        return result * chaos_mod * (1 + 0.12 * np.sum(np.abs(x_norm)))
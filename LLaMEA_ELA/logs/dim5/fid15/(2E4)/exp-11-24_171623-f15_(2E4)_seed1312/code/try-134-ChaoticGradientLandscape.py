import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial chaos interactions with modified exponents and increased nonlinearity
        poly_term = 0
        for i in range(self.dim):
            poly_term += (x_norm[i]**8 - 3.0 * x_norm[i]**6 + 2.0 * x_norm[i]**4 - 0.5 * x_norm[i]**2) * \
                        (1 + 0.5 * np.sin(15 * x_norm[i]) + 0.3 * np.cos(7 * x_norm[i]))
        
        # Multi-scale harmonic modulations with increased frequency components and altered amplitudes
        harm_term = 0
        scales = [1.5, 3.2, 5.1, 7.9]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            harm_term += np.sin(x_norm[i] * scale * np.pi) * np.cos(x_norm[i] * scale * np.pi / 2.1) * \
                        (1 + 0.3 * np.tanh(x_norm[i] * 4.0))
        
        # Chaotic gradient interactions with enhanced cross-dimensional coupling and modified coupling function
        grad_term = 0
        for i in range(self.dim):
            grad_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    coupling = np.sin(x_norm[i] * x_norm[j] * 7.0) + 1.5
                    grad_sum += coupling * np.exp(-distance * 3.0) * (x_norm[i] - x_norm[j])
            grad_term += grad_sum * np.tanh(x_norm[i]) ** 2
        
        # Saddle-point attraction with modified hyperbolic tangent conditioning and additional cubic terms
        saddle_term = 0
        for i in range(self.dim):
            saddle_term += (np.tanh(x_norm[i]) ** 5) * (x_norm[i]**6 - 2.5 * x_norm[i]**4 + 1.5 * x_norm[i]**2 - 0.3)
        
        # Multi-scale fractal-like self-similarity with adjusted weights and additional sine components
        fractal_term = 0
        weights = [0.7, 0.6, 0.5, 0.9]
        for i in range(self.dim):
            weight_idx = i % len(weights)
            weight = weights[weight_idx]
            fractal_term += weight * np.sin(x_norm[i] * 14.0) * np.cos(x_norm[i] * 10.0) * \
                           (1 + 0.4 * np.sin(x_norm[i] * 18.0) + 0.2 * np.cos(x_norm[i] * 12.0))
        
        # Global chaotic modulation with adaptive scaling and additional harmonic components
        chaos_mod = 1 + 0.4 * np.sin(np.sum(x_norm**2) * 4.0) + 0.15 * np.cos(np.sum(x_norm**2) * 2.5)
        
        # Combine all terms with modified dynamic weighting
        result = 0.32 * poly_term + 0.20 * harm_term + 0.25 * grad_term + \
                 0.15 * saddle_term + 0.08 * fractal_term
        
        return result * chaos_mod * (1 + 0.15 * np.sum(np.abs(x_norm)))
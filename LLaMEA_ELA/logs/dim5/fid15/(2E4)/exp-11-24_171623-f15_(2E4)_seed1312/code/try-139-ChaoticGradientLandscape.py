import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial chaos with nested fractal components and increased nonlinearity
        poly_term = 0
        for i in range(self.dim):
            base_poly = (x_norm[i]**9 - 3.5 * x_norm[i]**7 + 2.8 * x_norm[i]**5 - 1.2 * x_norm[i]**3 + 0.4 * x_norm[i])
            fractal_component = np.sin(x_norm[i] * 20.0) * np.cos(x_norm[i] * 15.0) * (1 + 0.3 * np.sin(x_norm[i] * 30.0))
            poly_term += base_poly * (1 + 0.4 * fractal_component)
        
        # Multi-scale harmonic modulations with dynamic frequency and amplitude
        harm_term = 0
        scales = [2.0, 4.5, 6.8, 9.2]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            freq_mod = 1 + 0.3 * np.sin(x_norm[i] * 7.0)
            harm_term += np.sin(x_norm[i] * scale * np.pi * freq_mod) * np.cos(x_norm[i] * scale * np.pi / 2.5) * \
                        (1 + 0.25 * np.tanh(x_norm[i] * 5.0))
        
        # Enhanced chaotic gradient interactions with nested coupling and dynamic weights
        grad_term = 0
        for i in range(self.dim):
            grad_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    coupling = np.sin(x_norm[i] * x_norm[j] * 9.0) + 1.8
                    weight = 1.0 + 0.2 * np.cos(x_norm[i] * 3.0)
                    grad_sum += coupling * np.exp(-distance * 4.0) * (x_norm[i] - x_norm[j]) * weight
            grad_term += grad_sum * np.tanh(x_norm[i]) ** 3
        
        # Saddle-point attraction with nested hyperbolic tangent and cubic components
        saddle_term = 0
        for i in range(self.dim):
            saddle_term += (np.tanh(x_norm[i]) ** 6) * (x_norm[i]**7 - 3.0 * x_norm[i]**5 + 2.0 * x_norm[i]**3 - 0.5 * x_norm[i])
        
        # Multi-scale fractal-like self-similarity with dynamic weights and nested sine components
        fractal_term = 0
        weights = [0.8, 0.7, 0.6, 0.9, 0.5]
        for i in range(self.dim):
            weight_idx = i % len(weights)
            weight = weights[weight_idx]
            fractal_term += weight * np.sin(x_norm[i] * 18.0) * np.cos(x_norm[i] * 14.0) * \
                           (1 + 0.35 * np.sin(x_norm[i] * 25.0) + 0.25 * np.cos(x_norm[i] * 20.0))
        
        # Global chaotic modulation with nested fractal scaling and additional harmonic components
        chaos_mod = 1 + 0.5 * np.sin(np.sum(x_norm**2) * 5.0) + 0.2 * np.cos(np.sum(x_norm**2) * 3.0) + \
                   0.1 * np.sin(np.sum(x_norm**2) * 7.0)
        
        # Nested basin hopping with dynamic scaling and multi-modal attraction
        basin_term = 0
        for i in range(self.dim):
            basin_term += (x_norm[i]**4 - 2.0 * x_norm[i]**2 + 0.5) * \
                         (1 + 0.3 * np.sin(x_norm[i] * 12.0) + 0.2 * np.cos(x_norm[i] * 8.0))
        
        # Combine all terms with dynamic weighting and global modulation
        result = 0.25 * poly_term + 0.22 * harm_term + 0.28 * grad_term + \
                 0.12 * saddle_term + 0.08 * fractal_term + 0.05 * basin_term
        
        return result * chaos_mod * (1 + 0.2 * np.sum(np.abs(x_norm)) + 0.1 * np.sum(x_norm**2))
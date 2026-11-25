import numpy as np

class FractalRBFMixtureLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced RBF components with nested sine modulations
        rbf_sum = 0
        centers = np.linspace(-1, 1, min(25, self.dim * 3))
        for i in range(len(centers)):
            if i < self.dim:
                distance = np.sum((x_norm - centers[i])**2)
                rbf_sum += np.exp(-3 * distance) * np.sin(5 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i])
        
        # Nested sine-wave modulation with chaotic coupling
        sine_mod = 0
        for i in range(self.dim):
            freq1 = 3 + np.sin(x_norm[i] * np.pi / 3)
            freq2 = 2 + np.cos(x_norm[i] * np.pi / 2)
            sine_mod += np.sin(freq1 * x_norm[i]) * np.cos(freq2 * x_norm[i])
        
        # Fractal-like coupling with recursive interaction terms and adaptive weights
        fractal_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                weight = 1.0 / (1.0 + np.exp(5 * (dist - 0.5)))
                fractal_term += weight * (np.sin(15 * dist) / (dist + 0.05)) * np.exp(-dist**3)
        
        # Hyperbolic tangent and polynomial mixing with enhanced curvature
        mix_term = 0
        for i in range(self.dim):
            mix_term += np.tanh(x_norm[i]**4) * (x_norm[i]**8 - 2*x_norm[i]**6 + x_norm[i]**4)
        
        # Cross-dimensional chaotic coupling with dynamic weights and additional nonlinearity
        chaos_term = 0
        for i in range(self.dim):
            weight = np.exp(-i / (self.dim + 1))
            for j in range(i+1, self.dim):
                if j < self.dim:
                    interaction = np.sin(x_norm[i] * x_norm[j]) * np.cos(x_norm[i] + x_norm[j])
                    chaos_term += weight * interaction * (1 + 0.5 * np.sin(3 * x_norm[i]))
        
        # Combine all terms with improved scaling
        result = 0.3 * rbf_sum + 0.25 * sine_mod + 0.2 * fractal_term + \
                 0.15 * mix_term + 0.1 * chaos_term
        
        # Enhanced conditioning and noise for better difficulty balance
        conditioning = 0.03 * np.sum(x_norm**10)
        
        return result + conditioning
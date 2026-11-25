import numpy as np

class FractalRBFMixtureLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial Basis Function components with fractal scaling
        rbf_sum = 0
        centers = np.linspace(-1, 1, min(20, self.dim * 2))
        for i in range(len(centers)):
            if i < self.dim:
                distance = np.sum((x_norm - centers[i])**2)
                rbf_sum += np.exp(-4 * distance) * np.sin(4 * np.pi * x_norm[i])
        
        # Sine-wave modulation with chaotic frequency coupling
        sine_mod = 0
        for i in range(self.dim):
            freq = 3 + np.sin(x_norm[i] * np.pi / 3)
            sine_mod += np.sin(freq * x_norm[i]) * np.cos(2.0 * x_norm[i])
        
        # Fractal-like coupling with recursive interaction terms
        fractal_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                fractal_term += (np.sin(12 * dist) / (dist + 0.15)) * np.exp(-dist**2)
        
        # Hyperbolic tangent and polynomial mixing for complex curvature
        mix_term = 0
        for i in range(self.dim):
            mix_term += np.tanh(x_norm[i]**3) * (x_norm[i]**6 - 2*x_norm[i]**4 + x_norm[i]**2)
        
        # Cross-dimensional chaotic coupling with exponential weights
        chaos_term = 0
        for i in range(self.dim):
            weight = np.exp(-i / (self.dim * 1.5))
            for j in range(i+1, self.dim):
                if j < self.dim:
                    chaos_term += weight * np.sin(x_norm[i] * x_norm[j]) * np.cos(x_norm[i] + x_norm[j])
        
        # Combine all terms with dynamic scaling
        result = 0.3 * rbf_sum + 0.25 * sine_mod + 0.18 * fractal_term + \
                 0.2 * mix_term + 0.07 * chaos_term
        
        # Add conditioning and noise to increase difficulty
        conditioning = 0.03 * np.sum(x_norm**9)
        
        # Introduce additional complexity with fractional powers and cross-terms
        frac_term = 0
        for i in range(self.dim):
            frac_term += np.power(np.abs(x_norm[i]), 1.7) * np.sin(4 * x_norm[i])
        
        # Add a global shaping term to improve conditioning
        global_shape = 0.06 * np.sum(np.sin(0.6 * x_norm)**2)
        
        return result + conditioning + frac_term + global_shape
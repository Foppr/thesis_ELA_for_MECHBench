import numpy as np

class FractalRBFMixtureLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced Radial Basis Function components with fractal scaling and chaotic centers
        rbf_sum = 0
        centers = np.sin(np.linspace(0, 4*np.pi, min(25, self.dim * 3))) * 0.8
        for i in range(len(centers)):
            if i < self.dim:
                distance = np.sum((x_norm - centers[i])**2)
                rbf_sum += np.exp(-8 * distance) * np.sin(5 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i])
        
        # Enhanced sine-wave modulation with chaotic frequency coupling and phase shifts
        sine_mod = 0
        for i in range(self.dim):
            freq = 3 + 2 * np.sin(x_norm[i] * np.pi / 3) + 0.5 * np.cos(x_norm[i] * np.pi)
            phase = np.sin(x_norm[i] * 2 * np.pi) * 0.3
            sine_mod += np.sin(freq * x_norm[i] + phase) * np.cos(2 * x_norm[i]) * np.tanh(x_norm[i])
        
        # Fractal-like coupling with recursive interaction terms and adaptive scaling
        fractal_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.abs(x_norm[i] - x_norm[j])
                scale_factor = 1 + 0.5 * np.sin(5 * dist)
                fractal_term += (np.sin(15 * dist) / (dist**2 + 0.05)) * np.exp(-dist**3) * scale_factor
        
        # Hyperbolic tangent and polynomial mixing with higher-order terms for complex curvature
        mix_term = 0
        for i in range(self.dim):
            mix_term += np.tanh(x_norm[i]**4) * (x_norm[i]**8 - 3*x_norm[i]**6 + 3*x_norm[i]**4 - x_norm[i]**2)
        
        # Enhanced cross-dimensional chaotic coupling with exponential weights and adaptive coupling
        chaos_term = 0
        for i in range(self.dim):
            weight = np.exp(-i / (self.dim * 0.7))
            for j in range(i+1, min(i+4, self.dim)):
                if j < self.dim:
                    coupling = np.sin(x_norm[i] * x_norm[j]) * np.cos(x_norm[i] + x_norm[j])
                    adaptive_factor = 1 + 0.3 * np.sin(x_norm[i] * x_norm[j] * 2)
                    chaos_term += weight * coupling * adaptive_factor
        
        # Additional chaotic interaction terms with different frequency patterns
        chaos_extra = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if j < self.dim:
                    dist = np.abs(x_norm[i] - x_norm[j])
                    chaos_extra += np.sin(7 * dist) * np.cos(3 * dist) * np.exp(-dist**2)
        
        # Combine all terms with dynamic scaling and increased complexity
        result = 0.3 * rbf_sum + 0.35 * sine_mod + 0.18 * fractal_term + \
                 0.15 * mix_term + 0.05 * chaos_term + 0.02 * chaos_extra
        
        # Add strong conditioning and noise to increase difficulty
        conditioning = 0.05 * np.sum(x_norm**10) + 0.03 * np.sum(np.sin(10 * x_norm)**2)
        
        return result + conditioning
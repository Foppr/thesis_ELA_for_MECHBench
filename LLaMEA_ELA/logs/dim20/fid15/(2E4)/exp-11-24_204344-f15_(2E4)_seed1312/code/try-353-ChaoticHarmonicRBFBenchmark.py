import numpy as np

class ChaoticHarmonicRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for stability
        self.chaotic_params = np.random.rand(dim) * 2.0 - 1.0
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Chaotic dynamical system component with time-varying parameters
        chaotic_term = 0.0
        for i in range(self.dim):
            param = self.chaotic_params[i]
            chaotic_val = np.sin(x[i] * param + np.cos(x[i] * 0.5)) * np.exp(-np.abs(x[i]) * 0.1)
            chaotic_term += chaotic_val ** 2
        
        # Radial basis function component with dynamic centers and widths
        rbf_term = 0.0
        for i in range(self.dim):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            rbf_val = np.exp(-np.sum((x - center) ** 2) / (2 * width ** 2))
            rbf_term += rbf_val
        
        # Gradient-enhanced harmonic oscillations with phase modulation
        harmonic_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + np.sin(i * 0.7) * 2.0
            phase = np.cos(i * 0.5) * np.pi
            amp = 1.0 + np.cos(i * 0.3) * 0.5
            harmonic_val = amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] * 0.8 + phase)
            harmonic_term += harmonic_val ** 2
        
        # Fractal-like recursive structure with self-similar patterns
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 0.5 + np.sin(i * 0.4) * 1.5
            fractal_val = np.sin(x[i] * scale) * np.cos(x[i] * scale * 0.7)
            fractal_term += fractal_val ** 3
        
        # Nonlinear interaction weights with altered coupling strengths
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.sin(i * j * 0.2) * 0.5 + 0.7
                interaction = weight * (x[i] ** 2 + x[j] ** 2) * np.sin(x[i] - x[j])
                interaction_term += interaction ** 2
        
        # Multi-scale conditioning with dimension-dependent modulation
        cond_term = 0.0
        for i in range(self.dim):
            condition = 1.0 + 0.3 * np.sin(i * 0.8) * np.cos(i * 0.6)
            cond_term += condition * x[i] ** 3
        
        # Final combined fitness function with adaptive scaling
        total = 0.25 * chaotic_term + 0.20 * rbf_term + 0.20 * harmonic_term + 0.15 * fractal_term + 0.12 * interaction_term + 0.10 * cond_term
        
        # Global normalization with chaotic modulation
        global_norm = 1.0 + 0.2 * np.sin(self.dim * 0.6) * np.cos(self.dim * 0.4)
        
        return total * global_norm
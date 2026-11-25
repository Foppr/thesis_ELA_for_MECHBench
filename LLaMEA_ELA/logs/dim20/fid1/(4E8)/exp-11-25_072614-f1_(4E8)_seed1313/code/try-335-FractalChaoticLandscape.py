import numpy as np

class FractalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Fractal dimension scaling factors
        self.fractal_dims = np.array([0.5 + 0.5 * np.sin(0.3 * np.pi * i) for i in range(dim)])
        # Multi-resolution frequency components
        self.freqs = np.array([1.0 + 0.5 * np.cos(0.4 * np.pi * i) for i in range(dim)])
        # Adaptive correlation structures
        self.correlations = np.array([0.3 + 0.4 * np.sin(0.2 * np.pi * i) for i in range(dim)])
        # Chaotic amplitude modulation
        self.amplitudes = np.array([1.0 + 0.3 * np.sin(0.5 * np.pi * i + 0.1 * dim) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal self-similar pattern with multi-scale components
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-resolution frequency modulation
            freq = self.freqs[i] * (1.0 + 0.2 * np.sin(0.3 * np.pi * i + 0.1 * np.sum(x)))
            # Self-similar chaotic pattern
            fractal_component = np.sin(freq * x[i]) * np.cos(freq * x[i]**2) * np.exp(-0.1 * x[i]**2)
            # Fractal dimension scaling
            dim_scale = self.fractal_dims[i] * (1.0 + 0.1 * np.sin(0.2 * np.pi * i + 0.05 * np.sum(x)))
            fractal_term += fractal_component * dim_scale
            
        fractal_term /= self.dim
        
        # Adaptive correlation structure
        correlation_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive correlation strength
                corr_strength = self.correlations[i] * (1.0 + 0.3 * np.cos(0.4 * np.pi * (i-j) + 0.2 * np.sum(x)))
                # Correlated chaotic interaction
                corr_interaction = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                correlation_term += corr_strength * corr_interaction
                
        correlation_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-scale chaotic modulation with amplitude variation
        chaos_term = 0.0
        for i in range(self.dim):
            # Chaotic amplitude modulation
            amp_mod = self.amplitudes[i] * (1.0 + 0.2 * np.sin(0.6 * np.pi * i + 0.15 * np.sum(x)))
            # Multi-scale chaotic component
            chaos_component = amp_mod * np.sin(2.0 * x[i] + 0.3 * np.sum(x)) * np.cos(1.5 * x[i]**2) * np.exp(-0.08 * x[i]**2)
            chaos_term += chaos_component
            
        chaos_term /= self.dim
        
        # Variable resolution landscape with fractal scaling
        resolution_term = 0.0
        for i in range(self.dim):
            # Variable resolution pattern
            res_pattern = np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.12 * x[i]**2)
            # Fractal scaling factor
            scale_factor = 1.0 + 0.5 * np.sin(0.4 * np.pi * i + 0.1 * np.sum(x))
            resolution_term += res_pattern * scale_factor
            
        resolution_term /= self.dim
        
        # Combined multi-scale chaotic landscape
        result = fractal_term + correlation_term + chaos_term + resolution_term
        
        return result
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base polynomial term with varying exponents
        poly_base = np.sum(x_norm**4)
        
        # Fractional Brownian motion inspired component with varying Hurst parameters
        fbm = 0.0
        for i in range(self.dim):
            hurst = 0.3 + 0.4 * np.sin(i * 0.5)
            fbm += np.sin(20 * np.pi * x_norm[i]) * np.cos(15 * np.pi * x_norm[i]) * np.exp(-hurst * np.abs(x_norm[i]))
        
        # Multi-scale trigonometric interaction with adaptive frequencies
        trig_interaction = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 2)
            amp = 1.5 + 0.8 * np.cos(i * 0.3)
            trig_interaction += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
            
        # Cross-dimensional exponential interactions with variable decay rates
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-dimensionality
                decay = 0.1 + 0.3 * np.sin(i * 0.4 + j * 0.3)
                cross_exp += np.exp(-decay * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(25 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Adaptive penalty term with dimensionality scaling
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.5 * (x_norm[i]**8 - 4 * x_norm[i]**6 + 6 * x_norm[i]**4 - 4 * x_norm[i]**2 + 1) * (1.0 + 0.2 * np.sin(i * 0.7))
        
        # Chaotic sine-cosine component with dynamic phase modulation
        chaotic = 0.0
        for i in range(self.dim):
            phase = np.sin(i * 0.8) * np.cos(i * 0.6)
            chaotic += 0.4 * np.sin(40 * np.pi * x_norm[i] + phase) * np.cos(35 * np.pi * x_norm[i] + phase) * np.exp(-0.2 * x_norm[i]**2)
        
        # Multi-modal sinusoidal with varying amplitudes and frequencies
        multimodal = 0.0
        for i in range(self.dim):
            freq = 3 + 2 * np.sin(i * 0.5)
            amp = 2.0 + 1.5 * np.cos(i * 0.3)
            multimodal += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Radial component with varying influence
        radial = 0.0
        dist = np.sqrt(np.sum(x_norm**2))
        radial = 0.3 * np.sin(30 * np.pi * dist) * np.exp(-0.5 * dist**2)
        
        # Dimensionality-dependent noise term
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(50 * np.pi * x_norm[i]) * np.cos(45 * np.pi * x_norm[i])
        
        # Asymmetric penalty for better conditioning
        asym_penalty = 0.0
        for i in range(self.dim):
            asym_penalty += 0.2 * np.abs(x_norm[i])**3 * np.sin(10 * np.pi * x_norm[i])
        
        # Combine all components with adaptive weights
        total = (0.8 * poly_base + 
                0.6 * fbm + 
                0.7 * trig_interaction + 
                0.5 * cross_exp + 
                0.9 * penalty + 
                0.4 * chaotic + 
                0.6 * multimodal + 
                0.3 * radial + 
                0.2 * noise + 
                0.5 * asym_penalty)
        
        return total
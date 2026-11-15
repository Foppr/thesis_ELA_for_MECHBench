import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_norm**2)
        
        # Sinusoidal modulations with varying frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 2)
            amp = 1.5 + 0.8 * np.sin(i * 0.5)
            sinusoidal += amp * np.sin(freq * np.pi * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Exponential decay cross-dimensional interactions
        cross_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                cross_decay += 0.4 * np.exp(-2.0 * dist) * np.sin(25 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Multi-scale fractal-like structure using recursive sine components
        fractal = 0.0
        for i in range(self.dim):
            scale = 1.0
            for k in range(3):
                scale *= 0.5
                fractal += 0.3 * np.sin(2**(k+1) * np.pi * x_norm[i]) * scale
        
        # Chaotic component with logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.25 * np.sin(60 * np.pi * x_norm[i]) * np.cos(50 * np.pi * x_norm[i]) * np.exp(-0.2 * x_norm[i]**2)
        
        # High-frequency oscillatory penalty with variable phase
        high_freq = 0.0
        for i in range(self.dim):
            phase = 0.3 * np.sin(i * 0.7)
            high_freq += 0.35 * np.sin(70 * np.pi * x_norm[i] + phase) * np.cos(60 * np.pi * x_norm[i] + phase)
        
        # Radial basis function with multi-peak structure
        radial = 0.0
        for i in range(self.dim):
            radial += 0.2 * np.exp(-1.5 * x_norm[i]**2) * np.sin(40 * np.pi * x_norm[i])
        
        # Cross-dimensional cubic interaction terms
        cubic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_interaction += 0.2 * (x_norm[i]**3 + x_norm[j]**3) * np.sin(15 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Asymmetric penalty with exponential growth
        asymmetric = 0.0
        for i in range(self.dim):
            asymmetric += 0.15 * np.exp(2.0 * np.abs(x_norm[i])) * np.sin(10 * np.pi * x_norm[i])
        
        # Multi-modal sinusoidal with varying amplitudes and frequencies
        multimodal = 0.0
        for i in range(self.dim):
            freq = 3**(i % 4 + 1)
            amp = 2.0 + 1.0 * np.cos(i * 0.6)
            multimodal += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(20 * np.pi * x_norm[i])
        
        # Central repulsion with radial dependency
        center_repulsion = 0.0
        dist_from_origin = np.sqrt(np.sum(x_norm**2))
        center_repulsion = 2.0 * np.exp(-0.5 * dist_from_origin**2) * np.sin(12 * dist_from_origin)
        
        # Combined fitness value
        return quadratic + sinusoidal + cross_decay + fractal + chaotic + high_freq + radial + cubic_interaction + asymmetric + multimodal + center_repulsion
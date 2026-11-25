import numpy as np

class WaveBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Wave interaction component with multiple frequency harmonics
        wave = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.5 * x_scaled[i])
            amp = 1.0 + 0.5 * np.cos(x_scaled[i] * 1.3)
            wave += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Exponential barrier regions with adaptive width and height
        barriers = 0.0
        for i in range(self.dim):
            # Multiple exponential barriers centered at different locations
            barrier_centers = [0.2, -0.3, 0.6, -0.8]
            for center in barrier_centers:
                width = 0.3 + 0.2 * np.sin(i * 0.4)
                height = 1.5 + 0.8 * np.cos(i * 0.6)
                barriers += height * np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Adaptive curvature component with dimensionally dependent exponents
        curvature = 0.0
        for i in range(self.dim):
            # Varying exponents based on dimension index for adaptive difficulty
            exponent = 2.0 + 0.5 * np.sin(i * 0.3)
            curvature += (x_scaled[i]**2)**exponent
        
        # Cross-dimensional interaction with periodic coupling terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling = np.sin(0.3 * x_scaled[i]) * np.cos(0.4 * x_scaled[j])
                distance = (x_scaled[i] - x_scaled[j])**2
                cross_interaction += coupling * np.exp(-distance)
        
        # Multi-scale periodic modulation with varying amplitudes and frequencies
        multi_scale = 0.0
        scales = [1, 2, 3, 4, 5]
        for scale in scales:
            for i in range(self.dim):
                amp = 0.8 + 0.3 * np.sin(scale * i * 0.2)
                freq = 1.0 + 0.7 * np.cos(scale * i * 0.3)
                multi_scale += amp * np.sin(freq * scale * x_scaled[i])
        
        # Asymmetric exponential decay with adaptive parameters
        asym_decay = 0.0
        for i in range(self.dim):
            # Different decay rates for positive and negative regions
            pos_decay = 1.2 + 0.3 * np.sin(i * 0.5)
            neg_decay = 1.0 + 0.4 * np.cos(i * 0.4)
            asym_decay += (x_scaled[i] > 0) * x_scaled[i]**pos_decay + (x_scaled[i] <= 0) * x_scaled[i]**neg_decay
        
        # Combined function with carefully balanced weights
        return 1.5 * wave + 2.0 * barriers + 1.3 * curvature + 0.8 * cross_interaction + 1.2 * multi_scale + 0.9 * asym_decay
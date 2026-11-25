import numpy as np

class WaveBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Wave interference component with multiple frequencies and amplitudes
        wave = 0.0
        for i in range(self.dim):
            freq1 = 2.0 + 1.5 * np.sin(x_scaled[i] * 0.5)
            freq2 = 3.0 + 2.0 * np.cos(x_scaled[i] * 0.7)
            amp1 = 1.0 + 0.5 * np.cos(x_scaled[i] * 1.2)
            amp2 = 0.8 + 0.4 * np.sin(x_scaled[i] * 1.5)
            wave += amp1 * np.sin(freq1 * x_scaled[i]) * np.cos(freq2 * x_scaled[i])
        
        # Exponential barrier regions with adaptive width and height
        barriers = 0.0
        for i in range(self.dim):
            # Multiple exponential barriers with varying positions and steepness
            barrier1 = np.exp(-5.0 * (x_scaled[i] - 0.3)**2) * (1.0 + 0.5 * np.sin(x_scaled[i] * 3.0))
            barrier2 = np.exp(-4.0 * (x_scaled[i] + 0.4)**2) * (1.0 + 0.3 * np.cos(x_scaled[i] * 2.5))
            barrier3 = np.exp(-6.0 * x_scaled[i]**2) * (1.0 + 0.4 * np.sin(x_scaled[i] * 4.0))
            barriers += barrier1 + barrier2 + barrier3
        
        # Adaptive curvature component with dimension-dependent scaling
        curvature = 0.0
        for i in range(self.dim):
            # Varying quadratic terms with chaotic coefficients
            coeff = 1.0 + 0.3 * np.sin(i * 0.8 + x_scaled[i])
            curvature += coeff * x_scaled[i]**2 * (1.0 + 0.2 * np.cos(x_scaled[i] * 2.0))
        
        # Cross-dimensional interaction with periodic modulation
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                # Periodic interaction terms with exponential decay
                phase = np.sin(2.0 * x_scaled[i] + 1.5 * x_scaled[j])
                weight = 1.0 / (1.0 + 0.5 * np.abs(i - j))
                interaction += weight * phase * np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Multi-scale periodic component with varying amplitudes
        multiscale = 0.0
        scales = [1, 2, 3, 4, 5]
        for scale in scales:
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * np.cos(scale * x_scaled[i] * 0.7) * \
                             (1.0 + 0.1 * np.sin(scale * x_scaled[i] * 2.0))
        
        # Combined function with adaptive weights
        return 1.5 * wave + 2.0 * barriers + 1.2 * curvature + 0.8 * interaction + 1.0 * multiscale
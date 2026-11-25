import numpy as np

class SinusoidalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with periodic modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial = 2.0 * np.sin(3.0 * r) * np.cos(2.0 * r)
        
        # Sinusoidal components in each dimension
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i * 0.7)
            amp = 1.5 + 0.3 * np.cos(i * 0.9)
            sinusoidal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.8)
        
        # Cross-dimensional interference patterns
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Pairwise interaction with phase shift and exponential decay
                phase = np.sin(0.5 * x_scaled[i] + 0.3 * x_scaled[j])
                dist = np.abs(x_scaled[i] - x_scaled[j])
                interference += phase * np.exp(-dist * 2.0) * (1.0 + 0.2 * np.sin(i + j))
        
        # Multi-scale periodicity with varying amplitudes
        multiscale = 0.0
        scales = [1, 2, 3, 4, 5]
        for scale in scales:
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * np.cos(scale * x_scaled[i] * 0.7) * \
                             np.exp(-0.1 * scale * np.abs(x_scaled[i]))
        
        # Valley-forming components with exponential decay
        valleys = 0.0
        for i in range(self.dim):
            # Create multiple local minima along each dimension
            valley_pos = np.sin(i * 1.2) * 0.8
            valleys += (x_scaled[i] - valley_pos)**2 * np.exp(-0.5 * (x_scaled[i] - valley_pos)**2)
        
        # Combined function with carefully balanced components
        return 1.5 * radial + 1.2 * sinusoidal + 0.8 * interference + 1.0 * multiscale + 0.9 * valleys
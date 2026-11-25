import numpy as np

class WaveGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial symmetry component with periodic wave interactions
        radial = np.sum(x_scaled**2)
        
        # Periodic sine-wave interactions between dimensions
        wave_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Sine-based interaction with distance-dependent amplitude
                dist = np.sqrt((x_scaled[i] - x_scaled[j])**2)
                wave_interaction += np.sin(3.0 * dist) * np.exp(-0.5 * dist**2)
        
        # Gaussian peaks with radial decay and periodic modulation
        gaussian_peaks = 0.0
        for i in range(self.dim):
            # Multiple peaks with varying heights and widths
            peak_height = 2.0 + 1.5 * np.sin(i * 0.7)
            peak_width = 0.5 + 0.3 * np.cos(i * 0.5)
            gaussian_peaks += peak_height * np.exp(-0.5 * (x_scaled[i] / peak_width)**2)
        
        # Exponentially decaying radial component with sinusoidal modulation
        decay_radial = np.exp(-0.5 * radial) * np.sin(2.0 * radial)
        
        # Combine all components with different weights
        return 1.5 * radial + 2.0 * wave_interaction + 1.8 * gaussian_peaks + 0.7 * decay_radial
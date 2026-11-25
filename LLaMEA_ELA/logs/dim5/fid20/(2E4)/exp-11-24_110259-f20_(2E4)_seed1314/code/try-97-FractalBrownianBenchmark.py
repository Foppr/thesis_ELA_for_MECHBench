import numpy as np

class FractalBrownianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal parameters
        self.H = np.random.rand(dim) * 0.8 + 0.2  # Hurst parameter (0.2-1.0)
        self.frequency_scale = np.random.rand(dim) * 2 + 1  # Spatial frequency scaling
        self.amplitude_scale = np.random.rand(dim) * 3 + 1  # Amplitude scaling
        self.phase_shift = np.random.rand(dim) * 2 * np.pi  # Phase shifts
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_normalized = x / 5.0
        
        # Fractal Brownian motion component
        fbm_values = []
        for i in range(self.dim):
            # Generate fractal noise with varying Hurst parameter
            h = self.H[i]
            freq = self.frequency_scale[i]
            amp = self.amplitude_scale[i]
            phase = self.phase_shift[i]
            
            # Create a sum of sinusoidal components with different frequencies and amplitudes
            value = 0.0
            for k in range(1, 11):  # Sum of first 10 harmonics
                freq_k = freq * (2 ** k)
                amp_k = amp / (k ** (h + 0.5))  # Amplitude decreases with frequency
                value += amp_k * np.sin(freq_k * x_normalized[i] + phase)
            
            fbm_values.append(value)
        
        # Spatially varying frequency components
        spatial_freq = []
        for i in range(self.dim):
            # Frequency varies based on position
            pos_dependent_freq = 1.0 + 0.5 * np.sin(x_normalized[i])
            spatial_freq.append(pos_dependent_freq)
        
        # Combine all components with adaptive weights
        result = 0.0
        for i in range(self.dim):
            # Main contribution from fractal Brownian motion
            result += fbm_values[i] * spatial_freq[i]
            
            # Add interaction terms between dimensions
            for j in range(i+1, self.dim):
                interaction = np.sin(x_normalized[i] + x_normalized[j]) * \
                             np.cos(x_normalized[i] - x_normalized[j])
                result += 0.3 * interaction
        
        # Add global scaling and periodic modulation
        global_scale = 1.0 + 0.2 * np.sin(np.sum(x_normalized**2))
        result *= global_scale
        
        # Add self-similar structure with multiple scales
        multi_scale = 0.0
        for scale in [0.5, 1.0, 2.0]:
            scale_factor = 1.0 / (scale ** 2)
            scale_term = np.sum(np.sin(scale * x_normalized) * np.cos(scale * x_normalized))
            multi_scale += scale_factor * scale_term
        
        result += 0.5 * multi_scale
        
        # Add noise with fractal characteristics
        noise = 0.01 * np.random.randn()
        noise += 0.005 * np.sin(np.sum(x_normalized**3))
        
        return result + noise
import numpy as np

class NestedOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Nested harmonic oscillations with varying frequencies and amplitudes
        harmonic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)
            amp = 1.5 + 0.5 * np.cos(0.3 * i)
            harmonic += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Radial basis function interactions with varying centers and widths
        rbf = 0.0
        for i in range(self.dim):
            center = np.sin(0.4 * i) * 0.8
            width = 0.5 + 0.3 * np.cos(0.6 * i)
            rbf += np.exp(-width * (x_scaled[i] - center)**2)
        
        # Exponential penalty terms with chaotic modulation
        penalty = 0.0
        for i in range(self.dim):
            # Chaotic penalty scaling with exponential growth
            scale = 1.0 + 2.0 * np.sin(0.3 * i + x_scaled[i])
            penalty += scale * np.exp(2.0 * np.abs(x_scaled[i]))
        
        # Multi-scale harmonic interference with nested frequency patterns
        interference = 0.0
        for scale in [1, 2, 3, 4, 5]:
            for i in range(self.dim):
                freq = scale * (1.0 + 0.5 * np.sin(0.2 * i))
                interference += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.8) * \
                               np.exp(-0.1 * scale * x_scaled[i]**2)
        
        # Asymmetric basin structure with exponential weighting
        basin = 0.0
        for i in range(self.dim):
            # Create asymmetric basins with different steepness on left vs right
            if x_scaled[i] >= 0:
                basin += np.exp(-0.5 * (x_scaled[i] - 0.3)**2) * (1.0 + 0.5 * x_scaled[i])
            else:
                basin += np.exp(-0.5 * (x_scaled[i] + 0.3)**2) * (1.0 - 0.5 * x_scaled[i])
        
        # Combined function with carefully balanced components
        return 1.5 * harmonic + 2.0 * rbf + 1.8 * penalty + 1.2 * interference + 0.9 * basin
import numpy as np

class FractalOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal component with chaotic coupling
        fractal = 0
        for i in range(self.dim):
            # Chaotic coupling between dimensions
            coupling = np.sin(np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[(i+1) % self.dim])
            term = np.sin(2**(i+1) * np.pi * x_norm[i]) * np.cos(3**(i+1) * np.pi * x_norm[i]) + coupling
            fractal += term / (1.0 + i * 0.2)
        
        # Multi-scale harmonic oscillator with dynamic phase modulation
        harmonic = 0
        for i in range(self.dim):
            freq = 2**(i % 5)  # Frequencies 1, 2, 4, 8, 16, 1, 2, 4, 8, 16, ...
            phase_mod = np.sin(0.5 * np.pi * x_norm[i]) * np.cos(0.3 * np.pi * x_norm[(i+2) % self.dim])
            damp = 1.0 / (1.0 + 0.2 * i)
            harmonic += damp * np.sin(freq * np.pi * x_norm[i] + phase_mod) * np.cos(freq * np.pi * x_norm[i] + phase_mod)
        
        # Complex interaction terms with asymmetric scaling
        interaction = 0
        scales = [1, 2, 4, 8, 16]  # Extended scale values for more complex interactions
        for scale in scales:
            if scale <= self.dim:
                # Asymmetric grouped interactions with exponential weights
                group_sum = np.sum(x_norm[:scale]**3)  # Changed to cubic for stronger nonlinearity
                interaction += np.sin(np.pi * group_sum) * np.cos(5 * np.pi * group_sum) * np.exp(-0.1 * scale)
        
        # Asymmetric conditioning with exponential decay and dynamic weights
        conditioning = 0
        for i in range(self.dim):
            if x_norm[i] >= 0:
                conditioning += (x_norm[i]**4) * np.exp(-0.8 * x_norm[i]**2) * (1 + 0.1 * np.sin(3 * np.pi * x_norm[i]))
            else:
                conditioning += (x_norm[i]**6) * np.exp(-0.5 * x_norm[i]**2) * (1 + 0.1 * np.cos(2 * np.pi * x_norm[i]))
        
        # Enhanced boundary attraction with dynamic scaling
        boundary = 0
        for i in range(self.dim):
            # Dynamic boundary influence based on dimension
            influence = 20 * (np.abs(x_norm[i]) - 1)**5  # Increased power for stronger boundary pull
            boundary += influence
        
        # Add gradient corridors with asymmetric slopes
        gradient_corridors = 0
        for i in range(self.dim):
            if x_norm[i] > 0:
                gradient_corridors += 0.5 * np.sin(4 * np.pi * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
            else:
                gradient_corridors += 0.5 * np.cos(4 * np.pi * x_norm[i]) * np.exp(-0.6 * x_norm[i]**2)
        
        # Combined result with adaptive scaling and enhanced complexity
        result = 2.0 * fractal + 1.8 * harmonic + 1.2 * interaction + 0.9 * conditioning + 0.8 * boundary + 0.6 * gradient_corridors
        
        return result
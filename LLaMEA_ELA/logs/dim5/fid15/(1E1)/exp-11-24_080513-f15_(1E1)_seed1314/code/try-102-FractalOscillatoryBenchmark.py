import numpy as np

class FractalOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Self-similar fractal component using recursive cosine patterns
        fractal = 0.0
        for i in range(self.dim):
            scale = 2.0 ** (i % 3)  # Changed from 4 to 3 for different scaling
            freq = 4.0 * scale      # Increased base frequency
            amp = 1.0 / (1.0 + 0.3 * i)  # Modified amplitude decay
            fractal += amp * np.cos(freq * x_normalized[i]) * np.sin(freq * x_normalized[i])
        
        # High-frequency oscillatory component with varying amplitudes and phases
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 12.0 + 6.0 * np.sin(i * 0.7)  # Increased base frequency
            amp = 0.4 + 0.6 * np.cos(i * 0.5)    # Modified amplitude range
            phase = 0.3 * np.sin(i * 0.9)        # Increased phase modulation
            oscillatory += amp * np.sin(freq * x_normalized[i] + phase) * np.cos(freq * x_normalized[i] + phase)
        
        # Geometric progression interaction terms with exponential decay
        geometric = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 3.0)  # Increased decay rate
                geometric += weight * (x_normalized[i]**2 + x_normalized[j]**2) * np.sin(6 * dist)  # Increased frequency
        
        # Multi-scale radial basis with fractal-like center distribution
        radial = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.35) * np.cos(i * 0.45)  # Slightly altered center positions
            width = 0.25 + 0.25 * np.sin(i * 0.6)        # Modified width distribution
            radial += np.exp(-0.5 * ((x_normalized[i] - center) / width)**2)
        
        # Cross-dimensional coupling with varying strength and periodicity (modified)
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.6 + 0.4 * np.sin(i * 0.4 + j * 0.3)  # Increased coupling strength
                period = 2.5 + 0.4 * np.cos(i * 0.6)             # Modified periodicity
                coupling += strength * np.sin(period * (x_normalized[i] - x_normalized[j])) * np.exp(-0.3 * (x_normalized[i] - x_normalized[j])**2)
        
        # Polynomial interaction with increasing degree and dimensionality (modified exponents)
        poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly += (x_normalized[i] * x_normalized[j])**(i % 4 + 3)  # Increased minimum exponent
        
        # Logarithmic noise component with chaotic phase modulation
        noise = 0.0
        r = 3.85  # Slightly altered chaos parameter
        x_prev = 0.5
        for i in range(self.dim):
            x_prev = r * x_prev * (1 - x_prev)
            phase_mod = np.sin(x_prev * 9 * np.pi)  # Increased phase modulation frequency
            noise += np.sin(22 * x_normalized[i] + phase_mod) * np.log(1.0 + 0.6 * x_normalized[i]**2)  # Increased frequency and log coefficient
        
        # Combine all components with modified weights
        return (0.25 * fractal + 0.3 * oscillatory + 0.18 * geometric + 
                0.12 * radial + 0.09 * coupling + 0.06 * poly + 0.02 * noise)
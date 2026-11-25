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
            scale = 2.0 ** (i % 4)
            freq = 3.0 * scale
            amp = 1.0 / (1.0 + 0.5 * i)
            fractal += amp * np.cos(freq * x_normalized[i]) * np.sin(freq * x_normalized[i])
        
        # High-frequency oscillatory component with varying amplitudes and phases
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 10.0 + 5.0 * np.sin(i * 0.7)
            amp = 0.3 + 0.7 * np.cos(i * 0.5)
            phase = 0.2 * np.sin(i * 0.9)
            oscillatory += amp * np.sin(freq * x_normalized[i] + phase) * np.cos(freq * x_normalized[i] + phase)
        
        # Geometric progression interaction terms with exponential decay
        geometric = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 2.0)
                geometric += weight * (x_normalized[i]**2 + x_normalized[j]**2) * np.sin(5 * dist)
        
        # Multi-scale radial basis with fractal-like center distribution
        radial = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.3) * np.cos(i * 0.4)
            width = 0.2 + 0.3 * np.sin(i * 0.6)
            radial += np.exp(-0.5 * ((x_normalized[i] - center) / width)**2)
        
        # Cross-dimensional coupling with varying strength and periodicity
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.5 + 0.5 * np.sin(i * 0.4 + j * 0.3)
                period = 2.0 + 0.5 * np.cos(i * 0.6)
                coupling += strength * np.sin(period * (x_normalized[i] - x_normalized[j])) * np.exp(-0.2 * (x_normalized[i] - x_normalized[j])**2)
        
        # Polynomial interaction with increasing degree and dimensionality
        poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly += (x_normalized[i] * x_normalized[j])**(i % 3 + 2)
        
        # Logarithmic noise component with chaotic phase modulation
        noise = 0.0
        r = 3.9
        x_prev = 0.5
        for i in range(self.dim):
            x_prev = r * x_prev * (1 - x_prev)
            phase_mod = np.sin(x_prev * 8 * np.pi)
            noise += np.sin(20 * x_normalized[i] + phase_mod) * np.log(1.0 + 0.5 * x_normalized[i]**2)
        
        # Combine all components with adaptive weights
        return (0.3 * fractal + 0.25 * oscillatory + 0.15 * geometric + 
                0.1 * radial + 0.08 * coupling + 0.07 * poly + 0.05 * noise)
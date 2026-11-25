import numpy as np

class FractalOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Chaotic logistic map component with dynamic parameter modulation
        chaotic = 0.0
        r_params = [3.5 + 0.4 * np.sin(i * 0.7) for i in range(self.dim)]
        x_prev = np.full(self.dim, 0.5)
        for i in range(self.dim):
            x_prev[i] = r_params[i] * x_prev[i] * (1 - x_prev[i])
            chaotic += np.sin(15 * x_normalized[i] + x_prev[i]) * np.cos(7 * x_normalized[i] + x_prev[i])
        
        # Multi-scale fractal cosine with dynamic frequency modulation
        fractal = 0.0
        for i in range(self.dim):
            freq_mod = 2.0 + 1.5 * np.sin(i * 0.5)
            scale = 3.0 ** (i % 5)
            freq = 4.0 * scale * freq_mod
            amp = 1.0 / (1.0 + 0.3 * i)
            fractal += amp * np.cos(freq * x_normalized[i]) * np.sin(freq * x_normalized[i])
        
        # High-frequency oscillatory component with time-varying phases and amplitudes
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 15.0 + 8.0 * np.sin(i * 0.6)
            amp = 0.4 + 0.6 * np.cos(i * 0.4)
            phase = 0.3 * np.sin(i * 0.8) + 0.2 * np.cos(i * 0.5)
            oscillatory += amp * np.sin(freq * x_normalized[i] + phase) * np.cos(freq * x_normalized[i] + phase)
        
        # Geometric progression interaction terms with dynamic weights and exponential decay
        geometric = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 3.0) * (1.0 + 0.5 * np.sin(i * 0.3))
                geometric += weight * (x_normalized[i]**2 + x_normalized[j]**2) * np.sin(7 * dist)
        
        # Multi-scale radial basis with chaotic center distribution and dynamic widths
        radial = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.4) * np.cos(i * 0.5) + 0.3 * np.sin(i * 0.2)
            width = 0.1 + 0.4 * np.sin(i * 0.7)
            radial += np.exp(-0.5 * ((x_normalized[i] - center) / width)**2)
        
        # Cross-dimensional coupling with dynamic strength and periodicity
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.6 + 0.4 * np.sin(i * 0.5 + j * 0.3)
                period = 2.5 + 0.8 * np.cos(i * 0.7)
                coupling += strength * np.sin(period * (x_normalized[i] - x_normalized[j])) * np.exp(-0.15 * (x_normalized[i] - x_normalized[j])**2)
        
        # Polynomial interaction with increasing degree, dimensionality, and chaotic coefficients
        poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.5 + 0.5 * np.sin(i * 0.4 + j * 0.3)
                poly += coeff * (x_normalized[i] * x_normalized[j])**(i % 4 + 2)
        
        # Logarithmic noise component with chaotic phase modulation and dynamic scaling
        noise = 0.0
        x_prev = np.full(self.dim, 0.5)
        for i in range(self.dim):
            x_prev[i] = 3.8 * x_prev[i] * (1 - x_prev[i])
            phase_mod = np.sin(x_prev[i] * 10 * np.pi) + 0.2 * np.cos(x_prev[i] * 15 * np.pi)
            noise += np.sin(25 * x_normalized[i] + phase_mod) * np.log(1.0 + 0.7 * x_normalized[i]**2)
        
        # Combine all components with adaptive weights and dynamic scaling
        return (0.25 * chaotic + 0.3 * fractal + 0.2 * oscillatory + 0.15 * geometric + 
                0.08 * radial + 0.07 * coupling + 0.06 * poly + 0.05 * noise)
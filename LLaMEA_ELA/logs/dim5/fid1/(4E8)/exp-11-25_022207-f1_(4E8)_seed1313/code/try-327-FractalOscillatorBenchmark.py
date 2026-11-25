import numpy as np

class FractalOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal component with chaotic coupling and multi-scale interactions
        fractal = 0
        for i in range(self.dim):
            # Chaotic coupling between dimensions with dynamic phase
            coupling = np.sin(np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[(i+1) % self.dim])
            # Multi-scale fractal terms with exponential growth
            term = np.sin(2**(i+1) * np.pi * x_norm[i]) * np.cos(3**(i+1) * np.pi * x_norm[i]) + coupling
            fractal += term / (1.0 + i * 0.1)
        
        # Multi-scale harmonic oscillator with dynamic phase modulation and frequency scaling
        harmonic = 0
        for i in range(self.dim):
            freq = 2**(i % 4)  # Frequencies 1, 2, 4, 8, 1, 2, 4, 8, ...
            phase_mod = np.sin(0.3 * np.pi * x_norm[i]) * np.cos(0.4 * np.pi * x_norm[(i+2) % self.dim])
            damp = 1.0 / (1.0 + 0.1 * i)
            harmonic += damp * np.sin(freq * np.pi * x_norm[i] + phase_mod) * np.cos(freq * np.pi * x_norm[i] + phase_mod)
        
        # Complex interaction terms with asymmetric scaling and grouped dynamics
        interaction = 0
        scales = [1, 2, 3, 4, 5]  # Reduced scale values for better control
        for scale in scales:
            if scale <= self.dim:
                # Asymmetric grouped interactions with polynomial weights
                group_sum = np.sum(x_norm[:scale]**2)  # Quadratic for smoother interaction
                interaction += np.sin(np.pi * group_sum) * np.cos(3 * np.pi * group_sum) * np.exp(-0.05 * scale)
        
        # Asymmetric conditioning with modified exponential decay and dynamic weights
        conditioning = 0
        for i in range(self.dim):
            if x_norm[i] >= 0:
                conditioning += (x_norm[i]**3) * np.exp(-0.6 * x_norm[i]**2) * (1 + 0.05 * np.sin(2 * np.pi * x_norm[i]))
            else:
                conditioning += (x_norm[i]**5) * np.exp(-0.4 * x_norm[i]**2) * (1 + 0.05 * np.cos(3 * np.pi * x_norm[i]))
        
        # Enhanced boundary attraction with modified scaling
        boundary = 0
        for i in range(self.dim):
            influence = 15 * (np.abs(x_norm[i]) - 1)**4  # Reduced power for less aggressive boundary pull
            boundary += influence
        
        # Gradient corridors with asymmetric slopes and dynamic modulation
        gradient_corridors = 0
        for i in range(self.dim):
            if x_norm[i] > 0:
                gradient_corridors += 0.3 * np.sin(3 * np.pi * x_norm[i]) * np.exp(-0.2 * x_norm[i]**2)
            else:
                gradient_corridors += 0.3 * np.cos(3 * np.pi * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Combined result with adjusted scaling factors for better balance
        result = 1.8 * fractal + 1.6 * harmonic + 1.4 * interaction + 1.0 * conditioning + 0.7 * boundary + 0.5 * gradient_corridors
        
        return result
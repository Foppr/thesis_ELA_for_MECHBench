import numpy as np

class OscillatoryRadialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequences for dynamic behavior
        self.chaos_seq = np.sin(np.arange(dim) * 0.5 + 1.0)
    
    def f(self, x):
        x = np.array(x)
        
        # Sinusoidal oscillation component with varying frequencies and amplitudes
        oscillation = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.4 + self.chaos_seq[i])
            amp = 1.0 + 0.5 * np.cos(i * 0.6 + self.chaos_seq[i])
            oscillation += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Radial basis functions with time-varying centers and widths
        radial = 0.0
        for i in range(self.dim):
            center = -3.0 + 6.0 * (i / self.dim) * np.cos(self.chaos_seq[i] * 1.5)
            width = 0.2 + 0.8 * np.sin(i * 0.3) * (1.0 + 0.3 * np.cos(self.chaos_seq[i]))
            radial += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.sin(x[i] * 0.4)
        
        # Chaotic gradient flow with dynamic direction and magnitude
        gradient = 0.0
        for i in range(self.dim):
            direction = np.sin(i * 0.7 + self.chaos_seq[i])
            magnitude = 1.0 + 0.5 * np.cos(i * 0.5 + self.chaos_seq[i])
            gradient += magnitude * (x[i] - direction)**2 * np.exp(-0.2 * (x[i] - direction)**2)
        
        # Coupling terms with chaotic modulation and asymmetric interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 1.0 + 0.4 * np.cos(i * j * 0.3 + self.chaos_seq[i] + self.chaos_seq[j])
                coupling += mod * np.sin(x[i] * x[j]) * np.cos(x[i] - x[j]) * (x[i]**2 + x[j]**2)
        
        # Fractal-like recursive structure with varying scale factors
        fractal = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.4 * np.sin(i * 0.9 + self.chaos_seq[i])
            fractal += scale * np.sin(x[i] * scale) * np.cos(x[i] * scale * 0.6) * np.exp(-0.03 * x[i]**2)
        
        # Dynamic harmonic landscape with multi-scale frequency modulation
        harmonic = 0.0
        for i in range(self.dim):
            freq_mod = 1.5 + 0.8 * np.sin(i * 0.4 + self.chaos_seq[i])
            harmonic += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] * 0.7) * (1.0 + 0.3 * np.sin(x[i]))
        
        # Combine all terms with adaptive weighting
        total = 0.25 * oscillation + 0.2 * radial + 0.15 * gradient + 0.2 * coupling + 0.1 * fractal + 0.1 * harmonic
        
        # Global scaling with chaotic modulation based on dimensionality
        global_scale = 1.0 + 0.4 * np.sin(self.dim * 0.6) * np.cos(self.dim * 0.4)
        
        return total * global_scale
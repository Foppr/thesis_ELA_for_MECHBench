import numpy as np

class SinusoidalFrequencyModulationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.base_freq = 2.0 * np.pi
        self.modulation_factor = 1.5
        self.decay_exponent = 3.0
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        r = np.sqrt(np.sum(x**2))
        
        # Base sinusoidal component with frequency modulation
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = self.base_freq * (1.0 + self.modulation_factor * np.sin(0.5 * x[i]))
            sinusoidal += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
        
        # Radial polynomial decay with varying exponents
        radial_decay = np.sum((x / 5.0)**self.decay_exponent)
        
        # Cross-dimension interaction terms with varying coupling strengths
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.5 * np.sin(0.7 * x[i] * x[j])
                interaction += coupling * np.sin(3.0 * x[i]) * np.cos(2.0 * x[j])
        
        # Add a global minimum at origin with additional noise-like perturbations
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(10.0 * x[i]) * np.cos(5.0 * x[i])
        
        return 2.0 * sinusoidal + 0.5 * radial_decay + 0.3 * interaction + 0.1 * noise
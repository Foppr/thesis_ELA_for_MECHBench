import numpy as np

class ExponentialSineMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive parameters for each dimension
        self.adaptive_amplitudes = [1.0 + 0.5 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)]
        self.decay_rates = [0.1 + 0.3 * np.cos(i * np.pi / (dim + 2)) for i in range(dim)]
        self.modulation_frequencies = [0.5 + 0.5 * np.sin(i * np.pi / (dim + 3)) for i in range(dim)]
        self.basin_centers = np.random.uniform(-5.0, 5.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Exponential decay potentials with dimensionally adaptive rates
        for i in range(self.dim):
            amplitude = self.adaptive_amplitudes[i]
            decay_rate = self.decay_rates[i]
            result += amplitude * np.exp(-decay_rate * np.abs(x[i]))
        
        # Sine-wave modulated gradient components
        for i in range(self.dim):
            frequency = self.modulation_frequencies[i]
            result += 2.0 * np.sin(frequency * x[i]) * np.cos(frequency * x[i])
        
        # Multi-basin attraction with adaptive centering
        basin_attraction = 0.0
        for i in range(self.dim):
            center = self.basin_centers[i]
            distance = np.abs(x[i] - center)
            basin_attraction += 1.5 * np.exp(-0.5 * (distance / (1.0 + 0.1 * np.sin(i * np.pi / (self.dim + 1))))**2)
        result += basin_attraction
        
        # Cross-dimension coupling with sine modulation
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.3 * np.sin((x[i] + x[j]) / 2)
                coupling_term += coupling_strength * np.cos(x[i] - x[j])
        result += coupling_term
        
        # Adaptive noise modulation based on position
        noise_modulation = 0.0
        for i in range(self.dim):
            noise_modulation += 0.2 * np.sin(x[i])**2 * np.cos(x[i])
        result += noise_modulation
        
        # Global phase shift with dimension-dependent scaling
        global_shift = np.sum(np.sin(x) * np.cos(x)) / self.dim
        result *= (1.0 + 0.3 * global_shift)
        
        return result
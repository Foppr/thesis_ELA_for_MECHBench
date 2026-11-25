import numpy as np

class ExponentialRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize exponential decay correlation coefficients
        self.decay_rates = np.random.uniform(0.1, 2.0, dim)
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        # Initialize radial gradient field parameters
        self.gradient_centers = np.random.uniform(-4.0, 4.0, (dim, 3))
        self.gradient_strengths = np.random.uniform(1.0, 3.0, (dim, 3))
        self.gradient_widths = np.random.uniform(0.5, 2.0, (dim, 3))
        # Initialize adaptive frequency modulation parameters
        self.modulation_frequencies = np.random.uniform(0.5, 3.0, dim)
        self.modulation_amplitudes = np.random.uniform(0.1, 1.0, dim)
        self.modulation_phases = np.random.uniform(-np.pi, np.pi, dim)
        # Initialize coupling between dimensions with adaptive weights
        self.adaptive_couplings = np.random.uniform(0.5, 2.0, (dim, dim))
        np.fill_diagonal(self.adaptive_couplings, 0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay correlation component
        exp_corr = 0
        for i in range(self.dim):
            decay_rate = self.decay_rates[i]
            amplitude = self.amplitudes[i]
            exp_corr += amplitude * np.exp(-decay_rate * np.abs(x[i]))
        
        # Radial gradient field component with multiple centers
        radial_grad = 0
        for i in range(self.dim):
            for j in range(3):  # Three gradient centers per dimension
                center = self.gradient_centers[i, j]
                strength = self.gradient_strengths[i, j]
                width = self.gradient_widths[i, j]
                distance = np.abs(x[i] - center)
                radial_grad += strength * np.exp(-0.5 * (distance / width)**2)
        
        # Adaptive frequency modulation component
        adaptive_freq = 0
        for i in range(self.dim):
            freq = self.modulation_frequencies[i]
            amp = self.modulation_amplitudes[i]
            phase = self.modulation_phases[i]
            adaptive_freq += amp * np.sin(freq * x[i] + phase) + 0.3 * np.cos(2 * freq * x[i] + phase)
        
        # Cross-dimension coupling with adaptive weights
        coupling = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling += self.adaptive_couplings[i, j] * np.log(1 + np.abs(x[i] - x[j]))
        
        # Combine all components with different weights
        result = (1.5 * exp_corr + 
                 2.0 * radial_grad + 
                 1.0 * adaptive_freq + 
                 0.7 * coupling)
        
        return result
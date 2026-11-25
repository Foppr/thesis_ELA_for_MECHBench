import numpy as np

class AdaptiveRidgeHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Self-adaptive elliptic parameter sections
        self.elliptic_sections = np.random.uniform(0.5, 3.0, min(20, dim))
        # Dynamic ridge structures with varying heights and widths
        self.ridge_heights = np.random.uniform(1.0, 5.0, min(25, dim))
        self.ridge_widths = np.random.uniform(0.1, 1.5, min(25, dim))
        # Stochastic harmonic interference components
        self.harmonic_amplitudes = np.random.uniform(0.2, 2.0, min(30, dim))
        self.harmonic_frequencies = np.logspace(0.5, 3.0, min(30, dim))
        # Adaptive scaling factors for each dimension
        self.scaling_factors = np.random.uniform(0.8, 1.5, min(25, dim))
        # Multi-scale ridge structures with exponential decay
        self.ridge_decay_rates = np.random.uniform(0.1, 2.0, min(20, dim))
        # Cross-dimensional harmonic coupling
        self.coupling_strength = 0.3
        # Noise sensitivity and stochastic modulation
        self.noise_level = 0.15
        # Initial condition sensitivity parameters
        self.sensitivity_exponent = np.random.uniform(1.2, 3.0, min(20, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Elliptic sections with adaptive parameters
        elliptic_term = 0.0
        for i in range(min(len(self.elliptic_sections), self.dim)):
            section = self.elliptic_sections[i]
            # Adaptive elliptic contour with varying eccentricity
            elliptic_term += section * (x_norm[i] ** 2) * (1.0 + 0.3 * np.sin(5.0 * x_norm[i]))
            
        # Dynamic ridge structures with exponential decay and harmonic interference
        ridge_term = 0.0
        for i in range(min(len(self.ridge_heights), self.dim)):
            height = self.ridge_heights[i]
            width = self.ridge_widths[i]
            decay = self.ridge_decay_rates[i]
            # Ridge with exponential decay and harmonic modulation
            ridge_term += height * np.exp(-0.5 * (x_norm[i] / width) ** 2) * (
                1.0 + 0.2 * np.sin(3.0 * x_norm[i]) * np.cos(2.0 * x_norm[i])
            ) * np.exp(-decay * np.abs(x_norm[i]))
            
        # Stochastic harmonic interference with cross-dimensional coupling
        harmonic_term = 0.0
        for i in range(min(len(self.harmonic_amplitudes), self.dim)):
            amplitude = self.harmonic_amplitudes[i]
            frequency = self.harmonic_frequencies[i]
            # Harmonic component with adaptive scaling and stochastic noise
            harmonic_term += amplitude * np.sin(frequency * x_norm[i]) * (
                1.0 + self.noise_level * np.random.uniform(-1.0, 1.0)
            )
            
        # Cross-dimensional coupling with harmonic interference
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coupling = self.coupling_strength * (
                    np.sin(x_norm[i]) * np.cos(x_norm[j]) + 
                    np.cos(2.0 * x_norm[i]) * np.sin(0.5 * x_norm[j])
                )
                # Add cross-dimensional harmonic interference
                coupling_term += coupling * np.sin(0.5 * (x_norm[i] + x_norm[j]))
                
        # Adaptive scaling and sensitivity to initial conditions
        scaling_term = 0.0
        for i in range(min(len(self.scaling_factors), self.dim)):
            scaling = self.scaling_factors[i]
            sensitivity = self.sensitivity_exponent[i]
            # Apply adaptive scaling with sensitivity to initial conditions
            scaling_term += scaling * (np.abs(x_norm[i]) ** sensitivity) * (
                1.0 + 0.1 * np.sin(4.0 * x_norm[i])
            )
            
        # Combined landscape with weighted components
        result = 0.35 * elliptic_term + 0.3 * ridge_term + 0.2 * harmonic_term + 0.1 * coupling_term + 0.05 * scaling_term
        
        return result
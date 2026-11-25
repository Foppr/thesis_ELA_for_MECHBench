import numpy as np

class AdaptiveRidgeHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Self-adaptive elliptic parameters with dynamic scaling
        self.elliptic_axes = np.logspace(0.5, 3.5, min(20, dim))
        self.elliptic_exponents = np.random.uniform(1.2, 4.0, min(20, dim))
        # Dynamic ridge structures with varying heights and widths
        self.ridge_heights = np.random.uniform(0.5, 3.0, min(15, dim))
        self.ridge_widths = np.random.uniform(0.3, 2.0, min(15, dim))
        # Stochastic harmonic interference parameters
        self.harmonic_frequencies = np.logspace(1.0, 4.0, min(25, dim))
        self.harmonic_amplitudes = np.random.uniform(0.1, 1.5, min(25, dim))
        # Adaptive conditioning gradients
        self.conditioning_factors = np.linspace(0.8, 12.0, min(25, dim))
        # Cross-dimensional coupling with varying strengths
        self.cross_coupling = np.random.uniform(0.1, 0.8, min(15, dim))
        # Initial condition sensitivity parameters
        self.sensitivity_exponent = np.random.uniform(1.5, 3.5, min(20, dim))
        # Multi-scale modulation for enhanced complexity
        self.modulation_scales = np.logspace(0.5, 3.0, min(20, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Elliptic sections with self-adaptive scaling and harmonic modulation
        elliptic_term = 0.0
        for i in range(min(len(self.elliptic_axes), self.dim)):
            axis = self.elliptic_axes[i]
            exponent = self.elliptic_exponents[i]
            # Add harmonic modulation to elliptic components
            harmonic_mod = np.sin(self.harmonic_frequencies[i % len(self.harmonic_frequencies)] * x_norm[i])
            elliptic_term += axis * (x_norm[i] ** exponent) * (1.0 + 0.3 * harmonic_mod)
            
        # Dynamic ridge structures with varying heights and widths
        ridge_term = 0.0
        for i in range(min(len(self.ridge_heights), self.dim)):
            height = self.ridge_heights[i]
            width = self.ridge_widths[i]
            # Ridge with Gaussian profile and harmonic interference
            ridge_term += height * np.exp(-0.5 * (x_norm[i] / width) ** 2) * (
                1.0 + 0.2 * np.sin(self.harmonic_frequencies[i % len(self.harmonic_frequencies)] * x_norm[i])
            )
            
        # Stochastic harmonic interference across dimensions
        harmonic_term = 0.0
        for i in range(min(len(self.harmonic_amplitudes), self.dim)):
            amplitude = self.harmonic_amplitudes[i]
            freq = self.harmonic_frequencies[i % len(self.harmonic_frequencies)]
            harmonic_term += amplitude * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
            
        # Adaptive conditioning gradients with exponential and multi-scale modulation
        condition_term = 0.0
        for i in range(min(len(self.conditioning_factors), self.dim)):
            factor = self.conditioning_factors[i]
            # Combine exponential and harmonic conditioning
            condition_term += factor * (np.exp(0.2 * np.abs(x_norm[i])) - 1.0) + \
                             0.3 * factor * np.sin(self.modulation_scales[i % len(self.modulation_scales)] * x_norm[i])
            
        # Cross-dimensional coupling with ridge structures
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coupling = self.cross_coupling[i % len(self.cross_coupling)]
                # Add coupling between dimensions with harmonic interference
                cross_term += coupling * (
                    np.sin(x_norm[i]) * np.cos(x_norm[j]) + 
                    0.2 * np.sin(2.0 * x_norm[i]) * np.sin(1.5 * x_norm[j])
                ) * np.exp(-0.1 * (x_norm[i] ** 2 + x_norm[j] ** 2))
                
        # Initial condition sensitivity with adaptive exponents
        sensitivity_term = 0.0
        for i in range(min(len(self.sensitivity_exponent), self.dim)):
            exp = self.sensitivity_exponent[i]
            # Sensitivity to initial conditions with exponential scaling
            sensitivity_term += np.abs(x_norm[i]) ** exp
            
        # Combined landscape with adaptive weighting
        result = 0.25 * elliptic_term + 0.2 * ridge_term + 0.2 * harmonic_term + \
                 0.2 * condition_term + 0.1 * cross_term + 0.05 * sensitivity_term
        
        return result
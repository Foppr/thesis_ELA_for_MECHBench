import numpy as np

class AdaptiveRidgeHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Self-adaptive elliptic parameters with dynamic scaling
        self.elliptic_axes = np.logspace(0.5, 3.5, min(20, dim))
        self.elliptic_centers = np.random.uniform(-2.0, 2.0, min(20, dim))
        # Dynamic ridge structures with varying heights and widths
        self.ridge_heights = np.random.uniform(1.0, 8.0, min(25, dim))
        self.ridge_widths = np.random.uniform(0.2, 2.0, min(25, dim))
        # Stochastic harmonic interference parameters
        self.harmonic_amplitudes = np.random.uniform(0.5, 3.0, min(30, dim))
        self.harmonic_frequencies = np.logspace(1.0, 4.0, min(30, dim))
        # Cross-dimensional interaction coefficients
        self.cross_interaction = np.random.uniform(0.1, 1.0, min(15, dim))
        # Condition number scaling factors for dynamic conditioning
        self.conditioning_factors = np.logspace(0.8, 3.0, min(20, dim))
        # Multi-scale stochastic modulation for enhanced multimodality
        self.modulation_scales = np.logspace(0.5, 3.5, min(25, dim))
        # Adaptive noise components
        self.noise_amplitudes = np.random.uniform(0.1, 0.8, min(20, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Elliptic section component with self-adaptive axes and centers
        elliptic_term = 0.0
        for i in range(min(len(self.elliptic_axes), self.dim)):
            axis = self.elliptic_axes[i]
            center = self.elliptic_centers[i]
            elliptic_term += axis * ((x_norm[i] - center) ** 2)
            
        # Dynamic ridge structures with varying heights and widths
        ridge_term = 0.0
        for i in range(min(len(self.ridge_heights), self.dim)):
            height = self.ridge_heights[i]
            width = self.ridge_widths[i]
            ridge_term += height * np.exp(-0.5 * ((x_norm[i] / width) ** 2))
            
        # Stochastic harmonic interference with multi-scale components
        harmonic_term = 0.0
        for i in range(min(len(self.harmonic_amplitudes), self.dim)):
            amp = self.harmonic_amplitudes[i]
            freq = self.harmonic_frequencies[i]
            harmonic_term += amp * np.sin(freq * x_norm[i])
            
        # Cross-dimensional interaction with adaptive coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                if len(self.cross_interaction) > min(i, j):
                    interaction = self.cross_interaction[min(i, j)]
                    cross_term += interaction * np.sin(x_norm[i]) * np.cos(x_norm[j])
                    
        # Dynamic conditioning with multi-scale exponential factors
        condition_term = 0.0
        for i in range(min(len(self.conditioning_factors), self.dim)):
            factor = self.conditioning_factors[i]
            condition_term += factor * (np.exp(0.2 * np.abs(x_norm[i])) - 1.0)
            
        # Multi-scale stochastic modulation with adaptive noise
        modulation_term = 0.0
        for i in range(min(len(self.modulation_scales), self.dim)):
            scale = self.modulation_scales[i]
            modulation_term += np.sin(scale * x_norm[i]) * np.cos(2.0 * scale * x_norm[i])
            
        # Adaptive noise component
        noise_term = 0.0
        for i in range(min(len(self.noise_amplitudes), self.dim)):
            amp = self.noise_amplitudes[i]
            noise_term += amp * np.sin(5.0 * x_norm[i]) * np.cos(3.0 * x_norm[i])
            
        # Combine all terms with adaptive weighting
        result = 0.25 * elliptic_term + 0.2 * ridge_term + 0.15 * harmonic_term + \
                 0.15 * cross_term + 0.1 * condition_term + 0.08 * modulation_term + 0.07 * noise_term
        
        return result
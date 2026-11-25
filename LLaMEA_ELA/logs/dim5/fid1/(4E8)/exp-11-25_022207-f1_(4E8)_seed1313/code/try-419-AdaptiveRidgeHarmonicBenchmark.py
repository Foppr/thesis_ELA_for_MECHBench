import numpy as np

class AdaptiveRidgeHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Self-adaptive elliptic parameter sections
        self.elliptic_sections = np.random.uniform(0.5, 2.0, min(30, dim))
        # Dynamic ridge structures with varying heights and widths
        self.ridge_heights = np.random.uniform(1.0, 5.0, min(25, dim))
        self.ridge_widths = np.random.uniform(0.1, 1.0, min(25, dim))
        # Stochastic harmonic interference components
        self.harmonic_amplitudes = np.random.uniform(0.2, 1.5, min(40, dim))
        self.harmonic_frequencies = np.logspace(0.5, 3.0, min(40, dim))
        # Adaptive scaling factors for each dimension
        self.scaling_factors = np.random.uniform(0.8, 1.5, min(35, dim))
        # Cross-dimensional coupling with varying strength
        self.coupling_strengths = np.random.uniform(0.1, 0.8, min(20, dim))
        # Initial condition sensitivity parameters
        self.sensitivity_params = np.random.uniform(0.5, 2.0, min(30, dim))
        # Multi-scale harmonic components for enhanced multimodality
        self.multi_scale_harmonics = np.random.uniform(0.1, 1.0, min(35, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Elliptic section component with self-adaptive parameters
        elliptic_term = 0.0
        for i in range(min(len(self.elliptic_sections), self.dim)):
            section = self.elliptic_sections[i]
            x_squared = x_norm[i] ** 2
            elliptic_term += section * x_squared * (1.0 + 0.3 * np.sin(5.0 * x_norm[i]))
            
        # Ridge structure component with dynamic characteristics
        ridge_term = 0.0
        for i in range(min(len(self.ridge_heights), self.dim)):
            height = self.ridge_heights[i]
            width = self.ridge_widths[i]
            # Gaussian ridge with adaptive width and height
            ridge_term += height * np.exp(-0.5 * (x_norm[i] / width) ** 2)
            
        # Stochastic harmonic interference component
        harmonic_term = 0.0
        for i in range(min(len(self.harmonic_amplitudes), self.dim)):
            amplitude = self.harmonic_amplitudes[i]
            frequency = self.harmonic_frequencies[i]
            harmonic_term += amplitude * np.sin(frequency * x_norm[i])
            
        # Cross-dimensional coupling with adaptive scaling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                if j < len(self.coupling_strengths):
                    strength = self.coupling_strengths[j]
                    coupling_term += strength * np.sin(x_norm[i]) * np.cos(x_norm[j])
                    
        # Multi-scale harmonic components
        multi_scale_term = 0.0
        for i in range(min(len(self.multi_scale_harmonics), self.dim)):
            scale = self.multi_scale_harmonics[i]
            multi_scale_term += scale * np.sin(10.0 * x_norm[i]) * np.cos(3.0 * x_norm[i])
            
        # Adaptive scaling and sensitivity adjustment
        scaling_term = 0.0
        for i in range(min(len(self.scaling_factors), self.dim)):
            scaling = self.scaling_factors[i]
            sensitivity = self.sensitivity_params[i]
            scaling_term += scaling * (x_norm[i] ** 2) * np.exp(-sensitivity * x_norm[i])
            
        # Combined landscape with weighted contributions
        result = 0.3 * elliptic_term + 0.25 * ridge_term + 0.2 * harmonic_term + \
                 0.15 * coupling_term + 0.08 * multi_scale_term + 0.02 * scaling_term
        
        return result
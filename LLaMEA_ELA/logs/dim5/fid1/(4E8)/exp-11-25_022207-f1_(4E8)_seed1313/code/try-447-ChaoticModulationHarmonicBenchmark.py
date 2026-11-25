import numpy as np

class ChaoticModulationHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Self-adaptive elliptic parameters with chaotic scaling
        self.elliptic_axes = np.logspace(0.3, 4.0, min(25, dim))
        self.elliptic_centers = np.random.uniform(-1.5, 1.5, min(25, dim))
        # Dynamic ridge structures with chaotic height variations
        self.ridge_heights = np.random.uniform(0.8, 9.0, min(30, dim))
        self.ridge_widths = np.random.uniform(0.1, 2.5, min(30, dim))
        # Stochastic harmonic interference with chaotic frequency modulation
        self.harmonic_amplitudes = np.random.uniform(0.3, 3.5, min(35, dim))
        self.harmonic_frequencies = np.logspace(0.8, 4.2, min(35, dim))
        # Cross-dimensional interaction with chaotic coupling coefficients
        self.cross_interaction = np.random.uniform(0.1, 2.0, min(20, dim))
        # Condition number scaling with chaotic conditioning factors
        self.conditioning_factors = np.logspace(0.5, 3.5, min(25, dim))
        # Multi-scale chaotic modulation for enhanced multimodality
        self.modulation_scales = np.logspace(0.2, 4.0, min(30, dim))
        # Chaotic noise components with deterministic chaos
        self.noise_amplitudes = np.random.uniform(0.05, 1.5, min(25, dim))
        # Chaotic modulation parameters for irregular curvature
        self.chaos_params = np.random.uniform(0.1, 0.9, min(20, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Elliptic section component with chaotic axes and centers
        elliptic_term = 0.0
        for i in range(min(len(self.elliptic_axes), self.dim)):
            axis = self.elliptic_axes[i]
            center = self.elliptic_centers[i]
            elliptic_term += axis * ((x_norm[i] - center) ** 2)
            
        # Dynamic ridge structures with chaotic height and width variations
        ridge_term = 0.0
        for i in range(min(len(self.ridge_heights), self.dim)):
            height = self.ridge_heights[i]
            width = self.ridge_widths[i]
            ridge_term += height * np.exp(-0.5 * ((x_norm[i] / width) ** 2))
            
        # Stochastic harmonic interference with chaotic modulation
        harmonic_term = 0.0
        for i in range(min(len(self.harmonic_amplitudes), self.dim)):
            amp = self.harmonic_amplitudes[i]
            freq = self.harmonic_frequencies[i]
            # Add chaotic modulation to frequency
            chaos_mod = np.sin(self.chaos_params[min(i, len(self.chaos_params)-1)] * x_norm[i])
            harmonic_term += amp * np.sin(freq * x_norm[i] * (1.0 + 0.2 * chaos_mod))
            
        # Enhanced cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                if len(self.cross_interaction) > min(i, j):
                    interaction = self.cross_interaction[min(i, j)]
                    # Add chaotic interference to cross-term
                    chaos_interf = np.sin(2.0 * x_norm[i] * x_norm[j])
                    cross_term += interaction * np.sin(x_norm[i]) * np.cos(x_norm[j]) * (1.0 + 0.3 * chaos_interf)
                    
        # Dynamic conditioning with chaotic factors
        condition_term = 0.0
        for i in range(min(len(self.conditioning_factors), self.dim)):
            factor = self.conditioning_factors[i]
            # Add chaotic modulation to conditioning
            chaos_mod = np.cos(self.chaos_params[min(i, len(self.chaos_params)-1)] * x_norm[i])
            condition_term += factor * (np.exp(0.4 * np.abs(x_norm[i])) - 1.0) * (1.0 + 0.15 * chaos_mod)
            
        # Multi-scale chaotic modulation with irregular curvature
        modulation_term = 0.0
        for i in range(min(len(self.modulation_scales), self.dim)):
            scale = self.modulation_scales[i]
            # Add chaotic component to modulation
            chaos_mod = np.sin(3.0 * x_norm[i] * self.chaos_params[min(i, len(self.chaos_params)-1)])
            modulation_term += np.sin(scale * x_norm[i]) * np.cos(2.0 * scale * x_norm[i]) * (1.0 + 0.2 * chaos_mod)
            
        # Chaotic noise component with deterministic chaos
        noise_term = 0.0
        for i in range(min(len(self.noise_amplitudes), self.dim)):
            amp = self.noise_amplitudes[i]
            # Add chaotic modulation to noise
            chaos_mod = np.cos(4.0 * x_norm[i] * self.chaos_params[min(i, len(self.chaos_params)-1)])
            noise_term += amp * np.sin(5.0 * x_norm[i]) * np.cos(3.0 * x_norm[i]) * (1.0 + 0.2 * chaos_mod)
            
        # Combine all terms with adaptive weighting
        result = 0.18 * elliptic_term + 0.22 * ridge_term + 0.15 * harmonic_term + \
                 0.14 * cross_term + 0.13 * condition_term + 0.10 * modulation_term + 0.08 * noise_term
        
        return result
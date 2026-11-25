import numpy as np

class NestedHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.nest_levels = max(1, int(np.log2(dim) + 1))
        self.frequency_scaler = 3.0
        self.phase_coupling = 0.8
        self.ridge_strength = 2.0
        self.adaptive_scaling = 1.5
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Create nested harmonic oscillations with multiple frequency layers
        harmonic_sum = np.zeros(self.dim)
        for level in range(1, self.nest_levels + 1):
            freq = self.frequency_scaler * (2 ** level)
            layer_contrib = np.sin(freq * x_norm) * np.cos(freq * x_norm * 0.5)
            # Add phase coupling between dimensions
            if level > 1:
                phase_coupling_term = self.phase_coupling * np.sin(freq * x_norm * 0.3) * np.cos(freq * x_norm * 0.7)
                layer_contrib += phase_coupling_term
            
            harmonic_sum += layer_contrib / (level ** 1.5)
        
        # Add adaptive ridge structures with dynamic scaling
        ridge_terms = np.zeros(self.dim)
        for i in range(self.dim):
            # Create ridges with varying amplitudes based on dimension position
            ridge_amp = self.ridge_strength * (1.0 + 0.3 * np.sin(i * 0.7))
            ridge_terms[i] = ridge_amp * np.sin(2.0 * x_norm[i]) ** 2
        
        # Combine harmonic and ridge components
        combined = harmonic_sum + 0.6 * ridge_terms
        
        # Add dynamic phase modulation based on dimensionality
        phase_mod = np.sum(np.sin(x_norm * (1.0 + 0.2 * np.sin(self.dim * 0.5))) * 
                          np.cos(x_norm * (0.7 + 0.3 * np.cos(self.dim * 0.3))))
        
        # Add adaptive penalty based on solution distribution
        penalty = 0.2 * self.dim * np.std(x_norm)**2 * (1.0 + 0.1 * np.sin(self.dim * 0.8))
        
        # Add chaotic basin interactions with nested structure
        basin_interaction = 0.3 * np.sum(np.abs(x_norm)**(1.8 + 0.1 * np.sin(self.dim * 0.6)))
        
        # Apply adaptive scaling factor
        scale_factor = self.adaptive_scaling * (1.0 + 0.05 * np.log(self.dim + 1))
        
        return scale_factor * (np.sum(combined**2) + phase_mod + penalty + basin_interaction)